"""Cotizador de envios EnvíaYa para los parametros de Jhon."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Protocol


CONFIG = {
    "L1": Decimal("3"),
    "L2": Decimal("10"),
    "PMAX": Decimal("50"),
    "TARIFA_TRAMO_1": Decimal("6000"),
    "TARIFA_TRAMO_2": Decimal("9000"),
    "COSTO_KG_EXCEDENTE": Decimal("800"),
    "RECARGO_RURAL": Decimal("0.15"),
    "RECARGO_NACIONAL": Decimal("0.40"),
    "DESC_FRECUENTE": Decimal("0.05"),
    "DESC_VIP": Decimal("0.15"),
    "DESC_EMPRESARIAL": Decimal("0.12"),
    "DESC_CUPON": Decimal("0.10"),
    "RECARGO_FINDE": Decimal("2000"),
    "COSTO_MINIMO": Decimal("5000"),
}


class EstrategiaZona(Protocol):
    """Contrato para aplicar el recargo correspondiente a una zona."""

    def aplicar(self, tarifa: Decimal) -> Decimal:
        ...


class SinRecargo:
    """Estrategia para zona urbana o exencion empresarial."""

    def aplicar(self, tarifa: Decimal) -> Decimal:
        return tarifa


@dataclass(frozen=True)
class RecargoPorcentual:
    """Estrategia que aumenta la tarifa segun la tasa de la zona."""

    tasa: Decimal

    def aplicar(self, tarifa: Decimal) -> Decimal:
        return tarifa * (Decimal("1") + self.tasa)


ESTRATEGIAS_ZONA: dict[str, EstrategiaZona] = {
    "urbana": SinRecargo(),
    "rural": RecargoPorcentual(CONFIG["RECARGO_RURAL"]),
    "nacional": RecargoPorcentual(CONFIG["RECARGO_NACIONAL"]),
}

DESCUENTOS_CLIENTE = {
    "frecuente": CONFIG["DESC_FRECUENTE"],
    "vip": CONFIG["DESC_VIP"],
    "empresarial": CONFIG["DESC_EMPRESARIAL"],
}


def _validar_peso(peso) -> Decimal:
    try:
        peso_decimal = Decimal(str(peso))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("peso inválido") from None
    if not peso_decimal.is_finite() or not 0 < peso_decimal <= CONFIG["PMAX"]:
        raise ValueError("peso inválido")
    return peso_decimal


def _validar_entrada(peso, zona: str, dia: int, cupon: str | None) -> None:
    _validar_peso(peso)
    if zona not in ESTRATEGIAS_ZONA:
        raise ValueError("zona inválida")
    if not isinstance(dia, int) or isinstance(dia, bool) or not 1 <= dia <= 7:
        raise ValueError("día inválido")
    if cupon is not None and cupon != "ENVIO10":
        raise ValueError("cupón desconocido")


def _tarifa_base(peso: Decimal) -> Decimal:
    if peso <= CONFIG["L1"]:
        return CONFIG["TARIFA_TRAMO_1"]
    if peso <= CONFIG["L2"]:
        return CONFIG["TARIFA_TRAMO_2"]
    return CONFIG["TARIFA_TRAMO_2"] + (peso - CONFIG["L2"]) * CONFIG["COSTO_KG_EXCEDENTE"]


def _seleccionar_estrategia_zona(zona: str, peso: Decimal, cliente: str) -> EstrategiaZona:
    # CAMBIO=1: empresarial con peso estrictamente mayor que L2 no paga recargo de zona.
    if cliente == "empresarial" and peso > CONFIG["L2"]:
        return SinRecargo()
    return ESTRATEGIAS_ZONA[zona]


def _redondear_total(total: Decimal) -> int:
    total = max(total, CONFIG["COSTO_MINIMO"])
    return int(total.quantize(Decimal("1E2"), rounding=ROUND_HALF_UP))


def calc(p, z, c, d, cup=None):
    """Devuelve el costo final del envio en pesos colombianos."""
    peso = _validar_peso(p)
    _validar_entrada(peso, z, d, cup)

    estrategia = _seleccionar_estrategia_zona(z, peso, c)
    total = estrategia.aplicar(_tarifa_base(peso))

    # El descuento empresarial es 12%; los desconocidos siguen sin descuento
    # porque el enunciado no define un tratamiento distinto para esos clientes.
    descuento_cliente = DESCUENTOS_CLIENTE.get(c, Decimal("0"))
    total *= Decimal("1") - descuento_cliente

    # B=1: si hay cliente y cupon, se aplican en secuencia.
    if cup == "ENVIO10":
        total *= Decimal("1") - CONFIG["DESC_CUPON"]

    # E=9: el recargo de sabado o domingo se suma despues de descuentos.
    if d in (6, 7):
        total += CONFIG["RECARGO_FINDE"]

    return _redondear_total(total)
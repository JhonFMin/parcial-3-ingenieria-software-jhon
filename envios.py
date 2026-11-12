"""Calculo de envios de acuerdo con los requisitos R1-R8 de Jhon."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


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
    "DESC_CUPON": Decimal("0.10"),
    "RECARGO_FINDE": Decimal("2000"),
    "COSTO_MINIMO": Decimal("5000"),
}


def _validar_peso(peso):
    try:
        peso = Decimal(str(peso))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("peso inválido") from None
    if not peso.is_finite() or peso <= 0 or peso > CONFIG["PMAX"]:
        raise ValueError("peso inválido")
    return peso


def _tarifa_base(peso):
    if peso <= CONFIG["L1"]:
        return CONFIG["TARIFA_TRAMO_1"]
    if peso <= CONFIG["L2"]:
        return CONFIG["TARIFA_TRAMO_2"]
    return CONFIG["TARIFA_TRAMO_2"] + (peso - CONFIG["L2"]) * CONFIG["COSTO_KG_EXCEDENTE"]


def calc(p, z, c, d, cup=None):
    """Devuelve el costo final del envio en pesos colombianos."""
    peso = _validar_peso(p)

    if z not in ("urbana", "rural", "nacional"):
        raise ValueError("zona inválida")
    if not isinstance(d, int) or isinstance(d, bool) or d < 1 or d > 7:
        raise ValueError("día inválido")
    if cup is not None and cup != "ENVIO10":
        raise ValueError("cupón desconocido")

    total = _tarifa_base(peso)

    if z == "rural":
        total *= Decimal("1") + CONFIG["RECARGO_RURAL"]
    elif z == "nacional":
        total *= Decimal("1") + CONFIG["RECARGO_NACIONAL"]

    # Los descuentos de cliente y cupon se aplican en secuencia.
    if c == "frecuente":
        total *= Decimal("1") - CONFIG["DESC_FRECUENTE"]
    elif c == "vip":
        total *= Decimal("1") - CONFIG["DESC_VIP"]

    if cup == "ENVIO10":
        total *= Decimal("1") - CONFIG["DESC_CUPON"]

    # Para E = 9 impar, el recargo del fin de semana va despues de descuentos.
    if d in (6, 7):
        total += CONFIG["RECARGO_FINDE"]

    total = max(total, CONFIG["COSTO_MINIMO"])
    return int(total.quantize(Decimal("1E2"), rounding=ROUND_HALF_UP))
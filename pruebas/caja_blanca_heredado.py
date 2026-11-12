"""Caminos de caja blanca del cotizador heredado."""

import pytest

from envios_heredado import calc


CAMINOS = [
    ("WB01", (2.99, "urbana", "normal", 4, None, False), 6000),
    ("WB02", (0, "urbana", "normal", 4, None, False), ValueError),
    ("WB03", (50.01, "urbana", "normal", 4, None, False), ValueError),
    ("WB04", (3.01, "urbana", "normal", 4, None, False), 9000),
    ("WB05", (10.01, "urbana", "normal", 4, None, False), 9000),
    ("WB06", (2.99, "rural", "normal", 4, None, False), 6900),
    ("WB07", (2.99, "nacional", "normal", 4, None, False), 8400),
    ("WB08", (2, "costera", "normal", 4, None, False), ValueError),
    ("WB09", (2.99, "urbana", "normal", 7, None, False), 8000),
    ("WB10", (2.99, "urbana", "frecuente", 4, None, False), 5700),
    ("WB11", (2.99, "urbana", "vip", 4, None, False), 5100),
    ("WB12", (2.99, "urbana", "normal", 4, "OTRO", False), ValueError),
    ("WB13", (2.99, "urbana", "normal", 4, "ENVIO10", False), 5400),
    ("WB14", (2, "urbana", "vip", 4, "ENVIO10", False), 5000),
    ("WB15", (2.99, "urbana", "normal", 4, None, True), (6000, "costo: 6000\n")),
]


@pytest.mark.parametrize("camino, entradas, esperado", CAMINOS, ids=[c[0] for c in CAMINOS])
def test_camino_independiente_heredado(camino, entradas, esperado, capsys):
    if esperado is ValueError:
        with pytest.raises(ValueError):
            calc(*entradas)
    elif isinstance(esperado, tuple):
        resultado_esperado, salida_esperada = esperado
        assert calc(*entradas) == resultado_esperado
        assert capsys.readouterr().out == salida_esperada
    else:
        assert calc(*entradas) == esperado

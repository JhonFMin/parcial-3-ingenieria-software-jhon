import pytest

from envios import calc


CASOS = [
    ("P01", (0, "urbana", "normal", 3, None), (ValueError, "peso inv\u00e1lido")),
    ("P02", (-0.01, "urbana", "normal", 3, None), (ValueError, "peso inv\u00e1lido")),
    ("P03", (50.01, "urbana", "normal", 3, None), (ValueError, "peso inv\u00e1lido")),
    ("P04", (3, "urbana", "normal", 5, None), 6000),
    ("P05", (3.01, "urbana", "normal", 5, None), 9000),
    ("P06", (10, "urbana", "normal", 5, None), 9000),
    ("P07", (11.3125, "urbana", "normal", 5, None), 10100),
    ("P08", (0.01, "urbana", "normal", 5, None), 6000),
    ("P09", (50, "urbana", "normal", 5, None), 41000),
    ("P10", (2, "costera", "normal", 3, None), ValueError),
    ("P11", (2, "rural", "normal", 0, None), ValueError),
    ("P12", (2, "rural", "normal", 8, None), ValueError),
    ("P13", (2, "urbana", "normal", -1, None), ValueError),
    ("P14", (4, "rural", "normal", 5, None), 10400),
    ("P15", (4, "nacional", "normal", 5, None), 12600),
    ("P16", (4, "urbana", "normal", 5, None), 9000),
    ("P17", (4, "urbana", "normal", 7, None), 11000),
    ("P18", (4, "urbana", "normal", 6, None), 11000),
    ("P19", (4, "urbana", "frecuente", 5, None), 8600),
    ("P20", (4, "urbana", "vip", 5, None), 7700),
    ("P21", (4, "urbana", "normal", 5, "ENVIO10"), 8100),
    ("P22", (4, "urbana", "vip", 5, "ENVIO10"), 6900),
    ("P23", (4, "urbana", "frecuente", 5, "ENVIO10"), 7700),
    ("P24", (4, "urbana", "normal", 5, "OTRO"), ValueError),
    ("P25", (4, "urbana", "vip", 6, None), 9700),
    ("P26", (2, "urbana", "vip", 5, "ENVIO10"), 5000),
    ("P27", (4, "rural", "vip", 6, "ENVIO10"), 9900),
    ("P28", (2.99, "urbana", "normal", 5, None), 6000),
    ("P29", (9.99, "urbana", "normal", 5, None), 9000),
    ("P30", (10.01, "urbana", "normal", 5, None), 9000),
    ("P31", (49.99, "urbana", "normal", 5, None), 41000),
    ("P32", (4, "urbana", "vip", 7, None), 9700),
]


@pytest.mark.parametrize(
    "caso, argumentos, esperado",
    CASOS,
    ids=[caso[0] for caso in CASOS],
)
def test_casos_de_caja_negra(caso, argumentos, esperado):
    if esperado is ValueError:
        with pytest.raises(ValueError):
            calc(*argumentos)
    elif isinstance(esperado, tuple):
        tipo_error, mensaje = esperado
        with pytest.raises(tipo_error, match=mensaje):
            calc(*argumentos)
    else:
        assert calc(*argumentos) == esperado

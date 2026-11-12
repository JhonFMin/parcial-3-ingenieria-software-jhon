"""Pruebas de la solicitud de cambio CAMBIO=1."""

import pytest

from envios import calc


@pytest.mark.parametrize(
    "peso, zona, dia, cupon, esperado",
    [
        (4, "rural", 5, None, 9100),
        (10, "rural", 5, None, 9100),
        (10.01, "rural", 5, None, 7900),
        (11, "nacional", 7, "ENVIO10", 9800),
    ],
    ids=["SC-01", "SC-02", "SC-03", "SC-04"],
)
def test_cambio_empresarial(peso, zona, dia, cupon, esperado):
    assert calc(peso, zona, "empresarial", dia, cupon) == esperado


def test_peso_no_numerico_se_rechaza():
    with pytest.raises(ValueError, match="peso inválido"):
        calc("abc", "urbana", "empresarial", 5)
# Changelog

All notable changes to this project are recorded here.

## [2.1.0] - CAMBIO=1 empresarial

- Add 12% discount for the `empresarial` customer.
- Waive the zone surcharge for empresarial shipments strictly above 10 kg.
- Preserve all R1-R8 calculations and pass the 37-test regression suite.

## [2.0.0] - Refactor R1-R8

- Validate weight, zone, day, and coupon according to Jhon's parameters.
- Apply weekend charges after sequential discounts.
- Use Decimal and half-up rounding to the nearest 100 pesos.
- Extract calculation responsibilities and add the zone Strategy pattern.

## [1.0.0] - Heredado

- Preserve the original personalized calculator as the baseline for defect analysis.
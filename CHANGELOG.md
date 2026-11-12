# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows Semantic Versioning.

## [2.1.0] - 2026-11-11

### Added

- Added the empresarial customer with a 12% discount.
- Waived the zone surcharge for empresarial shipments strictly above 10 kg.
- Added four change-specific cases and retained the full regression suite.

## [2.0.0] - 2026-11-11

### Changed

- Refactored the calculation into validation, tariff, zone strategy, discount, and rounding responsibilities.
- Changed monetary arithmetic to `Decimal` with half-up rounding to the nearest 100 pesos.
- Removed the inherited `flag` argument; this is a breaking change to the public function signature.

### Fixed

- Corrected validation for weight, zone, day, and unknown coupons.
- Applied the Saturday and Sunday surcharge after discounts.
- Corrected rounding and preserved the $5,000 minimum.

## [1.0.0] - 2026-11-11

### Added

- Preserved the personalized inherited calculator as the baseline for defect analysis.

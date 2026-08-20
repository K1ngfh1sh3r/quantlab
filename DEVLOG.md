# QuantLab Development Log

## Day 4

### Goals

- Create the technical indicators module.
- Implement the first moving average.
- Add the corresponding unit tests.

### Achievements

- Created the indicators module.
- Implemented the Simple Moving Average (SMA).
- Added unit tests for the SMA indicator.

---

## Day 5

### Goals

- Add an Exponential Moving Average indicator.
- Improve indicator validation.
- Increase test coverage.

### Achievements

- Added the Exponential Moving Average (EMA).
- Implemented parameter validation for SMA and EMA.
- Added more than 12 unit tests with pytest.
- Used pandas `ewm()` for EMA calculation.

---

## Day 6

### Goals

- Finalize the technical indicators module.
- Add additional indicators.
- Improve test coverage.

### Achievements

- Added new technical indicators.
- Improved input validation.
- Added additional pytest unit tests.
- Improved the overall indicators module structure.

---

## Day 7

### Goals

- Prepare the foundation of the backtesting engine.
- Design the core backtesting components.

### Achievements

- Created the backtesting module.
- Implemented the initial Portfolio and Trade structure.
- Defined the first interactions between portfolio and engine.
- Prepared the associated unit tests.

---

## Day 8

### Goals

- Implement transaction management.
- Represent financial operations.

### Achievements

- Created the `Trade` class.
- Implemented BUY and SELL operations.
- Added validation for:
  - valid transaction types;
  - positive quantities.
- Added unit tests.

---

## Day 9

### Goals

- Develop portfolio management.
- Track portfolio positions.

### Achievements

- Implemented the `Portfolio` class.
- Added management of:
  - initial capital;
  - available cash;
  - owned shares;
  - trade history.
- Added portfolio valuation.
- Added unit tests.

---

## Day 10

### Goals

- Create the main backtesting engine.
- Connect strategies with the portfolio.

### Achievements

- Created the `BacktestEngine`.
- Executed trading strategies on historical market data.
- Generated BUY / HOLD / SELL signals.
- Tracked portfolio value over time.
- Added the first engine tests.

---

## Day 11

### Goals

- Improve engine robustness.
- Add input validation.

### Achievements

- Added validation for:
  - missing price columns;
  - invalid strategies;
  - invalid trading signals.
- Improved exception handling.
- Increased test coverage.

---

## Day 12

### Goals

- Finalize the first version of the backtesting engine.
- Stabilize the architecture.

### Achievements

- Validated the complete workflow:
  - historical market data;
  - trading strategy;
  - execution;
  - portfolio management;
  - backtest results.
- Stabilized the engine architecture.
- Validated everything with pytest and Ruff.

---

## Day 13

### Goals

- Improve engine quality.
- Add performance statistics.

### Achievements

- Added portfolio statistics:
  - final portfolio value;
  - total profit;
  - percentage return.
- Added last traded price tracking.
- Added unit tests.

---

## Day 14

### Goals

- Add configurable trade quantities.
- Improve backtesting flexibility.

### Achievements

- Added the `quantity` parameter to `BacktestEngine`.
- Supported multiple shares per transaction.
- Added quantity validation.
- Added unit tests covering:
  - custom quantities;
  - portfolio evolution;
  - invalid quantities.
- All tests passed with pytest.

---

## Day 15

### Goals

- Add transaction commissions.
- Improve simulation realism.

### Achievements

- Implemented transaction commissions.
- Applied commissions to BUY and SELL operations.
- Added commission validation.
- Updated existing tests.
- Adjusted expected portfolio values.
- All tests passed with pytest.

---

## Day 16

### Goals

- Export backtest results.
- Improve result usability.

### Achievements

- Stored the latest backtest results.
- Added the `export_csv()` method.
- Exported:
  - trading signals;
  - portfolio value evolution.
- Added unit tests for:
  - CSV generation;
  - exporting without a previous backtest;
  - exported file contents.
- Validated with pytest and Ruff.

---

## Day 17

### Goals

- Implement the first trading strategy.
- Connect strategies with technical indicators.

### Achievements

- Created the `Strategy` base class.
- Implemented the `MovingAverageStrategy`.
- Added SMA crossover signal generation.
- Added data preparation through `prepare_data()`.
- Added comprehensive unit tests.
- Validated with pytest and Ruff.

---

## Day 18

### Goals

- Improve the backtesting engine.
- Introduce portfolio performance reporting.

### Achievements

- Refactored the engine workflow.
- Added portfolio performance statistics.
- Improved strategy preparation handling.
- Added extensive unit tests.
- Validated with pytest and Ruff.

---

## Day 19

### Goals

- Create the analytics module.
- Implement portfolio performance metrics.

### Achievements

- Created the `analytics` package.
- Implemented:
  - `total_return()`;
  - `max_drawdown()`;
  - `volatility()`.
- Added comprehensive unit tests.
- Validated with pytest and Ruff.

---

## Day 20

### Goals

- Integrate analytics into the backtesting engine.
- Introduce reporting capabilities.

### Achievements

- Added `calculate_returns()`.
- Integrated analytics metrics into `BacktestEngine.statistics()`.
- Added `BacktestEngine.report()`.
- Implemented the `BacktestReport` class.
- Added the `summary()` method.
- Added unit and integration tests.
- Validated with pytest, Ruff and GitHub Actions.

---

## Day 21

### Goals

- Add the first backtest visualization.
- Introduce equity curve visualization.
- Integrate visualization into backtest reports.

### Achievements

- Created the `visualization` package.
- Implemented `plot_equity_curve()`.
- Added validation for empty portfolio value series.
- Added unit tests for equity curve generation and plotted data.
- Extended `BacktestReport` to store backtest results.
- Added `BacktestReport.plot_equity_curve()`.
- Integrated equity curve visualization with backtest reports.
- Added integration tests.
- All 172 tests passed with pytest.
- Ruff validation passed successfully.

---

## Day 22

### Objectives

- Improve the backtest reporting system.
- Add additional performance visualizations.
- Integrate visualizations into `BacktestReport`.
- Strengthen test coverage for reporting and visualization features.

### Achievements

- Added a portfolio drawdown visualization using Matplotlib.
- Added `plot_drawdown()` to the visualization module.
- Integrated drawdown visualization into `BacktestReport`.
- Added a unified `plot()` method to generate the available backtest visualizations.
- Added `available_plots()` to expose supported report visualizations.
- Added integration tests for:
  - drawdown plotting;
  - available visualizations;
  - combined report plotting.
- Verified that the equity curve and drawdown visualizations are correctly triggered by the report.
- Improved import formatting and code consistency with Ruff.
- Full test suite passes with pytest.
- Ruff checks pass successfully.

---

## Day 23

### Objectives

- Strengthen the backtesting engine.
- Improve input validation and error handling.
- Extend test coverage for edge cases.

### Achievements

- Improved `BacktestEngine` input validation.
- Added validation for:
  - invalid market data types;
  - invalid initial capital;
  - empty datasets;
  - invalid quantities;
  - invalid commissions;
  - invalid strategy objects;
  - invalid trading signals.
- Improved engine robustness against invalid inputs.
- Added extensive unit tests covering engine edge cases.
- Validated the implementation with pytest and Ruff.

---

## Day 24

### Objectives

- Consolidate the backtesting architecture.
- Strengthen portfolio and trade components.
- Improve test coverage and code quality.

### Achievements

- Extended and stabilized the `Portfolio` component.
- Strengthened transaction handling through the `Trade` model.
- Added comprehensive tests for:
  - portfolio initialization;
  - portfolio valuation;
  - BUY operations;
  - SELL operations;
  - insufficient cash;
  - insufficient positions;
  - trade history;
  - invalid trade types;
  - invalid quantities.
- Extended backtesting engine tests.
- Added tests for CSV export and reporting behavior.
- Validated the complete backtesting workflow.
- Full test suite passed successfully.
- Ruff checks passed successfully.
- Committed and pushed all changes to GitHub.

---

## Day 25

### Objectives

- Measure the quality and test coverage of QuantLab.
- Identify remaining uncovered code paths.
- Prepare the project for the next development phase.

### Achievements

- Audited the complete QuantLab source tree and test suite.
- Verified the current project architecture across:
  - analytics;
  - backtesting;
  - data;
  - indicators;
  - strategies;
  - visualization.
- Installed and configured `pytest-cov` inside the project virtual environment.
- Generated an HTML coverage report.
- Measured the complete test suite with coverage reporting.
- Reached **98% overall test coverage**.
- Executed **210 tests successfully**.
- Identified only 5 uncovered statements across the project.
- Confirmed that most core modules currently reach 100% coverage.
- Verified that the remaining uncovered lines are concentrated in:
  - `analytics/report.py`;
  - `backtesting/engine.py`.
- Confirmed that the project remains fully validated with pytest.
- Identified minor `ResourceWarning` messages related to unclosed SQLite connections during the test run, without affecting test success.
- No source-code changes were required during the coverage audit.
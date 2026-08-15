# Interactive CLI Pizza Ordering System

A terminal-driven interactive order process built in Python. Collects customer order parameters, calculates dynamic itemized pricing with sales tax and conditional delivery fees, and generates formatted billing summaries with reward threshold logic.

## Technical Highlights

* **Dynamic Cost Calculation:** Computes final totals taking into account tiered item sizes, quantity metrics, subtotal sales tax multipliers ($10\%$), and conditional service fulfillment fees (delivery flat rate).
* **Personalized Logic & Control Flow:** Features conditional branch handlers to customize terminal output for recognized administrative user accounts versus standard clients.
* **Formatted Billing & Rewards:** Formats currency outputs to two decimal places (`${total:,.2f}`) and evaluates order thresholds ($\ge \$50.00$) to trigger promotional coupon rewards.
* **Input Normalization:** Normalizes text input via lowercasing (`.lower()`) to ensure reliable comparison handling across user prompts.

## Key Dependencies

* **Python Version:** Built with standard Python 3.x routines (requires zero external `pip` packages).

## Usage

```bash
python main.py

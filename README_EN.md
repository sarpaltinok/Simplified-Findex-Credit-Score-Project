# Simplified Findeks Credit Score Project

This project is a simplified simulation of the Findeks Credit Score system, designed to calculate and visualize credit scores based on sample financial data. It is written in Python and uses pandas for data processing and matplotlib for visualization.

## Features

- **Data Processing:** Reads and cleans financial data from a CSV file.
- **Credit Score Calculation:** Calculates a credit score for each individual based on payment habits, debt status, credit usage, and new credit activity.
- **Visualization:** Provides histogram and pie chart visualizations of the credit score distribution and risk categories.

## Project Structure

```
src/
├── main.py              # Entry point for the project
├── data_processing.py   # Handles data loading, cleaning, and score calculation
├── calculation.py       # Contains scoring logic and risk categorization
├── visualization.py     # Generates visualizations for the results
data_base/
└── test.csv             # Sample data file (not included)
```

## Getting Started

### Prerequisites

- Python 3.8+
- pandas
- matplotlib

Install dependencies with:

```bash
pip install pandas matplotlib
```

### Usage

1. Place your data file as `data_base/test.csv` with the required columns:

    - `Delay_from_due_date`
    - `Num_of_Delayed_Payment`
    - `Outstanding_Debt`
    - `Credit_Utilization_Ratio`
    - `Num_of_Loan`
    - `Num_Credit_Card`
    - `Num_Bank_Accounts`
    - `Num_Credit_Inquiries`

2. Run the project:

```bash
python src/main.py
```

3. View the printed credit scores and the generated visualizations.

## Credit Score Calculation

The credit score is calculated as a weighted sum of four components:

- **Payment Habit Score** (45%)
- **Debt Status Score** (32%)
- **Credit Usage Score** (18%)
- **New Credit Score** (5%)

Each component is scored between 0 and 100, and the final score is scaled to a 0–1900 range.

## License

This project is for educational purposes.

---

**Note:** This is a simplified model and should not be used for real financial decisions.

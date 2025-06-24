import pandas as pd
from calculation import payment_habit_score, new_credit_score, debt_status_score, credit_usage_score, calculate_credit_score

columns_needed = [
    "Delay_from_due_date",           # Delay duration (payment habit)
    "Num_of_Delayed_Payment",        # Number of delayed payments
    "Outstanding_Debt",              # Outstanding debt
    "Credit_Utilization_Ratio",      # Debt/limit ratio
    "Num_of_Loan",                   # Number of active loans
    "Num_Credit_Card",               # Number of credit cards
    "Num_Bank_Accounts",             # Number of bank accounts
    "Num_Credit_Inquiries"           # Recent credit inquiries
]

# Load and clean data
df = pd.read_csv("data_base/test.csv", usecols=columns_needed)
df = df.fillna(df.mean(numeric_only=True))

# Convert columns that should be numeric
df[columns_needed] = df[columns_needed].apply(pd.to_numeric, errors='coerce')

# Calculate scores and credit score for each row
df['Payment_Habit_Score'] = df.apply(payment_habit_score, axis=1)
df['Debt_Status_Score'] = df.apply(debt_status_score, axis=1)
df['Credit_Usage_Score'] = df.apply(credit_usage_score, axis=1)
df['New_Credit_Score'] = df.apply(new_credit_score, axis=1)

df['Credit_Score'] = df.apply(
    lambda row: calculate_credit_score(
        row['Payment_Habit_Score'],
        row['Debt_Status_Score'],
        row['Credit_Usage_Score'],
        row['New_Credit_Score']
    ),
    axis=1
)

# Show results
print(df[['Credit_Score']].head(50))








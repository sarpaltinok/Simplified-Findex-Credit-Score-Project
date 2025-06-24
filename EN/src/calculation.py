def calculate_credit_score(
    payment_habit_score,  # 0-100 range
    debt_status_score,    # 0-100 range
    credit_usage_score,   # 0-100 range
    new_credit_score      # 0-100 range
):
    # Weighted average according to each component's percentage
    overall_score = (
        payment_habit_score * 0.45 +
        debt_status_score * 0.32 +
        credit_usage_score * 0.18 +
        new_credit_score * 0.05
    )
    
    # Convert from 0-100 scale to 0-1900 scale
    credit_score = int((overall_score / 100) * 1900)
    return credit_score

def payment_habit_score(row):
    if row['Num_of_Delayed_Payment'] == 0:
        return 100
    elif row['Delay_from_due_date'] <= 2:
        return 70
    else:
        return 40

def debt_status_score(row):
    ratio = row['Credit_Utilization_Ratio']
    if ratio < 0.3:
        return 100
    elif ratio < 0.7:
        return 70
    else:
        return 40

def credit_usage_score(row):
    if row['Num_of_Loan'] <= 1 and row['Num_Credit_Card'] <= 3:
        return 100
    elif row['Num_of_Loan'] <= 3:
        return 70
    else:
        return 40

def new_credit_score(row):
    if row['Num_Credit_Inquiries'] == 0:
        return 100
    elif row['Num_Credit_Inquiries'] <= 1:
        return 70
    else:
        return 40
    
def categorize(credit_score):
    if not (1 <= credit_score <= 1900):
        raise ValueError("Credit score must be between 1 and 1900.")
    
    if credit_score <= 699:
        return "High risk"
    elif credit_score <= 1099:
        return "Medium risk"
    elif credit_score <= 1499:
        return "Low risk"
    elif credit_score <= 1699:
        return "Good"
    else:
        return "Very good"



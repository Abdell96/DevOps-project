def calculate_bmi(height: float, weight: float) -> float:
    """Calculate Body Mass Index (BMI)"""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")
    return weight / (height ** 2)

def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """Calculate Basal Metabolic Rate (BMR)"""
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive numbers")
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be either 'male' or 'female'")

    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # female
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)












#def calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate):
#    monthly_interest_rate = (annual_interest_rate / 100) / 12
#    total_payments = duration_years * 12
#    
#    if monthly_interest_rate > 0:
#        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
#    else:
#        monthly_payment = loan_amount / total_payments

#    return round(monthly_payment, 2)

#def calculate_total_cost(monthly_payment, duration_years):
#    total_payments = duration_years * 12
#    total_cost = monthly_payment * total_payments
#    return round(total_cost, 2)

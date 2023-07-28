import pytest


def calculate_premium(month_salary: int, working_months: int, sick_days: bool):
    if working_months >= 36:
        premium = (month_salary * 12) / 100 * 30
        if not sick_days:
            last_premium = (month_salary * 12) / 100 * 33
            print(f"Ваша премия составила 33%: {last_premium}")
            return last_premium
        else:
            print(f"Ваша премия составила 30%: {premium}")
            return premium
    elif 18 <= working_months < 36:
        premium = (month_salary * 12) / 100 * 25
        if not sick_days:
            last_premium = (month_salary * 12) / 100 * 28
            print(f"Ваша премия составила 28%: {last_premium}")
            return last_premium
        else:
            print(f"Ваша премия составила 25%: {premium}")
            return premium
    elif 3 <= working_months < 18:
        premium = (month_salary * 12) / 100 * 15
        if not sick_days:
            last_premium = (month_salary * 12) / 100 * 18
            print(f"Ваша премия составила 18%: {last_premium}")
            return last_premium
        else:
            print(f"Ваша премия составила 15%: {premium}")
            return premium
    else:
        print("Премия не начислена, вы работаете менее 3х месяцев")


calculate_premium(month_salary=25000, working_months=1, sick_days=False)

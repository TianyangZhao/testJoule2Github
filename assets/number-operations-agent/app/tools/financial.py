"""Financial tool for common financial calculations."""

from langchain_core.tools import tool


@tool
def financial_calculator(
    operation: str,
    principal: float = 0.0,
    rate: float = 0.0,
    time: float = 0.0,
    n: float = 1.0,
    part: float = 0.0,
    total: float = 0.0,
    value: float = 0.0,
    percentage: float = 0.0,
) -> str:
    """Perform a financial calculation.

    Operations:
    - 'simple_interest': Computes I = principal * rate * time
        Args: principal, rate (as decimal, e.g. 0.05 for 5%), time (years)
    - 'compound_interest': Computes A = principal * (1 + rate/n)^(n*time)
        Args: principal, rate (decimal), time (years), n (compounding periods per year)
    - 'percentage_of': Computes what percentage part is of total
        Args: part, total
    - 'percent_value': Computes the given percentage of a value
        Args: value, percentage (e.g. 15 for 15%)
    - 'loan_repayment': Monthly repayment using amortisation formula
        Args: principal (loan amount), rate (annual rate as decimal), time (years)

    Returns:
        Calculated result with a brief explanation.
    """
    operation = operation.strip().lower().replace(" ", "_")

    if operation == "simple_interest":
        interest = principal * rate * time
        total_amount = principal + interest
        return (
            f"Simple Interest: I = {principal} × {rate} × {time} = {round(interest, 4)}\n"
            f"Total amount = {round(total_amount, 4)}"
        )

    elif operation == "compound_interest":
        if n <= 0:
            return "Error: Compounding periods (n) must be greater than 0."
        amount = principal * (1 + rate / n) ** (n * time)
        interest_earned = amount - principal
        return (
            f"Compound Interest: A = {principal} × (1 + {rate}/{n})^({n}×{time})\n"
            f"Total amount = {round(amount, 4)}\n"
            f"Interest earned = {round(interest_earned, 4)}"
        )

    elif operation == "percentage_of":
        if total == 0:
            return "Error: Total cannot be zero when computing percentage."
        result = (part / total) * 100
        return f"{part} is {round(result, 4)}% of {total}"

    elif operation == "percent_value":
        result = value * percentage / 100
        return f"{percentage}% of {value} = {round(result, 4)}"

    elif operation == "loan_repayment":
        if time <= 0:
            return "Error: Loan term (time) must be greater than 0."
        monthly_rate = rate / 12
        n_payments = time * 12
        if monthly_rate == 0:
            # Zero-interest loan
            monthly_payment = principal / n_payments
        else:
            monthly_payment = principal * (
                monthly_rate * (1 + monthly_rate) ** n_payments
            ) / ((1 + monthly_rate) ** n_payments - 1)
        total_paid = monthly_payment * n_payments
        total_interest = total_paid - principal
        return (
            f"Loan Repayment:\n"
            f"  Principal: {principal}\n"
            f"  Annual rate: {rate * 100}%\n"
            f"  Term: {time} years ({int(n_payments)} monthly payments)\n"
            f"  Monthly payment: {round(monthly_payment, 4)}\n"
            f"  Total paid: {round(total_paid, 4)}\n"
            f"  Total interest: {round(total_interest, 4)}"
        )

    else:
        return (
            f"Error: Unknown operation '{operation}'. "
            "Supported: simple_interest, compound_interest, percentage_of, percent_value, loan_repayment."
        )

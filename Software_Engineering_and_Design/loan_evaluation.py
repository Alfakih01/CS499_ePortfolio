# loan_evaluation.py

def evaluate_loan(income, credit_score, existing_debt):
    """
    Evaluates a loan application based on income, credit score, and existing debt.
    A weighted scoring system:
      - Income: weight 0.4
      - Credit Score: weight 0.5
      - Existing Debt: weight 0.1 (negative impact)
    """
    score = (income * 0.4) + (credit_score * 0.5) - (existing_debt * 0.1)
    return score

def decision(score, threshold=50):
    """
    Decides whether to approve the loan based on the calculated score.
    """
    return "Approve" if score >= threshold else "Reject"

if __name__ == "__main__":
    # Sample input values
    income = 50000       # Annual income
    credit_score = 700   # Credit score
    existing_debt = 5000 # Existing debt
    
    score = evaluate_loan(income, credit_score, existing_debt)
    print("Loan Evaluation Score:", score)
    print("Decision:", decision(score))

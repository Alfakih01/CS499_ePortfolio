#!/usr/bin/env python3
"""
Enhanced Loan Evaluation Script

This script evaluates a loan application using a weighted scoring system.
It is designed using an object-oriented approach to encapsulate the evaluation process.
The evaluation considers income, credit score, and existing debt.
Weights are dynamically configurable via a dictionary to allow flexibility.
"""

class LoanEvaluation:
    def __init__(self, income, credit_score, existing_debt, weights=None):
        if income < 0:
            raise ValueError("Income must be non-negative.")
        if existing_debt < 0:
            raise ValueError("Existing debt must be non-negative.")
        
        self.income = income
        self.credit_score = credit_score
        self.existing_debt = existing_debt
        
        # Default weights if none provided
        self.weights = weights if weights is not None else {'income': 0.4, 'credit_score': 0.5, 'existing_debt': 0.1}
        self.score = None

    def evaluate(self):
        """
        Evaluates the loan application using a dynamic weighted scoring system.
        Returns the calculated score.
        """
        self.score = (self.income * self.weights['income'] +
                      self.credit_score * self.weights['credit_score'] -
                      self.existing_debt * self.weights['existing_debt'])
        return self.score

    def decision(self, threshold=50):
        """
        Determines whether to approve or reject the loan based on the calculated score.
        :param threshold: The score threshold for loan approval (default is 50)
        :return: "Approve" if score >= threshold, else "Reject"
        """
        if self.score is None:
            self.evaluate()
        return "Approve" if self.score >= threshold else "Reject"

def main():
    try:
        income = float(input("Enter applicant income: "))
        credit_score = float(input("Enter applicant credit score: "))
        existing_debt = float(input("Enter applicant existing debt: "))
        
        # Create an instance of LoanEvaluation with default weights
        loan_app = LoanEvaluation(income, credit_score, existing_debt)
        score = loan_app.evaluate()
        decision = loan_app.decision()
        
        print(f"\nLoan Evaluation Score: {score:.2f}")
        print(f"Loan Decision: {decision}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

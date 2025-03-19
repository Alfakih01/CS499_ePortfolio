#!/usr/bin/env python3
"""
Enhanced Loan Evaluation Module

This module provides an object-oriented approach to evaluate loan applications using a dynamic, weighted scoring system.
It validates input values and determines a loan decision based on configurable weights and thresholds.
"""

class LoanEvaluation:
    def __init__(self, income, credit_score, existing_debt, weights=None):
        """
        Initializes a LoanEvaluation instance.
        
        :param income: float, applicant income (non-negative number)
        :param credit_score: float, applicant credit score
        :param existing_debt: float, applicant's existing debt (non-negative)
        :param weights: dict, optional custom weights with keys 'income', 'credit_score', and 'existing_debt'
        """
        if income < 0:
            raise ValueError("Income must be non-negative.")
        if existing_debt < 0:
            raise ValueError("Existing debt must be non-negative.")
        
        self.income = income
        self.credit_score = credit_score
        self.existing_debt = existing_debt
        
        # Default weights if none are provided
        self.weights = weights if weights is not None else {'income': 0.4, 'credit_score': 0.5, 'existing_debt': 0.1}
        self.score = None

    def evaluate(self):
        """
        Evaluates the loan application using the weighted scoring system.
        
        :return: float, the computed loan evaluation score
        """
        self.score = (self.income * self.weights['income'] +
                      self.credit_score * self.weights['credit_score'] -
                      self.existing_debt * self.weights['existing_debt'])
        return self.score

    def decision(self, threshold=50):
        """
        Determines the loan decision based on the evaluation score and a threshold.
        
        :param threshold: float, the score threshold for loan approval (default is 50)
        :return: str, "Approve" if score >= threshold, else "Reject"
        """
        # Evaluate score if not already done
        if self.score is None:
            self.evaluate()
        return "Approve" if self.score >= threshold else "Reject"


def main():
    try:
        income = float(input("Enter applicant income: "))
        credit_score = float(input("Enter applicant credit score: "))
        existing_debt = float(input("Enter applicant existing debt: "))
        
        # Create a LoanEvaluation instance with default weights
        loan_eval = LoanEvaluation(income, credit_score, existing_debt)
        score = loan_eval.evaluate()
        decision = loan_eval.decision()
        
        print(f"\nLoan Evaluation Score: {score:.2f}")
        print(f"Loan Decision: {decision}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

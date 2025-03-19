#include <iostream>
#include <string>
#include <limits>
#include <stdexcept>

// Named constants for calculations and thresholds
const int INCOME_DIVISOR = 1000;
const int CREDIT_HISTORY_MULTIPLIER = 10;
const int APPROVAL_THRESHOLD = 50;

class LoanApplication {
private:
    std::string applicantName;
    int income;
    int creditHistory;
    int creditScore;

public:
    // Constructor initializes numerical values to 0
    LoanApplication() : income(0), creditHistory(0), creditScore(0) {}

    // Method to gather and validate user input
    void getInput() {
        std::cout << "Enter applicant name: ";
        std::getline(std::cin, applicantName);
        if (applicantName.empty()) {
            throw std::runtime_error("Applicant name cannot be empty.");
        }

        std::cout << "Enter applicant income: ";
        while (!(std::cin >> income) || income < 0) {
            std::cout << "Invalid input. Please enter a non-negative income: ";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }

        std::cout << "Enter credit history rating (1-10): ";
        while (!(std::cin >> creditHistory) || creditHistory < 1 || creditHistory > 10) {
            std::cout << "Invalid input. Please enter a rating between 1 and 10: ";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear input buffer
    }

    // Method to calculate credit score based on input values
    void calculateCreditScore() {
        creditScore = (income / INCOME_DIVISOR) + (creditHistory * CREDIT_HISTORY_MULTIPLIER);
    }

    // Method to display the result to the user
    void displayResult() const {
        std::cout << "\nApplicant: " << applicantName << std::endl;
        std::cout << "Calculated Credit Score: " << creditScore << std::endl;
        if (creditScore >= APPROVAL_THRESHOLD) {
            std::cout << "Loan Approved!" << std::endl;
        } else {
            std::cout << "Loan Denied!" << std::endl;
        }
    }
};

int main() {
    try {
        LoanApplication app;
        app.getInput();
        app.calculateCreditScore();
        app.displayResult();
    } catch (const std::exception &ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }
    return 0;
}

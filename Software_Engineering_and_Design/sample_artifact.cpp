// sample_artifact.cpp
#include <iostream>
#include <string>

// Function to calculate credit score based on dummy criteria
int calculateCreditScore(int income, int creditHistory) {
    // Simplified formula: credit score = (income / 1000) + (creditHistory * 10)
    return (income / 1000) + (creditHistory * 10);
}

int main() {
    std::string applicantName;
    int income;
    int creditHistory;
    
    std::cout << "Enter applicant name: ";
    std::getline(std::cin, applicantName);
    
    std::cout << "Enter applicant income: ";
    std::cin >> income;
    
    std::cout << "Enter credit history rating (1-10): ";
    std::cin >> creditHistory;
    
    int score = calculateCreditScore(income, creditHistory);
    
    std::cout << "Applicant: " << applicantName << std::endl;
    std::cout << "Calculated Credit Score: " << score << std::endl;
    
    if(score >= 50) {
        std::cout << "Loan Approved!" << std::endl;
    } else {
        std::cout << "Loan Denied!" << std::endl;
    }
    
    return 0;
}

-- Enhanced SQL Schema for Loan Application System
-- Database: LoanApplications
-- This schema has been optimized for normalization, data integrity, and performance.

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS LoanApplications;
USE LoanApplications;

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS LoanApplications;
DROP TABLE IF EXISTS Applicants;

-- Create table for storing applicant information
CREATE TABLE Applicants (
    ApplicantID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE, -- Enforce unique email addresses
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create table for storing loan application details
CREATE TABLE LoanApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY,
    ApplicantID INT NOT NULL,
    ApplicationDate DATE DEFAULT CURRENT_DATE,
    Income DECIMAL(10,2) NOT NULL,
    CreditScore INT NOT NULL,
    ExistingDebt DECIMAL(10,2) NOT NULL,
    LoanAmount DECIMAL(10,2) NOT NULL,
    Status VARCHAR(20) DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_applicant
        FOREIGN KEY (ApplicantID)
        REFERENCES Applicants(ApplicantID)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes to improve query performance
CREATE INDEX idx_income ON LoanApplications(Income);
CREATE INDEX idx_status ON LoanApplications(Status);

-- Insert sample applicant data
INSERT INTO Applicants (FirstName, LastName, Email, Phone)
VALUES ('John', 'Doe', 'johndoe@example.com', '555-1234');

-- Insert sample loan application data
INSERT INTO LoanApplications (ApplicantID, Income, CreditScore, ExistingDebt, LoanAmount, Status)
VALUES (1, 50000.00, 700, 5000.00, 25000.00, 'Pending');

-- Example of a trigger to automatically update the loan status based on credit score
DELIMITER $$
CREATE TRIGGER trg_update_loan_status
AFTER INSERT ON LoanApplications
FOR EACH ROW
BEGIN
    IF NEW.CreditScore >= 650 THEN
        UPDATE LoanApplications
        SET Status = 'Approved'
        WHERE ApplicationID = NEW.ApplicationID;
    ELSE
        UPDATE LoanApplications
        SET Status = 'Rejected'
        WHERE ApplicationID = NEW.ApplicationID;
    END IF;
END$$
DELIMITER ;

-- End of enhanced schema

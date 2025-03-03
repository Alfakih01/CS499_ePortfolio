-- schema.sql

-- Create a database for loan applications
CREATE DATABASE IF NOT EXISTS LoanApplications;
USE LoanApplications;

-- Table for storing applicant information
CREATE TABLE IF NOT EXISTS Applicants (
    ApplicantID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100),
    Phone VARCHAR(20)
);

-- Table for storing loan application details
CREATE TABLE IF NOT EXISTS LoanApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY,
    ApplicantID INT,
    ApplicationDate DATE,
    Income DECIMAL(10,2),
    CreditScore INT,
    ExistingDebt DECIMAL(10,2),
    LoanAmount DECIMAL(10,2),
    Status VARCHAR(20),
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
);

-- Insert sample applicant data
INSERT INTO Applicants (FirstName, LastName, Email, Phone)
VALUES ('John', 'Doe', 'johndoe@example.com', '555-1234');

-- Insert sample loan application data
INSERT INTO LoanApplications (ApplicantID, ApplicationDate, Income, CreditScore, ExistingDebt, LoanAmount, Status)
VALUES (1, CURDATE(), 50000, 700, 5000, 25000, 'Pending');

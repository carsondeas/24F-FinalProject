CREATE DATABASE IF NOT EXISTS skillseeker;

USE skillseeker;

CREATE TABLE IF NOT EXISTS Department (
    departmentID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Professor (
    professorID INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE IF NOT EXISTS Course (
    courseID INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    name VARCHAR(255),
    professorID INT,
    FOREIGN KEY (professorID) REFERENCES Professor(professorID)
);

CREATE TABLE IF NOT EXISTS Skill (
    skillID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Course_Skill (
    skillID INT,
    courseID INT,
    proficiencyLevel INT,
    PRIMARY KEY (skillID, courseID),
    FOREIGN KEY (skillID) REFERENCES Skill(skillID),
    FOREIGN KEY (courseID) REFERENCES Course(courseID)
);

CREATE TABLE IF NOT EXISTS Student (
    NUID INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    GPA DOUBLE,
    major VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Student_Course (
    NUID INT,
    courseID INT,
    PRIMARY KEY (NUID, courseID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID),
    FOREIGN KEY (courseID) REFERENCES Course(courseID)
);

CREATE TABLE IF NOT EXISTS Student_Skill (
    skillID INT,
    NUID INT,
    proficiencyLevel INT,
    PRIMARY KEY (skillID, NUID),
    FOREIGN KEY (skillID) REFERENCES Skill(skillID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID)
    );

CREATE TABLE IF NOT EXISTS CoOp (
    jobID INT PRIMARY KEY AUTO_INCREMENT,
    jobTitle VARCHAR(255),
    companyName VARCHAR(255),
    industry VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS CoOp_Skill (
    skillID INT,
    jobID INT,
    proficiencyLevel INT,
    PRIMARY KEY (skillID, jobID),
    FOREIGN KEY (skillID) REFERENCES Skill(skillID),
    FOREIGN KEY (jobID) REFERENCES CoOp(jobID)
    );

CREATE TABLE IF NOT EXISTS Student_CoOp (
    NUID INT,
    jobID INT,
    PRIMARY KEY (NUID, jobID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID),
    FOREIGN KEY (jobID) REFERENCES CoOp(jobID)
);

CREATE TABLE IF NOT EXISTS Employer (
    employerID INT PRIMARY KEY AUTO_INCREMENT,
    contactEmail VARCHAR(255),
    contactPhone VARCHAR(255),
    contactName VARCHAR(255),
    industry VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Employer_CoOp (
    employerID INT,
    jobID INT,
    PRIMARY KEY (employerID, jobID),
    FOREIGN KEY (employerID) REFERENCES Employer(employerID),
    FOREIGN KEY (jobID) REFERENCES CoOp(jobID)
);

CREATE TABLE IF NOT EXISTS CoOpAdvisor (
    advisorID INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE IF NOT EXISTS AdvisorStudent (
    NUID INT,
    advisorID INT,
    PRIMARY KEY (NUID, advisorID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID),
    FOREIGN KEY (advisorID) REFERENCES CoOpAdvisor(advisorID)
);

CREATE TABLE IF NOT EXISTS AdvisorEmployer (
    employerID INT,
    advisorID INT,
    PRIMARY KEY (employerID, advisorID),
    FOREIGN KEY (employerID) REFERENCES Employer(employerID),
    FOREIGN KEY (advisorID) REFERENCES CoOpAdvisor(advisorID)
);


-- Insert data into Department
INSERT INTO Department (name) VALUES 
('Computer Science'), 
('Finance'), 
('Engineering');

-- Insert data into Professor
INSERT INTO Professor (email, name, departmentID) VALUES 
('jdoe@university.edu', 'John Doe', 1), 
('asmith@university.edu', 'Alice Smith', 2), 
('bwong@university.edu', 'Bob Wong', 3);

-- Insert data into Course
INSERT INTO Course (description, name, professorID) VALUES 
('Database Design', 'CS3200', 1), 
('Advanced Algorithms', 'CS3000', 1), 
('Corporate Finance', 'FINA3301', 2);

-- Insert data into Skill
INSERT INTO Skill (name) VALUES 
('Python'), 
('C++'), 
('Financial Analysis');

-- Insert data into Course_Skill
INSERT INTO Course_Skill (skillID, courseID, proficiencyLevel) VALUES 
(1, 1, 3), 
(2, 2, 4), 
(3, 3, 5);

-- Insert data into Student
INSERT INTO Student (email, name, GPA, major) VALUES 
('student1@northeastern.edu', 'Alice Green', 3.8, 'Computer Science'), 
('student2@northeastern.edu', 'Bob Brown', 3.5, 'Finance'), 
('student3@northeastern.edu', 'Charlie White', 3.7, 'Engineering');

-- Insert data into Student_Course
INSERT INTO Student_Course (NUID, courseID) VALUES 
(1, 1), 
(2, 3), 
(3, 2);

-- Insert data into Student_Skill
INSERT INTO Student_Skill (skillID, NUID, proficiencyLevel) VALUES 
(1, 1, 4), 
(3, 2, 5), 
(2, 3, 3);

-- Insert data into CoOp
INSERT INTO CoOp (jobTitle, companyName, industry) VALUES 
('Software Engineer Intern', 'Google', 'Tech'), 
('Finance Analyst Intern', 'Goldman Sachs', 'Finance'), 
('Mechanical Engineer Intern', 'Tesla', 'Automotive');

-- Insert data into Student_CoOp
INSERT INTO Student_CoOp (NUID, jobID) VALUES 
(1, 1), 
(2, 2), 
(3, 3);

-- Insert data into Employer
INSERT INTO Employer (contactEmail, contactPhone, contactName, industry) VALUES 
('hr@google.com', '123-456-7890', 'Google HR', 'Tech'), 
('hr@goldmansachs.com', '987-654-3210', 'Goldman HR', 'Finance'), 
('hr@tesla.com', '555-555-5555', 'Tesla HR', 'Automotive');

-- Insert data into Employer_CoOp
INSERT INTO Employer_CoOp (employerID, jobID) VALUES 
(1, 1), 
(2, 2), 
(3, 3);

-- Insert data into CoOpAdvisor
INSERT INTO CoOpAdvisor (email, name, departmentID) VALUES 
('advisor1@northeastern.edu', 'Emma Johnson', 1), 
('advisor2@northeastern.edu', 'Michael Lee', 2), 
('advisor3@northeastern.edu', 'Sophia Carter', 3);

-- Insert data into AdvisorStudent
INSERT INTO AdvisorStudent (NUID, advisorID) VALUES 
(1, 1), 
(2, 2), 
(3, 3);

-- Insert data into AdvisorEmployer
INSERT INTO AdvisorEmployer (employerID, advisorID) VALUES 
(1, 1), 
(2, 2), 
(3, 3);

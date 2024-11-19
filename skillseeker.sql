CREATE DATABASE skillseeker;

USE skillseeker;

CREATE TABLE Department (
    departmentID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

CREATE TABLE Professor (
    professorID INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE Course (
    courseID INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    name VARCHAR(255),
    professorID INT,
    FOREIGN KEY (professorID) REFERENCES Professor(professorID)
);

CREATE TABLE Skill (
    skillID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

CREATE TABLE Course_Skill (
    skillID INT,
    courseID INT,
    proficiencyLevel INT,
    PRIMARY KEY (skillID, courseID),
    FOREIGN KEY (skillID) REFERENCES Skill(skillID),
    FOREIGN KEY (courseID) REFERENCES Course(courseID)
);

CREATE TABLE Student (
    NUID INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    GPA DOUBLE,
    major VARCHAR(255)
);

CREATE TABLE Student_Course (
    NUID INT,
    courseID INT,
    PRIMARY KEY (NUID, courseID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID),
    FOREIGN KEY (courseID) REFERENCES Course(courseID)
);

CREATE TABLE Student_Skill (
    skillID INT,
    NUID INT,
    proficiencyLevel INT,
    PRIMARY KEY (skillID, NUID),
    FOREIGN KEY (skillID) REFERENCES Skill(skillID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID)
    );

CREATE TABLE CoOp (
    jobID INT PRIMARY KEY AUTO_INCREMENT,
    jobTitle VARCHAR(255),
    companyName VARCHAR(255),
    industry VARCHAR(255)
);

CREATE TABLE Student_CoOp (
    NUID INT,
    jobID INT,
    PRIMARY KEY (NUID, jobID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID),
    FOREIGN KEY (jobID) REFERENCES CoOp(jobID)
);

CREATE TABLE Employer (
    employerID INT PRIMARY KEY AUTO_INCREMENT,
    contactEmail VARCHAR(255),
    contactPhone VARCHAR(255),
    contactName VARCHAR(255),
    industry VARCHAR(255)
);

CREATE TABLE Employer_CoOp (
    employerID INT,
    jobID INT,
    PRIMARY KEY (employerID, jobID),
    FOREIGN KEY (employerID) REFERENCES Employer(employerID),
    FOREIGN KEY (jobID) REFERENCES CoOp(jobID)
);

CREATE TABLE CoOpAdvisor (
    advisorID INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE AdvisorStudent (
    NUID INT,
    advisorID INT,
    PRIMARY KEY (NUID, advisorID),
    FOREIGN KEY (NUID) REFERENCES Student(NUID),
    FOREIGN KEY (advisorID) REFERENCES CoOpAdvisor(advisorID)
);

CREATE TABLE AdvisorEmployer (
    employerID INT,
    advisorID INT,
    PRIMARY KEY (employerID, advisorID),
    FOREIGN KEY (employerID) REFERENCES Employer(employerID),
    FOREIGN KEY (advisorID) REFERENCES CoOpAdvisor(advisorID)
);

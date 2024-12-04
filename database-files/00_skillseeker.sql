CREATE DATABASE IF NOT EXISTS skillseeker;

USE skillseeker;
-- Computer Science, Engineering, Finance, Communication, Health Sciences, Chemical Engineering, Civil Engineering, Mechanical Engineering, Information Technology, Chemistry, Physics, Math, Calculus
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

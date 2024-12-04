USE skillseeker;

-- Insert data into Department
INSERT INTO Department (name) VALUES 
('Computer Science'),            -- departmentID = 1
('Finance'),                     -- departmentID = 2
('Engineering'),                 -- departmentID = 3
('Data Science'),                -- departmentID = 4
('Cybersecurity'),               -- departmentID = 5
('Information Systems'),         -- departmentID = 6
('Computer Engineering'),        -- departmentID = 7
('Artificial Intelligence'),     -- departmentID = 8
('Software Engineering'),        -- departmentID = 9
('Mathematics'),                 -- departmentID = 10
('Physics'),                     -- departmentID = 11
('Biology'),                     -- departmentID = 12
('Chemistry'),                   -- departmentID = 13
('Psychology'),                  -- departmentID = 14
('English'),                     -- departmentID = 15
('Business'),                    -- departmentID = 16
('Mechanical Engineering'),      -- departmentID = 17
('Electrical Engineering'),      -- departmentID = 18
('Civil Engineering'),           -- departmentID = 19
('Aerospace Engineering'),       -- departmentID = 20
('Robotics'),                    -- departmentID = 21
('Statistics'),                  -- departmentID = 22
('Economics'),                   -- departmentID = 23
('Marketing'),                   -- departmentID = 24
('Accounting'),                  -- departmentID = 25
('Design'),                      -- departmentID = 26
('Environmental Science'),       -- departmentID = 27
('Journalism'),                  -- departmentID = 28
('Philosophy'),                  -- departmentID = 29
('Public Health');               -- departmentID = 30


-- Insert data into Professor
INSERT INTO Professor (email, name, departmentID) VALUES 
('jdoe@northeastern.edu', 'John Doe', 1),          -- professorID = 1
('asmith@northeastern.edu', 'Alice Smith', 2),     -- professorID = 2
('bwong@northeastern.edu', 'Bob Wong', 3),         -- professorID = 3
('ejohnson@northeastern.edu', 'Emma Johnson', 1),  -- professorID = 4
('mlee@northeastern.edu', 'Michael Lee', 1),       -- professorID = 5
('scarter@northeastern.edu', 'Sophia Carter', 1),  -- professorID = 6
('dbrown@northeastern.edu', 'David Brown', 4),     -- professorID = 7
('odavis@northeastern.edu', 'Olivia Davis', 5),    -- professorID = 8
('wwilson@northeastern.edu', 'William Wilson', 6), -- professorID = 9
('jtaylor@northeastern.edu', 'James Taylor', 7),   -- professorID = 10
('imartinez@northeastern.edu', 'Isabella Martinez',8), -- professorID = 11
('bmoore@northeastern.edu', 'Benjamin Moore', 9),  -- professorID = 12
('cthomas@northeastern.edu', 'Charlotte Thomas', 10), -- professorID = 13
('hjackson@northeastern.edu', 'Henry Jackson', 11), -- professorID = 14
('gmartin@northeastern.edu', 'Grace Martin', 12),  -- professorID = 15
('alee@northeastern.edu', 'Alexander Lee', 13),    -- professorID = 16
('aharris@northeastern.edu', 'Amelia Harris', 14), -- professorID = 17
('lclark@northeastern.edu', 'Lucas Clark', 15),    -- professorID = 18
('mrodriguez@northeastern.edu', 'Mia Rodriguez', 16), -- professorID = 19
('jhernandez@northeastern.edu', 'Jacob Hernandez',1), -- professorID = 20
('lmartinez@northeastern.edu', 'Lily Martinez',1), -- professorID = 21
('jwilson@northeastern.edu', 'Joshua Wilson',4),   -- professorID = 22
('eanderson@northeastern.edu', 'Ethan Anderson',1),-- professorID = 23
('zthompson@northeastern.edu', 'Zoe Thompson',1),  -- professorID = 24
('mwhite@northeastern.edu', 'Mason White',1),      -- professorID = 25
('hking@northeastern.edu', 'Hannah King',1),       -- professorID = 26
('lscott@northeastern.edu', 'Logan Scott',1),      -- professorID = 27
('asmith2@northeastern.edu', 'Ava Smith',1),       -- professorID = 28
('jyoung@northeastern.edu', 'Jack Young',1),       -- professorID = 29
('ggonzalez@northeastern.edu', 'Grace Gonzalez',1),-- professorID = 30
('dbaker@northeastern.edu', 'Daniel Baker',1),     -- professorID = 31
('sjones@northeastern.edu', 'Sofia Jones',1),      -- professorID = 32
('mmiller@northeastern.edu', 'Matthew Miller',1),  -- professorID = 33
('cflores@northeastern.edu', 'Chloe Flores',1),    -- professorID = 34
('jlee@northeastern.edu', 'James Lee',1);          -- professorID = 35

-- Insert data into Course
INSERT INTO Course (description, name, professorID) VALUES 
('Database Design', 'CS3200', 1),            -- courseID = 1
('Advanced Algorithms', 'CS3000', 1),        -- courseID = 2
('Corporate Finance', 'FINA3301', 2),        -- courseID = 3
('Introduction to Computer Science', 'CS2500', 4), -- courseID = 4
('Computer Systems', 'CS3650', 5),           -- courseID = 5
('Machine Learning', 'CS4100', 6),           -- courseID = 6
('Data Mining', 'DS4100', 7),                -- courseID = 7
('Cybersecurity Fundamentals', 'CY2550', 8), -- courseID = 8
('Web Development', 'IS2000', 9),            -- courseID = 9
('Computer Architecture', 'CS4500', 10),     -- courseID = 10
('Artificial Intelligence', 'CS4120', 11),   -- courseID = 11
('Software Engineering', 'CS4800', 12),      -- courseID = 12
('Calculus I', 'MATH1341', 13),              -- courseID = 13
('Physics I', 'PHYS1151', 14),               -- courseID = 14
('Biology I', 'BIOL1111', 15),               -- courseID = 15
('Organic Chemistry', 'CHEM2311', 16),       -- courseID = 16
('Introduction to Psychology', 'PSYC1101', 17), -- courseID = 17
('English Composition', 'ENGW1111', 18),     -- courseID = 18
('Business Management', 'BUSN1101', 19),     -- courseID = 19
('Advanced Machine Learning', 'CS5100', 6),  -- courseID = 20
'Big Data Analytics', 'DS4200', 7),          -- courseID = 21
('Network Security', 'CY3550', 8),           -- courseID = 22
('Mobile App Development', 'CS5520', 23),    -- courseID = 23
('Cloud Computing', 'CS5610', 24),           -- courseID = 24
('Operating Systems', 'CS3700', 25),         -- courseID = 25
('Deep Learning', 'CS6200', 6),              -- courseID = 26
('Data Visualization', 'DS4300', 7),         -- courseID = 27
('Cryptography', 'CY4500', 8),               -- courseID = 28
('Embedded Systems', 'CS4620', 10),          -- courseID = 29
('Natural Language Processing', 'CS6120', 11), -- courseID = 30
('Software Project Management', 'CS4810', 12), -- courseID = 31
('Discrete Mathematics', 'MATH2331', 13),    -- courseID = 32
('Linear Algebra', 'MATH2341', 13),          -- courseID = 33
('Probability and Statistics', 'MATH3081', 13), -- courseID = 34
('Quantum Mechanics', 'PHYS2303', 14),       -- courseID = 35
('Genetics', 'BIOL2301', 15),                -- courseID = 36
('Physical Chemistry', 'CHEM3401', 16),      -- courseID = 37
('Cognitive Psychology', 'PSYC3404', 17),    -- courseID = 38
('Advanced Writing', 'ENGW3302', 18),        -- courseID = 39
('Entrepreneurship', 'BUSN2401', 19);        -- courseID = 40

-- Insert data into Skill
INSERT INTO Skill (name) VALUES 
('Python'),                   -- skillID = 1
('Java'),                     -- skillID = 2
('C++'),                      -- skillID = 3
('SQL'),                      -- skillID = 4
('Machine Learning'),         -- skillID = 5
('Data Analysis'),            -- skillID = 6
('Cybersecurity'),            -- skillID = 7
('Web Development'),          -- skillID = 8
('Artificial Intelligence'),  -- skillID = 9
('Software Engineering'),     -- skillID = 10
('Algorithms'),               -- skillID = 11
('Data Structures'),          -- skillID = 12
('Computer Architecture'),    -- skillID = 13
('Operating Systems'),        -- skillID = 14
('Networking'),               -- skillID = 15
('Big Data'),                 -- skillID = 16
('Cloud Computing'),          -- skillID = 17
('Mathematics'),              -- skillID = 18
('Physics'),                  -- skillID = 19
('Biology'),                  -- skillID = 20
('Chemistry'),                -- skillID = 21
('Psychology'),               -- skillID = 22
('Writing'),                  -- skillID = 23
('Communication'),            -- skillID = 24
('Business Management'),      -- skillID = 25
('Leadership'),               -- skillID = 26
('Project Management'),       -- skillID = 27
('Financial Analysis'),       -- skillID = 28
('Critical Thinking'),        -- skillID = 29
('Problem Solving');          -- skillID = 30

-- Insert data into Course_Skill
INSERT INTO Course_Skill (skillID, courseID, proficiencyLevel) VALUES
(4, 1, 4),     -- SQL for CS3200
(6, 1, 3),     -- Data Analysis for CS3200
(11, 2, 5),    -- Algorithms for CS3000
(30, 2, 5),    -- Problem Solving for CS3000
(1, 4, 3),     -- Python for CS2500
(12, 4, 3),    -- Data Structures for CS2500
(14, 5, 4),    -- Operating Systems for CS3650
(13, 5, 3),    -- Computer Architecture for CS3650
(5, 6, 5),     -- Machine Learning for CS4100
(1, 6, 4),     -- Python for CS4100
(6, 6, 4),     -- Data Analysis for CS4100
(6, 7, 4),     -- Data Analysis for DS4100
(16, 7, 4),    -- Big Data for DS4100
(7, 8, 4),     -- Cybersecurity for CY2550
(15, 8, 3),    -- Networking for CY2550
(8, 9, 4),     -- Web Development for IS2000
(13, 10, 5),   -- Computer Architecture for CS4500
(3, 10, 4),    -- C++ for CS4500
(9, 11, 5),    -- Artificial Intelligence for CS4120
(5, 11, 5),    -- Machine Learning for CS4120
(10,12,5),     -- Software Engineering for CS4800
(27,12,4),     -- Project Management for CS4800
(18,13,5),     -- Mathematics for MATH1341
(19,14,5),     -- Physics for PHYS1151
(20,15,5),     -- Biology for BIOL1111
(21,16,5),     -- Chemistry for CHEM2311
(22,17,5),     -- Psychology for PSYC1101
(23,18,5),     -- Writing for ENGW1111
(25,19,5),     -- Business Management for BUSN1101
(5,20,5),      -- Machine Learning for CS5100
(16,21,5),     -- Big Data for DS4200
(6,21,5),      -- Data Analysis for DS4200
(7,22,5),      -- Cybersecurity for CY3550
(15,22,4),     -- Networking for CY3550
(2,23,5),      -- Java for CS5520
(8,23,5),      -- Web Development for CS5520
(17,24,5),     -- Cloud Computing for CS5610
(4,24,4),      -- SQL for CS5610
(14,25,5),     -- Operating Systems for CS3700
(13,25,4),     -- Computer Architecture for CS3700
(5,26,5),      -- Machine Learning for CS6200
(9,26,5),      -- Artificial Intelligence for CS6200
(6,27,5),      -- Data Analysis for DS4300
(16,27,5),     -- Big Data for DS4300
(7,28,5),      -- Cybersecurity for CY4500
(29,28,4),     -- Critical Thinking for CY4500
(3,29,5),      -- C++ for CS4620
(13,29,5),     -- Computer Architecture for CS4620
(9,30,5),      -- Artificial Intelligence for CS6120
(23,39,5),     -- Writing for ENGW3302
(26,31,4),     -- Leadership for CS4810
(27,31,5),     -- Project Management for CS4810
(18,32,5),     -- Mathematics for MATH2331
(18,33,5),     -- Mathematics for MATH2341
(18,34,5),     -- Mathematics for MATH3081
(19,35,5),     -- Physics for PHYS2303
(20,36,5),     -- Biology for BIOL2301
(21,37,5),     -- Chemistry for CHEM3401
(22,38,5),     -- Psychology for PSYC3404
(6,40,3),      -- Data Analysis for BUSN2401
(25,40,4),     -- Business Management for BUSN2401
-- Add aditional 60 entries to reach 100 row guideline
(1,20,5),
(5,20,5),
(6,20,4),
(1,26,5),
(5,26,5),
(6,26,4),
(1,11,5),
(9,11,5),
(6,11,4),
(2,23,5),
(12,23,5),
(8,23,5),
(17,24,5),
(6,24,4),
(4,1,5),
(1,4,4),
(12,4,4),
(11,2,5),
(1,2,4),
(10,12,5),
(27,12,4),
(13,10,5),
(14,25,5),
(15,22,5),
(7,22,5),
(16,21,5),
(6,21,5),
(9,30,5),
(6,30,4),
(27,31,5),
(26,31,4),
(18,32,5),
(18,33,5),
(18,34,5),
(16,27,5),
(6,27,5),
(7,28,5),
(29,28,4),
(23,39,5),
(23,18,5),
(11,19,3),
(6,19,3),
(9,11,5),
(5,11,5),
(5,6,5),
(1,6,4),
(1,5,4),
(13,5,4),
(1,4,4),
(12,4,4),
(4,1,5),
(1,1,5),
(6,1,4),
(9,6,5),
(6,6,5),
(5,6,5),
(6,7,5),
(16,7,5),
(6,21,5),
(16,21,5),
(4,24,5),
(17,24,5),
(1,24,4),
(3,29,5),
(13,29,5),
(14,25,5),
(13,25,4),
(1,19,3),
(4,1,5),
(2,1,4),
(5,26,5),
(6,26,5),
(1,26,5),
(9,11,5),
(1,11,4),
(6,11,4),
(5,30,5),
(1,30,4),
(6,30,4),
(7,28,5),
(15,28,4),
(5,20,5),
(1,20,5),
(6,20,4),
(5,6,5),
(1,6,4),
(6,6,4),
(7,22,5),
(15,22,5),
(5,26,5),
(9,26,5),
(6,26,4),
(16,27,5),
(6,27,5),
(1,27,4),
(9,30,5),
(5,30,5),
(6,30,4),
(27,31,5),
(26,31,4),
(13,10,5),
(3,10,4),
(5,20,5),
(9,20,5),
(6,20,4);


-- Insert data into Student
INSERT INTO Student (email, name, GPA, major) VALUES 
('student1@northeastern.edu', 'Alice Green', 3.8, 'Computer Science'),   -- NUID = 1
('student2@northeastern.edu', 'Bob Brown', 3.5, 'Finance'),              -- NUID = 2
('student3@northeastern.edu', 'Charlie White', 3.7, 'Engineering'),      -- NUID = 3
('student4@northeastern.edu', 'David Smith', 3.6, 'Computer Science'),   -- NUID = 4
('student5@northeastern.edu', 'Emily Johnson', 3.9, 'Data Science'),     -- NUID = 5
('student6@northeastern.edu', 'Frank Williams', 3.2, 'Cybersecurity'),   -- NUID = 6
('student7@northeastern.edu', 'Grace Davis', 3.4, 'Information Systems'),-- NUID = 7
('student8@northeastern.edu', 'Henry Miller', 3.7, 'Computer Engineering'), -- NUID = 8
('student9@northeastern.edu', 'Isabella Wilson', 3.5, 'Artificial Intelligence'), -- NUID = 9
('student10@northeastern.edu', 'Jack Anderson', 3.3, 'Software Engineering'), -- NUID = 10
('student11@northeastern.edu', 'Karen Thomas', 3.8, 'Mathematics'),      -- NUID = 11
('student12@northeastern.edu', 'Liam Jackson', 3.1, 'Physics'),          -- NUID = 12
('student13@northeastern.edu', 'Mia Martin', 3.6, 'Biology'),            -- NUID = 13
('student14@northeastern.edu', 'Noah Lee', 3.5, 'Chemistry'),            -- NUID = 14
('student15@northeastern.edu', 'Olivia Perez', 3.9, 'Psychology'),       -- NUID = 15
('student16@northeastern.edu', 'Paul Young', 3.4, 'English'),            -- NUID = 16
('student17@northeastern.edu', 'Quinn Hernandez', 3.7, 'Business'),      -- NUID = 17
('student18@northeastern.edu', 'Rachel King', 3.2, 'Computer Science'),  -- NUID = 18
('student19@northeastern.edu', 'Samuel Scott', 3.8, 'Computer Science'), -- NUID = 19
('student20@northeastern.edu', 'Taylor Green', 3.6, 'Computer Science'), -- NUID = 20
('student21@northeastern.edu', 'Uma Harris', 3.7, 'Data Science'),       -- NUID = 21
('student22@northeastern.edu', 'Victor Clark', 3.5, 'Cybersecurity'),    -- NUID = 22
('student23@northeastern.edu', 'Wendy Lewis', 3.9, 'Artificial Intelligence'), -- NUID = 23
('student24@northeastern.edu', 'Xavier Robinson', 3.3, 'Software Engineering'), -- NUID = 24
('student25@northeastern.edu', 'Yvonne Walker', 3.6, 'Information Systems'), -- NUID = 25
('student26@northeastern.edu', 'Zachary Hall', 3.8, 'Computer Engineering'), -- NUID = 26
('student27@northeastern.edu', 'Ava Allen', 3.5, 'Data Science'),        -- NUID = 27
('student28@northeastern.edu', 'Benjamin Young', 3.4, 'Cybersecurity'),  -- NUID = 28
('student29@northeastern.edu', 'Charlotte Hill', 3.7, 'Computer Science'), -- NUID = 29
('student30@northeastern.edu', 'Daniel Adams', 3.5, 'Computer Science'), -- NUID = 30
('student31@northeastern.edu', 'Evelyn Baker', 3.9, 'Artificial Intelligence'), -- NUID = 31
('student32@northeastern.edu', 'George Carter', 3.2, 'Computer Engineering'), -- NUID = 32
('student33@northeastern.edu', 'Hannah Mitchell', 3.6, 'Software Engineering'), -- NUID = 33
('student34@northeastern.edu', 'Ian Nelson', 3.8, 'Computer Science'),   -- NUID = 34
('student35@northeastern.edu', 'Julia Roberts', 3.7, 'Data Science');    -- NUID = 35

-- Insert data into Student_Course
INSERT INTO Student_Course (NUID, courseID) VALUES 
(1, 1),   -- Alice Green enrolls in CS3200
(1, 4),   -- Alice Green enrolls in CS2500
(1, 5),   -- Alice Green enrolls in CS3650
(1, 6),   -- Alice Green enrolls in CS4100
(1, 2),   -- Alice Green enrolls in CS3000
(2, 3),   -- Bob Brown enrolls in FINA3301
(2, 19),  -- Bob Brown enrolls in BUSN1101
(2, 40),  -- Bob Brown enrolls in BUSN2401
(3, 14),  -- Charlie White enrolls in PHYS1151
(3, 32),  -- Charlie White enrolls in MATH2331
(4, 6),   -- David Smith enrolls in CS4100
(4, 20),  -- David Smith enrolls in CS5100
(4, 26),  -- David Smith enrolls in CS6200
(5, 7),   -- Emily Johnson enrolls in DS4100
(5, 21),  -- Emily Johnson enrolls in DS4200
(5, 27),  -- Emily Johnson enrolls in DS4300
(6, 8),   -- Frank Williams enrolls in CY2550
(6, 22),  -- Frank Williams enrolls in CY3550
(6, 28),  -- Frank Williams enrolls in CY4500
(7, 9),   -- Grace Davis enrolls in IS2000
(7, 23),  -- Grace Davis enrolls in CS5520
(7, 24),  -- Grace Davis enrolls in CS5610
(8, 10),  -- Henry Miller enrolls in CS4500
(8, 29),  -- Henry Miller enrolls in CS4620
(9, 11),  -- Isabella Wilson enrolls in CS4120
(9, 30),  -- Isabella Wilson enrolls in CS6120
(9, 6),   -- Isabella Wilson enrolls in CS4100
(10,12),  -- Jack Anderson enrolls in CS4800
(10,31),  -- Jack Anderson enrolls in CS4810
(10,25),  -- Jack Anderson enrolls in CS3700
(11,13),  -- Karen Thomas enrolls in MATH1341
(11,32),  -- Karen Thomas enrolls in MATH2331
(11,33),  -- Karen Thomas enrolls in MATH2341
(11,34),  -- Karen Thomas enrolls in MATH3081
(12,14),  -- Liam Jackson enrolls in PHYS1151
(12,35),  -- Liam Jackson enrolls in PHYS2303
(13,15),  -- Mia Martin enrolls in BIOL1111
(13,36),  -- Mia Martin enrolls in BIOL2301
(14,16),  -- Noah Lee enrolls in CHEM2311
(14,37),  -- Noah Lee enrolls in CHEM3401
(15,17),  -- Olivia Perez enrolls in PSYC1101
(15,38),  -- Olivia Perez enrolls in PSYC3404
(16,18),  -- Paul Young enrolls in ENGW1111
(16,39),  -- Paul Young enrolls in ENGW3302
(17,19),  -- Quinn Hernandez enrolls in BUSN1101
(17,40),  -- Quinn Hernandez enrolls in BUSN2401
(18,1),   -- Rachel King enrolls in CS3200
(18,4),   -- Rachel King enrolls in CS2500
(18,5),   -- Rachel King enrolls in CS3650
(19,2),   -- Samuel Scott enrolls in CS3000
(19,5),   -- Samuel Scott enrolls in CS3650
(19,12),  -- Samuel Scott enrolls in CS4800
(20,6),   -- Taylor Green enrolls in CS4100
(20,20),  -- Taylor Green enrolls in CS5100
(20,26),  -- Taylor Green enrolls in CS6200
(21,7),   -- Uma Harris enrolls in DS4100
(21,21),  -- Uma Harris enrolls in DS4200
(21,27),  -- Uma Harris enrolls in DS4300
(22,8),   -- Victor Clark enrolls in CY2550
(22,22),  -- Victor Clark enrolls in CY3550
(22,28),  -- Victor Clark enrolls in CY4500
(23,11),  -- Wendy Lewis enrolls in CS4120
(23,30),  -- Wendy Lewis enrolls in CS6120
(24,12),  -- Xavier Robinson enrolls in CS4800
(24,31),  -- Xavier Robinson enrolls in CS4810
(25,9),   -- Yvonne Walker enrolls in IS2000
(25,23),  -- Yvonne Walker enrolls in CS5520
(25,24),  -- Yvonne Walker enrolls in CS5610
(26,10),  -- Zachary Hall enrolls in CS4500
(26,29),  -- Zachary Hall enrolls in CS4620
(27,7),   -- Ava Allen enrolls in DS4100
(27,21),  -- Ava Allen enrolls in DS4200
(27,27),  -- Ava Allen enrolls in DS4300
(28,8),   -- Benjamin Young enrolls in CY2550
(28,22),  -- Benjamin Young enrolls in CY3550
(28,28),  -- Benjamin Young enrolls in CY4500
(29,1),   -- Charlotte Hill enrolls in CS3200
(29,4),   -- Charlotte Hill enrolls in CS2500
(29,6),   -- Charlotte Hill enrolls in CS4100
(30,2),   -- Daniel Adams enrolls in CS3000
(30,5),   -- Daniel Adams enrolls in CS3650
(30,12),  -- Daniel Adams enrolls in CS4800
(31,11),  -- Evelyn Baker enrolls in CS4120
(31,30),  -- Evelyn Baker enrolls in CS6120
(31,6),   -- Evelyn Baker enrolls in CS4100
(32,10),  -- George Carter enrolls in CS4500
(32,29),  -- George Carter enrolls in CS4620
(33,12),  -- Hannah Mitchell enrolls in CS4800
(33,31),  -- Hannah Mitchell enrolls in CS4810
(34,1),   -- Ian Nelson enrolls in CS3200
(34,4),   -- Ian Nelson enrolls in CS2500
(34,6),   -- Ian Nelson enrolls in CS4100
(35,7),   -- Julia Roberts enrolls in DS4100
(35,21),  -- Julia Roberts enrolls in DS4200
(35,27),  -- Julia Roberts enrolls in DS4300
-- Add additional enrollments to reach 100 row guideline
(1, 11),
(1, 12),
(1, 20),
(1, 26),
(4, 1),
(4, 2),
(4, 5),
(5, 4),
(5, 5),
(5, 6),
(6, 23),
(6, 24),
(6, 25),
(7, 1),
(7, 2),
(7, 4),
(8, 5),
(8, 6),
(8, 11),
(9, 12),
(9, 19),
(9, 20),
(10,1),
(10,2),
(10,5),
(11,6),
(11,11),
(11,12),
(12,1),
(12,2),
(12,4),
(13,7),
(13,21),
(13,27),
(14,8),
(14,22),
(14,28),
(15,9),
(15,23),
(15,24),
(16,10),
(16,29),
(16,25),
(17,1),
(17,2),
(17,5),
(18,6),
(18,11),
(18,12),
(19,20),
(19,26),
(19,30),
(20,2),
(20,5),
(20,12),
(21,6),
(21,7),
(21,27),
(22,8),
(22,22),
(22,28),
(23,6),
(23,20),
(23,26),
(24,2),
(24,5),
(24,12),
(25,9),
(25,23),
(25,24),
(26,10),
(26,29),
(26,25),
(27,6),
(27,21),
(27,27),
(28,8),
(28,22),
(28,28),
(29,1),
(29,2),
(29,4),
(30,5),
(30,6),
(30,12),
(31,6),
(31,11),
(31,12),
(32,10),
(32,29),
(32,25),
(33,12),
(33,31),
(33,25),
(34,5),
(34,6),
(34,11),
(35,7),
(35,21),
(35,27);

-- Insert data into Student_Skill
INSERT INTO Student_Skill (skillID, NUID, proficiencyLevel) VALUES
-- NUIDs 1-35 correspond to students in the Student table

-- Assigning skills to each student

-- For NUID 1 (Alice Green, Computer Science)
(1, 1, 5),  -- Python
(4, 1, 4),  -- SQL
(11, 1, 4), -- Algorithms
(12, 1, 5), -- Data Structures
(10, 1, 4), -- Software Engineering
(29, 1, 5), -- Critical Thinking
(30, 1, 5), -- Problem Solving
(27, 1, 4), -- Project Management

-- For NUID 2 (Bob Brown, Finance)
(28, 2, 5), -- Financial Analysis
(25, 2, 4), -- Business Management
(24, 2, 4), -- Communication
(27, 2, 4), -- Project Management
(26, 2, 4), -- Leadership

-- For NUID 3 (Charlie White, Engineering)
(18, 3, 5), -- Mathematics
(19, 3, 4), -- Physics
(13, 3, 3), -- Computer Architecture

-- For NUID 4 (David Smith, Computer Science)
(1, 4, 5),  -- Python
(2, 4, 4),  -- Java
(5, 4, 4),  -- Machine Learning
(11, 4, 4), -- Algorithms
(6, 4, 4),  -- Data Analysis
(12, 4, 4), -- Data Structures

-- For NUID 5 (Emily Johnson, Data Science)
(1, 5, 5),  -- Python
(6, 5, 5),  -- Data Analysis
(16, 5, 4), -- Big Data
(29, 5, 5), -- Critical Thinking
(18, 5, 4), -- Mathematics

-- For NUID 6 (Frank Williams, Cybersecurity)
(7, 6, 5),  -- Cybersecurity
(15, 6, 4), -- Networking
(14, 6, 4), -- Operating Systems
(4, 6, 3),  -- SQL
(1, 6, 3),  -- Python

-- For NUID 7 (Grace Davis, Information Systems)
(8, 7, 5),  -- Web Development
(24, 7, 4), -- Communication
(27, 7, 4), -- Project Management
(2, 7, 3),  -- Java
(4, 7, 3),  -- SQL

-- For NUID 8 (Henry Miller, Computer Engineering)
(3, 8, 5),  -- C++
(13, 8, 4), -- Computer Architecture
(14, 8, 4), -- Operating Systems
(2, 8, 3),  -- Java
(1, 8, 3),  -- Python

-- For NUID 9 (Isabella Wilson, Artificial Intelligence)
(1, 9, 5),  -- Python
(5, 9, 5),  -- Machine Learning
(9, 9, 5),  -- Artificial Intelligence
(6, 9, 4),  -- Data Analysis
(29, 9, 5), -- Critical Thinking
(30, 9, 5), -- Problem Solving

-- For NUID 10 (Jack Anderson, Software Engineering)
(2, 10, 5), -- Java
(10, 10, 5),-- Software Engineering
(27, 10, 4),-- Project Management
(29, 10, 4),-- Critical Thinking
(30, 10, 4),-- Problem Solving
-- Skills for some remaining Students
(18, 11, 4), -- Mathematics for Karen Thomas
(19, 12, 4), -- Physics for Liam Jackson
(20, 13, 4), -- Biology for Mia Martin
(21, 14, 4), -- Chemistry for Noah Lee
(22, 15, 4), -- Psychology for Olivia Perez
(23, 16, 4), -- Writing for Paul Young
(25, 17, 4), -- Business Management for Quinn Hernandez
(1, 18, 5),  -- Python for Rachel King
(12, 19, 4), -- Data Structures for Samuel Scott
(5, 20, 4),  -- Machine Learning for Taylor Green
(4, 21, 5),  -- SQL for Uma Harris
(7, 22, 4),  -- Cybersecurity for Victor Clark
(9, 23, 5),  -- Artificial Intelligence for Wendy Lewis
(2, 24, 4),  -- Java for Xavier Robinson
(8, 25, 5),  -- Web Development for Yvonne Walker
(3, 26, 5),  -- C++ for Zachary Hall
(16, 27, 4), -- Big Data for Ava Allen
(6, 28, 4),  -- Data Analysis for Benjamin Young
(10, 29, 4), -- Software Engineering for Charlotte Hill
(27, 30, 4), -- Project Management for Daniel Adams

-- Insert data into CoOp
INSERT INTO CoOp (jobTitle, companyName, industry) VALUES
('Software Developer Intern', 'Microsoft', 'Tech'),          -- jobID = 1
('Data Analyst Intern', 'Facebook', 'Tech'),                 -- jobID = 2
('Cybersecurity Analyst Intern', 'Cisco', 'Tech'),           -- jobID = 3
('Machine Learning Intern', 'Amazon', 'Tech'),               -- jobID = 4
('Web Developer Intern', 'Twitter', 'Tech'),                 -- jobID = 5
('AI Research Intern', 'OpenAI', 'Tech'),                    -- jobID = 6
('Software Engineering Intern', 'Apple', 'Tech'),            -- jobID = 7
('Cloud Computing Intern', 'Google', 'Tech'),                -- jobID = 8
('Data Scientist Intern', 'IBM', 'Tech'),                    -- jobID = 9
('Network Engineer Intern', 'Juniper Networks', 'Tech'),     -- jobID = 10
('Backend Developer Intern', 'LinkedIn', 'Tech'),            -- jobID = 11
('Full Stack Developer Intern', 'Adobe', 'Tech'),            -- jobID = 12
('DevOps Engineer Intern', 'Red Hat', 'Tech'),               -- jobID = 13
('Systems Analyst Intern', 'Oracle', 'Tech'),                -- jobID = 14
('QA Engineer Intern', 'Dropbox', 'Tech'),                   -- jobID = 15
('Database Administrator Intern', 'SAP', 'Tech'),            -- jobID = 16
('Mobile App Developer Intern', 'Uber', 'Tech'),             -- jobID = 17
('Game Developer Intern', 'Electronic Arts', 'Tech'),        -- jobID = 18
('Data Engineer Intern', 'Spotify', 'Tech'),                 -- jobID = 19
('Cybersecurity Research Intern', 'Symantec', 'Tech'),       -- jobID = 20
('Business Analyst Intern', 'Deloitte', 'Consulting'),       -- jobID = 21
('Financial Analyst Intern', 'Goldman Sachs', 'Finance'),    -- jobID = 22
('Marketing Intern', 'Procter & Gamble', 'Consumer Goods'),  -- jobID = 23
('Product Management Intern', 'Salesforce', 'Tech'),         -- jobID = 24
('IT Support Intern', 'Dell', 'Tech'),                       -- jobID = 25
('UX/UI Designer Intern', 'Pinterest', 'Tech'),              -- jobID = 26
('Cloud Infrastructure Intern', 'VMware', 'Tech'),           -- jobID = 27
('Artificial Intelligence Intern', 'Tesla', 'Automotive'),   -- jobID = 28
('Robotics Intern', 'Boston Dynamics', 'Tech'),              -- jobID = 29
('Data Visualization Intern', 'Tableau', 'Tech'),            -- jobID = 30
('Machine Learning Engineer Intern', 'NVIDIA', 'Tech'),      -- jobID = 31
('Network Security Intern', 'Palo Alto Networks', 'Tech'),   -- jobID = 32
('Computer Vision Intern', 'Intel', 'Tech'),                 -- jobID = 33
('Natural Language Processing Intern', 'Amazon Alexa', 'Tech'), -- jobID = 34
('Embedded Systems Intern', 'Qualcomm', 'Tech'),             -- jobID = 35
('Blockchain Developer Intern', 'IBM', 'Tech'),              -- jobID = 36
('Cybersecurity Analyst Intern', 'CrowdStrike', 'Tech'),     -- jobID = 37
('Database Developer Intern', 'MongoDB', 'Tech'),            -- jobID = 38
('Software QA Intern', 'Atlassian', 'Tech'),                 -- jobID = 39
('Data Science Intern', 'Airbnb', 'Tech');                   -- jobID = 40

-- Insert data into CoOp_Skill
INSERT INTO CoOp_Skill (skillID, jobID, proficiencyLevel) VALUES
-- jobID 1: Software Developer Intern at Microsoft
(1, 1, 5),  -- Python
(2, 1, 5),  -- Java
(12, 1, 5), -- Data Structures
(11, 1, 5), -- Algorithms

-- jobID 2: Data Analyst Intern at Facebook
(1, 2, 5),  -- Python
(4, 2, 5),  -- SQL
(6, 2, 5),  -- Data Analysis
(16, 2, 4), -- Big Data

-- jobID 3: Cybersecurity Analyst Intern at Cisco
(7, 3, 5),  -- Cybersecurity
(15, 3, 4), -- Networking
(14, 3, 4), -- Operating Systems

-- jobID 4: Machine Learning Intern at Amazon
(5, 4, 5),  -- Machine Learning
(1, 4, 5),  -- Python
(9, 4, 5),  -- Artificial Intelligence
(6, 4, 4),  -- Data Analysis

-- jobID 5: Web Developer Intern at Twitter
(8, 5, 5),  -- Web Development
(4, 5, 4),  -- SQL
(2, 5, 4),  -- Java
(23, 5, 4), -- Writing

-- jobID 6: AI Research Intern at OpenAI
(9, 6, 5),  -- Artificial Intelligence
(5, 6, 5),  -- Machine Learning
(1, 6, 5),  -- Python
(29, 6, 5), -- Critical Thinking

-- jobID 7: Software Engineering Intern at Apple
(10, 7, 5), -- Software Engineering
(1, 7, 5),  -- Python
(27, 7, 4), -- Project Management
(30, 7, 5), -- Problem Solving

-- jobID 8: Cloud Computing Intern at Google
(17, 8, 5), -- Cloud Computing
(4, 8, 5),  -- SQL
(6, 8, 4),  -- Data Analysis
(15, 8, 4), -- Networking

-- jobID 9: Data Scientist Intern at IBM
(1, 9, 5),  -- Python
(6, 9, 5),  -- Data Analysis
(16, 9, 4), -- Big Data
(18, 9, 5), -- Mathematics

-- jobID 10: Network Engineer Intern at Juniper Networks
(15, 10, 5),-- Networking
(7, 10, 4),  -- Cybersecurity
(14, 10, 4), -- Operating Systems

-- jobID 11: Backend Developer Intern at LinkedIn
(1, 11, 5),  -- Python
(2, 11, 5),  -- Java
(12, 11, 4), -- Data Structures
(4, 11, 4),  -- SQL

-- jobID 12: Full Stack Developer Intern at Adobe
(8, 12, 5),  -- Web Development
(2, 12, 4),  -- Java
(1, 12, 4),  -- Python
(27, 12, 4), -- Project Management

-- jobID 13: DevOps Engineer Intern at Red Hat
(14, 13, 5), -- Operating Systems
(15, 13, 4), -- Networking
(1, 13, 4),  -- Python

-- jobID 14: Systems Analyst Intern at Oracle
(25, 14, 4), -- Business Management
(6, 14, 4),  -- Data Analysis
(27, 14, 4), -- Project Management

-- jobID 15: QA Engineer Intern at Dropbox
(10, 15, 5), -- Software Engineering
(30, 15, 4), -- Problem Solving
(1, 15, 4),  -- Python

-- jobID 16: Database Administrator Intern at SAP
(4, 16, 5),  -- SQL
(6, 16, 5),  -- Data Analysis
(16, 16, 4), -- Big Data

-- jobID 17: Mobile App Developer Intern at Uber
(2, 17, 5),  -- Java
(8, 17, 5),  -- Web Development
(1, 17, 4),  -- Python

-- jobID 18: Game Developer Intern at Electronic Arts
(3, 18, 5),  -- C++
(12, 18, 4), -- Data Structures
(30, 18, 4), -- Problem Solving

-- jobID 19: Data Engineer Intern at Spotify
(1, 19, 5),  -- Python
(16, 19, 5), -- Big Data
(6, 19, 5),  -- Data Analysis

-- jobID 20: Cybersecurity Research Intern at Symantec
(7, 20, 5),  -- Cybersecurity
(14, 20, 4), -- Operating Systems
(15, 20, 4), -- Networking

-- jobID 21: Business Analyst Intern at Deloitte
(25, 21, 5), -- Business Management
(28, 21, 4), -- Financial Analysis
(27, 21, 4), -- Project Management

-- jobID 22: Financial Analyst Intern at Goldman Sachs
(28, 22, 5), -- Financial Analysis
(25, 22, 4), -- Business Management
(30, 22, 4), -- Problem Solving

-- jobID 23: Marketing Intern at Procter & Gamble
(29, 23, 5), -- Critical Thinking
(24, 23, 4), -- Communication
(25, 23, 4), -- Business Management

-- jobID 24: Product Management Intern at Salesforce
(27, 24, 5), -- Project Management
(25, 24, 5), -- Business Management
(29, 24, 4), -- Critical Thinking

-- Adding additional rows for multiple skills per jobID
(7, 3, 4),    -- Additional Cybersecurity for jobID 3
(1, 4, 4),    -- Python for jobID 4
(4, 5, 5),    -- SQL for jobID 5
(9, 6, 5),    -- AI for jobID 6
(10, 7, 5),   -- Software Engineering for jobID 7
(17, 8, 5),   -- Cloud Computing for jobID 8
(1, 9, 5),    -- Python for jobID 9
(15, 10, 4),  -- Networking for jobID 10
(2, 11, 5),   -- Java for jobID 11
(8, 12, 5),   -- Web Development for jobID 12
(14, 13, 5),  -- Operating Systems for jobID 13
(27, 14, 4),  -- Project Management for jobID 14
(30, 15, 4),  -- Problem Solving for jobID 15
(4, 16, 5),   -- SQL for jobID 16
(2, 17, 5),   -- Java for jobID 17
(12, 18, 4),  -- Data Structures for jobID 18
(1, 19, 5),   -- Python for jobID 19
(7, 20, 5);   -- Cybersecurity for jobID 20


-- Insert data into Employer
INSERT INTO Employer (contactEmail, contactPhone, contactName, industry) VALUES
('hr@microsoft.com', '425-555-1234', 'Microsoft HR', 'Tech'),          -- employerID = 1
('hr@facebook.com', '650-555-5678', 'Facebook HR', 'Tech'),            -- employerID = 2
('hr@cisco.com', '408-555-7890', 'Cisco HR', 'Tech'),                  -- employerID = 3
('hr@amazon.com', '206-555-0001', 'Amazon HR', 'Tech'),                -- employerID = 4
('hr@twitter.com', '415-555-1234', 'Twitter HR', 'Tech'),              -- employerID = 5
('hr@openai.com', '888-555-4321', 'OpenAI HR', 'Tech'),                -- employerID = 6
('hr@apple.com', '408-555-6789', 'Apple HR', 'Tech'),                  -- employerID = 7
('hr@google.com', '650-555-8765', 'Google HR', 'Tech'),                -- employerID = 8
('hr@ibm.com', '914-555-7890', 'IBM HR', 'Tech'),                      -- employerID = 9
('hr@juniper.com', '669-555-1234', 'Juniper Networks HR', 'Tech'),     -- employerID = 10
('hr@linkedin.com', '650-555-7891', 'LinkedIn HR', 'Tech'),            -- employerID = 11
('hr@adobe.com', '415-555-5678', 'Adobe HR', 'Tech'),                  -- employerID = 12
('hr@redhat.com', '919-555-4321', 'Red Hat HR', 'Tech'),               -- employerID = 13
('hr@oracle.com', '650-555-9876', 'Oracle HR', 'Tech'),                -- employerID = 14
('hr@dropbox.com', '415-555-8765', 'Dropbox HR', 'Tech'),              -- employerID = 15
('hr@sap.com', '800-555-0000', 'SAP HR', 'Tech'),                      -- employerID = 16
('hr@uber.com', '415-555-6543', 'Uber HR', 'Tech'),                    -- employerID = 17
('hr@ea.com', '650-555-6789', 'Electronic Arts HR', 'Tech'),           -- employerID = 18
('hr@spotify.com', '212-555-3456', 'Spotify HR', 'Tech'),              -- employerID = 19
('hr@symantec.com', '650-555-4321', 'Symantec HR', 'Tech'),            -- employerID = 20
('hr@deloitte.com', '212-555-7654', 'Deloitte HR', 'Consulting'),      -- employerID = 21
('hr@goldmansachs.com', '212-555-0000', 'Goldman Sachs HR', 'Finance'),-- employerID = 22
('hr@pg.com', '513-555-1234', 'Procter & Gamble HR', 'Consumer Goods'),-- employerID = 23
('hr@salesforce.com', '415-555-8765', 'Salesforce HR', 'Tech'),        -- employerID = 24
('hr@dell.com', '512-555-9876', 'Dell HR', 'Tech'),                    -- employerID = 25
('hr@pinterest.com', '415-555-5432', 'Pinterest HR', 'Tech'),          -- employerID = 26
('hr@vmware.com', '877-555-8765', 'VMware HR', 'Tech'),                -- employerID = 27
('hr@tesla.com', '650-555-0001', 'Tesla HR', 'Automotive'),            -- employerID = 28
('hr@bostondynamics.com', '617-555-9876', 'Boston Dynamics HR', 'Tech'),-- employerID = 29
('hr@tableau.com', '206-555-6789', 'Tableau HR', 'Tech'),              -- employerID = 30
('hr@nvidia.com', '408-555-7654', 'NVIDIA HR', 'Tech'),                -- employerID = 31
('hr@paloaltonetworks.com', '408-555-1234', 'Palo Alto Networks HR', 'Tech'), -- employerID = 32
('hr@intel.com', '408-555-6789', 'Intel HR', 'Tech'),                  -- employerID = 33
('hr@amazonalexa.com', '206-555-3456', 'Amazon Alexa HR', 'Tech'),     -- employerID = 34
('hr@qualcomm.com', '858-555-4321', 'Qualcomm HR', 'Tech'),            -- employerID = 35;

-- Insert data into Employer_CoOp
INSERT INTO Employer_CoOp (employerID, jobID) VALUES
(1, 1),   -- Microsoft offers Software Developer Intern
(1, 24),  -- Microsoft offers Product Management Intern
(2, 2),   -- Facebook offers Data Analyst Intern
(2, 30),  -- Facebook offers Data Visualization Intern
(3, 3),   -- Cisco offers Cybersecurity Analyst Intern
(3, 37),  -- Cisco offers Cybersecurity Analyst Intern at CrowdStrike
(4, 4),   -- Amazon offers Machine Learning Intern
(4, 34),  -- Amazon Alexa offers NLP Intern
(5, 5),   -- Twitter offers Web Developer Intern
(6, 6),   -- OpenAI offers AI Research Intern
(6, 28),  -- Tesla offers AI Intern
(7, 7),   -- Apple offers Software Engineering Intern
(8, 8),   -- Google offers Cloud Computing Intern
(8, 9),   -- IBM offers Data Scientist Intern
(9, 36),  -- IBM offers Blockchain Developer Intern
(10, 10), -- Juniper Networks offers Network Engineer Intern
(11, 11), -- LinkedIn offers Backend Developer Intern
(12, 12), -- Adobe offers Full Stack Developer Intern
(13, 13), -- Red Hat offers DevOps Engineer Intern
(14, 14), -- Oracle offers Systems Analyst Intern
(15, 15), -- Dropbox offers QA Engineer Intern
(16, 16), -- SAP offers Database Administrator Intern
(17, 17), -- Uber offers Mobile App Developer Intern
(18, 18), -- Electronic Arts offers Game Developer Intern
(19, 19), -- Spotify offers Data Engineer Intern
(20, 20), -- Symantec offers Cybersecurity Research Intern
(21, 21), -- Deloitte offers Business Analyst Intern
(22, 22), -- Goldman Sachs offers Financial Analyst Intern
(23, 23), -- Procter & Gamble offers Marketing Intern
(24, 24), -- Salesforce offers Product Management Intern
(25, 25), -- Dell offers IT Support Intern
(26, 26), -- Pinterest offers UX/UI Designer Intern
(27, 27), -- VMware offers Cloud Infrastructure Intern
(28, 29), -- Boston Dynamics offers Robotics Intern
(29, 30), -- Tableau offers Data Visualization Intern
(30, 31), -- NVIDIA offers Machine Learning Engineer Intern
(31, 32), -- Palo Alto Networks offers Network Security Intern
(32, 33), -- Intel offers Computer Vision Intern
(33, 34), -- Amazon Alexa offers NLP Intern
(34, 35), -- Qualcomm offers Embedded Systems Intern
(35, 1),  -- Microsoft offers another Software Developer Intern

-- Add additional entries to reach at least 100
(4, 36),  -- Amazon Blockchain Developer Intern
(9, 8),   -- IBM Cloud Computing Intern
(15, 15), -- Dropbox QA Intern
(25, 25), -- Dell IT Support Intern
(6, 28),  -- OpenAI AI Research Intern
(7, 7),   -- Apple Software Engineer Intern
(9, 9),   -- IBM Data Scientist Intern
(26, 26), -- Pinterest UX/UI Designer Intern
(10, 10), -- Juniper Networks Network Engineer Intern
(17, 17), -- Uber Mobile App Developer Intern
(29, 29), -- Boston Dynamics Robotics Intern
(1, 1),   -- Microsoft Software Developer Intern
(13, 13), -- Red Hat DevOps Engineer Intern
(8, 31),  -- Google Machine Learning Engineer Intern
(14, 14), -- Oracle Systems Analyst Intern
(21, 21), -- Deloitte Business Analyst Intern
(5, 5),   -- Twitter Web Developer Intern
(3, 3),   -- Cisco Cybersecurity Analyst Intern
(27, 27), -- VMware Cloud Infrastructure Intern
(22, 22), -- Goldman Sachs Financial Analyst Intern;

-- Insert data into CoOpAdvisor
INSERT INTO CoOpAdvisor (email, name, departmentID) VALUES
('advisor1@northeastern.edu', 'Emily Reed', 1),  -- advisorID = 1
('advisor2@northeastern.edu', 'Michael Clark', 1), -- advisorID = 2
('advisor3@northeastern.edu', 'Sarah Lewis', 1), -- advisorID = 3
('advisor4@northeastern.edu', 'Joshua Scott', 4), -- advisorID = 4
('advisor5@northeastern.edu', 'Olivia Martinez', 5), -- advisorID = 5
('advisor6@northeastern.edu', 'Liam Carter', 1), -- advisorID = 6
('advisor7@northeastern.edu', 'Sophia Davis', 2), -- advisorID = 7
('advisor8@northeastern.edu', 'Mia Johnson', 3), -- advisorID = 8
('advisor9@northeastern.edu', 'Henry Brown', 1), -- advisorID = 9
('advisor10@northeastern.edu', 'Isabella Wilson', 6), -- advisorID = 10
('advisor11@northeastern.edu', 'Daniel White', 1), -- advisorID = 11
('advisor12@northeastern.edu', 'Grace Hill', 1), -- advisorID = 12
('advisor13@northeastern.edu', 'Jack Young', 1), -- advisorID = 13
('advisor14@northeastern.edu', 'Emma King', 4), -- advisorID = 14
('advisor15@northeastern.edu', 'Benjamin Wright', 7), -- advisorID = 15
('advisor16@northeastern.edu', 'Ava Lopez', 8), -- advisorID = 16
('advisor17@northeastern.edu', 'William Gonzales', 1), -- advisorID = 17
('advisor18@northeastern.edu', 'Ethan Perez', 9), -- advisorID = 18
('advisor19@northeastern.edu', 'Harper Adams', 3), -- advisorID = 19
('advisor20@northeastern.edu', 'Ella Rodriguez', 2), -- advisorID = 20
('advisor21@northeastern.edu', 'Logan Campbell', 1), -- advisorID = 21
('advisor22@northeastern.edu', 'Mason Lee', 1), -- advisorID = 22
('advisor23@northeastern.edu', 'Amelia Taylor', 1), -- advisorID = 23
('advisor24@northeastern.edu', 'Lucas Martin', 4), -- advisorID = 24
('advisor25@northeastern.edu', 'Zoe Walker', 5), -- advisorID = 25
('advisor26@northeastern.edu', 'Nathan Moore', 6), -- advisorID = 26
('advisor27@northeastern.edu', 'Abigail Harris', 7), -- advisorID = 27
('advisor28@northeastern.edu', 'Henry Thompson', 1), -- advisorID = 28
('advisor29@northeastern.edu', 'Chloe Anderson', 1), -- advisorID = 29
('advisor30@northeastern.edu', 'Lily Brooks', 4); -- advisorID = 30

-- Insert data into AdvisorStudent
INSERT INTO AdvisorStudent (NUID, advisorID) VALUES
-- Student assigned to Co-Op Advisor
(1, 1),  -- Alice Green assigned to Emily Reed
(1, 2),  -- Alice Green also assigned to Michael Clark
(2, 7),  -- Bob Brown assigned to Sophia Davis
(2, 20), -- Bob Brown also assigned to Ella Rodriguez
(3, 8),  -- Charlie White assigned to Mia Johnson
(3, 9),  -- Charlie White also assigned to Henry Brown
(4, 1),  -- David Smith assigned to Emily Reed
(4, 6),  -- David Smith also assigned to Liam Carter
(5, 4),  -- Emily Johnson assigned to Joshua Scott
(5, 14), -- Emily Johnson also assigned to Emma King
(6, 5),  -- Frank Williams assigned to Olivia Martinez
(6, 25), -- Frank Williams also assigned to Zoe Walker
(7, 10), -- Grace Davis assigned to Isabella Wilson
(7, 26), -- Grace Davis also assigned to Nathan Moore
(8, 15), -- Henry Miller assigned to Benjamin Wright
(8, 27), -- Henry Miller also assigned to Abigail Harris
(9, 16), -- Isabella Wilson assigned to Ava Lopez
(9, 11), -- Isabella Wilson also assigned to Daniel White
(10, 17),-- Jack Anderson assigned to William Gonzales
(10, 13),-- Jack Anderson also assigned to Jack Young
(11, 18),-- Karen Thomas assigned to Ethan Perez
(11, 29),-- Karen Thomas also assigned to Chloe Anderson
(12, 19),-- Liam Jackson assigned to Harper Adams
(12, 3), -- Liam Jackson also assigned to Sarah Lewis
(13, 23),-- Mia Martin assigned to Amelia Taylor
(13, 24),-- Mia Martin also assigned to Lucas Martin
(14, 5), -- Noah Lee assigned to Olivia Martinez
(14, 28),-- Noah Lee also assigned to Henry Thompson
(15, 20),-- Olivia Perez assigned to Ella Rodriguez
(15, 6), -- Olivia Perez also assigned to Liam Carter
(16, 2), -- Paul Young assigned to Michael Clark
(16, 8), -- Paul Young also assigned to Mia Johnson
(17, 21),-- Quinn Hernandez assigned to Logan Campbell
(17, 7), -- Quinn Hernandez also assigned to Sophia Davis
(18, 4), -- Rachel King assigned to Joshua Scott
(18, 10),-- Rachel King also assigned to Isabella Wilson
(19, 13),-- Samuel Scott assigned to Jack Young
(19, 17),-- Samuel Scott also assigned to William Gonzales
(20, 14),-- Taylor Green assigned to Emma King
(20, 18),-- Taylor Green also assigned to Ethan Perez
(21, 22),-- Uma Harris assigned to Mason Lee
(21, 1), -- Uma Harris also assigned to Emily Reed
(22, 15),-- Victor Clark assigned to Benjamin Wright
(22, 19),-- Victor Clark also assigned to Harper Adams
(23, 16),-- Wendy Lewis assigned to Ava Lopez
(23, 9), -- Wendy Lewis also assigned to Henry Brown
(24, 27),-- Xavier Robinson assigned to Abigail Harris
(24, 11),-- Xavier Robinson also assigned to Daniel White
(25, 25),-- Yvonne Walker assigned to Zoe Walker
(25, 3), -- Yvonne Walker also assigned to Sarah Lewis
(26, 28),-- Zachary Hall assigned to Henry Thompson
(26, 24),-- Zachary Hall also assigned to Lucas Martin
(27, 6), -- Ava Allen assigned to Liam Carter
(27, 7), -- Ava Allen also assigned to Sophia Davis
(28, 29),-- Benjamin Young assigned to Chloe Anderson
(28, 12),-- Benjamin Young also assigned to Grace Hill
(29, 2), -- Charlotte Hill assigned to Michael Clark
(29, 5), -- Charlotte Hill also assigned to Olivia Martinez
(30, 20),-- Daniel Adams assigned to Ella Rodriguez
(30, 4), -- Daniel Adams also assigned to Joshua Scott
(31, 16),-- Evelyn Baker assigned to Ava Lopez
(31, 17),-- Evelyn Baker also assigned to William Gonzales
(32, 15),-- George Carter assigned to Benjamin Wright
(32, 19),-- George Carter also assigned to Harper Adams
(33, 14),-- Hannah Mitchell assigned to Emma King
(33, 13),-- Hannah Mitchell also assigned to Jack Young
(34, 21),-- Ian Nelson assigned to Logan Campbell
(34, 24),-- Ian Nelson also assigned to Lucas Martin
(35, 23),-- Julia Roberts assigned to Amelia Taylor
(35, 30);-- Julia Roberts also assigned to Lily Brooks

-- Insert data into AdvisorEmployer
INSERT INTO AdvisorEmployer (employerID, advisorID) VALUES
(1, 1),   -- Microsoft assigned to Emily Reed
(1, 2),   -- Microsoft also assigned to Michael Clark
(2, 3),   -- Facebook assigned to Sarah Lewis
(2, 6),   -- Facebook also assigned to Liam Carter
(3, 4),   -- Cisco assigned to Joshua Scott
(3, 5),   -- Cisco also assigned to Olivia Martinez
(4, 6),   -- Amazon assigned to Liam Carter
(4, 7),   -- Amazon also assigned to Sophia Davis
(5, 8),   -- Twitter assigned to Mia Johnson
(5, 9),   -- Twitter also assigned to Henry Brown
(6, 10),  -- OpenAI assigned to Isabella Wilson
(6, 11),  -- OpenAI also assigned to Daniel White
(7, 12),  -- Apple assigned to Grace Hill
(7, 13),  -- Apple also assigned to Jack Young
(8, 14),  -- Google assigned to Emma King
(8, 15),  -- Google also assigned to Benjamin Wright
(9, 16),  -- IBM assigned to Ava Lopez
(9, 17),  -- IBM also assigned to William Gonzales
(10, 18), -- Juniper Networks assigned to Ethan Perez
(10, 19), -- Juniper Networks also assigned to Harper Adams
(11, 20), -- LinkedIn assigned to Ella Rodriguez
(11, 21), -- LinkedIn also assigned to Logan Campbell
(12, 22), -- Adobe assigned to Mason Lee
(12, 23), -- Adobe also assigned to Amelia Taylor
(13, 24), -- Red Hat assigned to Lucas Martin
(13, 25), -- Red Hat also assigned to Zoe Walker
(14, 26), -- Oracle assigned to Nathan Moore
(14, 27), -- Oracle also assigned to Abigail Harris
(15, 28), -- Dropbox assigned to Henry Thompson
(15, 29), -- Dropbox also assigned to Chloe Anderson
(16, 30), -- SAP assigned to Lily Brooks
(16, 1),  -- SAP also assigned to Emily Reed
(17, 2),  -- Uber assigned to Michael Clark
(17, 3),  -- Uber also assigned to Sarah Lewis
(18, 4),  -- Electronic Arts assigned to Joshua Scott
(18, 5),  -- Electronic Arts also assigned to Olivia Martinez
(19, 6),  -- Spotify assigned to Liam Carter
(19, 7),  -- Spotify also assigned to Sophia Davis
(20, 8),  -- Symantec assigned to Mia Johnson
(20, 9),  -- Symantec also assigned to Henry Brown
(21, 10), -- Deloitte assigned to Isabella Wilson
(21, 11), -- Deloitte also assigned to Daniel White
(22, 12), -- Goldman Sachs assigned to Grace Hill
(22, 13), -- Goldman Sachs also assigned to Jack Young
(23, 14), -- Procter & Gamble assigned to Emma King
(23, 15), -- Procter & Gamble also assigned to Benjamin Wright
(24, 16), -- Salesforce assigned to Ava Lopez
(24, 17), -- Salesforce also assigned to William Gonzales
(25, 18), -- Dell assigned to Ethan Perez
(25, 19), -- Dell also assigned to Harper Adams
(26, 20), -- Pinterest assigned to Ella Rodriguez
(26, 21), -- Pinterest also assigned to Logan Campbell
(27, 22), -- VMware assigned to Mason Lee
(27, 23), -- VMware also assigned to Amelia Taylor
(28, 24), -- Tesla assigned to Lucas Martin
(28, 25), -- Tesla also assigned to Zoe Walker
(29, 26), -- Boston Dynamics assigned to Nathan Moore
(29, 27), -- Boston Dynamics also assigned to Abigail Harris
(30, 28), -- Tableau assigned to Henry Thompson
(30, 29), -- Tableau also assigned to Chloe Anderson
(31, 30), -- NVIDIA assigned to Lily Brooks
(31, 1),  -- NVIDIA also assigned to Emily Reed
(32, 2),  -- Palo Alto Networks assigned to Michael Clark
(32, 3),  -- Palo Alto Networks also assigned to Sarah Lewis
(33, 4),  -- Intel assigned to Joshua Scott
(33, 5),  -- Intel also assigned to Olivia Martinez
(34, 6),  -- Amazon Alexa assigned to Liam Carter
(34, 7),  -- Amazon Alexa also assigned to Sophia Davis
(35, 8),  -- Qualcomm assigned to Mia Johnson
(35, 9),  -- Qualcomm also assigned to Henry Brown
(8, 14),  -- Google assigned to Emma King
(8, 2),   -- Google also assigned to Michael Clark
(7, 17),  -- Apple assigned to William Gonzales
(5, 8),   -- Twitter assigned to Mia Johnson
(15, 28), -- Dropbox assigned to Henry Thompson
(14, 24), -- Oracle assigned to Lucas Martin
(12, 23), -- Adobe assigned to Amelia Taylor
(10, 19), -- Juniper Networks assigned to Harper Adams
(9, 16),  -- IBM assigned to Ava Lopez
(11, 22), -- LinkedIn assigned to Mason Lee
(17, 27), -- Uber assigned to Abigail Harris
(20, 10), -- Symantec assigned to Isabella Wilson
(30, 1),  -- Tableau assigned to Emily Reed
(25, 15), -- Dell assigned to Benjamin Wright
(19, 6),  -- Spotify assigned to Liam Carter;

-- Insert data into Course_Professor
INSERT INTO Course_Professor (courseID, professorID) VALUES
(1, 1),  -- CS3200 taught by John Doe
(1, 4),  -- CS3200 also taught by Emma Johnson
(2, 1),  -- CS3000 taught by John Doe
(2, 5),  -- CS3000 also taught by Michael Lee
(3, 2),  -- FINA3301 taught by Alice Smith
(4, 4),  -- CS2500 taught by Emma Johnson
(5, 5),  -- CS3650 taught by Michael Lee
(6, 6),  -- CS4100 taught by Sophia Carter
(7, 7),  -- DS4100 taught by David Brown
(8, 8),  -- CY2550 taught by Olivia Davis
(9, 9),  -- IS2000 taught by William Wilson
(10, 10), -- CS4500 taught by James Taylor
(11, 11), -- CS4120 taught by Isabella Martinez
(12, 12), -- CS4800 taught by Benjamin Moore
(13, 13), -- MATH1341 taught by Charlotte Thomas
(14, 14), -- PHYS1151 taught by Henry Jackson
(15, 15), -- BIOL1111 taught by Grace Martin
(16, 16), -- CHEM2311 taught by Alexander Lee
(17, 17), -- PSYC1101 taught by Amelia Harris
(18, 18), -- ENGW1111 taught by Lucas Clark
(19, 19), -- BUSN1101 taught by Mia Rodriguez
(20, 6),  -- CS5100 taught by Sophia Carter
(21, 7),  -- DS4200 taught by David Brown
(22, 8),  -- CY3550 taught by Olivia Davis
(23, 9),  -- CS5520 taught by William Wilson
(24, 10), -- CS5610 taught by James Taylor
(25, 5),  -- CS3700 taught by Michael Lee
(26, 6),  -- CS6200 taught by Sophia Carter
(27, 7),  -- DS4300 taught by David Brown
(28, 8),  -- CY4500 taught by Olivia Davis
(29, 10), -- CS4620 taught by James Taylor
(30, 11), -- CS6120 taught by Isabella Martinez
(31, 12), -- CS4810 taught by Benjamin Moore
(32, 13), -- MATH2331 taught by Charlotte Thomas
(33, 13), -- MATH2341 taught by Charlotte Thomas
(34, 13), -- MATH3081 taught by Charlotte Thomas
(35, 14), -- PHYS2303 taught by Henry Jackson
(36, 15), -- BIOL2301 taught by Grace Martin
(37, 16), -- CHEM3401 taught by Alexander Lee
(38, 17), -- PSYC3404 taught by Amelia Harris
(39, 18), -- ENGW3302 taught by Lucas Clark
(40, 19), -- BUSN2401 taught by Mia Rodriguez
(1, 2),   -- CS3200 also taught by Alice Smith
(2, 3),   -- CS3000 also taught by Bob Wong
(3, 5),   -- FINA3301 also taught by Michael Lee
(4, 1),   -- CS2500 also taught by John Doe
(5, 2),   -- CS3650 also taught by Alice Smith
(6, 3),   -- CS4100 also taught by Bob Wong
(7, 4),   -- DS4100 also taught by Emma Johnson
(8, 5),   -- CY2550 also taught by Michael Lee
(9, 6),   -- IS2000 also taught by Sophia Carter
(10, 7),  -- CS4500 also taught by David Brown
(11, 8),  -- CS4120 also taught by Olivia Davis
(12, 9),  -- CS4800 also taught by William Wilson
(13, 10), -- MATH1341 also taught by James Taylor
(14, 11), -- PHYS1151 also taught by Isabella Martinez
(15, 12), -- BIOL1111 also taught by Benjamin Moore
(16, 13), -- CHEM2311 also taught by Charlotte Thomas
(17, 14), -- PSYC1101 also taught by Henry Jackson
(18, 15), -- ENGW1111 also taught by Grace Martin
(19, 16), -- BUSN1101 also taught by Alexander Lee
(20, 17), -- CS5100 also taught by Amelia Harris
(21, 18), -- DS4200 also taught by Lucas Clark
(22, 19), -- CY3550 also taught by Mia Rodriguez
(23, 12), -- CS5520 also taught by Benjamin Moore
(24, 13), -- CS5610 also taught by Charlotte Thomas
(25, 14), -- CS3700 also taught by Henry Jackson
(26, 15), -- CS6200 also taught by Grace Martin
(27, 16), -- DS4300 also taught by Alexander Lee
(28, 17), -- CY4500 also taught by Amelia Harris
(29, 18), -- CS4620 also taught by Lucas Clark
(30, 19), -- CS6120 also taught by Mia Rodriguez
(31, 10), -- CS4810 also taught by James Taylor
(32, 11), -- MATH2331 also taught by Isabella Martinez
(33, 12), -- MATH2341 also taught by Benjamin Moore
(34, 13), -- MATH3081 also taught by Charlotte Thomas
(35, 14), -- PHYS2303 also taught by Henry Jackson
(36, 15), -- BIOL2301 also taught by Grace Martin
(37, 16), -- CHEM3401 also taught by Alexander Lee
(38, 17), -- PSYC3404 also taught by Amelia Harris
(39, 18), -- ENGW3302 also taught by Lucas Clark
(40, 19); -- BUSN2401 also taught by Mia Rodriguez

-- Insert data into Student_Employer
INSERT INTO Student_Employer (NUID, employerID) VALUES
-- Alice Green (NUID = 1)
(1, 1),  -- Microsoft
(1, 4),  -- Amazon
(1, 8),  -- Google

-- Bob Brown (NUID = 2)
(2, 22), -- Goldman Sachs
(2, 21), -- Deloitte
(2, 23), -- Procter & Gamble

-- Charlie White (NUID = 3)
(3, 3),  -- Cisco
(3, 10), -- Juniper Networks
(3, 32), -- Palo Alto Networks

-- David Smith (NUID = 4)
(4, 1),  -- Microsoft
(4, 7),  -- Apple
(4, 13), -- Red Hat

-- Emily Johnson (NUID = 5)
(5, 9),  -- IBM
(5, 19), -- Spotify
(5, 30), -- Tableau

-- Frank Williams (NUID = 6)
(6, 3),  -- Cisco
(6, 20), -- Symantec
(6, 32), -- Palo Alto Networks

-- Grace Davis (NUID = 7)
(7, 5),  -- Twitter
(7, 12), -- Adobe
(7, 26), -- Pinterest

-- Henry Miller (NUID = 8)
(8, 10), -- Juniper Networks
(8, 14), -- Oracle
(8, 27), -- VMware

-- Isabella Wilson (NUID = 9)
(9, 6),  -- OpenAI
(9, 7),  -- Apple
(9, 28), -- Tesla

-- Jack Anderson (NUID = 10)
(10, 11), -- LinkedIn
(10, 24), -- Salesforce
(10, 8),  -- Google

-- Karen Thomas (NUID = 11)
(11, 13), -- Red Hat
(11, 16), -- SAP
(11, 30), -- Tableau

-- Liam Jackson (NUID = 12)
(12, 14), -- Oracle
(12, 35), -- Qualcomm
(12, 10), -- Juniper Networks

-- Mia Martin (NUID = 13)
(13, 15), -- Dropbox
(13, 18), -- Electronic Arts
(13, 4),  -- Amazon

-- Noah Lee (NUID = 14)
(14, 16), -- SAP
(14, 27), -- VMware
(14, 9),  -- IBM

-- Olivia Perez (NUID = 15)
(15, 17), -- Uber
(15, 26), -- Pinterest
(15, 19), -- Spotify

-- Paul Young (NUID = 16)
(16, 23), -- Procter & Gamble
(16, 24), -- Salesforce
(16, 6),  -- OpenAI

-- Quinn Hernandez (NUID = 17)
(17, 22), -- Goldman Sachs
(17, 21), -- Deloitte
(17, 11), -- LinkedIn

-- Rachel King (NUID = 18)
(18, 5),  -- Twitter
(18, 1),  -- Microsoft
(18, 8),  -- Google

-- Samuel Scott (NUID = 19)
(19, 2),  -- Facebook
(19, 6),  -- OpenAI
(19, 9),  -- IBM

-- Taylor Green (NUID = 20)
(20, 4),  -- Amazon
(20, 6),  -- OpenAI
(20, 30), -- Tableau

-- Uma Harris (NUID = 21)
(21, 27), -- VMware
(21, 18), -- Electronic Arts
(21, 19), -- Spotify

-- Victor Clark (NUID = 22)
(22, 32), -- Palo Alto Networks
(22, 33), -- Intel
(22, 15), -- Dropbox

-- Wendy Lewis (NUID = 23)
(23, 34), -- Amazon Alexa
(23, 35), -- Qualcomm
(23, 10), -- Juniper Networks

-- Xavier Robinson (NUID = 24)
(24, 3),  -- Cisco
(24, 12), -- Adobe
(24, 14), -- Oracle

-- Yvonne Walker (NUID = 25)
(25, 5),  -- Twitter
(25, 13), -- Red Hat
(25, 16), -- SAP

-- Zachary Hall (NUID = 26)
(26, 1),  -- Microsoft
(26, 7),  -- Apple
(26, 8),  -- Google

-- Ava Allen (NUID = 27)
(27, 19), -- Spotify
(27, 12), -- Adobe
(27, 4),  -- Amazon

-- Benjamin Young (NUID = 28)
(28, 24), -- Salesforce
(28, 8),  -- Google
(28, 30), -- Tableau

-- Charlotte Hill (NUID = 29)
(29, 1),  -- Microsoft
(29, 27), -- VMware
(29, 26), -- Pinterest

-- Daniel Adams (NUID = 30)
(30, 2),  -- Facebook
(30, 6),  -- OpenAI
(30, 12); -- Adobe

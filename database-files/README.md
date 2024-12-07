# `database-files` Folder

The 00_skillseeker.sql file contains the DDL for creating the database.
01_skillseeker_sample_data.sql file inserts data into the database.

To access mySQL in terminal run:
mysql -u root -p

After accessing mySQL...
Remove current database with by running the following:
DROP DATABASE IF EXISTS skillseeker;

- To create the database tables run the 00_skillseeker.sql file 
- To populate run the 01_skillseeker_sample_data.sql  file

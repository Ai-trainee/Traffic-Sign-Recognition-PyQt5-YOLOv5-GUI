@echo off
echo Creating the database...

REM Set path to the SQL file
set SQL_FILE_PATH=data/regn_mysql.sql

REM Database connection details
set DB_HOST=localhost
set DB_USER=root
set DB_PASSWORD=1234

REM Create the database using the SQL file
mysql -h %DB_HOST% -u %DB_USER% -p%DB_PASSWORD% < %SQL_FILE_PATH%

if %ERRORLEVEL% == 0 (
    echo Database created successfully.
    echo Please remember to update the following details in your code:
    echo DB_HOST: %DB_HOST%
    echo DB_USER: %DB_USER%
    echo DB_PASSWORD: %DB_PASSWORD%
    echo DB_NAME: [Your Database Name]
) else (
    echo Failed to create the database. Please check your MySQL installation and the SQL file.
)

pause

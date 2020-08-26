@ECHO OFF
set name=%1
@ECHO Creating new project %name% please wait..

:: change to your projects directory (mine is in D:\Projects)
:: d:    This is how to swap to a different hard drive within cmd
cd Projects 
mkdir %name%

py create_repo.py %name%

cd %name%
git init 

:: CHANGE REQUIRED: Enter your Github username here
git remote add origin git@github.com:YOUR-GITHUB-USERNAME-HERE/%name%.git

git pull origin master
code .

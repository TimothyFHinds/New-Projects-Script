# New-Projects (For Windows)

Creating a new project can become tedious. I set out to create a script which would allow me to automate this process. These scripts simplify the process by only requiring one command to get a new project started. 

## Use
Open a new command prompt or PowerShell and call the name of the windows batch script along with the name of your new project __without spaces__ as a command argument. 
#### Run in CMD
```
create NewProjectName
```
#### Run in Powershell
```
.\create NewProjectName
```

## Requirements
[Selenium][selenium] is a popular python package utilized for scraping and interacting with webpages. It will be used to interact with Github's website to create a remote repository.
```
pip install selenium
``` 
[Download the chrome webdriver][webdriver] for selenium *based on the version of Chrome you have* (Click the 3 dots button, Help, About Google Chrome). Then put webdriver.exe in a memorable location. I put mine within my projects directory *D:\Projects\webdriver.exe*.
## How to Install

1. __Clone__ the script files
```
git clone https://github.com/TimothyFHinds/New-Projects-Script
```
2. __Edit create.bat__ and __create_repo.py__ where the comments indicate to make modifications. 
3. __Move create.bat__ into your default directory. For example, mine is: *C:\Users\Tim*
4. __Move create_repo.py__ into your default projects directory.
5. You're ready to create!

[selenium]: https://selenium-python.readthedocs.io/
[webdriver]: https://sites.google.com/a/chromium.org/chromedriver/downloads
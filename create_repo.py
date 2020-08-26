
import sys
from selenium import webdriver

def create_repo(): 
    try:
        project_name = str(sys.argv[1])
        print(f'Creating {project_name}\'s git repository!')
    except:
        print('Incorrect arguments given, use one word without spaces for the name like this:')
        print('create NewProjectName')
        return None
    
    try:
        # CHANGE REQUIRED: Enter your chromedriver's path
        PATH = "D:\Projects\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.github.com/login")
        login = driver.find_element_by_id("login_field")

        # CHANGE REQUIRED: Enter your github username
        login.send_keys("YOUR-USERNAME")
        password = driver.find_element_by_id("password")
        
        # CHANGE REQUIRED: Enter your github password
        password.send_keys("YOUR-PASSWORD")
        driver.find_element_by_name("commit").click()

        driver.get("https://www.github.com/new")
        repo_name = driver.find_element_by_id("repository_name")
        repo_name.send_keys(project_name)

        driver.find_element_by_id("repository_auto_init").click()   # Checkbox for init with readme file
        
        create_button = driver.find_element_by_css_selector('button.first-in-line')
        create_button.submit()

        driver.quit()
    except:
        print('Failed to create github repository')
    

if __name__ == "__main__":
    create_repo()


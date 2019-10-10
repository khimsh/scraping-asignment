from bs4 import BeautifulSoup
from selenium import webdriver
import lxml


def get_user(user_email: str, user_password: str) -> dict:
    """
    1. Open '/login' in firefox with selenium
    2. Enter user_email & user_password; Submit
    3. Open '/profile'; Grab user name & lastname
    4. Return user name & lastname
    """

    login_url = 'http://applecity.ge/login'
    profile_url = 'http://applecity.ge/profile'

    browser = webdriver.Firefox()
    browser.get(login_url)

    # Select email & password inputs
    username = browser.find_element_by_id("userSigninLogin")
    password = browser.find_element_by_id("userSigninPassword")
    # Select submit button
    button = browser.find_element_by_xpath('//button[@type=\'submit\']')

    # Enter user creditentials & click submit
    username.send_keys(user_email)
    password.send_keys(user_password)
    button.click()

    # Open profile url & get the response html
    # If the response contains required data
    # return user name & lastname with status code 200
    # If it doesn't return status code 401
    # Close the browser
    browser.get(profile_url)
    soup = BeautifulSoup(browser.page_source, 'lxml')

    try:
        name_lastname = soup.find('input', {'id': 'accountName'}).get('value')
        return {'status': 200, 'message': name_lastname}
    except AttributeError as err:
        return {'status': 401, 'message': 'bad creditentials'}
    finally:
        browser.quit()

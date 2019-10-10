from bs4 import BeautifulSoup
from selenium import webdriver
import lxml


def get_user(user_email, user_password):

    login_url = 'http://applecity.ge/login'
    profile_url = 'http://applecity.ge/profile'

    browser = webdriver.Firefox()
    browser.get(login_url)

    username = browser.find_element_by_id("userSigninLogin")
    password = browser.find_element_by_id("userSigninPassword")
    button = browser.find_element_by_xpath('//button[@type=\'submit\']')

    username.send_keys(user_email)
    password.send_keys(user_password)
    button.click()

    browser.get(profile_url)

    soup = BeautifulSoup(browser.page_source, 'lxml')

    try:
        name_lastname = soup.find('input', {'id': 'accountName'}).get('value')
        print(name_lastname)
        return {'status': 200, 'message': name_lastname}
    except AttributeError as err:
        print(err)
        return {'status': 401, 'message': 'bad creditentials'}
    finally:
        browser.quit()

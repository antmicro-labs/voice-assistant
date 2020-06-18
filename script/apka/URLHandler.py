from selenium import webdriver
import time

class URLHandler:
    def __init__(self):
        self.driver = None


    def openURL(self):
        # Go to your page url
        driver = webdriver.Firefox()
        driver.get('http://www.reciperoulette.tv/')
        # Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
        button_element = driver.find_element_by_id('playbutton')
        button_element.click()
        time.sleep(5)
        driver.close()
        return None
        

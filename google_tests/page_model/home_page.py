# -*- coding: UTF-8 -*-
from google_tests.page_model.base_page import BasePage
from google_tests.locators.home_page import HomePageLocators
from google_tests.helpers.page_loader import require_loaded
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from time import sleep


class HomePage(BasePage):  
    @property
    def url(self):
        return 'https://google.com/'

    @property
    def search_bar(self):
        return self.driver.find_element(*HomePageLocators.SEARCH_BAR)

    @property
    def search_button(self):
        return self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)

    @property
    def feeling_lucky_button(self):
        return self.driver.find_element(*HomePageLocators.FEELING_LUCKY_BUTTON)

    @property
    def is_loaded(self):
        try:
            self.driver.find_element(*HomePageLocators.GOOGLE_LOGO)
            return True
        except NoSuchElementException:
            return False

    def load(self):
        self.driver.get(self.url)

    @require_loaded
    def type_in_search_bar(self, text):
        element = self.search_bar
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ESCAPE)

    @require_loaded
    def click_search_button(self):
        self.search_button.click()

    @require_loaded
    def click_feeling_lucky_button(self):
        self.feeling_lucky_button.click()

    def search_for(self, text):
        self.type_in_search_bar(text)
        self.click_search_button()

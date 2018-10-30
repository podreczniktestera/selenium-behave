# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By


class SearchResultsPageLocators:
    RESULT_SECTION = By.ID, 'rso'
    RESULT_ELEMENTS = By.CLASS_NAME, 'g'

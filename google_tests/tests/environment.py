# -*- coding: UTF-8 -*-
from selenium import webdriver


def before_scenario(context, scenario):
    driver = webdriver.Chrome()
    context.driver = driver


def after_scenario(context, scenario):
    context.driver.quit()

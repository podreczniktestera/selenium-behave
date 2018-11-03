# -*- coding: UTF-8 -*-
from behave.model import Status
from selenium import webdriver


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1600x900')
    
    driver = webdriver.Chrome(chrome_options=options)
    context.driver = driver


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        context.driver.save_screenshot('{}.jpg'.format(scenario.name))
    context.driver.quit()

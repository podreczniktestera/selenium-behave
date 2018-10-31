# -*- coding: UTF-8 -*-
from selenium import webdriver


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1600x900')
    
    driver = webdriver.Chrome(chrome_options=options)
    context.driver = driver


def after_scenario(context, scenario):
    context.driver.quit()

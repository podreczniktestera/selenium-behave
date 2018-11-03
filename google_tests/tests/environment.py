# -*- coding: UTF-8 -*-
from behave.model import Status
from selenium import webdriver
from google_tests.helpers.failure_handlers import handle_scenario_failure


def before_scenario(context, scenario):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1600, 900)
    context.driver = driver


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        handle_scenario_failure(context.driver, scenario.name)
    context.driver.quit()

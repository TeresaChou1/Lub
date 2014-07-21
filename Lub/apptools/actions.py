# -*- coding:utf-8 -*-
# lub web actions
# based on appium api
# appium's popular actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def lubsmartwait(driverinstance,ByWhat,Byvalue,timeout=60):
    if ByWhat in By.__dict__.keys():
        element=WebDriverWait(driverinstance, timeout).until(
            EC.presence_of_element_located((By.__dict__.get(ByWhat), Byvalue))
        )
        return element
    else:
        raise KeyError
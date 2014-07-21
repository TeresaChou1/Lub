# -*- coding:utf-8 -*-
# controls
from appium import webdriver
from lettuce import *
import os

LUB_APP_PATH=lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

@before.all
def startdriver():
    #描述desired_caps
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.3'
    desired_caps['deviceName'] = 'Android Emulator'
    #desired_caps['app'] = LUB_APP_PATH('ctriptest.apk')
    desired_caps['appPackage'] = 'ctrip.android.view'
    desired_caps['appActivity'] = 'ctrip.android.view.home.CtripSplashActivity'
    world.mobile=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

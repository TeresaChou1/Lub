# -*- coding:utf-8 -*-
# lub web actions
# based on appium api
# appium's popular actions
# 部分action可以直接与webtools共用
# 所以apptools这里封装的是移动端专用的一些action

#匿名函数,用于返回被测APK的绝对路径
LUB_APP_PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
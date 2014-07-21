# -*- coding:utf-8 -*-
# step definitions
from lettuce import *
from Lub.webtools.actions import *
from Lub.apptools.actions import *

@step(u'等待 "(.*)" 为 "(.*)" 的元素出现并点击它,最多等它 (\d+) 秒')
def clickbyname(step,bywhat,byvalue,timeout):
    lubclick(lubsmartwait(world.mobile,bywhat,byvalue,float(timeout)))
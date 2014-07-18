# -*- coding:utf-8 -*-
# lub web actions
# based on selenium api

import time

def lubfind(wbinstance,typename,typeval):
    """find element"""
    methodname='find_element_by_'+str(typename)
    if hasattr(wbinstance,methodname):
        thismethod=getattr(wbinstance,methodname)
        element=thismethod(typeval)
        return element

def lubfinds(wbinstance,typename,typeval):
    """find elements"""
    methodname='find_elements_by_'+str(typename)
    if hasattr(wbinstance,methodname):
        thismethod=getattr(wbinstance,methodname)
        elements=thismethod(typeval)
        return elements

def lubwait(stringtimeparam):
    """dead wait method"""
    time.sleep(float(stringtimeparam))

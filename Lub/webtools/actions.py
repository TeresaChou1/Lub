# -*- coding:utf-8 -*-
# lub web actions
# based on selenium api
# selenium's popular actions

import time

def lubget(wbinstance,url):
    """get url"""
    if hasattr(wbinstance,'get'):
        getmethod=getattr(wbinstance,'get')
        getmethod(url) #callback
    else:
        raise AttributeError

def lubclick(element):
    """click method"""
    if hasattr(element,'click'):
        return getattr(element,'click')
    else:
        raise AttributeError

def lubinput(element,inputwhat):
    """input method"""
    if hasattr(element,'send_keys'):
        inputmethod=getattr(element,'send_keys')
        inputmethod(inputwhat) #callback
    else:
        raise AttributeError

def lubfind(wbinstance,typename,typeval):
    """find element"""
    methodname='find_element_by_'+str(typename)
    if hasattr(wbinstance,methodname):
        thismethod=getattr(wbinstance,methodname)
        element=thismethod(typeval)
        return element
    else:
        raise AttributeError

def lubfinds(wbinstance,typename,typeval):
    """find elements"""
    methodname='find_elements_by_'+str(typename)
    if hasattr(wbinstance,methodname):
        thismethod=getattr(wbinstance,methodname)
        elements=thismethod(typeval)
        return elements
    else:
        raise AttributeError

def lubwait(stringtimeparam):
    """dead wait method"""
    time.sleep(float(stringtimeparam))

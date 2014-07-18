#!/usr/bin/env python
# -*- coding:utf-8 -*-
# lub commands

import sys,os
import optparse

projectdir=['webtc','apptc']
lettucedir=['features','step_definitions','support']

def genproject():
    for dir in projectdir:
        for ldir in lettucedir:
            try:
                os.makedirs(os.path.join(os.getcwd(),dir,ldir))
            except OSError,why:
                print u"已有一个Lub项目结构存在！%s" % why
    for dir in projectdir:
        with open(os.path.join(os.getcwd(),dir,'features','all.feature'),'w+') as featuref:
            featuref.writelines("Feature: 测试用例集\n")
            featuref.writelines("\tScenario: 测试场景一\n")
        with open(os.path.join(os.getcwd(),dir,'step_definitions','steps.py'),'w+') as stepf:
            stepf.writelines("# -*- coding:utf-8 -*-\n")
            stepf.writelines("# step definitions\n")
        with open(os.path.join(os.getcwd(),dir,'support','terrain.py'),'w+') as terrainf:
            terrainf.writelines("# -*- coding:utf-8 -*-\n")
            terrainf.writelines("# controls\n")

def run():
    os.system("lettuce "+str(os.getcwd()))

def runwithreport():
    pass

def main():
    parser = optparse.OptionParser(usage="%prog or type %prog -h (--help) for help")
    parser.add_option("-i", "--init",action="store",help=u"-i gen 自动初始化Lub项目",dest="initmode",default="",type="string")
    parser.add_option("-r", "--run",action="store",help=u"-r normal 调试运行模式 | -r report 报告输出运行模式",dest="runmode",default="",type="string")
    (options, args) = parser.parse_args()
    if options.initmode=="gen":
        genproject()
    elif options.runmode=="normal":
        run()
    elif options.runmode=="report":
        pass
    else:
        print parser.print_help()

if __name__=="__main__":
    main()


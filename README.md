### 为什么要做lub？

一开始是出于对[calabash](https://github.com/calabash "calabash")项目的热爱，后来，这种热爱化为动力。
我决定使用python的BDD框架来驱动自动化测试项目
当我发现[lettuce](http://lettuce.it/ "lettuce")之后我显得很兴奋。
这是一个非常优秀的BDD框架，完全采用python编写，有了lettuce之后，你几乎只要做一些附加工作就可以了。
所以lub就是对lettuce的一剂润滑剂，但是lub是没有办法称之为一个完整的自动化测试框架的，至少目前是如此。
所以，我在项目标题里打上了"demo"
很显然，lub还有很多工作需要去做。

### 既然有了lettuce，为什么还要Lub？

不可否认，lettuce是一个出色的BDD框架，但是要想运用到web和app的自动化测试中去就可能需要做一系列工作。
这些工作包括大家熟悉的封装，command管理，报告自定义，甚至是通信......等等工作。
lub希望可以做到：当你使用这个"润滑剂"时，你感受到了lettuce的BDD魅力。

### 安装Lub

```python
python setup.py install
```

### 需要的依赖

```python
lettuce
appium
selenium
```

### Quick Start

#### step1 创建一个lub项目

```bash
lub -i gen
```

#### step2 熟悉一下生成的结构

完成创建后，将在当前目录生成webtc和apptc两个文件夹，分别用于放置web端和移动端的用例
他们下面的结构是一模一样的：

```
features
--all.feature 自然语言描述的用例集
step_definitions
--steps.py 步骤action
support
--terrain.py 全局控制
```

#### step3 接下来我们先使用webtc做一个百度demo

先编写一个简单的用例，打开all.feature进行编辑

```
Feature: 测试用例集
	Scenario: 百度首页
      Given 打开 "http://www.baidu.com"
      When 在 "id" 为 "kw1" 的框中输入 "lud"
      And 点击 "id" 为 "su1" 的按钮
```

接着，我们在steps.py中开始为我们这些自然语言描述定义步骤

```python
# -*- coding:utf-8 -*-
# step definitions

from Lub.webtools.actions import *
from lettuce import *

@step(u'打开 "(.*)"')
def openurl(step,url):
    world.browser.get(url)

@step(u'在 "(.*)" 为 "(.*)" 的框中输入 "(.*)"')
def typekey(step,typename,typekey,typeval):
    lubfind(world.browser,typename,typekey).send_keys(typeval)

@step(u'点击 "(.*)" 为 "(.*)" 的按钮')
def clickelem(step,typename,typekey):
    lubfind(world.browser,typename,typekey).click()
```

这里，我们使用了lub自己封装的一些方法。
这里的world是lettuce提供的一个"世界"，很形象，你可以在全局控制中的一开始就将我们的webdriver实例放入这个世界里。
在steps中，我们只需要去拿就可以了。

我们来看看全局控制terrain.py里，我们写了什么有趣的东西：
注：terrain是特殊的py，它将最优先运行

```python
# -*- coding:utf-8 -*-
# controls

from lettuce import *
from selenium import webdriver

@before.each_scenario
def setup_some_scenario(scenario):
    world.browser=webdriver.Firefox()

@after.each_scenario
def setup_some_scenario(scenario):
    world.browser.close()

```
terrain中，我用了几个装饰器，非常实用，他们的全部内容可以参见lettuce这里
[lettuce terrain](http://lettuce.it/reference/terrain.html#reference-terrain "lettuce terrain")

#### step4 运行！

你可以直接使用下面的命令快速运行你的用例集，注意，需要在当前结构目录下运行调试
也就是在webtc目录或者apptc下运行，不然会提示找不到features目录

```python
lub -r normal
```

#### 扩展及其他

待补充

### 感谢以下这些优秀的框架

```
lettuce
selenium
appium
```

### 为什么要做lub？

一开始是出于对[calabash](https://github.com/calabash "calabash")项目的热爱，后来，这种热爱化为动力。
我决定使用python的BDD框架来驱动自动化测试项目
当我发现lettuce之后我显得很兴奋。
这是一个非常优秀的BDD框架，完全采用python编写。

### 既然有了lettuce，为什么还要Lub？

不可否认，lettuce是一个出色的BDD框架，但是要想运用到web和app的自动化测试中去就可能需要做一系列工作。
这些工作包括大家熟悉的封装等。
当然，lub还不忘记提供一些方便的command来进行管理。


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

#### step2 接下来我们先使用

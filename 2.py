'''
   note : （迭代器）：
     a . 有关迭代 ： 迭代意味着重复多次。
     b . 实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器
'''
# 迭代器实例： 斐波拉契亚数列
'''
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self
fib1 = Fibs()
for f in fib1:
    if(f > 20):
        print(f)
        break
        
'''
'''
    note: 
       a . 通过对可迭代对象调用内置函数iter， 可获得一个迭代器
         eg ; it = iter([1,2,3])
       b . 构造函数list显式地将迭代器转换为列表
'''

'''
    note : ( 生成器 )
       a . 包含yield语句的函数都被称为生成器 
       b . 生成器的行为与普通函数截然不同。生成器不是用return返回一个值，而是可以生成多个值，每次一个。
           每次使用yield 生成一个值后，函数都将被冻结，即在此停止执行，等待被重新唤醒。
           被重新唤醒后，函数将从停止的地方开始继续执行
'''
'''
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)

print(list(flatten(nested))) 
'''

'''
   note ： （从不同的角度理解生成和迭代）
     a . 迭代器协议是指对象需要提供 next 方法， 要么返回迭代中的下一项 ， 要么就引起一个 Stoplteration 异常，已终止迭代
         由于Python重视方法，而较少考虑对象，所以不仅可以迭代列表还可以 迭代文件等各式各样的对象。
     b . python 使用生成器对延迟操作提供了支持，延迟操作，即在需要的时候提供支持
        延迟计算在 大数据量计算的内存占用中起着极大的好处
     c . 如果想把代码写的Pythonic, 在保证代码可读性的前提下，代码行数越少越好
     d.. 千万注意，生成器只能遍历一次，如果遍历多次，可能不会有任何输出。
'''
# 迭代器，特性，生成器可能要反复查资料，反复理解
('\n'
 '# 初次接触八皇后问题(递归解法)\n'
 'import random\n'
 'def conflict(state, nextX):\n'
 '    nextY = len(state)\n'
 '    for i in range(nextY):\n'
 '        if(abs(state[i] - nextX)) in (0, nextY - i):\n'
 '            return True\n'
 '        return False\n'
 '\n'
 'def queens(num = 8 , state=()):\n'
 '    for pos in range( num ):\n'
 '        if(not conflict(state, pos)):\n'
 '            if(len(state) == num-1):\n'
 '                yield(pos,)\n'
 '            else:\n'
 '                for result in queens(num, state + (pos, )):\n'
 '                    yield(pos,)+result\n'
 '\n'
 'def prettyprint(solution):\n'
 '    def line(pos, length=len(solution)):\n'
 '        return \'.\'*(pos) + \'X\' + \'.\' * (length-pos-1)\n'
 '    for pos in solution:\n'
 '        print(line(pos))\n'
 'prettyprint(random.choice(list(queens(8))))\n')

'''
   note （本章小结）：
       a . Python 有很多特殊方法，其名称以两个下划线开头和结尾。这些方法的功能各不相同，但大都由python在特定情况下
           自动调用。
       b . 对于自己构造的每一个类，可能都需要为它实现一个构造函数。 构造函数名为__init__，在对象创建后被调用
       c .  有关特性，迭代器，生成器可以到B站上找一些视频加深理解
'''

'''
   note : （模块）：
      a . 任何python 程序都可作为模块导入。
      b . 文件的储存位置也很重要，要告诉解释其去哪里找这个模块： 可执行如下命令：
             import sys
             sys.path.append('C:/python')
      c . 模块并不是用来执行操作的，而是用于定义变量，函数，类的。
           鉴于定义只需做一次，因此导入模块多次和导入一次的效果相同。
      d . 要让代码是可重用的，务必将其模块化
      e . Python打包技术现已被python packaging authority控制简化 ， 详情参阅 'python打包用户指南'： packaging.python.org
      f . 如果要打印的数据结构太大，一行容纳不下，可使用模块pprint中的函数pprint
'''

'''
   note : （让模块可用）：
       1 . 将模块放在正确的位置：
           a . 在模块sys的变量path中找到目录列表（即搜索路径）
           b . 找到其中的site-packages，并把模块保存到这里
       2 . 不过总要求将模块放到正确的位置可能不是个好办法
           这时候就必须告诉解释器到哪里去查找： 标准做法是将模块所在的目录包含在环境变量PYTHONPATH中
'''

'''
   note: （包）：
    a . 为组织模块，可将其编组为包： 包其实就是另一种模块，但有趣的是它们可包含其他模块。
        模块存储在 扩展名为 .py 的文件中，而包则是一个目录。 要被python视为包，目录必须包含
        文件__init__.py
'''

'''
   note ：（探索模块: 快速轻松理解python 模块）：
    a . __all__ 旨在定义模块的公有接口
         因此 使用 from copy import * 将只能变量__all__中列出的四个函数。
         要导入其它函数，必须显式导入：
         from copy import PyStringMap
         编写模块时，像这样设置__all__很有用，因为模块可能包含大量其它程序不需要的变量，函数，类
         如果不设置，则在import * 方式导入时，导入所有不以下划线打头的全局名称
    b . 所有的标准库开发文档都可以到 python官方网站中找到
    c . 要学习python ，阅读源代码是除动手编写代码外的最佳方式
'''
'''
import copy
print([n for n in dir(copy) if not n.startswith('_')])
print(dir(copy))
print(copy.__all__)

print(range.__doc__)
'''
'''
import copy
print(copy.__file__)
'''
'''
import webbrowser
webbrowser.open('http://www.4399.com')
'''

'''
   note : 
        a . 集合 ：  可以直接用函数set 创建集合，也可使用花括号显式指定
            集合主要用于成员资格检查，因此将忽略重复的元素
            与字典一样，集合中元素的排列顺序是不确定的
            由于集合只能包含不可变得值，所以不呢个包含其他值，但是在现实生活中，经常会遇到
            集合的集合，所幸有 frozenset 类型， 它表示不可变类型，常常用于两个集合相加
        b . r'原始字符'：所有''的句子原封不动打印，无需转义
'''

'''
   note : ( python正则 )
       a . 字符集 ： 
             字符集匹配任何字符都很有用，但需要较为精细的控制：
                 [pj]ython 与 python 和 jython 都匹配，但不与其他字符串匹配
             指定排除字符集，可在开头添加 ^ , 例如 [^abc]与除 a b c 以外的其他任何字符都匹配
       b . 二选一和子模式
       c . 完整的正则表达式运算符清单参阅python库中的regular expression syntax部分
       d . 模块re : 1.包含多个使用正则表达式的函数
                    2.在模块re中，查找与模式匹配的子串的函数都在找到时返回MatchObject
                    MatchObject 对象包含与模式匹配的子串的信息，还包含模式的哪部分与子串的哪部分匹配的消息，这些子串部分
                    称为编组
                    3.要让正则表达式更容易理解，一种办法是在调用模块re中的函数时使用标志VERBOSE。  
'''

'''
   note : （文件）
       a . 要打开文件可使用函数open, 它位于自动导入的模块io中。
           函数open将文件名作为唯一必不可少的参数，并返回一个文件对象。
       b . 调用函数open时，如果只指定货文件名，将获得一个可读取的文件对象。
           如果要写入文件，必须通过指定模式来显式的指出这一点。
       c . python中的随机存取（在文件中移动，只访问感兴趣的部分）：
            方法seek(offset[, whence])将当前位置移到offset 和 whence指定的地方
            参数offset指定字节数，而whence默认为 io.SEEK_SET(0)，这意味偏移量是相对于文件开头的。
            参数whence还可设置为 io.SEEK_CUR(1)或io.SEEK_END(2)
            前者表示相对于当前位置移动，而后者表示相对于文件末尾进行移动
       d . 对于写入过的文件，一定要将其关闭，因为python可能缓冲你写入的数据
           要确保文件得以关闭，可使用一条try/finally语句.并在finally子句中调用close
          # 在这里打开文件
          try:
              # 将数据写入到文件中
          finally:
              file.close()   
       e . python中的with...as 类似于 try...except......finally...
           用法： 
                with A() as b:
           其中A是一个类，该类中必须包含两个 函数__enter__() 和 __exit__()
           b 为函数__enter__()的返回值
       f . 迭代文件内容，最常见的是迭代文本文件中的行，这可通过简单地对文件本身进行迭代来做到
'''

'''
   note （图形页面交互）：
       a . Tkinter是事实上的Python标准GUI工具包（包含在python标准安装中）
           还有其他工具包。但是这有优点，也有缺点：除非其他人也安装你使用的GUI工具包，否则无法运行你编写的程序
       b . 编写GUI程序时，绘制用户界面草图通常很有帮助。
       c . GUI工具包中用户触发事件执行的操作。
           在Tkinter中，要给组件添加事件处理程序，可使用方法bind
'''

'''
   note （数据库）：
       a . 为了和底层SQL数据库正确的交互，DB API定义了一些构造函数和常量，用于提供特殊的类型和值
       b . 不要让你的数据库（以及其它任何东西）暴露在原始用户输入的“火力范围”内
'''

'''
   note : （网络）：
       a . 需要注意的是，任何连接到网络的软件都是安全隐患，自己编写的软件尤其如此。
       b . 几个网络模块：
             1.socket: 套接字基本是一个信息通道，通过套接字向对方发送消息。
                      套接字分为两类：服务器套接字河客户端套接字
               客户端与服务端建立连接的过程：
                  服务器套接字先调用方法bind，再调用方法listen来监听特定的地址。然后即可建立连接
                  为传输数据，套接字提供了两个方法： send 和 recv
       c . 利用模块urllib 河urllib，可以通过网络访问文件
           函数urlopen返回一个类似于文件的对象，可从中读取数据。
           如果要让urllib替你下载文件，并将其父本存储在一个本地文件中，可使用urlretrieve
           eg : urlretrieve('http://www.python.org','C:\\python_webpage.html')
       d . 模块SocketServer是标准库提供的服务器框架的基石
       e . 如果连接持续的时间比较长，比如完整的聊天会话，就需要能够同时处理多个连接
           处理多个连接的主要方式有三种 ： 分叉，线程化，异步I/O
           另一种避免线程和分叉的办法是使用 Stackless Python(它支持一种类似于线程的并行方式名为微线程) 
'''
# 先把网络编程从14.3开始到后面的节数放在这里

'''
   note: (python 与 web)
       a . Tidy是用于对格式不正确且不严谨的HTML进行修复的工具。
           它还提供了极大的配置空间，让你能够开/关各种校正
       b . 要对Tidy 生成的格式良好的XHTML进行解析，一种较为简单的方式是使用标准库模块html.parser中的HTMLParser类
       c . beautiful soup是一个小巧而出色的模块，用于解析你在Web上可能遇到的不严谨且格式糟糕的HTML
       d . 使用CGI创建动态网页分为三步：
             a . 准备web服务器：
                  （CGI程序烨必须放在可通过web访问的目录中。另外，必须将其标记为CGI脚本
                    为此将脚本文件的扩展名指定为.cgi即可）
             b . 添加！#行
                 如果没有！#行，web 服务器将不知道如何执行脚本
                 一般来说只需在脚本开头添加此行： #！/usr/bin/env python
                 在windows中，可使用python可执行文件的完整路径：
                  #！C:\Python36\python.exe
             c . 设置文件权限（至少当web服务器运行在UNIX和Linux系统中如此）
                  必须确保谁都可以读取和执行你的脚本文件（否则web服务器将无法运行它）
                  同时确保只有你才能写入
'''
# 从P265往后面走需要UNIX Linux 相关知识，暂时搁置在这里

'''
   note : （测试基础）：
       a . 调试是程序员躲不开的宿命
           测试在先，编码在后；这也称为测试驱动的编程
           开发软件时，必须要知道软件要解决什么问题——要实现什么样的目标。
           要阐明程序的目标，可编写需求说明。
           测试程序就是需求说明，可帮助确保程序开发过程紧扣这些需求
       b . 覆盖率是一个重要的测试概念；
           trace作为 python 标准覆盖率工具，可以测量测试期间实际运行的代码所占的比例。
       c . 测试四部曲：
           1> . 确定需要实现的新功能。
           2> . 编写实现功能的框架代码，让程序能够运行，但测试仍然无法通过
                （测试程序存在的意义就是发现问题，所以尽量挑刺
           3> . 编写让测试刚好通过的代码
           4> . 改进代码以全面而准确地实现所需的功能，同时确保测试依然能够成功
       d . python 中unittest 和 doctest 模块可以替你自动完成测试过程
       e . 单元测试可让程序管用，源代码检查可让程序更好，而性能分析可让程序更快
           1> . 使用PyChecker和PyLint检查源代码
                这两个模块是作为命令行工具使用的
       f . 如果程序速度达不到要求才进行优化，一般是不进行优化的
           标准库包含一个卓越的性能分析模块profile，还有一个速度更快C语言版本
           (迷恋性能分析很可能让你忽略真正重要的事情，如清晰而易于理解的代码)
'''

'''
    note （扩展Python）：
      ａ．　提升速度：
     　　　　　 １．使用python开发原型
                2 . 对程序进行性能分析以找出瓶颈
                3 . 使用C，C++ C# java Fortran 扩展重写瓶颈部分
       b .  简单易行的方式： Jython: for java 和 IronPython : for C# 和其它.net框架
           Python 实现方式 参阅Jython 和 IronPython网站即可
       c.  SWIG:
           SWIG 是一款自动为C语言库生成包装代码的工具，包装代码自动处理Python C API
           (好吧，稍微有一点点不理解)
           
'''
# 扩展python 这块去学下如何嵌入R语言代码

'''
   note:（程序打包）：
     a .
'''

'''
    note (趣味编程)：
       a . 你应该做好应对变化的心理准备，并欣然接受最初的设计肯定需要修订的事实。
       b . 原型设计：
             一般而言，如果想知道python 某个方面的工作原理，可尝试使用它。
             原型指的是尝试性实现，即一个模型，它实现了最终程序的主要功能。
             对程序的结构（需要哪些类和函数）有一定想法后，建议实现一个功能可能极其有限的简单版本、
             所以利用python设计程序的时候，好的习惯是拥有两个版本：
             一个是摸着石头过河，一个是修订后的完美版本。
             尽量减少推倒重来
       c . 配置：
              提高代码抽象程度： 
                一：将代码放在函数和方法中并将较大的结构隐藏在类中实现的
                二：提取代码中的符号常量
                     a . 提取常量（和C语言一样，把经常要输入的值定义为一个全局变量
                         eg: PI = 3.14
                     b . 配置文件
                         有些常量必须暴露给用户，例如，如果用户不喜欢你编写的GUI程序的背景色，应该允许他们使用
                         其它颜色。
                         可将这些配置变量放在独立的文件中，而不将它们放在模块开头。
                         为此，最简单的方式是专门为配置创建一个模块。例如，如果PI是在模块文件config.py中设置的，就
                         可在主程序中像下卖弄这样做：
                            from config import PI
                          另一种方式是使用标准库模块configparser，从而可在配置文件中使用标准格式。
                          这样可以这样配置 greeting:hello world
                         必须用[files]，[colors]等标题将配置文件分成几部分。
        d. 日志大致上就是收集与程序运行相关的数据，供你事后进行研究或积累
           正确的做法是使用标准库中的模块logging:
             基本用法代码：
              import logging
              
              logging.basicConfig(level = logging.INFO, filename = 'mylog.log')
              
              logging.info('starting program')
              
              logging.info('Tring to divide 1 by 0')
              
              print(1 / 0)
              
              logging.info('The division succeeded')
              logging.info('Ending program')
           查看详尽的日志文件也许能帮助你找出问题出在什么地方 
           
           日志可让如下方式运行（在你合理配置模块logging的条件下
           1. 记录不同类型的条目（信息，调试信息，警告，自定义类型）。默认情况下，只记录警告
           2. 只记录与程序特定部分相关的条目。
           3. 记录有关时间、日期等方面信息。
           4. 记录到其他位置，如套接字。
           5. 配置日志器，将一些或大部分日志过滤掉，这样无需重写程序就能获得所需的日志消息。
'''

'''
    note （全书小结）：
          a . 灵活性 ： 设计和编程时，应以灵活性为目标。
              随着对所面临的问题了解得越来越深入，你应心甘情愿乃至随时准备修改程序的方方面面，不要固守最初的想法
          b . 原型设计：要深入了解问题和可能的实现方案，一个重要的技巧是编写程序的简化版本
          c . 配置： 提取变量，将变量放在配置文件中
                     同时通过使用环境变量和命令行选项，可进一步提高程序的可配置性
          d . 日志： 日志对找出程序存在的问题或监视其行为大有裨益
'''

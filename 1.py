'''
# 将以数指定年月日的日期打印出来

months = ['Feb','Jan','Mar','apr','May','jun','july','Aug','sep','Oct','Nov','Dec']

# 列表：包含数 1-31 的结尾
endings = ['st','nd','rd'] + 17*['th']+['st','nd','rd']+7*['th']+['st']

year = input('year : ')
month = input('Month(1-12): ')
day = input('Day(1-31): ')

month_number = int(month)
day_number = int(day)

# 索引取值
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name + ' '+ ordinal + ','+ year)
'''
# 提取特定格式的域名
'''
url = input('plkease enter the url: ')
domin = url[11:-4]

print('Domin name '+domin)
'''
# 海龟绘图法示例
'''
from turtle import *
import turtle
import time
#定义画笔颜色
turtle.color('purple')
#定义画笔宽度
#turtle.size(5)
#定义画笔速度
turtle.speed(1)
#定义画笔起点
turtle.goto(0,0)
for i in range(4) :
    turtle.forward(100)
    turtle.right(90)
#定义终止点
turtle.up()
turtle.goto(-150,-120)
#再次定义画笔颜色
turtle.color('red')
#打印done
turtle.write('done')
time.sleep(3)
'''
# 登陆用户名的缩小版
'''
database = [['a','123'],['b','1234'],['c','12345']]

username = input('username :　')
pin = input('password : ')

if[username,pin] in database:
    print("access granted")
else:
    print("retry")
'''
# 在屏幕中央打印字体
'''
sentence = input('sentence ;　')

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2 # //除后向下取整

print()
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * left_margin + '|' + ' ' * (box_width-2) + '|' )
print(' ' * left_margin + '|'+' '*((box_width-text_width-2)//2) +   sentence  + ' '*((box_width-text_width-2)//2) + '|')
print(' ' * left_margin + '|' + ' ' * (box_width-2)+ '|' )
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()
'''
# 海龟绘图法进一步尝试
from turtle import *
'''
def HSB2RGB(hues):
    hues = hues * 3.59
    rgb = [0.0, 0.0, 0.0]
    i = int(hues / 60) % 6
    f = hues / 60 - i
    if (i == 0):
        rgb[0] = 1;
        rgb[1] = f;
        rgb[2] = 0
    elif (i == 1):
        rgb[0] = 1 - f;
        rgb[1] = 1;
        rgb[2] = 0
    elif (i == 2):
        rgb[0] = 0;
        rgb[1] = 1;
        rgb[2] = f
    elif (i == 3):
        rgb[0] = 0;
        rgb[1] = 1 - f;
        rgb[2] = 1
    elif (i == 4):
        rgb[0] = f;
        rgb[1] = 0;
        rgb[2] = 1
    elif (i == 5):
        rgb[0] = 1;
        rgb[1] = 0;
        rgb[2] = 1 - f
    return rgb


def rainbow():
    import turtle
    import time
    hues = 0.0
    turtle.color(1, 0, 0)
    #绘制彩虹
    turtle.speed(5)
    turtle.size(3)
    turtle.up()
    turtle.goto(-650,-150)
    turtle.down()
    turtle.right(110)
    for i in range (100):
        turtle.circle(600)
        turtle.right(0.23)
        hues = hues + 1
        rgb = HSB2RGB(hues)
        turtle.color(rgb[0],rgb[1],rgb[2])
        turtle.up
def main():
    import turtle
    turtle.setup(1200, 800, 0 ,0)
    turtle.bgcolor((64/255,64.255,1))
    turtle.tracer(False)
    turtle.goto(0,0)
    turtle.down()
    turtle.color('yellow')
    turtle.write("Done!")
    turtle.font = ("Script MT Bold",80,"bold")
    turtle.tracer(True)

    turtle.mainloop()

    if __name__ == "__main__":
        main()
'''
'''
import turtle
for i in range(360):
    turtle.setheading(i)
    turtle.speed(10)
    turtle.color('yellow')
    #turtle.bgpic(r'birthday.png')
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
turtle.color('red')
turtle.write('江姐姐生日快乐@+！！！')
turtle.sleep(3)
'''
'''
# 根据指定的宽度打印格式良好的价格列表
width = int(input('please input the width : '))

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width) # 这里花括号表示要替换两次
fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)

print(header_fmt.format('Item', 'Price'))

print('-' * width)

print(fmt.format('Apples',0.4))
print(fmt.format('Pears',0.5))
print(fmt.format('Cantaloupes',1.92))
print(fmt.format('Dried Apricots (16 oz.)',8))
print(fmt.format('Prunes (4 lbs.)',12))

print('=' * width)
# 字符串规范输出不熟
'''
'''
# string 方法
print('I love you'.center(40,'*'))  # center
# find
sentence = 'I LOVE YOU '
print(sentence.find(' '))
# join
seq = ['1', '2','3', '4', '5' ]
sep = '+'
print(sep.join(seq)) # 注意这里join的顺序也很重要，sep.join(seq)表示把sep加紧seq
# lower将字符串变为小写
print("I LOVE YOU".lower())
# 查找替换功能 replace
print("I HATE YOU".replace("HATE","lOVE"))
# split去除序列特定字符
print('1+2+3+4'.split('+'))
# strip去除字符串开头结尾的空白
print("  I LOVE YOU    ".strip())
# translate 函数
'''
'''
# 字典学习
data = {'age':'43','name': 'Leo'}
print(len(data))
print(data['age'])  # 字典索引取 【】，创建用｛｝

# 字典示例，简单数据库
people = {
    'Alice' :{
        'phone': '2341',
        'addr' : 'Foo drive 23'
    },
    'Beth' : {
        'phone' : '9102',
        'addr' : 'Bar street 42'
    },
    'Cecil' : {
        'phone' : '3158',
        'addr' : 'Baz avenue 90'
    }
}

# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}
name = input('Name : ')

# 查找对象为电话号码还是地址、
request = input("phone(p) or address (a) ?")

# 使用正确的键
if(request == 'p'):
    key = 'phone'
if(request == 'a'):
    key = 'addr'

# 仅当名字被正确包含时才打印信息
if name in people:
    print("{}'s {} is {}".format(name, labels[key], people[name][key]))
'''

'''
note :  
      a . 这里字典people里面镶嵌 字典每个人对应的字典
      b . 这里输出使用format特别有趣
'''
'''
   常见字典方法：
      a . clear删除所有字典项 
      b . copy(浅复制)返回一个新字典。其包含的键值对与原来字典相同，如果就地修改的化原字典也会发生变化
      c . deepcopy(深复制)，不会改变原字典的值
      d . fromkeys 创建新字典，包含指定键，键值均为 none eg:　｛｝．ｆｒｏｍｋｅｙｓ（［＇ｎａｍｅ＇，＇ａｇｅ＇］）
      e . get, 用get访问不存在的键时没有发生异常。
      g . items 返回一个包含所有字典项的列表，其中每个元素都为 （key,value）的形式 返回值属于 字典视图，可自己手动转化成列表 
      h . keys 返回字典视图 ，包含指定字典中的键
      i . pop 获取指定键值，并将该键值对删除
      j . popitem 随机弹出字典项。（字典是无序的）
      k . setdefault 当所查询键不存在时，插入一个 键：NONE 的字典项
      l . update 使用一个字典项来更新另一个字典
'''

'''
     a. 当要对字典执行字符串格式设置操作，不能使用format 和 命名参数 ，而必须使用 format_map
'''

'''
   note : (语句)
     a . print 语句 可利用 sep 语句来自定义 分隔符 eg : sep = "_"
     b . import 时 给模块指定 别名用 as : import math as foobar 
     c . 赋值魔法 ： *rest 
          a,b,*rest = [1,2,3,4]
         python 也支持链式赋值 ， 增强赋值
     d . 标准值false和None 各种类型的0，空序列 以及 空映射  都被视为假，其他值均被视为 真
     e . python 中的 is 检查两个对象是否相同（而不是相等）
     f . 一些迭代工具 ： 
     g . 跳出循环 ： break ; continue ; while true a
     h . 其它神奇语句 ： 
         （1） pass 
              在编写代码时，将其用作占位符
         （2） del 
              删除名称
         （3） exec , eval 作为函数主要强调命名空间的重要性
               exec用于将字符串作为python程序执行
               eval 计算用字符串表示的表达式并返回结果
     i . 推导 ： 列表推导是一种从其他列表创建列表的方式：
         eg: [x * x for x in range(10)]
     
     
'''

'''
    note : (代码块)  ：
       a . python 标准缩进为 4个空格。
       b . python 中 使用 冒号 表示代码块
'''

'''
    note : (抽象) ：
       a . 函数用 def 定义
       b . 给函数编写文档 ： 在def语句后面添加独立的字符串
           def square(x):
               'Calculates the square of the number x'
               return x * x
            #文档字符串可以通过以下方式访问：
             square._doc_
       c . 在函数内部给参数赋值对外部没有影响（可以类比C#中形参 实参学习）
       d . 将列表或者字典作为形参： 
       e . 关键字参数： 
           位置参数： 给函数传参数时，按照顺序，依次传值（不过传值如果根据参数名称传值，顺序就无所谓）
           收集参数： 可以一次传入多个值
                      eg : def power(*args):
                           def leo(*rest):
           分配参数： 传递字典
                      eg : def with_stars(**kwds):
                       
           默认参数： 即在给出形参时已经把值确定了。 
                      eg : def power(m.n=3):
                      attention: 必选参数在前，默认参数在后，否则python会报错
                                 默认参数一定要指向不变对象！
'''

'''
    note : 在继续往下走之前，先重温一下python里面比较魔幻的三种数据结构
            元组 ： 定义元组后无法再添加或修改元祖中的元素，但是可以重新赋值，元组的索引以 0 为基点
                    定义tuple  tuple1 = tuple(50,)
            列表 ： 列表可以包含任何种类的对象： 数字，字符串，甚至是其他列表(列表推导) []
            字典 ： 键值对
             
'''
'''
#  为了搞懂神奇的各种各样的参数而写的代码
def story(**kwds):
    return 'Once upon a time, there was a ''{job} called {name},'.format_map(kwds)
def power(x, y, *rest):
    if(rest):
        print('Received redundant parameters: ', rest )
    return pow(x,y)
def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if(stop is  None):
        start, stop = 0, start
    result = []

    i = start
    while(i < stop):
        result.append(i)
        step = step + i
    return result
print(story(job='king',name = 'Gumby'))
params = {'job':'language','name': 'python'}
print(story(**params))
del params['job']
print(story(job = 'stoke of genius',**params))
'''
# 如果啥时候对参数迷糊了可以重新返回这里疯狂调用函数（笑）

'''
    note : ( 有关命名空间和作用域 )
          a . 除全局作用域外，每个函数调用都将创建一个。（慎用全局变量，它是众多bug的根源）
          b . 有关函数内部访问全局变量的问题： 可利用globals 来访问全局变量。类似vars， 返回一个包含全局变量的字典，
              locals 返回一个包含局部变量的字典
          c . 如何告诉 python 函数内部定义的变量是全局变量呢？
              global x 
          d . 有关全局局部变量的简单例子： 
              def combine(parameter) : 
                  print(parameter + global()['parameter'])
'''

'''
    note : ( 有关递归 )
          a . 递归在C语言中 那个 智力塔中 已经有比较明显的体现了，后来在数据结构的学习中 树 中运用的也比较多，这个暑假还
              是想把数据结构重新学习一下。
          b . 循环往往比递归效率更高，然而递归可读性更高，要理解别人写的递归算法。
          c . 理解递归，主要是理解 最小条件 和 问题是如何被分解的 这种逻辑。
'''
'''
# 经典递归实现
def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# 二分查找的递归实现
def search(sequence, number, lower, upper):
    if(lower == upper):
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper)//2
        if(number) > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
'''
# 有关函数式编程
# 理解暂时比较有限，主要是常用的命令式编程表达解决问题的步骤，函数编程体现的是一个映射。

'''
    note : (深入抽象) ： 
        a . 重新温习 面向对象编程的几个特性：
            （1）. 多态： 对不同类型的对象执行相同的操作。
                  这个世界的多变和复杂造就了多态的重要性
            （2）. 封装： 对外部隐藏有关对象工作院里的细节。（黑盒）
            （3）. 继承： 由父类继承出子类  
        b . python中的多态
           在python中，重要的不是数据的类型，重要的是它是否是能按你所希望的那样行事
           在编程界也被戏称 鸭子类型：
             如果走起来像鸭子，叫起来像鸭子，那么它就是鸭子
'''

# 创建类

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("hello, world! I am {}.".format(self.name))

foo = Person()
foo.set_name('夏灿')
foo.greet()


'''
   note( 类 );
    a . python 中类的方法第一个参数 为 self，实际上可以随便命名，但是由于它总是指向对象本身，因此习惯上将其命名为self。
    b . 类定义其实就是要执行的代码段
    c . 有关类的继承 ：  
          class Filter:
          class SPAMFilter(Filter):     (SPAMFIlter 是 Filter 的子类)
    d . 这里隐藏属性相关好像了解的不太清楚
    e . 深入研讨继承： 
        （1）. 要确定一个类是否是另一个类的子类，可用内置方法 issubclass
               顺序很重要  ： issubclass(SPAMFilter, Filter)
        （2）. 如果有一个类，想知道基类，可访问特殊属性 _bases_
             eg : SPAMFilter.bases
        （3）. 要确定对象是否是特定类的实例，可使用 isinstance
            eg : isinstance(s, SPAMFilter)
        （4）. 多重继承
        （5）. 接口： 处理多态对象时，我们只关心其接口（协议）——对外暴露的方法和属性
               如果要确定对象是由什么组成的，应该研究模块inspect
        （6）. python通过引入模块abc提供了官方解决方案 。 这个模块为所谓的抽象基类提供了支持
               抽象基类用于指定子类必须提供哪些功能，却不实现这些功能
        （7）. 一些比较有趣的函数：
               random.choice(sequence) : 从一个非空序列中随机选择一个元素
               getattr : 获取属性的值，还可以提供默认值
               hasattr : 确定对象是否有指定的属性
               setattr : 将对象的指定属性设置为指定的值
'''
'''
# 多重继承代码实例
class Calculor:
    def calculate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print('Hi, my value is',self.value)

class TalkingCalculator(Calculor, Talker):
    pass
# 上面就完成了一个会说话的计算器基本模型
# 使用多重模型时一定注意： 如果多个超类以不同方式实现了同一个方法，必须在class语句中小心排列，因为位于前面的方法将覆盖
# 后面类的方法。
'''

'''
   note  : (有关面向对象的一点思考)
        a . 将相关的东西放在一起，最好将他们作为一个类的属性和方法。（或者是多个基类）
        b . 一个类的方法应只关心其所属实例的属性
        c 。 慎用继承，（尤其是多重继承），容易产生bug qaq
        d . 确保自己的方法简单，尽量控制简短，如果不行，保持一面
        e . 在确定类和方法时，可通过下列步骤进行： 
           记录问题描述 ——> 给所有名词，动词，形容词加上标记 ——> 在名词中找出可能的类，动词中找出可能的方法，形容词
           中找出可能的属性 ——> 将找出的方法和属性分配给各个类
           进一步改进模型 ： 
           （1） 设想一系列用例，即使用程序的场景，并尽力保证这些用例涵盖了所有需要的功能
           （2） 透彻而仔细地考虑每个场景，确保模型包含了所需的一切，否则修改，然后不断重复
'''

'''
   note : （异常)
        a . python 使用异常对象来表示异常状态，并在遇到错误时引发异常，异常对象未被处理时，程序终止显示错误消耗死
        b . 如何创建异常类，务必直接或间接地继承Exception
        c . 有关捕捉异常 ： 代码实例如下
        d . 如果要使用一个except子句捕获多种异常，可在一个元组中指定这些异常，代码实例同下
        e . 异常魔法 ： 用一段代码捕获所有的异常：
            try:
                pass
            except:
                print('something wrong happened')
            但是注意用异常魔法时，你不能知道发生了哪些异常
        f . finally子句发生异常时执行清理工作，和try 子句配套
        g . 在检查对象是否包含特定属性时，try/except也很有用：
            eg : 
                try:
                   obj.write
                except AttributeError
                   print('The object is not writeable')
                else:
                   print('The obkect is writeable')    
        h . 如果只想发出警告，指出情况偏离正轨，可使用warnings 中的函数 warn
'''

'''
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x/ y)
except ZeroDivisionError:
    print("the second number can not be zero")

try:
    x = int(input('Enter the firsr number: '))
    y = int(input('Enter the second number: '))
    print(x / y )
except(ZeroDivisionError, TypeError, NameError): # 圆括号表示在捕获多个异常时，也只向except提供了一个参数——一个元组
    print('Your numbers were bugs')

# 小型除法程序异常处理
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is ',value)
    except Exception as e:
        print('Invaliud input: ',e)
        print('Please try again')
    else:
        break
# 上述程序将会打印错误信息并且要求用户持续输入直到得到正确结果
'''

'''
    note (魔性方法_特性_迭代器)：
         a . 魔性方法 1 ：构造函数
             其实就是一些初始化方法，只是多了下划线。
             但是构造函数将在对象创建后自动调用它们
             继承函数中重写构造函数时，需要用函数super继承基类的构造函数：
               eg :
                   class Bird:
                      def __init__(self):
                           self.hungry = True
                      def eat(self):
                           if self.hungry:
                               print('Aaaah...')
                               self.hungry = FALSE
                           else:
                               print('No thanks')
                   class SongBird(Bird):
                       def __init__(self):
                           super().__init__()
                           self.sound = 'Squawk !'
                       def sing(self):
                           print(self.sound)
'''

'''
    note （基本的序列和映射协议） ：
        a . __len__(self) : 这个方法应返回集合包含的项数，如果__len__返回0. 对象在布尔上下文中将被视为假
        b . __getitem__(self, key): 这个方法应返回与指定键相关联的值。
        c . __setitem__(self, key, value) : 这个方法应以与键相关联的方式储存值，以便以后能够使用__getitem__来获取
        d . __delitem__(self, key) : 这个方法在对对象的组成部分使用__del__语句时才被调用。应删除与key相关联的值
'''

# the following lines are the practice for the note //这里没懂
def check_index(key):
    '''
    指定的键是否是可接受的索引？

    键必须是非负整数，才是可接受的。如果不是整数，将引发TypeError异常；
    如果是负数，将引发IndexError异常（序列长度无穷）
    '''
    if not isinstance(key, int): raise TypeError
    if(key < 0): raise IndexError

class ArithmeticSequence :

    def __init__(self, start = 0, step = 1):
        '''
        初始化算术序列

        start  - 序列中的第一个值
        step -两个相邻值的差
        changed -一个字典。包含用户修改后的值
        '''
        self.start = start    #  储存起始值
        self.stop = step      #  储存步长
        self.changed = {}     #  没有任何元素被修改

    def __getitem__(self, key):
        '''
        从算术序列中获取一个元素
        '''
        check_index(key)

        try: return self.changed[key]  # 修改过？
        except KeyError:               # 如果没有修改过
            return self.start + key * self.step     # 就计算元素的值

    def __setitem__(self, key, value):
        '''

           修改算术序列中的元素
        '''

        check_index(key)

        self.changed[value] = value
s = ArithmeticSequence(1,2)
s[4]
# 9.5重新学习


'''
   note: (从list,dict和str派生)
     a . 如果只想定制某种操作的行为，就没有理由去重新实现其他所有方法。
          通过继承来实现，例如，如果要实现一种行为类似于内置列表的序列类型，可直接继承list
     b . 如果要更详细的了解有哪些魔法方法，可参阅 'python refernce manual'中的special method names
     c . 函数property : 通过调用函数property将存取方法作为参数（获取方法在前，设置方法在后）创建了一个特性，然后将名称
         size 关联到这个特性。
'''

# -*- coding: utf-8 -*-
'''
Understand other's thinking of this model
Try to improve it

muhoushaonian
2018/8/25
'''

'''
绘制饼图
'''
'''
收获：
1.解决matplotlib中文乱码的问题
  解决办法：在代码中动态设置参数
matplotlib.rcParams['font.sans-serif'] = ['Simei']
matplotlib.rcParams['font.family'] = 'sans-serif'
2.中文字符前加u
'''
def draw_pie(path):
    import matplotlib.pyplot as plt
    import pandas as pd
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    data = open(path)
    data = pd.read_csv(data)

    # 女
    female = data[data.gender == u'Female']
    '''
    u/U indicate unicode usually, English can be decode.But Chinese must occur with u
    r/R (非转义字符)
    '''
    # 男
    male = data[data.gender == u'Male']

    # 调节图形的大小，宽，高
    plt.figure(figsize=(5, 4))
    # 定义饼状图的标签
    labels = [u'Female(女)', u'Male(男)']
    # 每个标签占多大，自动去算百分比
    sizes = [female.shape[0], male.shape[0]]  # shae
    colors = ['orange', 'lightskyblue']
    # 将某部分爆炸出来，使用括号，将第一块分割出来，熟知的大小是分隔出来的与其他两块的间隙
    explode = (0.05, 0)

    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=True,
                                      startangle=90, pctdistance=0.6)
    # labeldistance ,文本的位置离原点有多远
    # autopct 圆里面的文本格式， %3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow 饼是否有阴影
    # startangle 起始角度，0，表示从0开始逆时针旋转，为第一块。一般选择从90度开始比较好看
    # pctdistance 百分比的text离圆心的距离
    for t in l_text:
        t.set_size = 15
        
    for t in p_text:
        t.set_size = 15

    # 设置x, y 轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title(u'性别比',size = 30)
    plt.rc('font',family = 'STXihei', size = 8)
    plt.legend()
#plt.savefig(u'图片\性别比.png', font = 'png')
    plt.show()
    plt.close()

if __name__ == '__main__':
    import time
    import pandas as pd

    path = u'diabetic_data.csv'
    #绘制饼图
    draw_pie(path)


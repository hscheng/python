# groupbar
# https://chrisalbon.com/python/matplotlib_grouped_bar_plot.html

import matplotlib
import matplotlib.pyplot as plt
import random

# 提取颜色库
# https://stackoverflow.com/questions/22408237/named-colors-in-matplotlib
colorset = [hex for name, hex in matplotlib.colors.cnames.items() if 'FF'  in hex and '00'  in hex]

import random
# 用于颜色随机抽样

def groupbar(df,idx,cols,title = 'GroupBarRes',xlabel = 'x label',ylabel='y label'):
    # Setting the positions and width for the bars
    col_cnt = len(cols)
    colors = random.sample(colorset,col_cnt)
    print(colors)
    pos = list(range(len(df[idx]))) 
    width = 0.2

    # Plotting the bars
    fig, ax = plt.subplots(figsize=(10,5))

    # 循环作图
    for i,col in enumerate(cols):
        plt.bar([p + width*i for p in pos],df[col],width,alpha=0.5,color = colors[i])

    # 图表标题
    ax.set_title(title)
    # Y轴标题
    ax.set_ylabel(ylabel)
    # X轴标题
    ax.set_xlabel(xlabel)
    # X轴标签位置
    ax.set_xticks([p + 1.5 * width for p in pos])
    # X轴标签
    ax.set_xticklabels(df[idx])
    # 坐标轴范围
    plt.xlim(min(pos)-width, max(pos)+width*4)
    plt.ylim([0, max([max(df[i]) for i in cols])*1.1])
    # 添加图例
    plt.legend(cols, loc='upper left')
    #plt.grid()
    plt.show()

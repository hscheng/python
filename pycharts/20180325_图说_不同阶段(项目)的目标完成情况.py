
# coding: utf-8

# In[1]:

# ref:http://blog.csdn.net/dgatiger/article/details/50414549
# 载入pyplot之前进行字体设置
import matplotlib  
matplotlib.use('qt4agg')  
#指定默认字体  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
matplotlib.rcParams['font.family']='sans-serif'  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus'] = False   


# In[2]:

import matplotlib.pyplot as plt
import numpy as np


# In[3]:

get_ipython().magic('matplotlib inline')


# In[4]:

# https://matplotlib.org/gallery/api/barchart.html#sphx-glr-gallery-api-barchart-py
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom')


# In[5]:

ax.xaxis.set_label('s')


# In[31]:

# 坐标轴标签
tags = ['M1','M2','M3','M4','M5','M6']
'''# 目标值
vals_tar = [0.5333,0.5461,0.5461,0.5361]
# 实际值
vals_act = [0.4833,0.5561,0.5561,0.5381]'''

# 目标值
vals_tar = [200,180,280,260,300,310]
# 实际值
vals_act = [190,160,320,270,290,305]

# 完成率
vals_rate = np.array(vals_act)/np.array(vals_tar)

# 标记是否达标
idx = list(np.where(vals_rate>1)[0])

# 颜色设置
colors = list(map(lambda x: 'r' if x<1 else 'g',vals_rate))


tag_cnt = len(tags)
x_pos = list(range(tag_cnt))
# x_pos[-1] = tag_cnt-0.8 # 调整间距


fig,ax = plt.subplots()

fig.set_figheight(5)
fig.set_figwidth(13)
fig.set_facecolor('w')
#fig.frameon = 'False'


# 去除左右两边以及上面的spines，设置为无色
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ylim_min = min(min(vals_tar),min(vals_act))*0.9
ylim_min = 0
ylim_max = max(max(vals_tar),max(vals_act))*1.1
ax.set(ylim=[ylim_min,ylim_max])

# 调整坐标轴线的位置
ax.spines['left'].set_position(('data',-1))
ax.spines['bottom'].set_position(('data',ylim_min))

# 绘制直方图    
bchart = ax.bar(left = x_pos,height=vals_act,align='center',color='salmon',edgecolor='none',width=0.5)
bchart2 = ax.bar(left = x_pos,height=vals_tar,align='center',color='none',edgecolor='black',linewidth=1.5,width=0.6)


# x轴设置
# ax.xaxis.set(ticks = x_pos,ticklabels=tags)
ax.set_xticks(x_pos)
ax.set_xticklabels(tags,fontdict={'size':14})
#matplotlib.rc('xtick',labelsize=14)
#matplotlib.rcParams.update({'font.size':1})
ax.tick_params(axis='x',direction = 'inout',length = 0)
# y轴设置
# ax.yaxis.set(ticks = np.arange(ylim_min,ylim_max,0.05))
ax.yaxis.set(visible = False)

# 主图形设置
[bchart[i].set_color('darkseagreen') for i in idx]

'''# 对累计状态进行特殊标记，最后一个bar
bchart[tag_cnt-1].set_edgecolor('k')
bchart[tag_cnt-1].set_linestyle('--')
bchart[tag_cnt-1].set_facecolor('r')
bchart[tag_cnt-1].set_linewidth(2)'''
# 加数据标签
'''autolabel2(bchart,colors)
autolabel2(bchart2,colors)'''

# 柱形图下方添加数据标签
ax.text(-1,ylim_min-ylim_max*0.1,'目标值',fontsize=14)
# 添加每个item的文字，并用颜色标识是否达标
for i,j,k in zip(x_pos,vals_tar,colors):
    ax.text(i,ylim_min-ylim_max*0.1,'{:0.0f}'.format(j),fontsize = 14, color=k,horizontalalignment='center')

ax.text(-1,ylim_min-ylim_max*0.2,'实际值',fontsize=14)
# 添加每个item的文字，并用颜色标识是否达标
for i,j,k in zip(x_pos,vals_act,colors):
    ax.text(i,ylim_min-ylim_max*0.2,'{:0.0f}'.format(j),fontsize = 14, color=k,horizontalalignment='center')
    
ax.text(-1,ylim_min-ylim_max*0.3,'完成率',fontsize=14)
# 添加每个item的文字，并用颜色标识是否达标
for i,j,k in zip(x_pos,vals_rate,colors):
    ax.text(i,ylim_min-ylim_max*0.3,'{0:.2%}'.format(j),fontsize = 14, color=k,horizontalalignment='center')

    
'''
ax.text(1,0.6,'bbb',fontsize = 12, color='g',horizontalalignment='center')
ax.text(2,0.6,'ccc',fontsize = 12, color='g',horizontalalignment='center')
ax.text(3,0.6,'ddd',fontsize = 12, color='g',horizontalalignment='center')
'''
plt.title(s = '各阶段目标完成情况',fontsize=20,fontweight=20,loc='center')
#ax.title = '22'#(text ='dfdfa',fontsize=12,horizontalalignment='center')

#text='', color=None, verticalalignment='baseline', horizontalalignment='left',
# 图表展示
plt.show()


# In[34]:

# 坐标轴标签
tags = ['A','B','C','D','E','F']
'''# 目标值
vals_tar = [0.5333,0.5461,0.5461,0.5361]
# 实际值
vals_act = [0.4833,0.5561,0.5561,0.5381]'''

# 目标值
vals_tar = [200,180,280,260,300,310]
# 实际值
vals_act = [190,160,320,270,290,305]

# 完成率
vals_rate = np.array(vals_act)/np.array(vals_tar)
vals_avg = np.average(vals_act)
# 标记是否达标
idx = list(np.where(vals_rate>1)[0])

# 颜色设置
colors = list(map(lambda x: 'r' if x<1 else 'g',vals_rate))


tag_cnt = len(tags)
x_pos = list(range(tag_cnt))
# x_pos[-1] = tag_cnt-0.8 # 调整间距


fig,ax = plt.subplots()

fig.set_figheight(5)
fig.set_figwidth(8)
fig.set_facecolor('w')
#fig.frameon = 'False'


# 去除左右两边以及上面的spines，设置为无色
# ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_color('none')

ylim_min = min(min(vals_tar),min(vals_act))*0.9
ylim_min = 0
ylim_max = max(max(vals_tar),max(vals_act))*1.1
ax.set(xlim=[ylim_min,ylim_max*1.2])

# 调整坐标轴线的位置
# ax.spines['left'].set_position(('data',-1))
# ax.spines['bottom'].set_position(('data',ylim_min))

# 绘制直方图    
bchart = ax.barh(bottom = x_pos,width=vals_act,align='center',color='salmon',edgecolor='none',height=0.5)
bchart2 = ax.barh(bottom = x_pos,width=vals_tar,align='center',color='none',edgecolor='black',linewidth=1.5,height=0.6)


# x轴设置
ax.set_yticks(x_pos)
ax.set_yticklabels(tags,fontdict={'size':14})
ax.tick_params(axis='y',direction = 'inout',length = 0)
# y轴设置
# ax.yaxis.set(ticks = np.arange(ylim_min,ylim_max,0.05))
# ax.yaxis.set(visible = False)
ax.xaxis.set(visible = False)

# 主图形设置
[bchart[i].set_color('darkseagreen') for i in idx]


# 加数据标签
'''autolabel2(bchart,colors)
autolabel2(bchart2,colors)'''

# 提示差异值==========================================
# 添加左侧文字
ax.text(ylim_max,tag_cnt,'目标值',fontsize=12, horizontalalignment='center')
# 添加每个item的文字，并用颜色标识是否达标
for i,j,k in zip(x_pos,vals_tar,colors):
    ax.text(ylim_max,i,'{:0.0f}'.format(j),fontsize = 12, color=k,horizontalalignment='center')

ax.text(ylim_max*1.1,tag_cnt,'实际值',fontsize=12, horizontalalignment='center')
# 添加每个item的文字，并用颜色标识是否达标
for i,j,k in zip(x_pos,vals_act,colors):
    ax.text(ylim_max*1.1,i,'{:0.0f}'.format(j),fontsize = 12, color=k,horizontalalignment='center')

ax.text(ylim_max*1.2,tag_cnt,'完成率',fontsize=12, horizontalalignment='center')
# 添加每个item的文字，并用颜色标识是否达标
for i,j,k in zip(x_pos,vals_rate,colors):
    ax.text(ylim_max*1.2,i,'{0:.2%}'.format(j),fontsize = 12, color=k,horizontalalignment='center')
    
#实际完成值均值参考线
ax.axvline(x=vals_avg, color = 'k', linewidth = 2,linestyle='--')
ax.text(vals_avg,6,'平均值',fontsize=12, horizontalalignment='center')
ax.text(vals_avg,-1.5,'{:0.0f}'.format(vals_avg),fontsize=12, horizontalalignment='center')

plt.title(s = '各项目完成情况',fontsize=20,fontweight=20,loc='left')
#ax.title = '22'#(text ='dfdfa',fontsize=12,horizontalalignment='center')

#text='', color=None, verticalalignment='baseline', horizontalalignment='left',
# 图表展示
plt.show()


# In[ ]:




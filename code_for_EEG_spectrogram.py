#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:11:27 2020

@author: yejohnny
"""

#heatmap for EEG

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator,FormatStrFormatter
import matplotlib.ticker as ticker
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap,ListedColormap
import numpy as np
from scipy import stats
from sklearn import preprocessing

file = 'E:/ZYL/Arousal/EEG/EEG1.csv' 

data = pd.read_csv(file,index_col='EpochNo')

#sns.heatmap(data)
Hz_list = []
for i in data.index.to_list():
    values = i[:-2]
    Hz_list.append(float(values))


#data = data.T

data.index = Hz_list
data = data.sort_index(ascending=False) 
#data = data[data.index>1]
#data = data[data.index<26]
data.to_csv(file.split('.')[0] +'_analysis_.csv')

#normaliezd_data = stats.zscore(data)
#normaliezd_data2 = stats.zscore(normaliezd_data)

normaliezd_data = preprocessing.minmax_scale(data,feature_range=(0, 1), axis=0, copy=True)




data_min= 0  ### 颜色半
data_max= 1

print(normaliezd_data.max().max(),normaliezd_data.min().min())

top = mpl.cm.get_cmap('Blues_r', 128)
bottom = mpl.cm.get_cmap('hot_r', 128)

newcolors = np.vstack((top(np.linspace(0.05,0.3, 128)),
                       bottom(np.linspace(0.05,0.3, 128))))
newcmp = ListedColormap(newcolors, name='copper_Blue')


f, ax = plt.subplots(figsize=(20,3),dpi=300)
sns.set(font = 'Times New Roman', font_scale=1.2)

Paired = ["windows blue", "amber"]
plot = sns.heatmap(normaliezd_data,vmin=data_min,vmax=data_max,cmap='RdYlBu_r',cbar_kws={'shrink':0.8})

ax.xaxis.set_major_locator(ticker.MultipleLocator(60))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0,size = 15)
majors = list(range(60,1261,60))
majors.insert(0,0)
majors.insert(0,'')
ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))


#ax.yaxis.set_major_locator(ticker.AutoMinorLocator())
#ax.yaxis.set_major_locator(ticker.AutoLocator())
#ax.set_yticklabels(ax.get_yticklabels(),rotation=0,size = 15)
'''
ymajors = list(range(25,5,-5))
ymajors.append(5)
ymajors.append(0)
ax.yaxis.set_major_formatter(ticker.FixedFormatter(ymajors))
'''


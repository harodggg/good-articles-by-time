# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:12:16 2018

@author: peter
"""

import matplotlib.pyplot as plt
date=['2018-5','2018-6','2018-7','2018-8','2018-9','2018-10','2018-11','2018-12',
    '2019-1','2019-2','2019-3','2019-4','2019-5','2019-6','2019-7','2019-8','2019-9','2019-10','2019-11','2019-12',
    '2020-1','2020-2','2020-3']
number=[27,100,202,75,310,387,265,226,
        186,142,110,36,100,133,128,130,74,110,50,32,
        108,60,46]
print("total number: ",sum(number))

plt.figure(figsize=(10,10))

plt.title("时间与文章阅读数",fontproperties='SimHei',fontsize=25)
plt.xlabel("时间",fontproperties='SimHei',fontsize=15)
plt.ylabel("文章阅读数",fontproperties='SimHei',fontsize=15)
plt.gcf().autofmt_xdate()
plt.plot(date,number)
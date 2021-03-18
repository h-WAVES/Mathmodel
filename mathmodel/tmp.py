# -*- coding: utf-8 -*- 

# @Time : 2021-03-18 13:49 
# @Author : hht 
# @File : tmp.py
# @Desc:temp file


from mathmodel import dataset

boston_data=dataset.load_boston(type='pandas')
print(type(boston_data))

from .base import *

__all__ = ['load_iris',
           'load_boston',
           'load_wine',
           'bunchtoDF']

"""
    'using 默认是pandas格式，如需转化通过type指定'
    
    from mathmodel import dataset
    
    boston_data=dataset.load_boston(type='pandas')
    print(type(boston_data))

->  <class 'pandas.core.frame.DataFrame'>

"""

import pandas
from pandas import Series, DataFrame

# kakao = Series([1, 2, 3], index=['a','b','c'])
# print(kakao)
#
#
# row = {'col1':[1,2,3,4],
#        'col2':[3,4,5,6],
#        'col3':[7,8,9, '']
# }
# data = DataFrame(row)
# print(data)
#
#
# print(type(data['col1']))

import pandas_datareader.data as web
import datetime
start = datetime.datetime(2020, 8, 1)
end = datetime.datetime(2020, 8, 20)
gs = web.DataReader('078930.KS', 'yahoo', start, end)
print(gs)

print(gs.info())

import matplotlib.pyplot as plt
print(plt.plot(gs['Close']))


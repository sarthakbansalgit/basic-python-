import matplotlib.pyplot as pl
x = ['delhi','haldwani','ramnagar','udaypur','lucknow','rarhmera']
y = [21,3,4,45,23,66]
pl.xlabel('city')
pl.ylabel('sales')
pl.title('sales according to cites')
pl.bar(x,y)
pl.show()

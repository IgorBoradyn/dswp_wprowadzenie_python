from datetime import datetime

print('{0:_<10} {0:_>10} {0:_^10}'.format('test1'))
print('{:.2}'.format('test2'))
print('{:_^5.3}'.format('test'))
print('{:%Y-%m-%d %H:%M}'.format(datetime(2023, 3, 6, 18, 35)))
print('{:_=+5d} {:=+05d}'.format(10, -10))



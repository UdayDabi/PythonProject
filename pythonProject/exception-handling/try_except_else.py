a = 10
b = 2

try:
    c = a / b
    print('division:', c)
except ZeroDivisionError as e:
    print('exception:', e)
finally:
    print(  'in finally block')
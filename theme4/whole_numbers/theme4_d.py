d = int(input())

hours = d // 30
remainder = d % 30
minutes = remainder * 2
print('It is', hours, 'hours', minutes, 'minutes.')

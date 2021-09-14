block = int(input('Blocks: '))

if block >= 8192:
    result = block / 8192
    unit   = 'GB'
elif block >= 8:
    result = block / 8
    unit   = 'MB'
else:
    result = block * 128
    unit   = 'KB'

print (f'{block} block = {result} {unit}')

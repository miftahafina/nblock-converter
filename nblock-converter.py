while True:
    print('Type number (int) or "exit"')
    block = input('Block: ')

    if block == 'exit':
        break
    else:
        try:
            block = int(block)
            if block >= 8192:
                result = block / 8192
                unit   = 'GB'
            elif block >= 8:
                result = block / 8
                unit   = 'MB'
            else:
                result = block * 128
                unit   = 'KB'
            print (f'=> {block} block = {result} {unit}')

        except ValueError:
            print(f'=> {block} is not an integer number')

while True:
    try:
        l= [int(i) for i in input('введите целые числа через пробел ').split( )]
        break  
    except (IndexError, ValueError, TypeError):
        print('неверный ввод данных')
        continue
def get_ranges(arg):
    arg=sorted(list(set(arg)))
    str_arg=''
    previous_num=arg[0]-1
    start_num=0
    for i in arg:
        if start_num==0:
            start_num=i

        if previous_num+1!=i:
            if start_num==i:
                str_arg+=f'{i}, '
            else:
                str_arg+=f'{start_num}-{previous_num}, '
            start_num=i
        if arg[-1]==i:
            if arg[-1]==start_num:
                str_arg+=f'{i}'
            else:
                str_arg+=f'{start_num}-{i}'
                    
        previous_num=i
    return ''.join(str_arg)   
print(get_ranges(l))










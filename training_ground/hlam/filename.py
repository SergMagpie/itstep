fn_parts = input('Введите имя файла ').split('.')
if len(fn_parts)>1 and fn_parts[0] and fn_parts[-1]:
    print('Расширение файла: ',fn_parts[-1])
else: raise ValueError('the file has no extension')        

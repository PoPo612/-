filename = 'demo.py'
with open(filename,'r') as fp:
    lines = fp.readlines()
maxlength = len(max(lines,key=len))
lines = [line.rstrip().ljust(maxlength)+'#'+str(index)+'\n'
         for index, line in enumerate(lines)]#删除原有的空格，添加空格使每一行与最长行的长度相等，使用index（指定元素首次出现的下标）添加行号
with open(filename[:-3]+'_new.py','w') as fp:
    fp.writelines(lines)#将字符串写入文件

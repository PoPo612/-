filename = 'demo.py'
with open(filename,'r') as fp:
    lines = fp.readlines()
maxlength = len(max(lines,key=len))
lines = [line.rstrip().ljust(maxlength)+'#'+str(index)+'\n'
         for index, line in enumerate(lines)]
with open(filename[:-3]+'_new.py','w') as fp:
    fp.writelines(lines)
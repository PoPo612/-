#!/usr/bin/env python
# coding: utf-8

# In[25]:


s = int(input("请输入一个数为游戏总人数:"))
man = [i for i in range(1,s+1)]#创建一个对应的列表
def move(man, sep):#定义move函数
    for i in range(sep):
        item = man.pop(0)
        man.append(item)
while len(man) > 2:
    move(man, 2)
    
    print("kill {}".format(man.pop(0)))
print("最后剩下的站位：{}".format(man))
    


# In[ ]:





# -*- coding: utf-8 -*- 
import random
import string
import os
#flag值
def random_flag(len):
    #flag中所包含的字符
    seed = 'ABCDEFGHJKMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789' 
    sa = []
    for i in range(len):
    	sa.append(random.choice(seed))
    salt = ''.join(sa)
    flag = 'flag{'+salt+'}'
    print (flag)
    return flag

#创建单独文件
def mkfile(name):
    f = open(name+'.txt','w')
    f.write(name)
    f.close


if __name__ == '__main__':
    len = 8  #定义flag长度
    count = 100 #定义flag数量
    for i in range(count):
        flag = random_flag(len)
        mkfile(flag)

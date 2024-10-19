#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random

n = int(input('값의 범위 입력해주세요 (1~n)\n ex) 1~500 사이값\n'))
answer = random.randint(1,n)
count = 0

while True:
    a = int(input('정답 값을 입력하세요'))
    count += 1
    if a == answer:
        print ('축하합니다. %d번만에 정답 %d를 맞추셨습니다 ~!!!'%(count, answer))
        break
    elif a > answer :
        print('down')
    else:
        print('up')


#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import timedelta

def time_delta(t1,t2):
    
    space_split = t1.split()
    space_split2 = t2.split()

    if space_split[5][0] == '-':
        t1hrs = space_split[5][1] + space_split[5][2]
        t1hrs = int(t1hrs)
        
        t1mins = space_split[5][3] + space_split[5][4]
        t1mins = int(t1mins)
        
        
    if space_split[5][0] == '+':
        t1hrs = space_split[5][1] + space_split[5][2]
        t1hrs = int(t1hrs)*(-1)
        
        t1mins = space_split[5][3] + space_split[5][4]
        t1mins = int(t1mins)*(-1)

        
    if space_split2[5][0] == '-':
        t2hrs = space_split2[5][1] + space_split2[5][2]
        t2hrs = int(t2hrs)
    
        t2mins = space_split2[5][3] + space_split2[5][4]
        t2mins = int(t2mins) 
        
        
    if space_split2[5][0] == '+':
        t1hrs = space_split2[5][1] + space_split2[5][2]
        t2hrs = int(t2hrs)*(-1)
    
        t2mins = space_split2[5][3] + space_split2[5][4]
        t2mins = int(t2mins)*(-1)
        

    months = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', '07':'Jul','08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
    
    if space_split[2] in months.values():
        for key, value in months.items():
            key_list = list(months.keys())
            val_list = list(months.values())
                
            if space_split[2] == value:
                position = val_list.index(value)
                k1 = key_list[position]

            if space_split2[2] == value:
                position = val_list.index(value)
                k2 = key_list[position]
            

    start = datetime.datetime(int(space_split[3]),int(k1),int(space_split[1]), int(space_split[4].split(':')[0]), int(space_split[4].split(':')[1]),int(space_split[4].split(':')[2])) + timedelta(hours = t1hrs, minutes = t1mins)
    end = datetime.datetime(int(space_split2[3]),int(k2),int(space_split2[1]), int(space_split2[4].split(':')[0]), int(space_split2[4].split(':')[1]),int(space_split2[4].split(':')[2])) + timedelta(hours = t2hrs, minutes = t2mins)
    
    result = abs(end-start)

    return int(result.total_seconds())


t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    print(delta)

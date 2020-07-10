# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:06:45 2020

@author: Necro
"""
def mul_strings(num1,num2):
    my_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    
    
    ln1=len(num1)
    ln2=len(num2)
    first=0
    second=0
    for i in range(ln1):
        first+=my_dict[num1[i]]*10**(ln1-i-1)
    for j in range(ln2):
        second+=my_dict[num2[j]]*10**(ln2-j-1)
    
    return (str(first*second))
    
def main():
    
    num1 = "2"
    num2 = "3"
    print("Testcase for:",num1," & ",num2)
    if mul_strings(num1,num2)==str(int(num1)*int(num2)):
        print("passed")
    else:
        print("failed")
    num1 = "123" 
    num2 = "456"
    print("Testcase for:",num1," & ",num2)
    if mul_strings(num1,num2)==str(int(num1)*int(num2)):
        print("passed")
    else:
        print("failed")

if __name__ == '__main__':

    main()
import random
import pandas as pd
import numpy as np
def comput(x,y,z):
    rnd_list=[random.randint(x,y) for a in range(z)] #构建基础随机序列
    comput_mod=""
    for i in map(str,rnd_list):
        comput_mod=comput_mod+i+random.choice([" + "," - "]) #随机添加加减号
        if eval(comput_mod[:-3])<0: #小学生从左到右不能有负数
            comput_mod=comput_mod[:-3-len(i)-3]+" + "+comput_mod[-3-len(i):]
    comput_1stmod=comput_mod[:-3] #截取算式长度，符合外观要求
    k=eval(comput_1stmod) #得到算式的结果
    j=comput_1stmod+" = " #添加等号
    return j,k
####################以上完成单个对应算式的构建，以下构建整表#######################
# (w,x,y,z)=input("please input by the following order:(w,x,y,z).\nw,number of the question(Can be divided exactly by 3).\nx,buttom of range_numerical.\ny,top of range_numerical.\nz,compute length.\nmust input 4 value:")
seq=[]
for ql in range(60): #question number
    seq.append(comput(0,50,2))
seq=pd.DataFrame(seq,index=None)
seq=seq.rename(columns={0:"q1",1:"a1"})
seq_new=pd.DataFrame({})
seq_new["q2"]=list(seq["q1"][int(60/3):2*int(60/3)])
seq_new["a2"]=list(seq["a1"][int(60/3):2*int(60/3)])
seq_new["q3"]=list(seq["q1"][2*int(60/3):])
seq_new["a3"]=list(seq["a1"][2*int(60/3):])
seq_new["q1"]=list(seq["q1"][0:int(60/3)])
seq_new["a1"]=list(seq["a1"][0:int(60/3)])
seq_new.to_excel('D:/dev/py/powerfulmod2.xlsx')

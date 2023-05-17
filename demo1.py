'''
将用户id、商品id、商品类id、商品id转换为数字
'''
import pandas as pd
i = 0
user_dic = {}
i1 = 1
goods_dic = {}
i2 = 1
D1 = {'goods_id' : [],'cat_id':[],'brandsn':[]}
D  = {'user_id':[],'goods_id':[],'is_clk':[],'is_like':[],'is_addcart':[],'is_order':[],'date':[]}
U_id = {'user_id':[],'user':[]}
G_id = {'goods_id':[],'goods':[]}
C_id = {'cat_id':[],'cat':[]}
B_id = {'brandsn':[],'brand':[]}
for i in range(61):
    s = str(i).zfill(5)
    with open('E:/训练集/训练集/traindata_user/part-'+s,'r') as f:
        data = f.readlines()
    for d in data:
        d = d.replace('\n','')
        data1 = d.split(',')
        user = data1[0] #顾客名
        goods = data1[1] #商品名
        t = int(data1[-1][-2:]) #找到2月份的日期转换为整数
        if user not in user_dic.keys():
            user_dic[user] = i1
            U_id['user_id'].append(user)
            U_id['user'].append(i1)
            i1+=1
        if goods not in goods_dic.keys():
            goods_dic[goods] = i2
            G_id['goods_id'].append(i2)
            G_id['goods'].append(goods)
            i2+=1
        D['user_id'].append(user_dic[user])
        D['goods_id'].append(goods_dic[goods])
        D['is_clk'].append(int(data1[2]))
        D['is_like'].append(int(data1[3]))
        D['is_addcart'].append(int(data1[4]))
        D['is_order'].append(int(data1[5]))
        D['date'].append(t)
df = pd.DataFrame(D)
df.to_csv('data.csv')
df = pd.DataFrame(U_id)
df.to_csv('userID.csv')
# hai
c_dic1 = {}
b_dic1 = {}
i2 = 1
i3 = 1
i4 = 1
for i in range(3):
    s = str(i).zfill(5)
    with open('E:/训练集/训练集/traindata_goodsid/part-'+s,'r') as f:
        data = f.readlines()
    for d in data:
        d = d.replace('\n','')
        data1 = d.split(',')
        goods = data1[0] #商品名
        if goods not in goods_dic.keys():
            goods_dic[goods] = i2
            G_id['goods_id'].append(goods)
            G_id['goods'].append(i2)
            i2+=1
        if data1[1] not in c_dic1.keys():
            c_dic1[data1[1]] = i3
            C_id['cat_id'].append(data1[1])
            C_id['cat'].append(i3)
            i3+=1
        if data1[2] not in b_dic1.keys():
            b_dic1[data1[2]] = i4
            B_id['brandsn'].append(data1[2])
            B_id['brand'].append(i4)
            i4+=1
        D1['goods_id'].append(goods_dic[goods])
        D1['cat_id'].append(c_dic1[data1[1]])
        D1['brandsn'].append(b_dic1[data1[2]])
df = pd.DataFrame(D1)
df.to_csv('goods.csv')
df = pd.DataFrame(G_id)
df.to_csv('goodsID.csv')
df = pd.DataFrame(C_id)
df.to_csv('catID.csv')
df = pd.DataFrame(B_id)
df.to_csv('brandID.csv')


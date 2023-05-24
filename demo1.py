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
D  = {'user_id':[],'goods_id':[],'is_clk':[],'is_like':[],'is_addcart':[],'date':[], 'is_order':[]}
U_id = {'user_id':[],'user':[]}
G_id = {'goods_id':[],'goods':[]}
C_id = {'cat_id':[],'cat':[]}
B_id = {'brandsn':[],'brand':[]}

goodsorder = set()

for i in range(61):
    s = str(i).zfill(5)
    with open('训练集/训练集/traindata_user/part-'+s,'r') as f:
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
            G_id['goods_id'].append(goods)
            G_id['goods'].append(i2)
            i2+=1
        D['user_id'].append(user_dic[user])
        D['goods_id'].append(goods_dic[goods])
        D['is_clk'].append(int(data1[2]))
        D['is_like'].append(int(data1[3]))
        D['is_addcart'].append(int(data1[4]))
        D['date'].append(t)
        D['is_order'].append(int(data1[5]))
        if int(data1[5]) == 1:
            goodsorder.add(data1[1])


goodsorder = list(goodsorder)
print(goodsorder)

goods1 = []
B = {'goods': []}
for i in range(2):
    s = str(i).zfill(5)
    with open('测试集a/测试集a/predict_goods_id/part-' + s, 'r') as f:
        data = f.readlines()
    for d in data:
        d = d.replace('\n', '')
        # data1 = d.split(',')
        goods = d  # 商品名
        goods1.append(goods)

goods2 = []
for i in goodsorder:
    if i in goods1:
        goods2.append(i)
        B['goods'].append(goods)
print(len(goods))
df = pd.DataFrame(B)
df.to_csv('g.csv', index=False)
goods2 = goods2[:int(len(goods2) / 50)]

C = {'user_id': [], 'goods_id': []}
data = pd.read_excel('a榜需要预测的uid_5000.xlsx')
for index, row in data.iterrows():
    # print(index,row)
    for i in goods2:
        C['user_id'].append(row['user_id'])
        C['goods_id'].append(i)
df = pd.DataFrame(C)
df.to_csv('u2i.csv', index=False)
#
# df = pd.DataFrame(D)
# df.to_csv('data.csv', index=False)
# df = pd.DataFrame(U_id)
# df.to_csv('userID.csv', index=False)
#
# c_dic1 = {}
# b_dic1 = {}
#
# i3 = 1
# i4 = 1
# for i in range(3):
#     s = str(i).zfill(5)
#     with open('训练集/训练集/traindata_goodsid/part-'+s,'r') as f:
#         data = f.readlines()
#     for d in data:
#         d = d.replace('\n','')
#         data1 = d.split(',')
#         goods = data1[0] #商品名
#         if goods not in goods_dic.keys():
#             goods_dic[goods] = i2
#             G_id['goods_id'].append(goods)
#             G_id['goods'].append(i2)
#             i2+=1
#         if data1[1] not in c_dic1.keys():
#             c_dic1[data1[1]] = i3
#             C_id['cat_id'].append(data1[1])
#             C_id['cat'].append(i3)
#             i3+=1
#         if data1[2] not in b_dic1.keys():
#             b_dic1[data1[2]] = i4
#             B_id['brandsn'].append(data1[2])
#             B_id['brand'].append(i4)
#             i4+=1
#         D1['goods_id'].append(goods_dic[goods])
#         D1['cat_id'].append(c_dic1[data1[1]])
#         D1['brandsn'].append(b_dic1[data1[2]])
# df = pd.DataFrame(D1)
# df.to_csv('goods.csv', index=False)
# df = pd.DataFrame(G_id)
# df.to_csv('goodsID.csv', index=False)
# df = pd.DataFrame(C_id)
# df.to_csv('catID.csv', index=False)
# df = pd.DataFrame(B_id)
# df.to_csv('brandID.csv', index=False)
#







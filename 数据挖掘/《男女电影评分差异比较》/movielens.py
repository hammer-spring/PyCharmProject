import pandas as pd
import numpy as np
# 读入数据
unames = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_table('ml-100k/u.user', sep = '\|', names = unames, engine='python')
rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_table('ml-100k/u.data', sep='\t', names = rnames, engine='python')
# 选择需要的数据列，提高效率
users_df = pd.DataFrame()
users_df['user id'] = users['user id']
users_df['gender'] = users['gender']
ratings_df = pd.DataFrame()
ratings_df['user id'] = ratings['user id']
ratings_df['rating'] = ratings['rating']
# 将数据合并
rating_df = pd.merge(users_df, ratings_df)
gender_table = pd.pivot_table(rating_df, index = ['gender', 'user id'], values = 'rating')
# 利用pandas 中的数据透视表pivot_table()函数对数据进行聚合，gender_table 中的数据形式为：
# gender user id
# F 2       3.709677
#   5       2.874286
# ...
# M 898     3.500000
#   899     3.525926
# …
gender_df = pd.DataFrame(gender_table)
# 分男女
Female_df = gender_df.query("gender == ['F']")
Male_df = gender_df.query("gender == ['M']")
# 按性别计算评分的标准差
Female_std = np.std(Female_df)
Male_std = np.std(Male_df)
print ('Gender', '\nF\t%.6f' % Female_std, '\nM\t%.6f' % Male_std)
"""
 _*_ coding : utf-8 _*_
 @Time : 2025-04-22 14:28
 @Author : luotao
 @File : pandas_io.py
 @Description : 
    pip install pandas
    pip install pymysql
    pip install openpyxl # excel文件读写
"""
import pandas as pd
import pymysql
import datetime
def my_read_sql():
    conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="kuroneko.678",db="mytest")
    df = pd.read_sql("select name,age from user",con=conn)
    print(f"前几行==>\n{df.head()}") 
    print(f"（行数，列数）==> {df.shape}") 
    # print(f"列类型==>\n{df.dtypes}") 
    return df

def my_read_json(file_path="pandas-base/inputdata/movie_boxofficecn_bs4.json"):
    df = pd.read_json(file_path)
    print(f"前几行==>\n{df.head()}") 
    print(f"（行数，列数）==> {df.shape}") 
    # print(f"列类型==>\n{df.dtypes}") 
    return df

def my_read_excel(file_path="pandas-base/inputdata/my-excel.xlsx"):
    df = pd.read_excel(file_path,header=None, names=["Name","Age"])
    print(f"前几行==>\n{df.head()}") 
    print(f"（行数，列数）==> {df.shape}") 
    # print(f"列类型==>\n{df.dtypes}") 
    return df

def my_read_csv_custom_file(file_path="pandas-base/inputdata/csv_custom.txt"):
    df = pd.read_csv(file_path,sep="|",header=None, names=["Name","Age"])
    print(f"前几行==>\n{df.head()}") 
    print(f"（行数，列数）==> {df.shape}") 
    # print(f"列类型==>\n{df.dtypes}") 
    return df

def my_read_csv_file(file_path="pandas-base/inputdata/nba.csv"):
    df = pd.read_csv(file_path)
    print(f"前几行==>\n{df.head()}") 
    print(f"（行数，列数）==> {df.shape}") 
    # print(f"列类型==>\n{df.dtypes}") 
    return df

def my_series():  
    s_by_list = pd.Series([5,2,3,4,1],index=["a","b","c","d","e"]) 
    s_by_dict = pd.Series({"a":5,"b":2,"c":3,"d":4,"e":1}) # index 默认为字典的key
    print(s_by_dict)
    print(s_by_dict["a"]) # 单个key返回原生类型
    print(s_by_dict[["a","e"]]) # 多key还是<class 'pandas.core.series.Series'>
    print('==============series排序==========================')
    print(f'降序==>{s_by_list.sort_values(ascending=False)}')


def my_dataframe_loc(): 
    """dataframe查询  """
    data = {
        "ID":[1,2,3],
        "Name":["@luotao","@kuroneko","@旺财"],
        "Age":[18,20,25],
        "Score":[100,60,30]
    }
    df = pd.DataFrame(data)
    print(df)
    # print(df.dtypes)
    # print(df["Name"]) # 单列返回类型<class 'pandas.core.series.Series'>
    # print(df[["Name","Age"]]) # 多列返回类型还是<class 'pandas.core.frame.DataFrame'>
    # print(df.loc[0:1]) # 第一行到第二行数据
    print("========================================")
    df.set_index("ID",inplace=True) # 在原 DataFrame 上进行设置索引
    df.loc[:,"Name"]=df["Name"].str.replace("@","").astype("object") # ：表示所有行
    # print(df.head()) 
    print(f"按列表,索引为1和2的Name列和Age列==>\n{df.loc[[1,2],["Name","Age"]]}") 
    print(f"按区间查询==>\n{df.loc[1:2,"Name":"Age"]}") 
    print(f"按条件表达式查询==>\n{df.loc[(df['Score']==100) | (df['Score']==60),:]}") 
    def my_query(df):
        return (df['Age'] >=18) & (df['Score'] >=60)
    print(f"调函数my_query查询==>\n{df.loc[my_query,:]}") 
    print('================新增一列NewColumnScore========================')
    df.loc[:,['NewColumnScore']]=df['Score'] + df['Age'] # 新增一列NewColumnScore
    print('================新增一列NewColumnScore2传入函数my_func生成值========================')
    def my_func(x):
        if x["Score"] >=60:
            return "及格"
        else:
            return "不及格"
    df.loc[:,['NewColumnScore2']]=df.apply(my_func,axis=1) # # 新增一列NewColumnScore2传入函数my_func生成值
    print(df['NewColumnScore2'].value_counts()) # 统计NewColumnScore2列的值
    print(df.head())
    print('================新增多列,不会修改原df,而是返回一个新df========================')
    print(df.assign(
        NewColumnScore3=df['Score'] + 1,
        NewColumnScore4=df['Score'] + 2,
    ))# 新增多列,不会修改原df,而是返回一个新df
    print('=================新增一列NewColumnScore5=======================')
    df['NewColumnScore5']=''
    df.loc[df['Score'] >=60,'NewColumnScore5']='合格'
    df.loc[df['Score'] <60,'NewColumnScore5']='不合格'
    print(df.head())

def my_dataframe_statistics(): 
    """dataframe统计  """
    data = {
        "ID":[1,2,3],
        "Name":["@luotao","@kuroneko","@旺财"],
        "Age":[18,20,25],
        "Score":[100,60,30],
        'Date':['2025-04-22','2025-04-23','2025-04-24']
    }
    df = pd.DataFrame(data)
    print(df['Name'])
    print(df.head())
    print("========================================")
    print(f"统计摘要==>\n{df.describe()}")
    print(f"统计某一列的唯一值==>\n{df['Name'].unique()}")
    print(f"某一列的值计数==>\n{df['Name'].value_counts()}")
    print('==============df排序==========================')
    print(f'按分数降序和年龄升序排序==>{df.sort_values(by=['Score','Age'],ascending=[False,True])}')
    print(f'series的str属性==>{df['Date'].str.replace('-','').str.slice(0,8 )}')
    print('==============df新增一列中文日期==========================')
    def my_func(x):
        year,month,day =  x['Date'].split('-')
        return f'{year}年{month}月{day}日'
    df.loc[:,['中文日期']]=df.apply(my_func,axis=1)
    print(df)
    print('==============将中文日期列的年月日字符去除==========================')
    # df['中文日期']= df['中文日期'].str.replace('年','').str.replace('月','').str.replace('日','') # 方法一：字符串替换
    df['中文日期'] = df['中文日期'].str.replace('[年月日]','',regex=True)  # 方法二：正则表达式替换
    print(df)
def download(content,file_path):
    with open(file_path, "w", encoding='utf-8') as fp:  # 使用'w'模式写入文本数据
        fp.write(content)

def my_dataframe_None():
    """ 空值处理 """
    data = {
        "ID":[1,2,3,None ],
        "Name":["@luotao",None,"@旺财",None],
        "Age":[18,20,25,None],
        "Score":[None,60,30,None],
        "EmptyColumn": [None, None, None, None]  # 这一列全是 NaN
    }
    df = pd.DataFrame(data)
    print(df.head())
    print('==============删除所有值均为 NaN 的行或列==========================')
    # print(f"按行删除所有值均为 NaN 的行==>\n{df}")
    df.dropna(axis=0,how='all',inplace=True)
    # print(f"按列删除所有值均为 NaN 的列==>\n{df}")
    df.dropna(axis=1,how='all',inplace=True)
    print(df)
    print('=================填充缺省值=======================')
    # print('将Score列中值为NaN的行填充为0')
    df.loc[:,'Score']=df['Score'].fillna(0)# 等价于 df.fillna({'Score':0},inplace=True) 
    df.loc[:, 'Name'] = df['Name'].ffill()#前向填充填充 Name 列的 NaN 值
    print(df)
    df.to_excel('.output/clean.xlsx',index=False) # 不将写入索引

def my_to_excel():
    df = my_read_json()
    file_path = f'.output/movie{str(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx'
    header=["电影名称","上映年份","制片地区","评分","导演","票房","提交人"]
    df.to_excel(file_path,index=False,header=header) # index=False 表示不保存索引

if __name__ == "__main__":
    # my_read_csv_file()
    # my_read_csv_custom_file()
    # my_read_sql()
    # my_series()
    # my_dataframe_loc()    
    my_dataframe_statistics()
    # my_dataframe_None()
    # my_dataframe_calc()
    # my_to_excel()    


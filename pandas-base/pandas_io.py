import pandas as pd
import pymysql
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
    s_by_list = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"]) 
    s_by_dict = pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5}) # index 默认为字典的key
    print(s_by_dict)
    print(s_by_dict["a"]) # 单个key返回原生类型
    print(s_by_dict[["a","e"]]) # 多key还是<class 'pandas.core.series.Series'>

def my_dataframe(): 
    data = {
        "Name":["luotao","kuroneko"],
        "Age":[18,20]
    }
    df = pd.DataFrame(data)
    print(df)
    # print(df.dtypes)
    # print(df["Name"]) # 单列返回类型<class 'pandas.core.series.Series'>
    # print(df[["Name","Age"]]) # 多列返回类型还是<class 'pandas.core.frame.DataFrame'>
    print(df.loc[0:1]) # 第一行到第二行数据，

def download(content,file_path):
    with open(file_path, "w", encoding='utf-8') as fp:  # 使用'w'模式写入文本数据
        fp.write(content)

if __name__ == "__main__":
    # my_read_csv_file()
    # my_read_csv_custom_file()
    # my_read_sql()
    # my_series()
    # my_dataframe()
    df = my_read_json()
    df.to_excel("./movie_boxofficecn_bs4.xlsx",index=False) # index=False 表示不保存索引
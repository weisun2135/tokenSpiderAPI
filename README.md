# 安装运行
安装 python 3.7
mongodb

1.安装Pipenv  

'''
python install pipenv  
'''

2.clone到本地

3.在当前文件夹下执行 

'''
pipenv install 
'''
会自动下载所需要的包并创建独立的环境


运行  

'''pipenv run main.py'''


# API使用
1.http://127.0.0.1:5000/api/count/  币种数量

2.http://127.0.0.1:5000/api/all/    返回所有币种信息

3.http://127.0.0.1:5000/api/symbol/btc（币种代号 ）

4.http://127.0.0.1:5000/api/name/bitcoin (币种项目全称) 

5.http://127.0.0.1:5000/api/symbol/btc/info 返回一个网址，访问有详细信息，下同

6.http://127.0.0.1:5000/api/name/btc/info

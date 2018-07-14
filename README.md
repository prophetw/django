# 开发环境依赖
python3+
构建一个虚拟环境 不会对本地环境有影响或者依赖
pip3 install virtualenv
virtualenv
virtualenv env
source env/bin/activate

cd mysite
pip3 install requirements.txt  安装项目依赖
or python3 -m pip install requirements.txt


# 本地开发
官方文档
https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial02/
python manage.py runserver 启动本地开发服务


# 指令
编辑 models.py 文件，改变模型。
运行 python manage.py makemigrations 为模型的改变生成迁移文件。
运行 python manage.py migrate 来应用数据库迁移。

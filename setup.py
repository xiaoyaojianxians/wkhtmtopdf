from setuptools import find_packages,setup

setup(
include_package_data=True,
name='wkhtmtopdf',
author='robin',
version='1.0.0',
author_email='xiaoyaojianxians@163.com',
url='https://github.com/xiaoyaojianxians/wkhtmtopdf',
description='这是一款处理将微信推文或者普通网页html转换成pdf的工具',
packages=find_packages(),
data_files=[('Lib/site-packages',['wkhtmltopdf.exe'])],
install_requires=[ 'wechatsogou','Werkzeug==0.11.15','pdfkit'],  # 指定了当前软件包所依赖的其他python类库。这些指定的python类库将会在本package被安装的时候一并被安装
python_requires='>=3'
)
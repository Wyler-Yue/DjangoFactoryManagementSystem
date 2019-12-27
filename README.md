# DjangoFactoryManagementSystem
这是学习制作Django设备管理系统的过程记录，同时学习GitHub的使用

网站已经部署在heroku，可以使用测试账号登录
```bash
user: test0
passwd: test0
```
以下为网站链接：
https://factory-manage-test.herokuapp.com/index

参考教程为刘江的博客教程-实战二：Django2.2之CMDB资产管理系统，以下为教程链接：
http://www.liujiangblog.com/course/django/116

感谢 @liangliangyy 的相关教程文档，以下为GitHub链接：
https://github.com/liangliangyy/DjangoBlog

基于`python3.8`和`Django2.2.8`
![image](https://github.com/Wyler-Yue/image/blob/master/%E7%BD%91%E7%AB%99%E8%AE%BE%E5%A4%87%E6%A6%82%E5%86%B5.png)

## 安装

使用pip安装： `pip install -Ur requirements.txt`

如果你没有pip，使用如下方式安装：
- OS X / Linux 电脑，终端下执行: 

    ```
    curl http://peak.telecommunity.com/dist/ez_setup.py | python
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    ```

- Windows电脑：

    下载 http://peak.telecommunity.com/dist/ez_setup.py 和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py 这两个文件，双击运行。 

### 配置
配置都是在 `setting.py` 中，部分配置迁移到了后台配置中。

## 运行

### 迁移数据库
终端下执行:
```bash
python manage.py migrate
```

### 创建超级用户

 终端下执行:
```bash
python manage.py createsuperuser
```

### 开始运行： 

```bash
python manage.py runserver
```

浏览器打开: http://127.0.0.1:8000/index  就可以看到效果了。
![image](https://github.com/Wyler-Yue/image/blob/master/%E7%BD%91%E7%AB%99%E7%99%BB%E9%99%86%E7%95%8C%E9%9D%A2.png)

### 另附完整Linux部署展示 
```bash
git clone https://github.com/Wyler-Yue/DjangoFactoryManagementSystem.git
cd DjangoFactoryManagementSystem/
mkdir -p env && cd env
virtualenv -p /usr/bin/python3 DFMS
source ~/DjangoFactoryManagementSystem/env/DFMS/bin/activate
cd ..
pip install -Ur requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

具体运行情况如下
![image](https://github.com/Wyler-Yue/image/blob/master/linux%E9%83%A8%E7%BD%B2.png)

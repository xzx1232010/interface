FROM ubuntu:16.04
MAINTAINER xiasan
COPY sources.list /etc/apt/sources.list
#更新源
RUN apt-get update; \
	#安装必要基础软件
	apt install -y vim wget python3 python3-pip language-pack-zh-hans tzdata nginx; \
	#安装python第三方库
	pip3 install pandas==0.22 -i https://mirrors.aliyun.com/pypi/simple/ ; \
	pip3 install django -i https://mirrors.aliyun.com/pypi/simple/ ; \
	pip3 install mongoengine -i https://mirrors.aliyun.com/pypi/simple/ ; \
	pip3 install djangorestframework -i https://mirrors.aliyun.com/pypi/simple/ ; \
	pip3 install uwsgi -i https://mirrors.aliyun.com/pypi/simple ;
#解决docker时间时区问题
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime; \
	dpkg-reconfigure -f noninteractive tzdata;
#添加新用户，防止uwsgi以root用户启动
RUN groupadd -g 1000 xiasan && \
    useradd -r -u 1000 -g xiasan xiasan
#删除nginx默认文件
RUN rm /etc/nginx/sites-enabled/default  
#拷贝文件
RUN mkdir -p /home/reocar/app_action
ADD app_action /home/reocar/app_action
ADD uwsgi.ini /home/reocar
ADD nginx.conf /etc/nginx/nginx.conf
ADD start.sh /home/reocar
#暴露端口
EXPOSE 3000
#添加中文语言包环境变量
ENV LANG zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8
#运行服务
CMD sh /home/reocar/start.sh



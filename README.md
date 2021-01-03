### 1.软件的安装

1. VSCode下载（安装python，chinese，path intellisence，npm，npm intellisence，Vetur，VUE3 Snipper，vscode-icons，live-server）

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX

4. 安装小程序开发项目

### 二.git仓库

1. 安装git
2. 创建远程仓库myBlog
3. 初始化本地仓库,也就是再本地的myBlog文件夹下执行:`git init`,执行后会创建一个.git隐藏文件
4. 远程仓库和本地仓库进行关联:`git remote add origin '你的远程仓库地址'`
5. 如果出现错误,ssh没有创建
6. 先去创建密钥:ssh keygen,一路enter,生成密钥
7. 查看生成的密钥 cat~/.ssh/id_rsa.pub,将生成的密钥写入github上的settings下的SSH and GPG keys下
8. 推送四步骤
   - git status
   - git add .
   - git commit -m '备注'
   - git push -u origin master 首次提交到远程仓库
   - git push  之后的提交

### 三.创建myBlog项目

1. 空文件夹下,执行`django-admin startproject myBlog `
2. 给myBlog创建虚拟环境,使用:`python -m venv env `
3. 进入虚拟环境,windows:`.\\env\\Scripts\\activate`
4. 退出虚拟环境,windows下:`deactivate`
5. 使用VScode打开myBlog,执行:`python manage.py startapp article `

### 四.创建models

1. 创建model
2. 数据库同步
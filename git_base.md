# git基本命令 #
## 设置 Git 参数 ##

- 显示当前的 Git 配置

  `git config --list`

- 设置提交仓库时的用户名信息

  `git config --global user.name "王海云"`

- 设置提交仓库时的邮箱信息

  `git config --global user.email "1563713769@qq.com"`

## 新建代码仓库 #
- 在当前目录新建一个 Git 代码库

  `git init`

- 下载一个项目和它的整个代码历史
```
url 格式: https://github.com/[userName]/reposName
git clone [url]
```
## 添加删除文件
- 添加指定文件到暂存区
  `git add [file1] [file2]`

- 删除工作区文件，并且将这次删除放入暂存区
  `git rm [file1] [file2]`

- 改名文件，并且将这个改名放入暂存区
  `git mv [file-origin] [file-renamed]`

## 代码提交
- 提交暂存区到仓库
  `git commit –m [message]`

- 直接从工作区提交到仓库，前提该文件已经有仓库中的历史版本
  `git commit –a –m [message]  或者 git commit –am [message]`

## 查看信息
- 显示变更信息


```
  git status 或者 git status -sb(只显示两行内容，红色表示在工作区，绿色表示在暂存区)
```

- 显示当前分支的历史版本
```
git log
git log --oneline
```

## 同步远程仓库

- 增加远程仓库，并命名

  ```
  git remote add shortname
  ```


- 将本地的提交推送到远程仓库

  ```
  git push remote
  ```


- 将远程仓库的提交拉下到本地

  ```
  git pull remote
  ```

  # git GUI工具

  ## git GUI

  ## source Tree

  ## Egit

# 




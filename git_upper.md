# git配置

## .gitignore文件说明

- 使用场合

1. 忽略操作系统自动生成的文件，比如：缩略图，等；

2. 忽略编译生成的中间文件、可执行文件等，比如： C 语言编译产生的 .obj 文件和 .exe 文件；

3. 忽略你自己的带有敏感信息的配置文件，比如：存放口令的配置文件；


4. tmp/ 临时目录；


5. /log/ 日志目录；

- 创建.gitignore文件

```
vim .gitignore
```

- 强制添加 .gitignore 忽略的文件

```
git add –f <file name>
```

- 查看 .gitignore 策略生效行号

```
git check-ignore –v <file name>
```



## 换行

-  CR: carriage return 回车，光标到首行， ‘\r’ = return
-  LF: line feed 换行，光标下移一行，’\n’ = newline
-  linux: 换行用 \n表示


- windows: 换行用 \r\n表示


-  MAC OS: 换行用 \r表示


- 提交时转换为LF，检出时转换为CRLF，默认设置不用修改，Git 是 linux 配置

```
git config --global core.autocrlf true
```

- 允许提交包含混合换行符的文件

```
git config --global core.safecrlf false
```

## 别名

- 以图形的方式打印 Git 提交日志

```
git log --pretty=format:'%h %ad | %s%d' --graph --date=short
```

- 设置别名

```
git config --global alias.ci commit
```

## 凭证

- 存储凭证，用于记住密码和用户名


```
git config --global credential.helper wincred
```

# git协议

## 本地协议（不建议使用）

- 克隆本地仓库

```
git clone /c/wd/test.git
```

- 克隆本地仓库，不建议使用 file:// 

```
git clone file:///c/wd/test.git
```

-  添加远程仓库的链接

```
git remote add origin /c/wd/test.git
```

## git协议（也不建议使用）

- 克隆远程仓库

```
git clone git://server_ip/test.git
```

-  添加远程仓库的链接

```
git remote add origin git://server_ip/test.git
```

## http协议

- 克隆远程仓库

```
git clone https://github.com/wangding/test.git 
```

- 添加远程仓库的链接

```
git remote add origin https://github.com/wangding/test.git
```

## ssh协议（重点）

- 克隆远程仓库，一般写成简短的命令

```
git clone ssh://git@github.com/wangding/test.gitgit clone 或者git@github.com:wangding/test.git
```

-  添加远程仓库的链接

```
git remote add origin git@github.com:wangding/test.git
```

- 生成 RSA 密钥对

```
ssh-Keygen -t rsa -C "1563713769@qq.com" 生成的密钥在家目录的.ssh文件夹里面
```

-  在 Github 网站添加公钥


-  使用 SSH 协议，克隆仓库或者添加远程链接

# git基本操作

## git

- git 命令信息

```
git
```

- 查看全部 git 子命令

```
git help -a
```

## git blame

- 逐行查看文件的修改历史

```
git blame <file name>
```

-  从第 100 行开始，到 110 行。逐行查看文件的修改历史

```
git blame –L 100,110 <file name>
```

## git clean

- 列出打算清除的档案

```
git clean -n
```

- 真正的删除

```
git clean –f
```

- 连 .gitignore 中忽略的档案也清除

```
git clean -x
```

## git add

- 添加新文件

```
git add 文件名
```

- 删除文件

```
git rm 文件名
```

- 编辑文件（增加内容、删除内容、修改内容）
- 文件改名

```
git mv 原文件名 新文件名
```

- 文件移动
- 文件夹的操作（添加、删除、改名、移动）

```
git add .
```

- 一个文件多个提交

```
git add –p
```

## git commit

- add & commit mothed 1

```
git add . 
git commit –m "message"
```

- add & commit mothed 2

```
git commit –a –m "message"
```

- add & commit mothed 3

```
git commit –am "message"
```

- 每个提交要保证适当的颗粒度、相关性和独立性。

  - 以一个小功能、小改进或一个 bug fix 为单位 


  - 对应的 unit test 程序在同一个 commit  


  - 无相关的修改不在同一个 commit  


  - 语法错误的半成品程序不能 commit 

- 参考资料

  [点我](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)

## 信息查看

- short and branch

```
git status -sb
```

- 查看某个提交信息

```
git show HEAD
```

- 查看提交历史

```
git log <file name>
git log --grep <msg>
git log -n
```

## git diff

![加载中](/images/1.png 'git diff')

## 回撤操作

![加载中](/images/2.png '回撤')

- 回撤暂存区内容到工作目录

```
git reset HEAD
```

- 回撤提交到暂存区

```
git reset HEAD --soft
```

- 回撤提交，放弃变更

```
git reset HEAD –-hard
```

- 回撤远程仓库，-f  即 --force

```
git push -f
```

## git reset

![加载中](/images/3.png 'git reset')

- 回撤上一次提交

```
git add .

git commit --amend –m “message”
```

- 变基操作，改写历史提交

```
git rebase –i HEAD~3
```

# 标签操作

## git tag

- 在当前提交上，打标签 

```
foogit tag foo
```

- 在当前提交上，打标签 foo，并给 message 信息注释

```
git tag foo –m "message"
```

- 在当前提交之前的第 4 个版本上，打标签

```
 foogit tag foo HEAD~4
```

- 列出所有标签

```
git tag
```

- 删除标签

```
git tag –d foo
```

- 把标签推送到远程仓库

```
git push origin --tags
```

- 把标签推送到远程仓库

```
git push origin v0.1
```

# git 分支（并行开发）

## 冲突解决

要点：

1. 在不同分支上，修改同一个文件；
2. 不同的人，修改了同一个文件；
3. 不同的仓库，修改了同一个文件；
4. 冲突只在合并分支的时候才会发生；
5. 发生冲突并不可怕，冲突的代码不会丢失；
6. 解决冲突，重新提交，commit 时不要给 message；
7. 冲突信息的格式；

## git branch

- 创建分支foo

```
git branch foo
```

- 切换到分支 foo

```
git checkout foo
```

- 创建分支并同时切换到 foo，一步做到

```
git checkout -b foo
```

- 修改分支名字

```
git branch –m old_name new_name
git branch –M old_name new_name      
```

- 删除分支 foo

```
git branch -d foo
Git branch –D foo
```

- 列出远程分支

```
git branch -r
```

- 查看已合并的分支

```
git branch --mergedgit branch --no-merged   
```

- 列出远程合并的分支

```
git branch -r --merged
```

- 取出远程 foo 分支

```
git checkout –t origin/foo
```

- 删除远程分支

```
git push origin <space>:<remote branch>
git fetch -p    
```

- 合并分支

```
git merge <branch name>
```

- 合并分支，拒绝 fast forward，产生合并 commit

```
git merge –-no-ff
```

## git stash

- 保存进度

```
git stash   
```

- 弹出进度

```
git stash pop
```

- 查看 stash 列表

```
git stash list
```

- 删除 stash 列表

```
git stash clear
```


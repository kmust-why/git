# git
用于记录有关git的知识
- [git基本命令](git_base.md)
- [git进阶命令](git_upper.md)

# 什么是git

git是一款开源免费的分布式的代码管理软件，这是对git最简明扼要的解释了，那么什么是分布式，什么是代码管理软件，这些在接下来都会一一解释，首先介绍一下git的历史：

1. git于2005年发布第一个版本。
2. git的作者同时也是linux的作者—— Linus Torvalds。
3. git的出生得益于当时的一款商业代码管理软件`BitKeeper`。当时Linus和全球开发者一起开发`linux`，都是通过`BitKeeper`这个软件进行代码管理的，并且`BitKeeper`是免费给这些开发者用的，后来因为某些开发者违规破解了该软件，被`BitKeeper`开发商发现后愤怒的收回了该软件的免费使用权。Linus没办法只得自己开发一个代码管理软件来应对全球各地开发者提交的代码，git因此应运而生。

#### 什么是集中式和分布式？

1. 集中式：**代码仓库**只在中央服务器上，所有人提交代码都是提交到中央服务器上，如果一旦断网，便不可进行代码的提交。
2. 分布式：分布式是在每个人的电脑中都有一个**代码仓库**，在代码提交的时候，先提交到本地，然后再推送到远程的服务器的代码仓库中。这种策略的好处是，即使开发人员处于断网，还是能不断的提交代码，能进行git操作。只要等到有网的时候，再推送到服务器的代码仓库。

![img](images/集中式.jpg)

#### git是怎样进行代码管理的？

1. 多人开发的时候，代码合并不可能每次都通过人力手工合并，因此git是专门做这个事情的。
2. git会将所有文件做个文件快照，等你下次提交代码到仓库中的时候，git会去检查哪些文件进行了改变，并将改变了的文件重新做快照。这样，他就能知道你这次提交的代码和之前的代码有哪些地方不同。
3. 如果多个人修改了同一份源代码文件，这时候到底该使用谁的代码就是个问题了，git此时就会出现一个冲突，指出哪些地方你们共同修改了，然后开发人员阅读源代码后决定最终要提交的代码（有可能是多人的代码的合并），然后重复第二点。
4. 远程仓库是在服务器上，本地仓库是在自己的电脑里。如果要让别人的电脑能知道你修改了哪些代码，你应该把本地仓库的代码提交到服务器上才行。

### git工作区、暂存区、仓库：

- 工作区：就是你代码编辑器中的代码。
- 暂存区：记录文件快照，以及文件信息等。
- 仓库：真正保存修改后的代码的地方。
- 在写完代码后，先使用`git add .`来将代码添加到缓存区。
- 用`git status`确认没有问题后，再用`git commit -m 'commit message'`将代码提交到仓库中。

### git关联本地仓库和远程仓库：

1. 在服务器创建一个远程仓库，这里以github为例。

2. 在本地项目中通过命令`git init`初始化本地仓库，这样本地的代码就有一个本地仓库了。

3. 通过以下命令将代码提交到本地仓库：

   ```
   git add .
   git commit -m 'commit message'

   ```

4. 关联本地仓库和远程仓库：

   ```
   git remote add origin 远程仓库地址

   ```

5. 添加ssk：

   ```
   ssh-keygen -t rsa -C "youremail@example.com"

   ```

   然后在`C:\Users\Administrator\.ssh`中找到`id_rsa.pub`，将里面的内容添加到github帐号上面。

6. 从服务器拉代码下来：

   ```
   git pull origin master

   ```

7. 提交本地代码到远程仓库：

   ```
   git push origin master

   ```

### git操作流程以及命令解释：

1. 写完代码以后，应该先提交到本地仓库。提交到本地仓库应该分为两步，第一步，把代码提交到暂缓区：

   ```
   git add .

   ```

   > 暂缓区是用来记录文件快照和一些文件信息（比如时间戳、长度等）。

   第二步，将代码提交到本地仓库：

   ```
   git commit -m "commit message"

   ```

2. 再从服务器上拉代码下来：

   ```
   git pull origin master

   ```

   > 在提交代码之前，一定要记得先从服务器上拉代码下来，因为有可能别人已经提交过代码到服务器上，如果你不拉代码，git是拒绝直接推送代码到服务器上的。另外master代表的是分支的名字。

3. 推送代码到远程仓库：

   ```
   git push origin master

   ```

### 分支：

分支的作用是，如果你的项目要开发一个新的功能，但要确保之前版本能够正常运行，此时你该怎么做呢？如果按照普通的想法，你肯定是想，既然要不影响原来代码执行，所以不能修改之前的代码，那就再拷贝一份代码，在拷贝后的代码中添加新功能。当然这是一种实现的方式，但是`git`作为一个自动化管理工具，肯定是不会让你做这种傻事了。而**分支**就是用来解决这个问题的。那怎么使用分支，以及使用分支又有哪些注意事项呢，接下来进行解释：

- `git checkout -b 分支名称`：从当前分支创建另外一个分支，比如要在当前版本的代码上新增一个功能，使用以上命令，将创建一个新的分支，新的分支会有原来分支的所有功能，并且在新的分支上做的任何更改不会影响原来的分支。
- `git merge 分支名称`：将指定的分支合并到当前分支上。比如我已经将一个新功能做完了，要合并到当前分支上，此时就使用这个命令。
- `git branch`：查看本地所有的分支以及当前处于哪个分支。
- `git branch 分支名称`：创建分支。
- `git branch -d 分支名称`：删除分支。

分支在本地玩是还不够的，还要将分支和远程的分支进行关联。

- `git push origin 分支名称`：将本地分支推送到远程分支，如果远程仓库没有这个分支，则会自动创建一个。
- `git checkout -b dev origin/dev`：根据远程的`dev`分支，创建一个本地的`dev`分支。
- `git branch --set-upstream dev origin/dev`：将远程的`dev`分支和本地的`dev`分支关联起来，以后使用`git pull origin dev`和`git push origin dev`的时候就可以简写成`git pull`和`git push`了。

### 分支冲突：

在多人开发中，经常多个人修改同一个文件，此时，在合并代码的时候，git就不不知道该怎么弄了，此时只能通过手动的修改代码，解决完冲突，然后再提交。 产生冲突后，一般会出现

```
<<<<<<<<<<<<HEAD
当前分支的代码
============分支名称
合并的分支的代码

```

此时你就要看，到底是要用当前分支的代码还是要用合并的分支的代码还是要兼容两者，修改完了后把`<<<`和`===`删掉，git就视为已经解决了冲突。
> 以上内容整理自黄勇




#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: ${NAME}.py
#time: ${DATE} ${TIME}



raise errorclass, errorvalue
sqlalchemy.exc.IntegrityError: (_mysql_exceptions.IntegrityError) (1215, 'Cannot add foreign key constraint') [SQL: u'\nCREATE TABLE questions (\n\tid INTEGER NOT NULL AUTO_INCREMENT, \n\ttitle VARCHAR(100) NOT NULL, \n\tcontent TEXT NOT NULL, \n\tcreate_time DATETIME, \n\tauthor_id VARCHAR(100), \n\tPRIMARY KEY (id), \n\tFOREIGN KEY(author_id) REFERENCES users (id)\n)\n\n']













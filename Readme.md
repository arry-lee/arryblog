## arryblog博客系统模块设计
基于系统功能结构图可以看出系统分为六大模块：文章模块，相册模块，笔记模块，用户模块，题库模块，源码模块。
简单介绍一下六大模块以及各大模块实现的具体功能。
### 用户模块
该模块提供给用户的功能有登录、注册
### 文章模块
文章模块分为三个小模块：文章操作、文章分组、标签管理
文章操作模块提供给用户的功能：新建文章，修改文章，删除文章；
标签管理模块提供给用户的功能：文章增加标签的功能，一个标签可以用于多个文章，一个文章可以对应多个标签。
文章分组模块提供给用户的功能：新建和删除文章分组
### 相册模块
该模块提供给用户的功能有：相册管理，照片管理
相册管理模块提供给用户的功能有：新建和删除相册
照片管理模块提供给用户的功能有：添加和删除照片、修改照片描述
### 笔记模块
笔记模块提供给用户的功能：新建笔记，修改笔记，删除笔记，汇总笔记；
### 题库模块
题库模块提供给用户的功能：编程题的增删改查；题目的浏览和测验
### 源码模块
源码模块提供给用户的功能：阅读 python 内置库的源码和文档，建立内置函数索引。
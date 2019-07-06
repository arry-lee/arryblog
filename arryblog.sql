-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: arryblog
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_49ada5569e485b49_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_49ada5569e485b49_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_2a1ff834894dacc5_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_6ef8780dfbd89563_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 用户',6,'add_user'),(17,'Can change 用户',6,'change_user'),(18,'Can delete 用户',6,'delete_user'),(19,'Can add 地址',7,'add_address'),(20,'Can change 地址',7,'change_address'),(21,'Can delete 地址',7,'delete_address'),(22,'Can add 文章类型',8,'add_articletype'),(23,'Can change 文章类型',8,'change_articletype'),(24,'Can delete 文章类型',8,'delete_articletype'),(25,'Can add 标签类型',9,'add_tag'),(26,'Can change 标签类型',9,'change_tag'),(27,'Can delete 标签类型',9,'delete_tag'),(28,'Can add 文章',10,'add_article'),(29,'Can change 文章',10,'change_article'),(30,'Can delete 文章',10,'delete_article'),(31,'Can add 文章图片',11,'add_articleimage'),(32,'Can change 文章图片',11,'change_articleimage'),(33,'Can delete 文章图片',11,'delete_articleimage'),(34,'Can add 评论',12,'add_comment'),(35,'Can change 评论',12,'change_comment'),(36,'Can delete 评论',12,'delete_comment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_address`
--

DROP TABLE IF EXISTS `df_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `receiver` varchar(20) NOT NULL,
  `addr` varchar(256) NOT NULL,
  `zip_code` varchar(6) DEFAULT NULL,
  `phone` varchar(11) NOT NULL,
  `is_defalut` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_address_user_id_29a784b183da5527_fk_df_user_id` (`user_id`),
  CONSTRAINT `df_address_user_id_29a784b183da5527_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_address`
--

LOCK TABLES `df_address` WRITE;
/*!40000 ALTER TABLE `df_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `df_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_article`
--

DROP TABLE IF EXISTS `df_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `type_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  `title` varchar(40) NOT NULL,
  `content` longtext NOT NULL,
  `view` int(11) NOT NULL,
  `like` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_article_type_id_627977d73a5ff9e8_fk_df_article_type_id` (`type_id`),
  KEY `df_article_user_id_3e3bf02e1545b84c_fk_df_user_id` (`user_id`),
  KEY `df_article_tag_id_56859a1830ef0365_fk_df_tag_id` (`tag_id`),
  CONSTRAINT `df_article_tag_id_56859a1830ef0365_fk_df_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `df_tag` (`id`),
  CONSTRAINT `df_article_type_id_627977d73a5ff9e8_fk_df_article_type_id` FOREIGN KEY (`type_id`) REFERENCES `df_article_type` (`id`),
  CONSTRAINT `df_article_user_id_3e3bf02e1545b84c_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_article`
--

LOCK TABLES `df_article` WRITE;
/*!40000 ALTER TABLE `df_article` DISABLE KEYS */;
INSERT INTO `df_article` VALUES (1,'2019-03-21 18:45:49.346791','2019-03-21 18:45:49.346832',0,1,1,3,'Hello World','<p>Hello World</p>\r\n<p>This is My First Blog!</p>\r\n<p>Welcome to My World!</p>',1,1),(2,'2019-03-21 19:40:36.812523','2019-03-21 19:40:36.812624',0,2,1,1,'你好 世界','<p>你好 世界</p>\r\n<p>欢迎来到arry的博客</p>\r\n<p>博客诞生于 2019 年 3月 21日</p>\r\n<p>&nbsp;</p>',1,1),(6,'2019-03-21 19:44:37.479792','2019-03-21 19:44:37.479903',0,1,1,4,'关于前端开发','<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>\r\n<p>关于前端开发</p>',1,1),(7,'2019-03-22 14:55:24.114251','2019-03-22 14:55:24.114290',0,6,1,1,'sublime 常用操作集','# sublime 常用操作集\r\n\r\n- Ctrl = C; Alt = A; Shift = S; Enter = E;\r\n## 多行操作\r\n- CAd 选多行\r\n- S右键 选多行\r\n- CAp 命令面板\r\n- Cp 搜项目文件\r\n- Cg 定位行号\r\n- Cw 关闭当前文件\r\n- CSw 关闭所有文件\r\n- CSv 格式化粘贴\r\n- Cd 选词 ++\r\n- Cl 选行 ++\r\n- CSl 选多行\r\n- CSE 插入行 ++\r\n- Cx 删当前行\r\n- Cm 定括号\r\n- Csm 选括号内容\r\n- Cj 选择标签内容\r\n- Cf 查找\r\n- Ch 替换\r\n- Cr 前往 method\r\n- Ckb 开关侧边栏\r\n- CF2 设置/删除标记\r\n- C/ 注释行\r\n- CS/ 当前位置插入注释\r\n- CA/ 块注释\r\n- SF11 全屏免打扰\r\n- AF3 选择所有相同的词\r\n- AS 2 分屏显示\r\n- A2 切换文件\r\n- 鼠标的前进后退键可切换Tab文件\r\n- 按Ctrl，依次点击或选取，可需要编辑的多个位置 \r\n- 按Ctrl+Shift+上下键，可替换行\r\n## 选择类\r\n- Ctrl+D 选中光标所占的文本，继续操作则会选中下一个相同的文本。\r\n- Alt+F3 选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑。举个栗子：快速选中并更改所有相同的变量名、函数名等。\r\n- Ctrl+L 选中整行，继续操作则继续选择下一行，效果和 Shift+↓ 效果一样。\r\n- Ctrl+Shift+L 先选中多行，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行。\r\n- Ctrl+Shift+M 选择括号内的内容（继续选择父括号）。举个栗子：快速选中删除函数中的代码，重写函数体代码或重写括号内里的内容。\r\n- Ctrl+M 光标移动至括号内结束或开始的位置。\r\n- Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。\r\n- Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。\r\n- Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。\r\n- Ctrl+Shift+] 选中代码，按下快捷键，展开代码。\r\n- Ctrl+K+0 展开所有折叠代码。\r\n- Ctrl+← 向左单位性地移动光标，快速移动光标。\r\n- Ctrl+→ 向右单位性地移动光标，快速移动光标。\r\n- shift+↑ 向上选中多行。\r\n- shift+↓ 向下选中多行。\r\n- Shift+← 向左选中文本。\r\n- Shift+→ 向右选中文本。\r\n- Ctrl+Shift+← 向左单位性地选中文本。\r\n- Ctrl+Shift+→ 向右单位性地选中文本。\r\n- Ctrl+Shift+↑ 将光标所在行和上一行代码互换（将光标所在行插入到上一行之前）。\r\n- Ctrl+Shift+↓ 将光标所在行和下一行代码互换（将光标所在行插入到下一行之后）。\r\n- Ctrl+Alt+↑ 向上添加多行光标，可同时编辑多行。\r\n- Ctrl+Alt+↓ 向下添加多行光标，可同时编辑多行。\r\n## 编辑类\r\n- Ctrl+J 合并选中的多行代码为一行。举个栗子：将多行格式的CSS属性合并为一行。\r\n- Ctrl+Shift+D 复制光标所在整行，插入到下一行。\r\n- Tab 向右缩进。\r\n- Shift+Tab 向左缩进。\r\n- Ctrl+K+K 从光标处开始删除代码至行尾。\r\n- Ctrl+Shift+K 删除整行。\r\n- Ctrl+/ 注释单行。\r\n- Ctrl+Shift+/ 注释多行。\r\n- Ctrl+K+U 转换大写。\r\n- Ctrl+K+L 转换小写。\r\n- Ctrl+Z 撤销。\r\n- Ctrl+Y 恢复撤销。\r\n- Ctrl+U 软撤销，感觉和 Gtrl+Z 一样。\r\n- Ctrl+F2 设置书签\r\n- Ctrl+T 左右字母互换。\r\n- F6 单词检测拼写\r\n## 显示类\r\n- Ctrl+Tab 按文件浏览过的顺序，切换当前窗口的标签页。\r\n- Ctrl+PageDown 向左切换当前窗口的标签页。\r\n- Ctrl+PageUp 向右切换当前窗口的标签页。\r\n- Alt+Shift+1 窗口分屏，恢复默认1屏（非小键盘的数字）\r\n- Alt+Shift+2 左右分屏-2列\r\n- Alt+Shift+3 左右分屏-3列\r\n- Alt+Shift+4 左右分屏-4列\r\n- Alt+Shift+5 等分4屏\r\n- Alt+Shift+8 垂直分屏-2屏\r\n- Alt+Shift+9 垂直分屏-3屏\r\n- Ctrl+K+B 开启/关闭侧边栏。\r\n- F11 全屏模式\r\n## 搜索类\r\n- Ctrl+F 打开底部搜索框，查找关键字。\r\n- Ctrl+shift+F 在文件夹内查找，与普通编辑器不同的地方是sublime允许添加多个文件夹进行查找，略高端，未研究。\r\n- Ctrl+P 打开搜索框。举个栗子：1、输入当前项目中的文件名，快速搜索文件，2、输入@和关键字，查找文件中函数名，3、输入：和数字，跳转到文件中 该行代码，4、输入#和关键字，查找变量名。\r\n- Ctrl+G 打开搜索框，自动带：，输入数字跳转到该行代码。举个栗子：在页面代码比较长的文件中快速定位。\r\n- Ctrl+R 打开搜索框，自动带@，输入关键字，查找文件中的函数名。举个栗子：在函数较多的页面快速查找某个函数。\r\n- Ctrl+： 打开搜索框，自动带#，输入关键字，查找文件中的变量名、属性名等。\r\n- Ctrl+Shift+P 打开命令框。场景栗子：打开命名框，输入关键字，调用sublime \r\n- text或插件的功能，例如使用package安装插件。\r\n- Esc 退出光标多行选择，退出搜索框，命令框等。',1,1);
/*!40000 ALTER TABLE `df_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_article_image`
--

DROP TABLE IF EXISTS `df_article_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_article_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `article_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_article_image_article_id_7e2c1f865e91f628_fk_df_article_id` (`article_id`),
  CONSTRAINT `df_article_image_article_id_7e2c1f865e91f628_fk_df_article_id` FOREIGN KEY (`article_id`) REFERENCES `df_article` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_article_image`
--

LOCK TABLES `df_article_image` WRITE;
/*!40000 ALTER TABLE `df_article_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `df_article_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_article_type`
--

DROP TABLE IF EXISTS `df_article_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_article_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `logo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_article_type`
--

LOCK TABLES `df_article_type` WRITE;
/*!40000 ALTER TABLE `df_article_type` DISABLE KEYS */;
INSERT INTO `df_article_type` VALUES (1,'2019-03-21 18:38:26.840622','2019-03-21 18:38:26.840898',0,'前端开发','frontend'),(2,'2019-03-21 18:38:56.429960','2019-03-21 18:38:56.429998',0,'后端开发','backend'),(3,'2019-03-21 18:39:23.931949','2019-03-21 18:39:23.931988',0,'机器学习','ml'),(4,'2019-03-21 18:40:07.068801','2019-03-21 18:40:07.068862',0,'深度学习','deeplearning'),(5,'2019-03-21 18:41:43.248317','2019-03-21 18:41:43.248355',0,'算法和数据结构','algorithm'),(6,'2019-03-22 14:52:14.649433','2019-03-22 14:52:14.649973',0,'工具说明','none');
/*!40000 ALTER TABLE `df_article_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_comment`
--

DROP TABLE IF EXISTS `df_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `article_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_comment_article_id_5fc764f39082ff5b_fk_df_article_id` (`article_id`),
  KEY `df_comment_user_id_64effc228b43eb39_fk_df_user_id` (`user_id`),
  CONSTRAINT `df_comment_article_id_5fc764f39082ff5b_fk_df_article_id` FOREIGN KEY (`article_id`) REFERENCES `df_article` (`id`),
  CONSTRAINT `df_comment_user_id_64effc228b43eb39_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_comment`
--

LOCK TABLES `df_comment` WRITE;
/*!40000 ALTER TABLE `df_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `df_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_tag`
--

DROP TABLE IF EXISTS `df_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `color` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_tag`
--

LOCK TABLES `df_tag` WRITE;
/*!40000 ALTER TABLE `df_tag` DISABLE KEYS */;
INSERT INTO `df_tag` VALUES (1,'2019-03-21 18:42:23.060409','2019-03-22 01:57:23.358870',0,'python','#3572a5'),(2,'2019-03-21 18:42:34.434659','2019-03-22 01:57:40.372484',0,'c++','#f34b7d'),(3,'2019-03-21 18:42:47.473777','2019-03-21 18:42:47.473835',0,'html','yellow'),(4,'2019-03-21 18:43:02.137926','2019-03-21 18:43:12.523380',0,'css','yellow'),(5,'2019-03-21 18:43:32.023405','2019-03-21 18:43:32.023657',0,'js','yellow'),(6,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061666',0,'leetcode','gold'),(7,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'动态规划','pink'),(8,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'树','pink'),(9,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'栈','pink'),(10,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'链表','pink'),(11,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'堆','pink'),(12,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'图','pink'),(13,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'并查集','pink'),(14,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'哈希表','pink'),(15,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'深度优先搜索','pink'),(16,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'广度优先搜索','pink'),(17,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'二分查找','pink'),(18,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'双指针','pink'),(19,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'回溯算法','pink'),(20,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'贪心算法','pink'),(21,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'分治算法','pink'),(22,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'二叉搜索树','pink'),(23,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'字典树','pink'),(24,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'递归','pink'),(25,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'队列','pink'),(26,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'线段树','pink'),(27,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'极小化极大','pink'),(28,'2019-03-21 18:44:05.061630','2019-03-21 18:44:05.061630',0,'拓扑排序','pink');
/*!40000 ALTER TABLE `df_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_user`
--

DROP TABLE IF EXISTS `df_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_user`
--

LOCK TABLES `df_user` WRITE;
/*!40000 ALTER TABLE `df_user` DISABLE KEYS */;
INSERT INTO `df_user` VALUES (1,'pbkdf2_sha256$20000$8uA8LC14NYAU$HVcfxmMko+yesbU+L9KKPYdHMNh5z3nlzMDNclrTff8=','2019-03-22 01:49:08.973204',1,'admin','','','arry_lee@qq.com',1,1,'2019-03-21 18:27:47.890261','2019-03-21 18:27:47.933327','2019-03-21 18:27:47.933344',0);
/*!40000 ALTER TABLE `df_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_user_groups`
--

DROP TABLE IF EXISTS `df_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `df_user_groups_group_id_53cae7a49e106c43_fk_auth_group_id` (`group_id`),
  CONSTRAINT `df_user_groups_group_id_53cae7a49e106c43_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `df_user_groups_user_id_349778591e83d933_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_user_groups`
--

LOCK TABLES `df_user_groups` WRITE;
/*!40000 ALTER TABLE `df_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `df_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `df_user_user_permissions`
--

DROP TABLE IF EXISTS `df_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `df_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `df_user_use_permission_id_2c1ead2528dba3e3_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `df_user_use_permission_id_2c1ead2528dba3e3_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `df_user_user_permissions_user_id_33fe5745c7a263e9_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `df_user_user_permissions`
--

LOCK TABLES `df_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `df_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `df_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_3fa3f88e99ae2647_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_4ad4d0f1d4620e7b_fk_df_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_3fa3f88e99ae2647_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_4ad4d0f1d4620e7b_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-03-21 18:38:26.851007','1','前端开发',1,'',8,1),(2,'2019-03-21 18:38:56.441361','2','后端开发',1,'',8,1),(3,'2019-03-21 18:39:23.935323','3','机器学习',1,'',8,1),(4,'2019-03-21 18:40:07.076124','4','深度学习',1,'',8,1),(5,'2019-03-21 18:41:43.249716','5','算法和数据结构',1,'',8,1),(6,'2019-03-21 18:42:23.065468','1','python',1,'',9,1),(7,'2019-03-21 18:42:34.448863','2','c++',1,'',9,1),(8,'2019-03-21 18:42:47.478823','3','html',1,'',9,1),(9,'2019-03-21 18:43:02.147834','4','css',1,'',9,1),(10,'2019-03-21 18:43:12.527663','4','css',2,'已修改 color 。',9,1),(11,'2019-03-21 18:43:32.027459','5','js',1,'',9,1),(12,'2019-03-21 18:44:05.068765','6','leetcode',1,'',9,1),(13,'2019-03-21 18:45:49.349263','1','Article object',1,'',10,1),(14,'2019-03-21 19:40:36.818292','2','你好 世界',1,'',10,1),(15,'2019-03-21 19:42:13.071732','3','Test',1,'',10,1),(16,'2019-03-21 19:43:01.427406','4','关于深度学习',1,'',10,1),(17,'2019-03-21 19:43:31.304686','5','关于机器学习',1,'',10,1),(18,'2019-03-21 19:44:37.499231','6','关于前端开发',1,'',10,1),(19,'2019-03-22 01:57:23.364244','1','python',2,'已修改 color 。',9,1),(20,'2019-03-22 01:57:40.376684','2','c++',2,'已修改 color 。',9,1),(21,'2019-03-22 14:52:14.659502','6','工具说明',1,'',8,1),(22,'2019-03-22 14:55:24.120236','7','sublime 常用操作集',1,'',10,1),(23,'2019-03-23 09:03:16.171281','4','关于深度学习',3,'',10,1),(24,'2019-03-23 09:03:16.201130','3','Test',3,'',10,1),(25,'2019-03-24 01:21:23.008337','5','关于机器学习',3,'',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_1cc8d60c16cea77d_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(10,'article','article'),(11,'article','articleimage'),(8,'article','articletype'),(12,'article','comment'),(9,'article','tag'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(7,'user','address'),(6,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-21 18:05:44.692822'),(2,'contenttypes','0002_remove_content_type_name','2019-03-21 18:06:19.978743'),(3,'auth','0001_initial','2019-03-21 18:06:20.445039'),(4,'auth','0002_alter_permission_name_max_length','2019-03-21 18:06:20.575423'),(5,'auth','0003_alter_user_email_max_length','2019-03-21 18:06:20.601062'),(6,'auth','0004_alter_user_username_opts','2019-03-21 18:06:20.643111'),(7,'auth','0005_alter_user_last_login_null','2019-03-21 18:06:20.668295'),(8,'auth','0006_require_contenttypes_0002','2019-03-21 18:06:20.680874'),(9,'user','0001_initial','2019-03-21 18:06:21.118208'),(10,'admin','0001_initial','2019-03-21 18:06:21.314956'),(11,'sessions','0001_initial','2019-03-21 18:06:21.368741');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-23 20:32:07

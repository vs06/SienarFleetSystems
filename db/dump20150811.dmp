CREATE DATABASE  IF NOT EXISTS `swxwcompare` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `swxwcompare`;
-- MySQL dump 10.13  Distrib 5.6.23, for Win32 (x86)
--
-- Host: localhost    Database: swxwcompare
-- ------------------------------------------------------
-- Server version	5.6.24-log

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
  KEY `auth_group__permission_id_6ffdd847bc3c0ee9_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_6ffdd847bc3c0ee9_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_2678c7f5684c5cb6_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
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
  CONSTRAINT `auth__content_type_id_2b4fb4b618d17676_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$N6Yy52ZLawOJ$65w10j70ZrEHrTeKx3GKsA1suqeQz5B8BBd9DwSxJOs=','2015-08-11 12:44:09.432370',1,'root','','','victorsousa88@yahoo.com.br',1,1,'2015-07-01 18:57:40.874876');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_7e966a4a9a47fdda_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_7e966a4a9a47fdda_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_2b7625bd939d49e8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_us_permission_id_6b6cc4d3058389e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_us_permission_id_6b6cc4d3058389e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_5da7b13adc06caf1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  KEY `djang_content_type_id_5410b218d5cf55b2_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_4ba1c628937e192a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_5410b218d5cf55b2_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_4ba1c628937e192a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-07-01 19:02:35.612876','1','Ship object',1,'',7,1),(2,'2015-07-01 19:08:53.116876','2','Ship object',1,'',7,1),(3,'2015-07-01 19:23:12.308876','2','Ship object',2,'No fields changed.',7,1),(4,'2015-08-11 13:26:13.740808','6','Ship object',2,'Changed armaprimaria, agilidade, casco, escudo, customin, customax, armasecundaria and manobrabilidade.',7,1),(5,'2015-08-11 13:27:31.262560','5','Ship object',2,'Changed armaprimaria, agilidade, casco, escudo, customin, customax, armasecundaria and manobrabilidade.',7,1);
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
  UNIQUE KEY `django_content_type_app_label_75e5e54024f125fb_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'sienarfleetsys','ship');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-07-01 18:57:21.048876'),(2,'auth','0001_initial','2015-07-01 18:57:22.714876'),(3,'admin','0001_initial','2015-07-01 18:57:23.036876'),(4,'contenttypes','0002_remove_content_type_name','2015-07-01 18:57:23.317876'),(5,'auth','0002_alter_permission_name_max_length','2015-07-01 18:57:23.484876'),(6,'auth','0003_alter_user_email_max_length','2015-07-01 18:57:23.607876'),(7,'auth','0004_alter_user_username_opts','2015-07-01 18:57:23.636876'),(8,'auth','0005_alter_user_last_login_null','2015-07-01 18:57:23.816876'),(9,'auth','0006_require_contenttypes_0002','2015-07-01 18:57:23.832876'),(10,'sessions','0001_initial','2015-07-01 18:57:23.933876');
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
INSERT INTO `django_session` VALUES ('59cs6qgpehzeu7eubypiezzgw3gz7lal','ODc2NTAxNzA0MDBiZDE4N2EzN2U0YTFhMDg0OWQ0MTM1MGQxOTg3ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1NGU5YjkxNGU5NjM0N2ZiYTY4OTZhYTcxNDRmNDcyN2QyMDZmOWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-08-24 17:51:47.108788'),('6r32d0beql9tzg5f6gyoe05lwbqx5ser','ODc2NTAxNzA0MDBiZDE4N2EzN2U0YTFhMDg0OWQ0MTM1MGQxOTg3ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1NGU5YjkxNGU5NjM0N2ZiYTY4OTZhYTcxNDRmNDcyN2QyMDZmOWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-08-25 12:44:09.435370'),('9ibhhrvozolt3zrmpd83h6bu4dfq1r6z','ODc2NTAxNzA0MDBiZDE4N2EzN2U0YTFhMDg0OWQ0MTM1MGQxOTg3ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1NGU5YjkxNGU5NjM0N2ZiYTY4OTZhYTcxNDRmNDcyN2QyMDZmOWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-07-15 19:23:03.804876'),('br0r6x4gmvzqwg2gplgtvig3oy9m6cc2','ZDNiY2VhNmFhNDFhMmM4YjIzOTRjOTc2NWMyNDAyMjc3YjM4MWRjNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI2NTRlOWI5MTRlOTYzNDdmYmE2ODk2YWE3MTQ0ZjQ3MjdkMjA2ZjljIn0=','2015-08-18 12:38:05.732551'),('kac5vlsurkap8abra8fssom2i2dcsxag','ZDA5ODFhMzc3MjdkNjAyNjU2NmZiMmEyMmI3YjAwZGIwNzJkNWVjMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1NGU5YjkxNGU5NjM0N2ZiYTY4OTZhYTcxNDRmNDcyN2QyMDZmOWMiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-24 13:21:20.626843'),('s6racahy0530hs8eh5mjg3ynwgaehgzb','MzljZTMyODJhNzcxOWVlNmU2MjkxNzMwYzYwNDQ4NzcxMzU3OWVhOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjU0ZTliOTE0ZTk2MzQ3ZmJhNjg5NmFhNzE0NGY0NzI3ZDIwNmY5YyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-24 18:32:16.121612'),('xda8a11cfygq1qblatfslfn14uta718m','ODc2NTAxNzA0MDBiZDE4N2EzN2U0YTFhMDg0OWQ0MTM1MGQxOTg3ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1NGU5YjkxNGU5NjM0N2ZiYTY4OTZhYTcxNDRmNDcyN2QyMDZmOWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-07-15 19:01:03.798876');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ship`
--

DROP TABLE IF EXISTS `ship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ship` (
  `idship` int(11) NOT NULL,
  `armaprimaria` int(11) DEFAULT NULL,
  `agilidade` int(11) DEFAULT NULL,
  `casco` int(11) DEFAULT NULL,
  `escudo` int(11) DEFAULT NULL,
  `customin` int(11) DEFAULT NULL,
  `customax` int(11) DEFAULT NULL,
  `armasecundaria` int(11) DEFAULT NULL,
  `manobrabilidade` int(11) DEFAULT NULL,
  `nome` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idship`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ship`
--

LOCK TABLES `ship` WRITE;
/*!40000 ALTER TABLE `ship` DISABLE KEYS */;
INSERT INTO `ship` VALUES (1,3,2,3,2,21,29,1,3,'X-Wing'),(2,2,3,3,0,12,19,0,2,'TIE Fighter'),(3,2,1,5,3,18,25,3,-2,'Y-Wing'),(4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TIE Advanced'),(5,3,1,8,5,42,46,1,2,'YT-1300 (Millenium Falcon)'),(6,3,2,6,4,33,39,3,2,'Firespray-31 (Slave I)'),(7,3,2,2,2,17,26,1,6,'A-Wing'),(8,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TIE Interceptor'),(9,1,2,4,1,19,25,1,1,'HWK-290'),(10,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Lambda Shuttle'),(11,3,1,3,5,12,22,3,-2,'B-Wing'),(12,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TIE Bomber'),(13,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Z-95 Headhunter'),(14,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TIE Defender'),(15,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'E-Wing'),(16,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TIE Phantom'),(17,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'YT-2400'),(18,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'VT-49 Decimator'),(19,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'M3-A Scyk Interceptor'),(20,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'StarViper'),(21,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'IG-2000 Aggressor'),(22,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'YV-666 Hound\'s Tooth'),(23,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Kihraxz Fighter'),(24,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'K-Wing'),(25,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TIE Punisher'),(26,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'GR-75 (Rebel Transport)'),(27,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'CR90 Corvette (Tantive IV)'),(28,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Imperial Raider'),(29,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Gozanti-Class Cruiser (Imperial Assault)');
/*!40000 ALTER TABLE `ship` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-11 14:47:07

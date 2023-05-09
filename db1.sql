/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.25 : Database - resort
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`resort` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `resort`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add booking',7,'add_booking'),
(26,'Can change booking',7,'change_booking'),
(27,'Can delete booking',7,'delete_booking'),
(28,'Can view booking',7,'view_booking'),
(29,'Can add cottage',8,'add_cottage'),
(30,'Can change cottage',8,'change_cottage'),
(31,'Can delete cottage',8,'delete_cottage'),
(32,'Can view cottage',8,'view_cottage'),
(33,'Can add employee',9,'add_employee'),
(34,'Can change employee',9,'change_employee'),
(35,'Can delete employee',9,'delete_employee'),
(36,'Can view employee',9,'view_employee'),
(37,'Can add events',10,'add_events'),
(38,'Can change events',10,'change_events'),
(39,'Can delete events',10,'delete_events'),
(40,'Can view events',10,'view_events'),
(41,'Can add facilities',11,'add_facilities'),
(42,'Can change facilities',11,'change_facilities'),
(43,'Can delete facilities',11,'delete_facilities'),
(44,'Can view facilities',11,'view_facilities'),
(45,'Can add login',12,'add_login'),
(46,'Can change login',12,'change_login'),
(47,'Can delete login',12,'delete_login'),
(48,'Can view login',12,'view_login'),
(49,'Can add package',13,'add_package'),
(50,'Can change package',13,'change_package'),
(51,'Can delete package',13,'delete_package'),
(52,'Can view package',13,'view_package'),
(53,'Can add salary_info',14,'add_salary_info'),
(54,'Can change salary_info',14,'change_salary_info'),
(55,'Can delete salary_info',14,'delete_salary_info'),
(56,'Can view salary_info',14,'view_salary_info'),
(57,'Can add room',15,'add_room'),
(58,'Can change room',15,'change_room'),
(59,'Can delete room',15,'delete_room'),
(60,'Can view room',15,'view_room'),
(61,'Can add request_materials',16,'add_request_materials'),
(62,'Can change request_materials',16,'change_request_materials'),
(63,'Can delete request_materials',16,'delete_request_materials'),
(64,'Can view request_materials',16,'view_request_materials'),
(65,'Can add registration',17,'add_registration'),
(66,'Can change registration',17,'change_registration'),
(67,'Can delete registration',17,'delete_registration'),
(68,'Can view registration',17,'view_registration'),
(73,'Can add offers',19,'add_offers'),
(74,'Can change offers',19,'change_offers'),
(75,'Can delete offers',19,'delete_offers'),
(76,'Can view offers',19,'view_offers'),
(77,'Can add menu',20,'add_menu'),
(78,'Can change menu',20,'change_menu'),
(79,'Can delete menu',20,'delete_menu'),
(80,'Can view menu',20,'view_menu'),
(81,'Can add leave',21,'add_leave'),
(82,'Can change leave',21,'change_leave'),
(83,'Can delete leave',21,'delete_leave'),
(84,'Can view leave',21,'view_leave'),
(85,'Can add feedback',22,'add_feedback'),
(86,'Can change feedback',22,'change_feedback'),
(87,'Can delete feedback',22,'delete_feedback'),
(88,'Can view feedback',22,'view_feedback'),
(89,'Can add event_book',23,'add_event_book'),
(90,'Can change event_book',23,'change_event_book'),
(91,'Can delete event_book',23,'delete_event_book'),
(92,'Can view event_book',23,'view_event_book'),
(93,'Can add chat',24,'add_chat'),
(94,'Can change chat',24,'change_chat'),
(95,'Can delete chat',24,'delete_chat'),
(96,'Can view chat',24,'view_chat'),
(101,'Can add attendance',25,'add_attendance'),
(102,'Can change attendance',25,'change_attendance'),
(103,'Can delete attendance',25,'delete_attendance'),
(104,'Can view attendance',25,'view_attendance'),
(105,'Can add menubooking',26,'add_menubooking'),
(106,'Can change menubooking',26,'change_menubooking'),
(107,'Can delete menubooking',26,'delete_menubooking'),
(108,'Can view menubooking',26,'view_menubooking'),
(109,'Can add menu_order_details',27,'add_menu_order_details'),
(110,'Can change menu_order_details',27,'change_menu_order_details'),
(111,'Can delete menu_order_details',27,'delete_menu_order_details'),
(112,'Can view menu_order_details',27,'view_menu_order_details'),
(113,'Can add menu_orders',28,'add_menu_orders'),
(114,'Can change menu_orders',28,'change_menu_orders'),
(115,'Can delete menu_orders',28,'delete_menu_orders'),
(116,'Can view menu_orders',28,'view_menu_orders'),
(117,'Can add bank',29,'add_bank'),
(118,'Can change bank',29,'change_bank'),
(119,'Can delete bank',29,'delete_bank'),
(120,'Can view bank',29,'view_bank');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(25,'resortapp','attendance'),
(29,'resortapp','bank'),
(7,'resortapp','booking'),
(24,'resortapp','chat'),
(8,'resortapp','cottage'),
(9,'resortapp','employee'),
(23,'resortapp','event_book'),
(10,'resortapp','events'),
(11,'resortapp','facilities'),
(22,'resortapp','feedback'),
(21,'resortapp','leave'),
(12,'resortapp','login'),
(20,'resortapp','menu'),
(27,'resortapp','menu_order_details'),
(28,'resortapp','menu_orders'),
(26,'resortapp','menubooking'),
(19,'resortapp','offers'),
(13,'resortapp','package'),
(17,'resortapp','registration'),
(16,'resortapp','request_materials'),
(15,'resortapp','room'),
(14,'resortapp','salary_info'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2022-06-30 05:14:00.199661'),
(2,'auth','0001_initial','2022-06-30 05:14:01.005031'),
(3,'admin','0001_initial','2022-06-30 05:14:01.189298'),
(4,'admin','0002_logentry_remove_auto_add','2022-06-30 05:14:01.199311'),
(5,'admin','0003_logentry_add_action_flag_choices','2022-06-30 05:14:01.210302'),
(6,'contenttypes','0002_remove_content_type_name','2022-06-30 05:14:01.398865'),
(7,'auth','0002_alter_permission_name_max_length','2022-06-30 05:14:01.473451'),
(8,'auth','0003_alter_user_email_max_length','2022-06-30 05:14:01.501457'),
(9,'auth','0004_alter_user_username_opts','2022-06-30 05:14:01.510459'),
(10,'auth','0005_alter_user_last_login_null','2022-06-30 05:14:01.573359'),
(11,'auth','0006_require_contenttypes_0002','2022-06-30 05:14:01.578361'),
(12,'auth','0007_alter_validators_add_error_messages','2022-06-30 05:14:01.587361'),
(13,'auth','0008_alter_user_username_max_length','2022-06-30 05:14:01.660840'),
(14,'auth','0009_alter_user_last_name_max_length','2022-06-30 05:14:01.732867'),
(15,'auth','0010_alter_group_name_max_length','2022-06-30 05:14:01.754861'),
(16,'auth','0011_update_proxy_permissions','2022-06-30 05:14:01.763855'),
(17,'auth','0012_alter_user_first_name_max_length','2022-06-30 05:14:01.834929'),
(18,'resortapp','0001_initial','2022-06-30 05:14:04.401712'),
(19,'sessions','0001_initial','2022-06-30 05:14:04.446527'),
(21,'resortapp','0002_attendance','2022-07-12 06:19:42.897894'),
(22,'resortapp','0003_alter_booking_booking_date_and_more','2022-07-13 06:34:49.134521'),
(23,'resortapp','0004_menu_photo_menubooking','2022-07-13 17:23:04.247754'),
(24,'resortapp','0005_remove_menu_cottage_id','2022-07-14 03:43:51.010003'),
(25,'resortapp','0006_menu_order_details_menu_orders_delete_menubooking_and_more','2022-07-14 06:10:42.653054'),
(26,'resortapp','0007_bank','2022-07-14 10:09:42.001321'),
(27,'resortapp','0008_leave_todate','2022-07-15 11:11:36.471338'),
(28,'resortapp','0009_booking_total_amount_alter_package_end_date_and_more','2022-07-18 05:14:41.347868'),
(29,'resortapp','0010_remove_offers_rate','2022-07-18 07:02:03.670339'),
(30,'resortapp','0011_room_status','2022-07-20 07:58:26.981988');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('hjwtfwtjmjl4bqjrn3q4l4v330ss70oh','eyJsaWQiOjUsInJpZCI6MX0:1oDLU7:CVLZh6mJ2LlhlHejY4roMvv8TbpaR6Rhy45DLYQo5Ww','2022-08-01 07:48:07.015880'),
('jg7g6e2zk2ie7g1lkhl4ds4tpvrz470a','.eJyrVsrJTFGyMtVRKgLRFjpKqSDaUEcpJbEkVclKycjAyEjXwFzXyEhJRykXJGemo1SSX5KYA2QZAIGOUhJI1NiyFgD-XxOt:1oETfM:yGBnlhy5FZ5vlHhLo0V3vdeqvq8QG3rm-SPk_CdPdxU','2022-08-04 10:44:24.556035');

/*Table structure for table `resortapp_attendance` */

DROP TABLE IF EXISTS `resortapp_attendance`;

CREATE TABLE `resortapp_attendance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `attendance` int NOT NULL,
  `employee_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_attendance_employee_id_id_b25f60f9_fk_resortapp` (`employee_id_id`),
  CONSTRAINT `resortapp_attendance_employee_id_id_b25f60f9_fk_resortapp` FOREIGN KEY (`employee_id_id`) REFERENCES `resortapp_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_attendance` */

insert  into `resortapp_attendance`(`id`,`date`,`attendance`,`employee_id_id`) values 
(1,'2022-07-11',1,3),
(2,'2022-07-11',1,4),
(3,'2022-07-12',1,3),
(5,'2022-07-14',1,3),
(6,'2022-07-14',1,4),
(7,'2022-07-22',1,3);

/*Table structure for table `resortapp_bank` */

DROP TABLE IF EXISTS `resortapp_bank`;

CREATE TABLE `resortapp_bank` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(50) NOT NULL,
  `ifsc` varchar(50) NOT NULL,
  `pin` bigint NOT NULL,
  `account_no` bigint NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_bank` */

insert  into `resortapp_bank`(`id`,`bank_name`,`ifsc`,`pin`,`account_no`,`amount`) values 
(1,'HDFC','HDFC0002345',1820,123456789,413500),
(2,'SBI','SBI0003456',1828,234567891,682500),
(3,'Canera Bank','CNR00006789',2021,987654321,700000);

/*Table structure for table `resortapp_booking` */

DROP TABLE IF EXISTS `resortapp_booking`;

CREATE TABLE `resortapp_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number_of_persn` int NOT NULL,
  `adults` int NOT NULL,
  `childrens` int NOT NULL,
  `date_arrival` date NOT NULL,
  `date_vaccate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `booking_date` date NOT NULL,
  `facilities_id_id` bigint NOT NULL,
  `package_id_id` bigint NOT NULL,
  `room_id_id` bigint NOT NULL,
  `user_id_id` bigint NOT NULL,
  `total_amount` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_booking_facilities_id_id_de0f7575_fk_resortapp` (`facilities_id_id`),
  KEY `resortapp_booking_package_id_id_db79e5fc_fk_resortapp_package_id` (`package_id_id`),
  KEY `resortapp_booking_room_id_id_79e544a9_fk_resortapp_room_id` (`room_id_id`),
  KEY `resortapp_booking_user_id_id_2d5d98ef_fk_resortapp` (`user_id_id`),
  CONSTRAINT `resortapp_booking_facilities_id_id_de0f7575_fk_resortapp` FOREIGN KEY (`facilities_id_id`) REFERENCES `resortapp_facilities` (`id`),
  CONSTRAINT `resortapp_booking_package_id_id_db79e5fc_fk_resortapp_package_id` FOREIGN KEY (`package_id_id`) REFERENCES `resortapp_package` (`id`),
  CONSTRAINT `resortapp_booking_room_id_id_79e544a9_fk_resortapp_room_id` FOREIGN KEY (`room_id_id`) REFERENCES `resortapp_room` (`id`),
  CONSTRAINT `resortapp_booking_user_id_id_2d5d98ef_fk_resortapp` FOREIGN KEY (`user_id_id`) REFERENCES `resortapp_registration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_booking` */

insert  into `resortapp_booking`(`id`,`number_of_persn`,`adults`,`childrens`,`date_arrival`,`date_vaccate`,`status`,`booking_date`,`facilities_id_id`,`package_id_id`,`room_id_id`,`user_id_id`,`total_amount`) values 
(21,5,3,2,'2022-07-20','2022-07-22','pending','2022-07-18',4,1,1,3,12000),
(39,2,0,2,'2022-07-19','2022-07-20','paid','2022-07-20',3,2,2,2,22500);

/*Table structure for table `resortapp_chat` */

DROP TABLE IF EXISTS `resortapp_chat`;

CREATE TABLE `resortapp_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `emp_id_id` bigint NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_chat_emp_id_id_184b1c3c_fk_resortapp_login_id` (`emp_id_id`),
  KEY `resortapp_chat_user_id_id_2fad5479_fk_resortapp_login_id` (`user_id_id`),
  CONSTRAINT `resortapp_chat_emp_id_id_184b1c3c_fk_resortapp_login_id` FOREIGN KEY (`emp_id_id`) REFERENCES `resortapp_login` (`id`),
  CONSTRAINT `resortapp_chat_user_id_id_2fad5479_fk_resortapp_login_id` FOREIGN KEY (`user_id_id`) REFERENCES `resortapp_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_chat` */

/*Table structure for table `resortapp_cottage` */

DROP TABLE IF EXISTS `resortapp_cottage`;

CREATE TABLE `resortapp_cottage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cottage_num` int NOT NULL,
  `cottage_details` longtext NOT NULL,
  `number_rooms` int NOT NULL,
  `cottage_facility` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_cottage` */

insert  into `resortapp_cottage`(`id`,`cottage_num`,`cottage_details`,`number_rooms`,`cottage_facility`) values 
(1,1001,'fully wifi ',4,'swimming pool area\r\nchildren play area'),
(2,1002,'Free Internet\r\nAir Conditioning\r\nRoom Service\r\nRestaurant/Coffee Shop',6,'boating'),
(3,1003,' kids play area, Wi-Fi, front desk and laundry service',3,'Seperate Kitchens Spaces');

/*Table structure for table `resortapp_employee` */

DROP TABLE IF EXISTS `resortapp_employee`;

CREATE TABLE `resortapp_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` int NOT NULL,
  `state` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `phone` bigint NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `adarnumber` bigint NOT NULL,
  `salary` bigint NOT NULL,
  `emptype` varchar(50) NOT NULL,
  `jobtitle` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `loginid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_employee_loginid_id_b70b49f6_fk_resortapp_login_id` (`loginid_id`),
  CONSTRAINT `resortapp_employee_loginid_id_b70b49f6_fk_resortapp_login_id` FOREIGN KEY (`loginid_id`) REFERENCES `resortapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_employee` */

insert  into `resortapp_employee`(`id`,`firstname`,`lastname`,`place`,`street`,`city`,`pincode`,`state`,`district`,`phone`,`gender`,`dob`,`adarnumber`,`salary`,`emptype`,`jobtitle`,`photo`,`loginid_id`) values 
(3,'Arun','MK','Ambadi','Kallayi','Areekode',673204,'Kerala','Malapuram',8976530922,'male','1993-06-25',325476897654,6000,'KITCHEN','Cleaning','WIN_20210303_15_36_05_Pro_I7m6y7p.jpg',7),
(4,'Shobana','S','karthikass','Kadathanadankallu','Manarkade',670906,'Kerala','Palakkad',9876567876,'female','1990-09-12',334565437890,7000,'ROOM','Bed Setting','WhatsApp Image 2021-07-31 at 1.56.16 PM_Wsl8JLn.jpeg',8);

/*Table structure for table `resortapp_event_book` */

DROP TABLE IF EXISTS `resortapp_event_book`;

CREATE TABLE `resortapp_event_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `requirements` longtext NOT NULL,
  `booking_date` date NOT NULL,
  `event_id_id` bigint NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_event_book_event_id_id_122e2e8b_fk_resortapp_events_id` (`event_id_id`),
  KEY `resortapp_event_book_user_id_id_93e88e85_fk_resortapp` (`user_id_id`),
  CONSTRAINT `resortapp_event_book_event_id_id_122e2e8b_fk_resortapp_events_id` FOREIGN KEY (`event_id_id`) REFERENCES `resortapp_events` (`id`),
  CONSTRAINT `resortapp_event_book_user_id_id_93e88e85_fk_resortapp` FOREIGN KEY (`user_id_id`) REFERENCES `resortapp_registration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_event_book` */

insert  into `resortapp_event_book`(`id`,`status`,`requirements`,`booking_date`,`event_id_id`,`user_id_id`) values 
(1,'accept','black and grey baloons','2022-07-08',1,3),
(2,'reject',' Use Yellow Flowers Decorations','2022-08-04',2,2),
(3,'pending','no requirements','2022-07-27',3,3),
(4,'','yellow baloons','2022-07-28',1,1),
(5,'','yellow baloons','2022-07-28',1,1),
(6,'','yellow baloons','2022-07-28',1,1),
(7,'','Yellow baloons','2022-07-28',1,1),
(9,'pending','decorations : use rose flowers','2022-07-30',1,1),
(10,'pending','N/A','2022-07-29',1,1),
(11,'pending','aaaaaa','2022-07-30',1,1),
(12,'paid','aaaaaa','2022-07-30',1,1);

/*Table structure for table `resortapp_events` */

DROP TABLE IF EXISTS `resortapp_events`;

CREATE TABLE `resortapp_events` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `event_name` varchar(50) NOT NULL,
  `eve_desc` longtext NOT NULL,
  `rate` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_events` */

insert  into `resortapp_events`(`id`,`event_name`,`eve_desc`,`rate`,`photo`) values 
(1,'Birthdays','more than 100 people can allowed',60000,'birthday2_DoGRSeI.jpg'),
(2,'Engagments','Small Family Engagments',20000,'events1.jpg'),
(3,'Birthdays','Friends Family Party including 10 Peoples',6000,'birthdayparty_DbrM986.jpg');

/*Table structure for table `resortapp_facilities` */

DROP TABLE IF EXISTS `resortapp_facilities`;

CREATE TABLE `resortapp_facilities` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `faci_name` varchar(50) NOT NULL,
  `rate` bigint NOT NULL,
  `desc` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_facilities` */

insert  into `resortapp_facilities`(`id`,`faci_name`,`rate`,`desc`) values 
(1,'Boating',1500,'Electric boat include 5 peoples'),
(2,'Trekking',2000,'Trekking at Nearest Mountains with Guide'),
(3,'Rock Climbing',2500,'Secure \r\nGuide Available\r\nDoctors Available'),
(4,'None of this',0,'no items');

/*Table structure for table `resortapp_feedback` */

DROP TABLE IF EXISTS `resortapp_feedback`;

CREATE TABLE `resortapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` longtext NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_feedback_user_id_id_09b8a0b4_fk_resortapp` (`user_id_id`),
  CONSTRAINT `resortapp_feedback_user_id_id_09b8a0b4_fk_resortapp` FOREIGN KEY (`user_id_id`) REFERENCES `resortapp_registration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_feedback` */

insert  into `resortapp_feedback`(`id`,`description`,`rating`,`date`,`user_id_id`) values 
(1,'good resort\r\npeacefull ',4,'2022-07-08',3),
(2,'good',4,'2022-07-13',3),
(3,'bad',1.5,'2022-07-13',3);

/*Table structure for table `resortapp_leave` */

DROP TABLE IF EXISTS `resortapp_leave`;

CREATE TABLE `resortapp_leave` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `reason` longtext NOT NULL,
  `requestdate` date NOT NULL,
  `employeeid_id` bigint NOT NULL,
  `todate` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_leave_employeeid_id_1d3c695c_fk_resortapp_employee_id` (`employeeid_id`),
  CONSTRAINT `resortapp_leave_employeeid_id_1d3c695c_fk_resortapp_employee_id` FOREIGN KEY (`employeeid_id`) REFERENCES `resortapp_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_leave` */

insert  into `resortapp_leave`(`id`,`date`,`status`,`reason`,`requestdate`,`employeeid_id`,`todate`) values 
(1,'2022-07-05','accept','Marriage Function','2022-07-22',3,'2022-07-15'),
(2,'2022-07-13','reject','Birthday partie','2022-07-30',3,'2022-07-15'),
(3,'2022-07-15','reject','Sudden bike accident','2022-07-15',4,'2022-07-15');

/*Table structure for table `resortapp_login` */

DROP TABLE IF EXISTS `resortapp_login`;

CREATE TABLE `resortapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_login` */

insert  into `resortapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(3,'sruthips','sruthips18','user'),
(4,'ashitha','ashitha18','user'),
(5,'akshara','akshara18','user'),
(7,'Arunmk','Arunmk18','employee'),
(8,'Shobanas','Shobana18','employee'),
(9,'shyamjith18','Shyamjith@18','user');

/*Table structure for table `resortapp_menu` */

DROP TABLE IF EXISTS `resortapp_menu`;

CREATE TABLE `resortapp_menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) NOT NULL,
  `item_description` longtext NOT NULL,
  `rate` bigint NOT NULL,
  `stock` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_menu` */

insert  into `resortapp_menu`(`id`,`item_name`,`item_description`,`rate`,`stock`,`photo`) values 
(1,'Burgers','cheesy',350,84,'food1_9RKg5km.jpg'),
(2,'vegitable fried rice','Chilli Paneer and Veg Fried Rice Combo ',400,99,'veg_fridrice.JPG'),
(3,'Mojito','Green Apple Flavour ',70,100,'drink2.jpg'),
(6,'Biriyani','dum biriyani',190,12,'biriyani.jpg');

/*Table structure for table `resortapp_menu_order_details` */

DROP TABLE IF EXISTS `resortapp_menu_order_details`;

CREATE TABLE `resortapp_menu_order_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` bigint NOT NULL,
  `status` varchar(30) NOT NULL,
  `menu_id_id` bigint NOT NULL,
  `menu_orderid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_menu_order_menu_orderid_id_98585fdf_fk_resortapp` (`menu_orderid_id`),
  KEY `resortapp_menu_order_menu_id_id_f31460a1_fk_resortapp` (`menu_id_id`),
  CONSTRAINT `resortapp_menu_order_menu_id_id_f31460a1_fk_resortapp` FOREIGN KEY (`menu_id_id`) REFERENCES `resortapp_menu` (`id`),
  CONSTRAINT `resortapp_menu_order_menu_orderid_id_98585fdf_fk_resortapp` FOREIGN KEY (`menu_orderid_id`) REFERENCES `resortapp_menu_orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_menu_order_details` */

insert  into `resortapp_menu_order_details`(`id`,`quantity`,`status`,`menu_id_id`,`menu_orderid_id`) values 
(1,10,'ordered',1,31),
(2,1,'ordered',1,32),
(3,1,'ordered',2,33),
(4,7,'ordered',6,34),
(5,5,'ordered',1,35),
(6,1,'ordered',6,36);

/*Table structure for table `resortapp_menu_orders` */

DROP TABLE IF EXISTS `resortapp_menu_orders`;

CREATE TABLE `resortapp_menu_orders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `book_date` date NOT NULL,
  `total_amount` bigint NOT NULL,
  `status` varchar(30) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_menu_order_user_id_id_49246746_fk_resortapp` (`user_id_id`),
  CONSTRAINT `resortapp_menu_order_user_id_id_49246746_fk_resortapp` FOREIGN KEY (`user_id_id`) REFERENCES `resortapp_registration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_menu_orders` */

insert  into `resortapp_menu_orders`(`id`,`book_date`,`total_amount`,`status`,`user_id_id`) values 
(31,'2022-07-15',3500,'paid',3),
(32,'2022-07-15',3830,'paid',3),
(33,'2022-07-15',3830,'paid',3),
(34,'2022-07-16',3830,'paid',3),
(35,'2022-07-18',3830,'paid',3),
(36,'2022-07-18',0,'pending',3);

/*Table structure for table `resortapp_offers` */

DROP TABLE IF EXISTS `resortapp_offers`;

CREATE TABLE `resortapp_offers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number_of_persn` int NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `offer_price` double NOT NULL,
  `package_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_offers_package_id_id_1a0ba421_fk_resortapp_package_id` (`package_id_id`),
  CONSTRAINT `resortapp_offers_package_id_id_1a0ba421_fk_resortapp_package_id` FOREIGN KEY (`package_id_id`) REFERENCES `resortapp_package` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_offers` */

insert  into `resortapp_offers`(`id`,`number_of_persn`,`start_date`,`end_date`,`offer_price`,`package_id_id`) values 
(1,4,'2022-07-18','2022-07-31',1000,1);

/*Table structure for table `resortapp_package` */

DROP TABLE IF EXISTS `resortapp_package`;

CREATE TABLE `resortapp_package` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pack_name` varchar(50) NOT NULL,
  `rate` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_package` */

insert  into `resortapp_package`(`id`,`pack_name`,`rate`,`photo`,`description`,`start_date`,`end_date`) values 
(1,'Summer Package',8000,'package_xWZeyHm.jpg','fully wi-fi\r\nswimming pool\r\nchildrens play area','2022-07-01','2022-07-10'),
(2,'None of this',0,'home 2.jpeg','no items','2022-07-18','2022-07-31');

/*Table structure for table `resortapp_payment` */

DROP TABLE IF EXISTS `resortapp_payment`;

CREATE TABLE `resortapp_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `amount` bigint NOT NULL,
  `status` varchar(50) NOT NULL,
  `book_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_payment_book_id_id_854fca81_fk_resortapp_booking_id` (`book_id_id`),
  CONSTRAINT `resortapp_payment_book_id_id_854fca81_fk_resortapp_booking_id` FOREIGN KEY (`book_id_id`) REFERENCES `resortapp_booking` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_payment` */

/*Table structure for table `resortapp_registration` */

DROP TABLE IF EXISTS `resortapp_registration`;

CREATE TABLE `resortapp_registration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` int NOT NULL,
  `state` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `phone` bigint NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `loginid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_registration_loginid_id_b38e93aa_fk_resortapp_login_id` (`loginid_id`),
  CONSTRAINT `resortapp_registration_loginid_id_b38e93aa_fk_resortapp_login_id` FOREIGN KEY (`loginid_id`) REFERENCES `resortapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_registration` */

insert  into `resortapp_registration`(`id`,`firstname`,`lastname`,`place`,`street`,`city`,`pincode`,`state`,`country`,`gender`,`phone`,`idproof`,`email`,`nationality`,`loginid_id`) values 
(1,'ashitha','s','thalassery','Thalassery','Kozhikode',673505,'Kerala','India','Female',8848097653,'2022-03-19.png','ashithas23@gmail.com','indian',3),
(2,'sruthi','ps','nittoor','kuttiady','Kozhikode',673507,'Kerala','India','Female',8848092013,'2022-03-19_XgzJ7Uv.png','sruthiips18@gmail.com','indian',4),
(3,'akshara','k','kallullaparabath','thallasery','kannur',675439,'kerala','india','Female',7898765457,'WhatsApp Image 2021-07-30 at 9.29.30 PM (2).jpeg','akshara@gmail.com','indian',5),
(4,'Shyam','ps','Sarovaram','Muttil','Wayanad',675432,'Kerala','India','Male',8976543466,'WhatsApp Image 2021-05-20 at 6.43.33 PM.jpeg','shyamjith18@gmail.com','Male',9);

/*Table structure for table `resortapp_request_materials` */

DROP TABLE IF EXISTS `resortapp_request_materials`;

CREATE TABLE `resortapp_request_materials` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `material_det` varchar(100) NOT NULL,
  `quantity` bigint NOT NULL,
  `status` varchar(50) NOT NULL,
  `emp_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_request_ma_emp_id_id_fc6ff1cf_fk_resortapp` (`emp_id_id`),
  CONSTRAINT `resortapp_request_ma_emp_id_id_fc6ff1cf_fk_resortapp` FOREIGN KEY (`emp_id_id`) REFERENCES `resortapp_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_request_materials` */

insert  into `resortapp_request_materials`(`id`,`material_det`,`quantity`,`status`,`emp_id_id`) values 
(1,'chair',5,'pending',3),
(2,'Bed',1,'pending',4),
(3,'Vessals',7,'pending',3),
(4,'Spoons',50,'pending',3),
(5,'Bed',3,'pending',4);

/*Table structure for table `resortapp_room` */

DROP TABLE IF EXISTS `resortapp_room`;

CREATE TABLE `resortapp_room` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `room_number` varchar(50) NOT NULL,
  `room_facility` varchar(50) NOT NULL,
  `number_of_persons` int NOT NULL,
  `description` longtext NOT NULL,
  `photo` varchar(100) NOT NULL,
  `rate` bigint NOT NULL,
  `cottage_id_id` bigint NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `room_number` (`room_number`),
  KEY `resortapp_room_cottage_id_id_53638259_fk_resortapp_cottage_id` (`cottage_id_id`),
  CONSTRAINT `resortapp_room_cottage_id_id_53638259_fk_resortapp_cottage_id` FOREIGN KEY (`cottage_id_id`) REFERENCES `resortapp_cottage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_room` */

insert  into `resortapp_room`(`id`,`room_number`,`room_facility`,`number_of_persons`,`description`,`photo`,`rate`,`cottage_id_id`,`status`) values 
(1,'A001','DOUBLE COT BED',4,'full wi-fi facilities\r\n','room2_oNA0LEj.jpg',2000,1,'un-available'),
(2,'A002','DOUBLE COT BED',4,'extra kitchen area','room4.jpg',4000,2,'un-available'),
(8,'A003','SINGLE COT BED',6,'Deluxe Non Ac Room \r\nCourtyard View\r\nDouble Bed\r\n Air Purifier\r\nBathtub\r\n','room6_TBc8iBt.jpg',3500,1,'available');

/*Table structure for table `resortapp_salary_info` */

DROP TABLE IF EXISTS `resortapp_salary_info`;

CREATE TABLE `resortapp_salary_info` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `salary_amount` bigint NOT NULL,
  `date` datetime(6) NOT NULL,
  `status` varchar(50) NOT NULL,
  `emp_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resortapp_salary_inf_emp_id_id_0c1103b7_fk_resortapp` (`emp_id_id`),
  CONSTRAINT `resortapp_salary_inf_emp_id_id_0c1103b7_fk_resortapp` FOREIGN KEY (`emp_id_id`) REFERENCES `resortapp_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `resortapp_salary_info` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

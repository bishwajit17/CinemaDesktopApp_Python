-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ali2suhail_prj
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `booking_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned NOT NULL,
  `show_id` int unsigned NOT NULL,
  `cust_name` varchar(50) NOT NULL,
  `cust_email` varchar(100) NOT NULL,
  `cust_phone` varchar(20) NOT NULL,
  `seat_type` enum('LH','UH','VIP') NOT NULL,
  `no_of_tickets` int unsigned NOT NULL,
  `total_paid` decimal(13,2) unsigned NOT NULL,
  `date_paid` datetime NOT NULL,
  PRIMARY KEY (`booking_id`),
  UNIQUE KEY `booking_id_UNIQUE` (`booking_id`),
  KEY `show_id_idx` (`show_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `show_id` FOREIGN KEY (`show_id`) REFERENCES `shows` (`show_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,1,1,'Edgaras Levinskas','edgar@gmail.com','09867646754','VIP',2,69.69,'2022-12-12 00:00:00'),(2,4,2,'Bishwajit Sonar','Bishu.radar@gmail.com','07792672812','LH',1,10.00,'2022-12-10 00:00:00'),(4,1,4,'Chu Yie Nian','noidea@gmail.com','09782637288','UH',3,100.00,'2022-12-03 00:00:00'),(5,2,9,'Bishwajit Sonar','Bishu.radar@gmail.com','07792672812','LH',1,5.00,'2022-12-11 05:23:00'),(6,2,9,'Thomas Win','threadripper32@500','06969696969','VIP',5,1204.00,'2022-12-01 18:23:10'),(7,8,10,'Lawson Flynn','LawsonFlynn@yahoo.com','08674456745','UH',2,12.00,'2022-12-31 05:34:00'),(8,8,10,'Guy Horne','GuySensei@gmail.com','95785939434','UH',1,10.00,'2022-12-31 12:34:00'),(9,8,10,'Thomas Jacob','tjzacharia@gmai.com','09945236537','LH',10,16.00,'2023-01-01 02:34:23'),(10,19,12,'Mikayla Sims','Msims@uwe.ac.uk','03484394950','VIP',1,20.00,'2022-12-04 10:30:00'),(11,19,12,'test','test@gmail.com','12345678910','LH',5,10.00,'2022-12-14 09:00:00'),(13,19,12,'test2','test2','12345678910','UH',70,10.00,'2022-12-14 09:00:00'),(14,1,24,'Joshua','joshuaprem@gmail.com','0123456789','LH',1,3.00,'2023-01-07 07:45:00'),(18,1,2,'Bishu Radar','bish','1234','LH',2,14.00,'2023-01-08 23:58:55'),(22,2,4,'edg ert','edgGilbert@edg.com','12354656789','LH',1,8.00,'2023-01-08 22:31:43'),(24,3,4,'World winner','world@gmail.com','+09898999','LH',4,32.00,'2023-01-09 11:19:11'),(25,1,28,'Bobby Bob','alisuhail123@gmail','07784663752','VIP',1,8.64,'2023-01-10 02:09:19'),(26,1,28,'Bishu Solar Radar','bish123@gmail.com','09983662374','VIP',7,60.48,'2023-01-10 02:11:16'),(28,1,22,'Bishu Radar','bishRadar123@gmail.com','123456789','VIP',1,8.64,'2023-01-10 06:31:46');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cinemas`
--

DROP TABLE IF EXISTS `cinemas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cinemas` (
  `cinema_id` int unsigned NOT NULL AUTO_INCREMENT,
  `cinema_name` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `morn_LH_price` decimal(13,2) unsigned NOT NULL,
  `morn_UH_price` decimal(13,2) unsigned NOT NULL,
  `morn_VIP_price` decimal(13,2) unsigned NOT NULL,
  `after_LH_price` decimal(13,2) unsigned NOT NULL,
  `after_UH_price` decimal(13,2) unsigned NOT NULL,
  `after_VIP_price` decimal(13,2) unsigned NOT NULL,
  `night_LH_price` decimal(13,2) unsigned NOT NULL,
  `night_UH_price` decimal(13,2) unsigned NOT NULL,
  `night_VIP_price` decimal(13,2) unsigned NOT NULL,
  PRIMARY KEY (`cinema_id`),
  UNIQUE KEY `cinema_id_UNIQUE` (`cinema_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cinemas`
--

LOCK TABLES `cinemas` WRITE;
/*!40000 ALTER TABLE `cinemas` DISABLE KEYS */;
INSERT INTO `cinemas` VALUES (1,'HC Bristol','Bristol',6.00,7.20,8.64,7.00,8.40,10.08,8.00,9.60,11.52),(2,'HC Cribbs','Bristol',6.00,7.20,8.64,7.00,8.40,10.08,8.00,9.60,11.52),(3,'HC London','London',10.00,12.00,14.40,11.00,13.20,15.84,12.00,14.40,17.28),(4,'HC Cardif','Cardiff',5.00,6.00,7.20,6.00,7.20,8.64,7.00,8.40,10.08),(6,'HC Bishwajit ','Londan',12.00,14.40,17.28,12.00,14.40,17.28,12.00,14.40,14.40),(7,'HC Birmingham','Birmingham',20.00,24.00,28.80,22.00,26.40,31.68,24.40,29.28,29.28);
/*!40000 ALTER TABLE `cinemas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_id` int unsigned NOT NULL AUTO_INCREMENT,
  `movie_name` varchar(100) NOT NULL,
  `released` int unsigned NOT NULL,
  `publisher` varchar(50) NOT NULL,
  `rating` decimal(13,1) NOT NULL,
  `description` varchar(250) NOT NULL,
  `age_rating` enum('PG8','PG12','PG16','PG18') NOT NULL,
  `genre` varchar(50) NOT NULL,
  `duration` time NOT NULL,
  PRIMARY KEY (`movie_id`),
  UNIQUE KEY `movie_name_UNIQUE` (`movie_name`),
  UNIQUE KEY `movie_id_UNIQUE` (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Top Gun: Mavrick',2022,'Paramount',9.2,'After thirty years Maverick is still pushing the envelope as a top naval aviator','PG18','Action Drama','01:10:00'),(2,'Avatar: The Way of Water',2022,'20th Century Studios',7.9,'Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na\'vi race to protect their home.','PG12','Action Adventure Fantasy','03:12:00'),(3,'The Emoji Movie',2017,'Sony Pictures',3.4,'Gene, a multi-expressional emoji, sets out on a journey to become a normal emoji.','PG8','Animation Action Comedy','01:26:00'),(4,'Bullet Train',2022,'Disney',7.3,'Five assassins aboard a swiftly-moving bullet train find out that their missions have something in common.','PG18','Action Comedy Thriller','02:07:00'),(14,'Thor: Love and Thunder',2022,'Disney',6.3,'Thor enlists the help of Valkyrie, Korg and ex-girlfriend Jane Foster to fight Gorr the God Butcher, who intends to make the gods extinct.','PG12','Action Adventure Comedy','01:58:00'),(18,'Veer',2012,'Indian Publisher',7.6,'Bishwajit Sonar stars as the handsome man who fights to get the code','PG18','Drama Comedy Romance','02:12:00'),(22,'Shre',2000,'Dreamworks',10.0,'A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.','PG8','Animation Adventure Comedy','01:30:00'),(26,'Avengers: Endgame',2021,'Disney',8.4,'After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos\' actions and restore balance to the universe.','PG12','Action Adventure Drama','03:01:00'),(27,'Spider-Man: No Way Home',2021,'Disney',8.2,'With Spider-Man\'s identity now revealed, Peter asks Doctor Strange for help. When a spell goes wrong, dangerous foes from other worlds start to appear, forcing Peter to discover what it truly means to be Spider-Man.','PG12','Action Adventure Comedy','01:00:00'),(28,'Minions',2015,'Illumination Entertainment',6.2,'Minions Stuart, Kevin, and Bob are recruited by Scarlet Overkill, a supervillain who, alongside her inventor husband Herb, hatches a plot to take over the world.','PG8','Animation Action Comedy','01:31:00'),(29,'Doctor Strange in the Multiverse of Madness',2022,'Disney',6.9,'Doctor Strange teams up with a mysterious teenage girl from his dreams who can travel across multiverses, to battle multiple threats.','PG16','Action Adventure Comedy','02:00:00'),(32,'Sherlock Holmes',2009,'Silver Pictures Wigram Productions',7.6,'Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England.','PG12','Action Adventure Mystry','02:03:00'),(33,'Deadpool 2',2018,'Disney',7.7,'Foul-mouthed mutant mercenary Wade Wilson (a.k.a. Deadpool) assembles a team of fellow mutant rogues to protect a young boy with supernatural abilities from the brutal, time-traveling cyborg Cable.','PG18','Action Adventure Comedy','01:59:00'),(34,'Deadpool',2016,'Disney',6.9,'Foul-mouthed mutant ','PG18','Action comedy','02:00:00'),(35,'Spiders',2022,'Disney',6.9,'Foul-mouthed mutant ','PG18','Action comedy','02:00:00');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `screens`
--

DROP TABLE IF EXISTS `screens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `screens` (
  `screen_id` int unsigned NOT NULL AUTO_INCREMENT,
  `cinema_id` int unsigned NOT NULL,
  `movie_id` int unsigned NOT NULL,
  `total_seats` int NOT NULL,
  `lower_hall` int NOT NULL,
  `upper_hall` int NOT NULL,
  `vip` int NOT NULL,
  PRIMARY KEY (`screen_id`),
  UNIQUE KEY `screen_id_UNIQUE` (`screen_id`),
  KEY `cinema_id_idx` (`cinema_id`),
  KEY `movie_id_idx` (`movie_id`),
  CONSTRAINT `cinema_id` FOREIGN KEY (`cinema_id`) REFERENCES `cinemas` (`cinema_id`),
  CONSTRAINT `movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `screens`
--

LOCK TABLES `screens` WRITE;
/*!40000 ALTER TABLE `screens` DISABLE KEYS */;
INSERT INTO `screens` VALUES (1,2,2,100,30,60,10),(2,1,2,72,21,44,7),(3,1,3,82,24,50,8),(4,1,4,64,19,36,9),(5,2,1,119,35,78,6),(6,2,4,101,30,70,1),(7,2,3,70,31,46,3),(8,2,4,59,17,34,8),(9,3,3,119,35,77,7),(10,3,4,59,17,35,7),(11,3,1,117,35,77,5),(12,3,2,97,29,67,1),(13,1,1,100,30,60,10),(14,4,18,100,30,60,10),(15,1,2,100,30,60,10),(16,1,27,100,30,60,10);
/*!40000 ALTER TABLE `screens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shows` (
  `show_id` int unsigned NOT NULL AUTO_INCREMENT,
  `screen_id` int unsigned NOT NULL,
  `show_date` date NOT NULL,
  `show_start` time NOT NULL,
  PRIMARY KEY (`show_id`),
  UNIQUE KEY `show_id_UNIQUE` (`show_id`),
  KEY `screen_id_idx` (`screen_id`),
  CONSTRAINT `screen_id` FOREIGN KEY (`screen_id`) REFERENCES `screens` (`screen_id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES (1,3,'2023-01-14','09:00:00'),(2,3,'2023-01-13','14:00:00'),(3,9,'2023-01-13','19:00:00'),(4,3,'2023-01-13','10:00:00'),(5,4,'2023-01-13','19:00:00'),(6,3,'2023-01-13','22:00:00'),(7,4,'2023-01-13','10:00:00'),(8,4,'2023-01-13','22:00:00'),(9,5,'2023-01-12','09:00:00'),(10,5,'2023-01-12','14:00:00'),(11,5,'2023-01-12','19:00:00'),(12,6,'2023-01-12','09:00:00'),(13,6,'2023-01-12','14:00:00'),(14,9,'2023-01-11','19:00:00'),(15,12,'2023-01-11','22:00:00'),(16,6,'2023-01-11','09:00:00'),(17,6,'2023-01-11','14:00:00'),(18,7,'2023-01-11','14:00:00'),(19,7,'2023-01-12','19:00:00'),(20,7,'2023-01-18','22:00:00'),(21,10,'2023-01-18','09:00:00'),(22,3,'2023-01-12','10:00:00'),(23,1,'2023-01-12','17:00:00'),(24,3,'2023-01-16','09:00:00'),(25,3,'2023-01-16','14:00:00'),(26,3,'2023-01-12','19:00:00'),(27,3,'2023-01-12','11:00:00'),(28,3,'2023-01-12','14:00:00'),(29,4,'2023-01-14','19:00:00'),(30,2,'2023-01-15','12:00:00'),(31,13,'2023-01-20','14:00:00'),(32,4,'2023-01-29','14:00:00'),(33,15,'2023-01-14','23:00:00'),(34,14,'2023-01-14','18:00:00'),(35,5,'2023-01-14','18:00:00'),(36,6,'2023-01-14','23:00:00'),(37,7,'2023-01-16','18:00:00'),(38,8,'2023-01-16','23:00:00'),(39,9,'2023-01-16','18:00:00'),(40,10,'2023-01-16','23:00:00'),(41,11,'2023-01-16','18:00:00'),(42,12,'2023-01-16','23:00:00'),(43,13,'2023-01-16','18:00:00'),(44,14,'2023-01-16','23:00:00'),(45,15,'2023-01-16','18:00:00'),(46,15,'2023-01-16','23:00:00'),(47,13,'2023-01-20','14:00:00'),(48,1,'2023-01-17','15:00:00'),(49,1,'2023-01-17','15:00:00'),(50,2,'2023-01-17','15:00:00'),(51,1,'2023-01-17','15:00:00'),(52,3,'2023-01-18','18:00:00'),(53,4,'2023-01-18','18:00:00'),(54,5,'2023-01-18','18:00:00'),(55,6,'2023-01-18','18:00:00'),(56,7,'2023-01-18','18:00:00'),(57,8,'2023-01-18','18:00:00'),(58,9,'2023-01-18','18:00:00'),(59,10,'2023-01-18','18:00:00');
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int unsigned NOT NULL AUTO_INCREMENT,
  `cinema_id` int unsigned NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(225) NOT NULL,
  `user_type` enum('Admin','Manager','Staff') NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`),
  KEY `cinema_id2_idx` (`cinema_id`),
  CONSTRAINT `cinema_id2` FOREIGN KEY (`cinema_id`) REFERENCES `cinemas` (`cinema_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,1,'Ali Suhail','202CB962AC59075B964B07152D234B70','Admin'),(2,2,'Edgaras','202CB962AC59075B964B07152D234B70','Admin'),(3,3,'bishu','202CB962AC59075B964B07152D234B70','Admin'),(4,1,'Ellie May Chang','202CB962AC59075B964B07152D234B70','Manager'),(5,2,'manager','202CB962AC59075B964B07152D234B70','Manager'),(6,3,'Isabelle Morrison','202CB962AC59075B964B07152D234B70','Manager'),(7,1,'Tianna Barton','202CB962AC59075B964B07152D234B70','Staff'),(8,2,'Tara Daugherty','202CB962AC59075B964B07152D234B70','Staff'),(9,3,'Joan Durham','202CB962AC59075B964B07152D234B70','Staff'),(10,4,'Bob Bobby','202CB962AC59075B964B07152D234B70','Admin'),(11,4,'Aneesa Mayo','202CB962AC59075B964B07152D234B70','Manager'),(12,4,'Rueben Sutherland','202CB962AC59075B964B07152D234B70','Staff'),(13,4,'Mehmet Stone','202CB962AC59075B964B07152D234B70','Staff'),(14,4,'Albert Johnson','202CB962AC59075B964B07152D234B70','Staff'),(15,1,'Oscar Carson','202CB962AC59075B964B07152D234B70','Staff'),(16,1,'Amaya Thomas','202CB962AC59075B964B07152D234B70','Staff'),(17,1,'Issac Floyd','202CB962AC59075B964B07152D234B70','Staff'),(18,1,'Dorothy Gallagher','202CB962AC59075B964B07152D234B70','Staff'),(19,2,'Alicia Delacruz','202CB962AC59075B964B07152D234B70','Staff'),(20,2,'Kezia Stark','202CB962AC59075B964B07152D234B70','Staff'),(21,3,'Owen Mckenzie','202CB962AC59075B964B07152D234B70','Staff');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-10  7:33:07

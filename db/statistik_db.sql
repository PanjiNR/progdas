-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.4.5 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for statistik_db
CREATE DATABASE IF NOT EXISTS `statistik_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `statistik_db`;

-- Dumping structure for table statistik_db.hasil_statistik
CREATE TABLE IF NOT EXISTS `hasil_statistik` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_kelompok` varchar(100) DEFAULT NULL,
  `rata_rata` float DEFAULT NULL,
  `tertinggi` float DEFAULT NULL,
  `terendah` float DEFAULT NULL,
  `gini` float DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table statistik_db.hasil_statistik: ~3 rows (approximately)
INSERT INTO `hasil_statistik` (`id`, `nama_kelompok`, `rata_rata`, `tertinggi`, `terendah`, `gini`, `created_at`) VALUES
	(3, 'Bandung', 1600000, 3000000, 800000, 0.3056, '2025-12-31 11:09:57'),
	(4, 'Jakarta', 2000000, 3000000, 1000000, 0.2222, '2025-12-31 11:10:53'),
	(5, 'Batam', 2500000, 4000000, 1000000, 0.25, '2025-12-31 12:23:22');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

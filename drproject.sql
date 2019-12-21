-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 21, 2019 at 02:09 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drproject`
--
CREATE DATABASE IF NOT EXISTS `drproject` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `drproject`;

-- --------------------------------------------------------

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
CREATE TABLE IF NOT EXISTS `people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `gender` enum('not specified','boy','girl') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'not specified',
  `age` int(11) NOT NULL DEFAULT '0',
  `nice` enum('naughty','nice') NOT NULL DEFAULT 'naughty',
  `toy` varchar(250) NOT NULL DEFAULT 'Surprise',
  `chimney` enum('no','yes') NOT NULL DEFAULT 'no',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `people`
--

INSERT INTO `people` (`id`, `name`, `gender`, `age`, `nice`, `toy`, `chimney`) VALUES
(2, 'John', 'boy', 12, 'nice', 'bike', 'yes'),
(3, 'Mary', 'girl', 12, 'nice', 'dolls house', 'yes'),
(4, 'Peter', 'boy', 6, 'naughty', 'bb gun', 'yes'),
(5, 'Anne', 'girl', 11, 'naughty', 'x-box', 'no'),
(7, 'Melanie', 'girl', 23, 'nice', 'Surprise', 'no'),
(8, 'Barry', 'boy', 4, 'nice', 'Surprise', 'no'),
(9, 'Sean', 'boy', 12, 'naughty', 'Surprise', 'no'),
(10, 'Jeremy', 'boy', 6, 'naughty', 'Lego', 'yes'),
(11, 'frank', 'not specified', 11, 'naughty', 'Surprise', 'no'),
(16, 'Nick', 'boy', 23, 'nice', 'Peace and Quiet', 'yes'),
(15, 'Someone', 'not specified', 0, 'naughty', 'Surprise', 'no'),
(19, 'Barbara', 'girl', 9, 'nice', 'Horse', 'no'),
(18, 'Andrew', 'boy', 15, 'naughty', 'TV', 'yes'),
(20, 'Tilly', 'girl', 6, 'nice', 'Dolls house', 'yes'),
(21, 'Amanda', 'girl', 5, 'nice', 'Big teddy', 'no'),
(22, 'Alan', 'boy', 6, 'nice', 'goals', 'yes'),
(23, 'Sandy', 'not specified', 4, 'nice', 'Chew toy', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `toys`
--

DROP TABLE IF EXISTS `toys`;
CREATE TABLE IF NOT EXISTS `toys` (
  `itemId` int(11) NOT NULL AUTO_INCREMENT,
  `item` varchar(250) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  PRIMARY KEY (`itemId`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `toys`
--

INSERT INTO `toys` (`itemId`, `item`, `stock`) VALUES
(1, 'bike', 25),
(2, 'doll', 17),
(3, 'playstation', 20),
(4, 'hula hoop', 5),
(5, 'jigsaw', 15),
(6, 'book', 110),
(7, 'new baby brother', 2),
(8, 'diamond necklace', 1),
(9, 'hurley', 13),
(10, 'x-box', 0),
(11, 'Yo-yo', 2),
(12, 'water pistol', 6),
(13, 'guitar', 5),
(14, 'dolls house', 2),
(15, 'Lego', 11),
(16, 'big teddy', 11),
(17, 'surprise', 85),
(18, 'goals', 2),
(19, 'tv', 21),
(20, 'horse', 1),
(21, 'iPhone', 11);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

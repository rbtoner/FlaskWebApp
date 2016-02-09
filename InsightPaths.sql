-- MySQL dump 10.13  Distrib 5.6.27, for osx10.8 (x86_64)
--
-- Host: localhost    Database: InsightPaths
-- ------------------------------------------------------
-- Server version	5.6.27

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
-- Table structure for table `pfilterMeta`
--

DROP TABLE IF EXISTS `pfilterMeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pfilterMeta` (
  `name` text,
  `mp` text,
  `v1p` text,
  `v2p` text,
  `cut_pre` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pfilterMeta`
--

LOCK TABLES `pfilterMeta` WRITE;
/*!40000 ALTER TABLE `pfilterMeta` DISABLE KEYS */;
INSERT INTO `pfilterMeta` VALUES ('sw','pfilter_sw_model.pkl','pfilter_sw_v1.pkl','pfilter_sw_v2.pkl',0.2),('dai','pfilter_dai_model.pkl','pfilter_dai_v1.pkl','pfilter_dai_v2.pkl',0.2),('aou','pfilter_aou_model.pkl','pfilter_aou_v1.pkl','pfilter_aou_v2.pkl',0.2),('madmax','pfilter_madmax_model.pkl','pfilter_madmax_v1.pkl','pfilter_madmax_v2.pkl',0.2),('utale','pfilter_utale_model.pkl','pfilter_utale_v1.pkl','pfilter_utale_v2.pkl',0.2),('slock','pfilter_slock_model.pkl','pfilter_slock_v1.pkl','pfilter_slock_v2.pkl',0.2),('lis','pfilter_lis_model.pkl','pfilter_lis_v1.pkl','pfilter_lis_v2.pkl',0.2),('got','pfilter_got_model.pkl','pfilter_got_v1.pkl','pfilter_got_v2.pkl',0.2),('han','pfilter_han_model.pkl','pfilter_han_v1.pkl','pfilter_han_v2.pkl',0.2);
/*!40000 ALTER TABLE `pfilterMeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sfilterMeta`
--

DROP TABLE IF EXISTS `sfilterMeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sfilterMeta` (
  `name` text,
  `mf` text,
  `v1f` text,
  `v2f` text,
  `cut60` double DEFAULT NULL,
  `cut80` double DEFAULT NULL,
  `cut90` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sfilterMeta`
--

LOCK TABLES `sfilterMeta` WRITE;
/*!40000 ALTER TABLE `sfilterMeta` DISABLE KEYS */;
INSERT INTO `sfilterMeta` VALUES ('sw','sfilter_sw_model.pkl','sfilter_sw_v1.pkl','sfilter_sw_v2.pkl',0.7,0.51,0.35),('dai','sfilter_dai_model.pkl','sfilter_dai_v1.pkl','sfilter_dai_v2.pkl',0.62,0.451049358974359,0.328166666666667),('aou','sfilter_aou_model.pkl','sfilter_aou_v1.pkl','sfilter_aou_v2.pkl',0.71,0.52,0.36),('madmax','sfilter_madmax_model.pkl','sfilter_madmax_v1.pkl','sfilter_madmax_v2.pkl',0.625,0.437333333333333,0.32),('utale','sfilter_utale_model.pkl','sfilter_utale_v1.pkl','sfilter_utale_v2.pkl',0.63,0.44,0.3),('slock','sfilter_slock_model.pkl','sfilter_slock_v1.pkl','sfilter_slock_v2.pkl',0.58,0.43,0.32),('lis','sfilter_lis_model.pkl','sfilter_lis_v1.pkl','sfilter_lis_v2.pkl',0.61,0.43,0.3),('got','sfilter_got_model.pkl','sfilter_got_v1.pkl','sfilter_got_v2.pkl',0.60536300146301,0.44,0.32),('han','sfilter_han_model.pkl','sfilter_han_v1.pkl','sfilter_han_v2.pkl',0.55,0.417486309771354,0.314825939486442);
/*!40000 ALTER TABLE `sfilterMeta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-31 22:50:05

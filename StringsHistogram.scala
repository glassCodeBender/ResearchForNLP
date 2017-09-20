/**
  * I'm not as good at programming as I thought so I wrote the program for Apache Spark.
  *
  * mapValues() & reduceByKey() are the shiznit!!!
  */
  
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .master("local")
  .appName("StringsHistogram")
  .enableHiveSupport()
  .getOrCreate()

val rdd = sc.textFile("/FileStore/tables/f10dnito1505888092349/texttest.txt")

val count = rdd.map(x => (x, 1)).reduceByKey(_ + _).sortByKey()

val vec = count.collect.toVector

val sorted = vec.sortWith(_._2 > _._2)

val finalResult = sorted.map(x => s"${x._1} - ${x._2}")
finalResult.foreach(println)

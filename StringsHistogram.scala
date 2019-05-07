
/**
  *
  * Program for Apache Spark with imports omitted because I used DataBricks.
  * Program creates a histogram of words discovered in Strings output from bulk_extractor.
  * bulk_extractor was used to extract all the strings from a Windows image. Then, Apache Spark 
  * was used to get a word count for each string that was extracted.
  * 
  * This program can be used to help remove stop words before doing further data analysis on Strings in an image. 
  *
  * I has many other uses though.
  */

val rdd = sc.textFile("/FileStore/tables/526w99d81505957985736/file01.txt")
val rdd2 = sc.textFile("/FileStore/tables/526w99d81505957985736/file02.txt")
val rdd3 = sc.textFile("/FileStore/tables/526w99d81505957985736/file03.txt")
val rdd4 = sc.textFile("/FileStore/tables/526w99d81505957985736/file04.txt")

val regex = "//d+-(HYPERFILE|ZIP|GZIP)-//d+//s+".r

val clean1 = rdd.map(x => regex.replaceAllIn(x, ""))
  .map(_.toLowerCase)
  .map(_.trim)


val clean2 = rdd2.map(x => regex.replaceAllIn(x, ""))
  .map(_.toLowerCase)
  .map(_.trim)

val result1 = clean1.union(clean2)

val clean3 = rdd3.map(x => regex.replaceAllIn(x, ""))
  .map(_.toLowerCase)
  .map(_.trim)

val result2 = result1.union(clean3)

val clean4 =  rdd4.map(x => regex.replaceAllIn(x, ""))
  .map(_.toLowerCase)
  .map(_.trim)

val result3 = result2.union(clean4)

/**
  *   Change code here to add more files.
  */

val fullRDD = result3.union(result3)

val count = fullRDD.map(x => (x, 1)).reduceByKey(_ + _)
val invert = count.map(_.swap).sortByKey(ascending = false)

val finalResult = invert.map(x => s"${x._2} - ${x._1}")
finalResult.saveAsTextFile("/FileStore/tables/testProgram")

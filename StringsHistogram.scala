
import scala.io.Source
import java.io._

/**
  * Program for Apache Spark with imports omitted
  *
  * Program creates a histogram of words discovered in Strings output from bulk_extractor.
  * I has many other uses though.
  */

val rdd = sc.textFile("/FileStore/tables/f10dnito1505888092349/texttest.txt")

val count = rdd.map(x => (x, 1)).reduceByKey(_ + _).sortByKey()

val vec = count.collect.toVector

val sorted = vec.sortWith(_._2 > _._2)

val finalResult = sorted.map(x => s"${x._1} - ${x._2}")
finalResult.foreach(println)

/** Alternative style program prints to file. */

val list = Source.fromFile("wordlist.txt").getLines.toVector
// Used to clean up bulk_extractor output
val reg = "$\\d+\\s+".r

// Over 7 million entries so process in parallel
val cleanedList = list.par
  .map(x => reg.replaceAllIn(x, ""))
  .map(_.toLowerCase)
  .map(_.trim)

val rdd = sc.parallelize(cleanedList)

// Pretty much groupBy combined with reduce function.
val count = rdd.map(x => (x, 1)).reduceByKey(_ + _)

val vec = count.collect.toVector

// Sort big to small
val sorted = vec.sortWith(_._2 > _._2)

// Make it print pretty
val finalResult = sorted.map(x => s"${x._1} - ${x._2}")

// Convert Vector to String
val result = finalResult.mkString("\n")

// Write to txt file
val file = new File("histogram.txt")
val bw = new BufferedWriter(new FileWriter(file))
bw.write(result)
bw.close()

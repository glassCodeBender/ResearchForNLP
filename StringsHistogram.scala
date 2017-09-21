
import scala.io.Source
import java.io._
import scala.annotation.tailrec

/**
  * Program for Apache Spark with imports omitted because I used DataBricks.
  * Program creates a histogram of words discovered in Strings output from bulk_extractor.
  * I has many other uses though.
  */

val newRDD = sc.textFile("/FileStore/tables/f10dnito1505888092349/file01.txt")

val files = List("/FileStore/tables/f10dnito1505888092349/file02.txt",
  "/FileStore/tables/f10dnito1505888092349/file03.txt",
  "/FileStore/tables/f10dnito1505888092349/file04.txt",
"/FileStore/tables/f10dnito1505888092349/file05.txt")

@tailrec
def filterIt(newRdd: List[String], oldRdd: RDD): RDD ={
  if (newRdd == None){
    oldRDD
  } else{
    val currentRDD = sc.textFile(newRDD.head)
    val regex = "//d+-(HYPERFILE|ZIP|GZIP)-//d+//s+".r

    val rdd = currentRDD.map(x => regex.replaceAllIn(x, ""))
   .map(x => regex3.replaceAllIn(x, "")).map(_.toLowerCase).map(_.trim)

    val result = oldRdd.union(rdd)
  }
  filterIt( newRDD.tail, result)
} // END filterAndUnion

val fullRdd = filterIt(files, newRDD)

val count = fullRdd.map(x => (x, 1)).reduceByKey(_ + _)
val invert = count.map((x, y) -> (y, x)).sortByKey(ascending = false)

// val vec = count.collect.toVector

// val sorted = vec.sortWith(_._2 > _._2)

val finalResult = invert.map(x => s"${x._2} - ${x._1}")

finalResult.collect.toTextFile("SparkWindows10")
// finalResult.take(50).foreach(println)


/** SECTIONS FOR DEALING WITH SMALLER AMOUNTS OF DATA  */


/** Alternative style program prints to file. */

val list = Source.fromFile("wordlist.txt").getLines.toVector
// Used to clean up bulk_extractor output
val reg = "$\\d+(\\s+|".r

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

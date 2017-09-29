package com.bigbrainsecurity.nlp

/**
  * A home for methods that extend the functionality of Scala's String operations.
  * 
  * These methods can be called as follows:
  * "hey, y'all, I'm, getting better, at programming".splitFirst(',')
  */

object StringOperations {

  implicit class StringOpsContd( str: String ) {

    /** Split on first occurrence of a character */
    def splitFirst( x: Char ): Array[String] = {
      val arr = str.split( x )
      if ( arr.length > 2 ) Array( arr( 0 ), arr.tail.mkString(x.toString) )
      else arr
    } // END splitFirst()

    /** Split on first occurrence of Char Array */
    def splitFirst( x: Array[Char] ): Array[String] = {
      val arr = str.split( x )
      if ( arr.length > 2 ) Array( arr( 0 ), arr.tail.mkString(x.mkString) )
      else arr
    } // END splitFirst()

    /** Split on the last occurrence of a character. */
    def splitLast( x: Char ): Array[String] = {
      val arr: Array[String] = str.split( x )
      val index = arr.length - 1

      if ( arr.length > 2 ) {
        val takeBeginning: Array[String] = arr.take( index )
        val splitUp: Array[String] = Array( takeBeginning.mkString(x.toString), arr.last )
        splitUp
      } else arr
    } // END splitFirst()

    /** Split on last occurrence of char array */
    def splitLast( x: Array[Char] ): Array[String] = {
      val arr: Array[String] = str.split( x )
      val index = arr.length - 1

      if ( arr.length > 2 ) {
        val takeBeginning: Array[String] = arr.take( index )
        val splitUp: Array[String] = Array( takeBeginning.mkString(x.mkString), arr.last )
        splitUp
      } else arr
    } // END splitFirst()

  } // END StringOpsContd implicit class
} // END StringOperations object

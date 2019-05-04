# ResearchForNLP
Natural Language Processing Related Scripts

The wordlist.txt file that this program processes is a wordlist produced by the linux program bulk_extractor. See bulk_extractor's man page for more information on using bulk_extractor to extract the strings from an image of an OS.

To use StringsHistogram.scala on massive amounts of data, because the txt file is so huge, you'll need to break up the
wordlist.txt file and break it up into smaller files. Then, once you parallelize the data, you can run a union command on the RDDs to combine them. Remember, Union commands are costly. Filter, then Union. 

Use the following command to break up wordlist.txt on linux or mac:

~$ awk '{outfile=sprintf("file%02d.txt",NR/90000000+1);print > outfile}' wordlist.txt

# ResearchForNLP
Natural Language Processing Related Scripts

To use StringsHistogram on massive amounts of data, because the txt file is so huge, you'll need to break up the
wordlist.txt file and break it up into smaller files. Then, once you parallelize the data, you can run a union command on the RDDs to combine them. Remember, Union commands are costly. Filter, then Union. 

Use the following command to break up wordlist.txt on linux or mac:

~$ awk '{outfile=sprintf("file%02d.txt",NR/90000000+1);print > outfile}' wordlist.txt

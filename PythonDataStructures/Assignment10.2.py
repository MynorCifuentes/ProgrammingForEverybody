# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
# by hour of the day for each of the messages. You can pull the hour out from the 'From ' 
# line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname=input("Enter file name: ")
fh = open(fname)
counts = dict()
lst = list()
for line in fh:
    
    if(line.startswith('From ')):
        Fwords = line.split()
        time = Fwords[5:]
        hour = time[0].split(':')
        lst.append(hour[0])

for word in lst:
    counts[word] = counts.get(word,0)+1

liss = list()
for key,val in sorted(counts.items()):
   print(key,val)
 
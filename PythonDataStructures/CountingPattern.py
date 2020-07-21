                    #Fist way to do this
# counts = dict()
# print('Enter a line of text: ')
# line= input('')

# words = line.split()
# print('Words: ', words)

# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('Count',counts) 
######################################################
counts = dict()
line = input('Enter a line of text: ')
words = line.split()

print('Words: ',words)
print('Counting...')

for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts: ', counts)

stuff= dict()
print(stuff.get('candy',-1))





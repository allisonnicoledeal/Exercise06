from sys import argv
import string
import re

script, filename = argv

txt = open(filename)
filetext = txt.read()

txt.close()

filetext = filetext.lower()

filetext = re.sub("[. ? !]" , " ", filetext)

# for c in string.punctuation:
#     filetext = filetext.replace (c, "")

word_array = filetext.split()

dictionary = {}

for word in word_array:
    #print "dictionary word is: " + dictionary[word]
    dictionary[word] = dictionary.get(word,0) +1
    # if word not in dictionary: if word == None
    #     dictionary[word] = 1
    # else:
    #     dictionary[word] += 1

sorted_value =sorted(dictionary.iteritems(), key= lambda x : (-x[1], x[0]))# reverse = True)

for key,value in sorted_value:
    print key,value



import sys
import re
import operator
from functools import reduce

# sys.argv[0] contains the file name
if 1:
    count_dict = {}
    count_list = []
    with open("abc.txt", 'r') as f:
        for line in f:
            for word in line.split():
                word = re.sub(r'[^\w\s]','',word)
                if word not in count_dict:
                    count_dict[word] = 1
                else:
                    count_dict[word] += 1
    count_list = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
    print (count_list[:10])
    count = []
    print (count_list[0][1])
    for i in range(len(count_list)):
        count.append(count_list[i][1])
    print (reduce(lambda a, b: a + b, count) / len(count))
    print ([x*x for x in count if x % 2 != 0])


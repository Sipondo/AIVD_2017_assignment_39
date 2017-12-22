import csv
import numpy as np
letters = "abcdefghijklmnopqrstuvwxyz"

with open("dutch.csv", 'w') as outfile:
    writer = csv.DictWriter(outfile, ['id', 'word', 'vector'])
    writer.writeheader()
    with open("dutch_raw", 'r') as infile:
        tick = 0
        for line in infile.readlines():
            tick = tick+1
            if tick%2:
                word = line.split()[0]
                if (len(word)==5):
                    if all(not x in word for x in ['-', "'", '"']):
                        vector = np.asmatrix([(1 if x in word else 0) for x in letters])
                        writer.writerow({'id': tick/2, 'word': word, 'vector': vector})

translate_table = {"H1": 1,
                   "H3": 2,
                   "H5": 2,
                   "H6": 2,
                   "H7": 2,
                   "V1": 3,
                   "V2": 4}

with open("vlakken.csv", 'w') as outfile:
    writer = csv.DictWriter(outfile, ['square', 'id', 'max', 'vector'])
    with open("vlakken_raw.csv", 'r') as infile:
        reader = csv.reader(infile)
        for line in reader:
            vector = np.asmatrix([(1 if x in line[1] else 0) for x in letters])
            writer.writerow({'square': line[0][0],
                             'id': translate_table[line[0][1:]],
                             'max': len(line[1])-int(line[2]),
                             'vector': vector})

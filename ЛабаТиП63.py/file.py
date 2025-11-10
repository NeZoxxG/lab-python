from collections import *
f = open("/Users/nezoxxg/sport.txt", "r", encoding="cp1251")
text = f.readlines()
sports = []
for line in text[1:]:
    parts = line.split('\t')
    if parts[3] == '':
        continue
    else:
        sport = parts[3].strip()
        if "," in sport:
            sport = sport.split(",")
            for i in range(len(sport)):
                sports.append(sport[i])
        else:
            sports.append(sport)

for i in range(len(sports)):
    sports[i] = sports[i].strip()

sports_3 = Counter(sports)
print(sports_3.most_common(3))


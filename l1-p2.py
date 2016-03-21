import string

def loadFile():
    inFile = open('julyTemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

def parseLine(line):
    tempSet = string.split(line)[1:3]
    if not len(tempSet) or not tempSet[0].isdigit():
        return False
    return tempSet

def loadMonthTemp(filePath):
    days = []
    fileHandler = open(filePath, 'r', 0);
    for line in fileHandler:
        line = parseLine(line)
        if line:
            days.append(line)
    return days

loadMonthTemp('w1/julyTemps.txt')


apt-get install libopenblas-base mklibs

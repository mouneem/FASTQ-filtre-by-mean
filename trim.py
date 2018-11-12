# Quality code
QCode = "!\#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI"

index = QCode[1]

#ask user for params
filename = str(raw_input("input file name:\n"))
outfilename = str(raw_input("output file name:\n"))
start = int(raw_input("Start from:\n"))
end = int(raw_input("End at:\n"))
score = int(raw_input("Min score:\n"))

#read the fq file
with open(filename) as f:
    content = f.readlines()

#start proc
i = 0
while i < len(content):
    Quality = content[i+3]
    NumericQuality = []
    for j in Quality:
        NumericQuality.append(QCode.find(j))
    NqHead = NumericQuality[start:end]
    mean = float(sum(NqHead)) / max(len(NqHead), 1)
    # print mean
    if mean>score:
        with open(outfilename, 'a+') as f:
            for k in range(4):
                f.write(content[i+k])
    else:
        print "Bad quality: ","Line Number:",i,Quality[:20],"Score :",mean," < given score = ",score
    i+=4

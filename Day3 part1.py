print("------------")
print("Star5")
# Read in all the lines of your file into a list of lines
lines_list = open(r'D:\AoC\2021\day3_input.txt').readlines()
columns = []
# Read each column from the row lists
for i in range(0,len(lines_list[0])-1):
    columns = list(zip(*lines_list))
countEpsi = "" # zeros binary
countGamma = "" # ones binary
for i in range(0,len(columns)):
    countOne = columns[i].count('1')
    countZero = columns[i].count('0')
    if countOne > countZero:
        countGamma += '1'
        countEpsi += '0'
    if countZero > countOne:
        countEpsi += '1'
        countGamma += '0'


deciones = int(countGamma, 2)
decizeros = int(countEpsi, 2)
multiply = deciones * decizeros
print("Multiplied: "+str(multiply))
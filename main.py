import csv

myList = []
cs = ('','','computer science','0')
hs = (' ',' ','history','0')
bl = ('','','biology','0')
md = ('','','medicine','0')

###################################
#opening the file
###################################
try:
    with open('students.csv', 'r') as myFile:
        myReader = csv.reader(myFile)
        next(myReader)
        myList = list(myReader)
        ###################################
        # find the excellent students
        ###################################
        for myItem in myList:
            if myItem[2] == cs[2] and myItem[3] > cs[3]:
                cs = (myItem[0], myItem[1],myItem[2], myItem[3])

            elif myItem[2] == hs[2] and myItem[3] > hs[3]:
                hs = (myItem[0], myItem[1],myItem[2], myItem[3])

            elif myItem[2] == bl[2] and myItem[3] > bl[3]:
                bl = (myItem[0], myItem[1],myItem[2], myItem[3])

            elif myItem[2] == md[2] and myItem[3] > md[3]:
                md =(myItem[0], myItem[1],myItem[2], myItem[3])
        exlStudents = [cs, hs, bl, md]
except FileNotFoundError:
    raise Exception('File not open or cant open it' )#throwing an execption if file coudn't found or coudn't open

###################################
#opening the output file and write the result
###################################

with open('excellentStudents.tsv', 'w') as myFile:
    myWriter = csv.writer(myFile, delimiter="\t", lineterminator="\n\n")
    header =( "The excellent students by their faculty are:",'','','')
    myWriter.writerow(header)
    for i in range(len(exlStudents)):
        myWriter.writerow(exlStudents[i])



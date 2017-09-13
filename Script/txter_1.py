

def writeList (listy):
    text_file = open("txt/txtList.txt", "w")
    text_file.write(str(listy))
    text_file.close()


def write2DListToExcel (listy):
    text_file = open("txt/txtTabedExcel.txt", "w")
    print (len(listy))
    for i in range (len(listy)):
        text_file.write(
            str(listy[i][0]) + "\t" + 
            str(listy[i][1]) + "\n"
        )

    text_file.close()

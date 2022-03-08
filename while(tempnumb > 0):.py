while(tempnumb > 0):
    tempOutput = tempnumb%basenum
    if tempOutput < 10:
        output = str(tempOutput) + output
    else:
        output = ["A","B","C","D","E","F"][tempOutput-10] + output

while(tempnumb > 0):
    tempout = tempnumb%basenum
    if (tempout < 10):
        output = str(tempout) + output
    else:
        answer = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        output = answer[tempout]+ output
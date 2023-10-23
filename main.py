# eng2uz = {'mother': 'ona', 'father': 'ota', 'brother': 'aka-uka', 'sister': 'opa-singil'}
# print('mothers' in eng2uz)


# myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
myFinalMarks = dict()
module = input('Module')
mark = input('Mark')
myFinalMarks[module] = int(mark)
print(myFinalMarks)
def calculateAvr(finalMarks):
    total = 0
    for key in finalMarks:
        total = total+int(finalMarks[key])
    result = total/len(finalMarks)
    return result
print(calculateAvr(myFinalMarks))
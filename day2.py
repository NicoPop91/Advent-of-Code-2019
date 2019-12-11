import copy

originalArray = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,1,9,23,27,2,27,9,31,1,31,5,35,2,35,9,39,1,39,10,43,2,43,13,47,1,47,6,51,2,51,10,55,1,9,55,59,2,6,59,63,1,63,6,67,1,67,10,71,1,71,10,75,2,9,75,79,1,5,79,83,2,9,83,87,1,87,9,91,2,91,13,95,1,95,9,99,1,99,6,103,2,103,6,107,1,107,5,111,1,13,111,115,2,115,6,119,1,119,5,123,1,2,123,127,1,6,127,0,99,2,14,0,0]

def computer(iNoun, iVerb, iArray):
    inputArray = copy.deepcopy(iArray)
    inputArray[1] = iNoun
    inputArray[2] = iVerb
    counter = 0
    ergebnis = 0
    while True:
        if inputArray[counter] == 99:
            # print("Break!")
            break
        if inputArray[counter] == 1:
            # Addition
            inputArray[inputArray[counter+3]] = inputArray[inputArray[counter+1]] + inputArray[inputArray[counter+2]]
        if inputArray[counter] == 2:
            # Multiplikation
            inputArray[inputArray[counter+3]] = inputArray[inputArray[counter+1]] * inputArray[inputArray[counter+2]]
        counter = counter + 4
    # print(inputArray[0])
    if inputArray[0] == 19690720:
        ergebnis = 100 * noun + verb
        print("Korrektes Ergebnis für Aufgabe 2 gefunden: ")
        print(ergebnis)

#Aufgabe 1
computer(12,2,originalArray)

#Aufgabe 2
noun = -1
verb = -1
ergebnis = 0

while noun < 100:
    noun = noun + 1
    verb = 0
    while verb < 100:
        verb = verb + 1
        #print(noun)
        #print(verb)
        computer(noun, verb, originalArray)

        

        
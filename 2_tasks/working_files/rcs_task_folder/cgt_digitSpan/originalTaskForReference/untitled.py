digitsForTrial = [];


if digitSpan <= 9:
    while len(digitsForTrial) < digitSpan:
        singleNumber = random.choice(numbersToChoose)

        if digitsForTrial.count(singleNumber) < 1:
            digitsForTrial.append(singleNumber)        
elif digitSpan > 9:
    while len(digitsForTrial) <= 9:
        singleNumber = random.choice(numbersToChoose)
        
        if digitsForTrial.count(singleNumber) == 0:
            digitsForTrial.append(singleNumber)
    
    while len(digitsForTrial) > 9 and len(digitsForTrial) < digitSpan:
        singleNumber = random.choice(numbersToChoose)
         
        if digitsForTrial.count(singleNumber) < 2:
            digitsForTrial.append(singleNumber)

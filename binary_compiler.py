type = input("typ převádení z binární [1] nebo do binární [2] ")
text = input("Napiš číslo: ")
letters = []
complete_number = 0
if type == "1":
    if len(text) < 8:
        for letter in range(8 - len(text)):
            letters.append(letter)
        for letter in text:
            letter = int(letter)
            letters.append(letter)
    if len(text) == 8:
        for letter in text:
            letter = int(letter)
            letters.append(letter)
    complete_number += letters[0]*128
    complete_number += letters[1]*64
    complete_number += letters[2]*32
    complete_number += letters[3]*16
    complete_number += letters[4]*8
    complete_number += letters[5]*4
    complete_number += letters[6]*2
    complete_number += letters[7]*1
    print(complete_number)
else:
    text = int(text)
    if text > 256:
        print("Nemožné")
    else:
        if text > 128:
            letters.append(1)
            text -= 128
        else:
            letters.append(0)
        if text > 64:
            letters.append(1)
            text -= 64
        else:
            letters.append(0) 
        if text > 32:
            letters.append(1)
            text -= 32
        else:
            letters.append(0)      
        if text > 16:
            letters.append(1)
            text -= 16
        else:
            letters.append(0)
        if text > 8:
            letters.append(1)
            text -= 8
        else:
            letters.append(0)
        if text > 4:
            letters.append(1)
            text -= 4
        else:
            letters.append(0)
        if text > 2:
            letters.append(1)
            text -= 2
        else:
            letters.append(0)
        if text > 1:
            letters.append(1)
            text -= 1
        else:
            letters.append(0)

        s = ''.join(str(x) for x in letters)
        print(s)
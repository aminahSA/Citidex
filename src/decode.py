import re

def decode(message_file):
  
    Lines = message_file.readlines()
    Lines.sort(key=lambda x: x[0])
    numPrevLine = 0
    answer = ""

    while len(Lines) != 0:        
        answer = answer + re.sub(r'^\d+', '', Lines[numPrevLine].strip())

        numPrevLine += 1
        Lines = Lines[numPrevLine:]
    
    return answer.rstrip()


file = open("coding_qual_input.txt", "r")
print(decode(file))
print("finished")
from string import ascii_lowercase
file = open('new_plates.txt', "w")

for b in ascii_lowercase:
    for c in ascii_lowercase:
        for d in range(0, 9):
            for e in range(0, 9):
                for f in range(0, 9):
                    for g in range(0, 9):
                        print(b+c+str(d)+str(e)+str(f)+str(g))
                        file.write(b+c+str(d)+str(e)+str(f)+str(g)+'\n')

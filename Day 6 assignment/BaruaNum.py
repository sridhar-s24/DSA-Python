#GETTING BARUA INPUTS

valid = False
c0 = 0
decNo = 1
while valid == False :
    BL = [int(i) for i in input('Enter Barua numbers... ').split()]
    l = len(BL)
    s2 = 0
    dC = 0
    c1 = 0
    for i in range(l):
        c1 = str(BL[i]).count('1')
        if str(BL[i])[0] == '1':
            if (c1 > 1 or int(str(BL[i])[1]) > 1) and dC <= 1:
                dC += 1
                decNo = BL[i]
            if dC > 1:
                print('BREAKING...')
                valid = False
                break
            valid = True
            
        else:
            s2 += 1
            dC += 1
            if s2 > 1 or dC > 1:
                print ('BREAKING...')
                valid = False
                break
            else:
                decNo = BL[i]
                valid = True

for i in range(l):
    if (BL[i] == decNo):
        continue
    c0 += str(BL[i]).count('0')

print(str(decNo) + ('0' * c0))

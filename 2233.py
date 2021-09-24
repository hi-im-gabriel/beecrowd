r=int(input(),16)
g=int(input(),16)
b=int(input(),16)
while True:
    if r<g:
        print(1)
        break
    tot=pow((int(g/b)),2)
    if r==g:
        if g==b:
            print(3)
            break
        if g<b:
            print(2)
            break
        print(hex(tot+2).replace('0x',''))
        break
    tot2=pow((int(r/g)),2)
    if g<b:
        print(hex(tot2+1).replace('0x',''))
        break
    if g==b:
        print(hex(tot2*2+1).replace('0x',''))
        break
    tot3=int(tot*tot2+tot2+1)
    print(hex(tot3).replace('0x',''))
    break

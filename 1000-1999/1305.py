#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))

def get_int_frac_parts(string):
    if '.' not in string:
        return int(string), 0
    else:
        value = string.split('.')
        if value[0] == '':
            return 0, float('.'+value[1])
        elif value[1] == '':
            return int(value[0]), 0
        else:
            return int(value[0]), float('.'+value[1])


while True:
    try:
        num = input()
        cutoff = float(input())
        values = get_int_frac_parts(num)
        if values[1] >= cutoff:                        
            print(values[0]+1)            
        else:
            print(values[0])
    except EOFError:
        break

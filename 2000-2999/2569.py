s=input().split()
n1=str(s[0].replace('7','0'))
op=s[1]
n2=str(s[2].replace('7','0'))
res=str(int(n1)+int(n2)) if op=='+' else str(int(n1)*int(n2))
res=int(res.replace('7','0'))
print(res)

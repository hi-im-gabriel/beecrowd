am, rm, em = map(int,input().split())
av, rv, ev = map(int,input().split())
s = input()
tm,tv=(len(s) * em) + rm + (am * 2),(len(s) * ev) + rv + (av * 2)

if tm < tv:print('Matheus')
elif tv < tm:print('Vinicius')
elif tv == tm:print('Empate')

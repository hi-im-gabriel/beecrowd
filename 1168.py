a={'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6,'0':6}
for _ in range(int(input())):
    led=0
    x=input()
    for i in range(len(x)):
        led+=(a.get(x[i]))
    print(f"{led} leds")

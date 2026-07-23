#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def get_results(my_list):
    greater =  my_list[0]
    line = ''
    for i in range(len(my_list)):
        greater = my_list[i] if my_list[i] >= greater else greater
    for i in range(len(my_list)):
        if (my_list[i]==greater):
            line+=str(i+1)+' '
    return line.strip()

def complete_sc(my_list, n_pilots):
    for i in range(n_pilots - len(my_list) + 1):
        my_list.append(0)
    return my_list
    

def map_to_list(x):
    my_list = []
    for i in range(x):
        my_list.append(0)  
    return my_list  

abcdefgtasd=1
while(True):
    line = input()
    grand_prix = int(line.split()[0])
    pilots = int(line.split()[1])
    arrival_order = []
    scoring_systems = []    
    if not grand_prix and not pilots:
        break
    for i in range(grand_prix):
        arrival_order.append(list(map(int, input().split())))
    number_of_scoring_sys = int(input())
    for i in range(number_of_scoring_sys):
        scoring_systems.append(complete_sc(list(map(int, input().split())), pilots))    
    # Getting the results for each of the scoring systems
    for i in range(number_of_scoring_sys):
        scores = map_to_list(pilots)
        for j in range(grand_prix):
            for k in range(pilots):
                scores[k] += scoring_systems[i][1:][arrival_order[j][k]-1]                        
        print(get_results(scores))

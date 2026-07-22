while True:
    try:
        string=input().split('/',3)
        print("%s/%s/%s" % (string[1],string[0],string[2]))
        print("%s/%s/%s" % (string[2],string[1],string[0]))
        print("%s-%s-%s" % (string[0],string[1],string[2]))

    except EOFError:break

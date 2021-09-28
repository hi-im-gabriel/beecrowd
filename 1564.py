while True:
    try:
        if int(input())>0:print("vai ter duas!")
        else:print("vai ter copa!")
    except EOFError:break

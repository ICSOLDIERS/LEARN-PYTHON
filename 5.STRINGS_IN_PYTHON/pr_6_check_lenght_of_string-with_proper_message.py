while True:
    str=input("enter the string:")
    if str=="quit":
        break
    if len(str)<10:
        print("too small")
        continue
    print("input is off sufficient lenght")
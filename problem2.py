def reverseList(l):
    l.reverse()
    for i in l:
        if type(i) == list:
            reverseList(i)
    return l


m = eval(input("Enter a list"))

print(reverseList(m))
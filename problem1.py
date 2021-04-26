n = []


def flatList(l):

    for i in l:

        if type(i) == list:
            flatList(i)

        else:
            n.append(i)

    return n



print()

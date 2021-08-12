def expanding(l):
    d = 0
    test=False
    for i in range(len(l)-1):
        if abs(l[i+1]-l[i]) > d:
            d=abs(l[i+1]-l[i])
            test=True
        else:
            test=False
    return test

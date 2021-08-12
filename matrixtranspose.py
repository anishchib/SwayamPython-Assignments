def transpose(anArray):
    transposed = [None] * len(anArray[0])
    # print(transposed)
    # print(len(transposed))
    # print(len(anArray))

    for i in range(len(transposed)):
        # print(i)
        transposed[i] = [None] * len(anArray)
    # print(transposed)
    # print(len(anArray))
    for t in range(len(transposed)):
        for tt in range(len(anArray)):
            # print(t,tt,tt,t)
            transposed[t][tt] = anArray[tt][t]
    return transposed

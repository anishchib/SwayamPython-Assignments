def sumsquare(l):
    sume=sumo=0
    ll=[]
    for i in l:
        if i%2 == 0:
          sume=sume + i**2
        else:
          sumo=sumo + i**2
    ll.append(sumo)
    ll.append(sume)
# print(sume,sumo)
    return ll

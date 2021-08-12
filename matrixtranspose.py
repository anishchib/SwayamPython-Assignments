def matrixTranspose(anArray):
  transposed = [None]*len(anArray[0])

  for i in range(len(transposed)):
    transposed[i] = [None]*len(transposed)

  for t in range(len(anArray)):
    for tt in range(len(anArray[t])):
        transposed[t][tt] = anArray[tt][t]
  return transposed

theArray = [['a','b','c'],['d','e','f'],['g','h','i']]

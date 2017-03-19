import array
import numpy as np
import scipy.cluster.hierarchy as hac

proteinFile = open('/home/lmt72/PDBbind2017/TinySet')
distances = []
a = []
for protein in proteinFile:
    protein = protein.strip()
    filename = "/home/lmt72/PDBdistances/"+protein+".distances"
    distanceFile = open(filename)
    for line in distanceFile:
        data= line.split()
        secondProtein = data[0]
        distance = data[1].strip()
        distances.append(distance)
    a.append(distances)
    distances=[]
npArray = np.array(a)
np.set_printoptions(threshold=np.inf,precision=2)
print npArray
npArray = hac.average(npArray)
print npArray

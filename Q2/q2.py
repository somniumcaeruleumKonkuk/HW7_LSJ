#q2.py

import numpy as np

def q2():
    Docs = np.array([[1,1,0,1,0,1],
                     [1,1,1,0,1,0],
                     [1,1,0,1,0,0]])
    
    Query = np.array([1,1,0,0,1,0])

    for i in range(3):
        result = np.cos(np.dot(Docs[i], Query) / (np.linalg.norm(Docs[i]) * np.linalg.norm(Query)))
        print("doc"+str(i+1)+"={0:s}\n".format(str(result)[:4]))

if __name__ == "__main__":
    q2()
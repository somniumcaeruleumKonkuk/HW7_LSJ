import numpy as np

def q1():
    arr = np.array([[1,2],[3,4]])
    eigenvalue, eigenvector = np.linalg.eig(arr)

    print("Eigenvalues:",(eigenvalue))
    print()
    print("Eigenvectors:",(eigenvector))
    print()

    determinant = np.linalg.det(arr)
    
    print("Determinant:",(determinant))

    print()

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])

    cross_product = np.cross(vec1, vec2)

    print("Cross product:",(cross_product))
    print()

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([[-15],[-21],[18]])
    
    solution = np.linalg.solve(A, b)
    
    print("Solution:",(solution))

if __name__ == '__main__':
    q1()

#q3.py

import pandas as pd
import numpy as np

def q3():
    val_list = [[1000, 25],
                [280, 120],
                [900, 30]]
    values = np.array(val_list)

    df1 = pd.DataFrame(values, index=['store1', 'store2', 'store3'], columns = ['unit price', 'number'])
    print(df1)
    print()

    for i in range(3):
        val_list[i] += [val_list[i][0] * val_list[i][1]]
    
    values = np.array(val_list)

    df2 = pd.DataFrame(values, index=['store1', 'store2', 'store3'], columns = ['unit price', 'number', 'total price'])
    print(df2)
    print()

    df3 = df2.sort_values(by="total price", ascending=False)
    print(df3.head(2))

if __name__ == "__main__":
    q3()
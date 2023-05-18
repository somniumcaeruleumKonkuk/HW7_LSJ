#q4.py 

import pandas as pd

def q4():
    f = pd.read_csv("gender2.csv", encoding='utf-8')
    df = pd.DataFrame(f)

    #1, 6, 11
    df1 = df.loc[:, ['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수']]

    df1 = df1.rename(columns={'2022년_계_총인구수': 'Total', '2022년_남_총인구수': 'Male', '2022년_여_총인구수': 'Female'})
    print(df1)

if __name__ == "__main__":
    q4()
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def similarity(): # produce csv that shows num of same url prsent in each user
                  # comparing to current single url
    df = pd.read_csv('user behaviours.csv')

    tot_row = len(df)
    pivot = 0
    comp = pivot + 1
    while pivot < tot_row:
        print(f'user{pivot}----')
        same = 0
        datalist = [df['User_Id'][pivot]]

        complist = list(df.iloc[comp].values)[2:16]
        for url in df.iloc[pivot, 2:16].values:
            if url != "nan":
                same = complist.count(url)
                datalist.append(same)
        with open("heatmap data.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(datalist)

        pivot += 1
    print("all similarity matrix found")


def build_heatmap():
    df = pd.read_csv('user behaviours.csv')
    col = [df.columns[0]]
    for i in df.columns[2:16]:
        col.append(i)

    df2 = pd.read_csv("heatmap data.csv", names= col, header=None)
    '''
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df2, center=0, cmap='Blues')
    ax.set_title('user behaviour similarity')
    plt.show()
    '''
    df_corr = df2.corr()
    np.ones_like(df_corr, dtype=np.bool)
    fig, ax = plt.subplots(figsize=(10, 8))
    # mask
    mask = np.triu(np.ones_like(df_corr, dtype=np.bool))
    # adjust mask and df
    mask = mask[1:, :-1]
    corr = df_corr.iloc[1:, :-1].copy()
    # plot heatmap
    sb.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='Blues',
               vmin=-1, vmax=1, cbar_kws={"shrink": .8})
    # yticks
    plt.yticks(rotation=0)
    plt.show()

def __main__():
    similarity()
    build_heatmap()

__main__()
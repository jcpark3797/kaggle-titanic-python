import numpy as np
import pandas as pd
import os
import seaborn as sns
import analyze

if __name__ == "__main__":
    links = ['./input/train.csv', './input/test.csv', './input/gender_submission.csv']
    print(links)

    print('-'*20)
    train_data = pd.read_csv(links[0])
    test_data = pd.read_csv(links[1])
    print('> check train data null values')
    print(train_data.isnull().sum())
    print('> check test data null values')
    print(test_data.isnull().sum())
    print('-'*20)


    name_dic = {}
    name_cate = list(map(lambda x:x,set(train_data['Name'].str.extract('([A-Za-z]+\\.).')[0].tolist())))
    for num in range(len(name_cate)):
        name_dic[name_cate[num]] = num

    print('name_dic =', name_dic)
    print('-'*20)

    analyze.check_servived_table(train_data) # analyze.py


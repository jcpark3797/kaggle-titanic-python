import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import analyze


if __name__ == "__main__":
    # Load Dataset
    links = ['./input/train.csv', './input/test.csv', './input/gender_submission.csv']
    print(links)

    # Analyze Data
    """
        train_data: Cabin > Age > Embarked(승선항)에 null 값이 존재한다.
        test_data: Cabin > Age > Fare(1건)에 null 값이 존재한다.
    """

    print('-'*20)
    train_data = pd.read_csv(links[0])
    test_data = pd.read_csv(links[1])
    print('> check train data null values')
    print(train_data.info())
    #print(train_data.isnull().sum())
    print('> check test data null values')
    print(test_data.info())
    #print(test_data.isnull().sum())
    print('-'*20)
    print(train_data.describe())
    print('-'*20)
    print(train_data.describe(include=['O']))
    print('-'*20)


    name_dic = {}
    name_cate = list(map(lambda x:x,set(train_data['Name'].str.extract('([A-Za-z]+\\.).')[0].tolist())))
    for num in range(len(name_cate)):
        name_dic[name_cate[num]] = num

    print('name_dic =', name_dic)
    print('-'*20)

    #analyze.print_survived_info_table(train_data) # analyze.py
    """
        age.png
        본 그래프를 통해 아래와 같은 사실을 얻게 되었다.
        1) 유아는 생존율 높음 (4이하)
        2) 80세 생존
        3) 15-35? 대부분 생존하지 못함
    """
    g = sns.FacetGrid(train_data, col='Survived')
    g.map(plt.hist, 'Age', bins=20)
    # g.savefig('test.png') or plt.show()

    grid = sns.FacetGrid(train_data, col='Survived', row='Pclass', size=2.2, aspect=1.6)
    grid.map(plt.hist, 'Age', alpha=.5, bins=20)
    grid.add_legend()
    # grid.savefig('Pclass.png') or plt.show()

    # study https://www.kaggle.com/startupsci/titanic-data-science-solutions
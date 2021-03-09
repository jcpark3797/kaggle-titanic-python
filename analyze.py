


def check_servived_table(train_data):
    print(train_data[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)) #t_pclass 티켓등급
    print('-'*20)
    print(train_data[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)) # t_sex 성별
    print('-'*20)
    print(train_data[['SibSp', 'Survived']].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False)) # t_sibsp 형재,자매/배우자
    print('-'*20)
    print(train_data[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False)) # t_parch 부모/자녀
    print('-'*20)
    print(train_data[["Embarked", "Survived"]].groupby(['Embarked'], as_index=False).mean().sort_values(by='Survived', ascending=False)) # t_embarked 승선항(C,Q,S)
    print('-'*20)
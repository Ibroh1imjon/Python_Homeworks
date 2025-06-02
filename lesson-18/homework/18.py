#Homework 2
import pandas as pd

df = pd.read_csv('task\\stackoverflow_qa.csv')
df['creationdate'] = pd.to_datetime(df['creationdate'])

# 1. 2014-yildan oldin yaratilgan savollar
df_before_2014 = df[df['creationdate'] < '2014-01-01']

# 2. Balli 50 dan katta bo‘lgan savollar
df_score_above_50 = df[df['score'] > 50]

# 3. Balli 50 dan 100 gacha bo‘lgan savollar
df_score_between_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. Scott Boston javob bergan savollar
df_answered_by_scott = df[df['ans_name'] == 'Scott Boston']

# 5. Quyidagi 5 foydalanuvchi javob bergan savollar
users = ['Scott Boston', 'unutbu', 'jezrael', 'DSM', 'Warren Weckesser']
df_answered_by_5 = df[df['ans_name'].isin(users)]

# 6. 2014-yil mart va oktyabr oralig‘ida, unutbu javob bergan va balli 5 dan kichik savollar
df_filtered = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]

# 7. Balli 5 va 10 oralig‘ida yoki ko‘rishlar soni 10,000 dan katta bo‘lgan savollar
df_score_or_views = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)
]

# 8. Scott Boston javob bermagan savollar
df_not_by_scott = df[df['ans_name'] != 'Scott Boston']


#Homework 3
import pandas as pd

titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]

# 2. Filter Passengers Who Paid More than $100
fare_over_100 = titanic_df[titanic_df['Fare'] > 100]

# 3. Select Passengers Who Survived and Were Alone
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# 5. Select Passengers with Siblings or Spouses and Parents or Children
with_family = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
under15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# 7. Select Passengers with Cabins and Fare Greater Than $200
cabin_fare_200 = titanic_df[
    titanic_df['Cabin'].notna() &
    (titanic_df['Fare'] > 200)
]

# 8. Filter Passengers with Odd-Numbered Passenger IDs
odd_passenger_id = titanic_df[titanic_df['PassengerId'] % 2 != 0]

# 9. Select Passengers with Unique Ticket Numbers
ticket_counts = titanic_df['Ticket'].value_counts()
unique_ticket_passengers = titanic_df[titanic_df['Ticket'].isin(ticket_counts[ticket_counts == 1].index)]

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == 'female')
]


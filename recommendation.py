import pandas as pd
import numpy as np

d1 = pd.read_csv("drive/My Drive/collabrative filtering/movies.csv")
d2 = pd.read_csv("drive/My Drive/collabrative filtering/ratings.csv")

df = pd.merge(d1,d2).drop(['genres','timestamp'],axis = 1)

#print(df.head())


df1 = df.pivot_table(index=['userId'],columns=['title'],values='rating')
#rint(df1.head())

userdf = df1.dropna(thresh=10,axis=1).fillna(0)
#print(userdf.head())


similarity = userdf.corr(method='pearson')
#print(similarity.head())

#print('Movies Available are: ',d1['title'])

def get_similar_movies(movies,ratings):
  similar = similarity[movies]*(rating)
  similar = similar.sort_values(ascending = False)[1:10]
  return similar



movv= input("Enter the Movie you have watched")
ratng = input("Enter your Rating: ")

z = get_similar_movies(movv,ratng)

print(z)

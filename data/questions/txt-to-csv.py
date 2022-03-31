import pandas as pd


# dataframe from text with delimiter
account = pd.read_csv("projectpro.txt",
                      delimiter='/')

# store dataframe into csv file
account.to_csv('projectpro.csv',
               index=None)

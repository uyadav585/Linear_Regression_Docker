import pandas 
ds = pandas.read_csv('salaryDataSet.csv')
x = ds['YearsExperience'].values.reshape(30,1)
y = ds['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x , y)
exp = float(input("enter your year of experience - "))
predicted_value = model.predict([[exp]])
print("As per your {} year experience you may get upto {} INR".format(exp,predicted_value[0]))

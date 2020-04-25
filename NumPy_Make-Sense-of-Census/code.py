# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
#The path to the data set has been stored in the variable named path
#Load the dataset and store it in a variable called data using np.genfromtxt()
#The parameter 'delimiter="," ' is set because the file that we are opening has extension CSV(Comma Separated Values)
#The parameter 'skip_header=1' is set because the first row of the data(which is called header) contains string values but in our numpy array we need only integers(Remember numpy array can only store data of a single data type)

data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#Append 'new_record' (given) to 'data' using "np.concatenate()" and store the new array in a variable called census
census = np.concatenate((data,new_record))
print(census.shape)

#We often associate the potential of a country based on the age distribution of the people residing there. We too want to do a simple analysis of the age distribution
#Create a new array called 'age' by taking only age column(age is the column with index 0) of 'census' array.
#Find the max age and store it in a variable called 'max_age'.
#Find the min age and store it in a variable called 'min_age'.
#Find the mean of the age and store it in a variable called 'age_mean'.
#Find the standard deviation of the age and store it in a variable called 'age_std'.

age = census[:,0]
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = age.mean()
print(age_mean)
age_std = np.std(age)
print(age_std)

#The constitution of the country tries it's best to ensure that people of all races are able to live harmoniously. Let's check the country's race distribution to identify the minorities so that the government can help them.

#Create four different arrays by subsetting 'census' array by Race column(Race is the column with index 2) and save them in 'race_0','race_1', 'race_2', 'race_3' and 'race_4' respectively(Meaning: Store the array where 'race'column has value 0 in 'race_0', so on and so forth)
#Store the length of the above created arrays in 'len_0', 'len_1','len_2', 'len_3' and 'len_4' respectively
#Find out which is the race with the minimum no. of citizens
#Store the number associated with the minority race in a variable called 'minority_race'(For eg: if "len(race_5)" is the minimum, store 5 in 'minority_race' because that is the index of the race having the least no. of citizens )

race_0 = census[census[:,2]==0]
len_0 = len(race_0)
print(len_0)
 
race_1 = census[census[:,2]==1]
#print(race_1)
len_1 = len(race_1)
print(len_1)
 
race_2 = census[census[:,2]==2]
#print(race_2)
len_2 = len(race_2)
print(len_2)
 
race_3 = census[census[:,2]==3]
len_3 = len(race_3)
print(len_3)
 
race_4 = census[census[:,2]==4]
len_4 = len(race_4)
print(len_4)
 
len_race = [len_0,len_1,len_2,len_3,len_4]
print(len_race)
 
#np.argmin() gives index of min element in array
minority_race = np.argmin(len_race)
print(minority_race)


#As per the new govt. policy, all citizens above age 60 should not be made to work more than 25 hours per week. Let us look at the data and see if that policy is followed.
#Create a new subset array called 'senior_citizens' by filtering 'census' according to age>60 (age is the column with index 0)
#Add all the working hours(working hours is the column with index 6) of 'senior_citizens' and store it in a variable called 'working_hours_sum'
#Find the length of 'senior_citizens' and store it in a variable called 'senior_citizens_len'

senior_citizens = census[census[:,0]>60]

working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum /senior_citizens_len
print(avg_working_hours)


#Our parents have repeatedly told us that we need to study well in order to get a good(read: higher-paying) job. Let's see whether the higher educated people have better pay in general.
#Create two new subset arrays called 'high' and 'low' by filtering 'census' according to education-num>10 and education-num<=10 (education-num is the column with index 1) respectively.
#Find the mean of income column(income is the column with index 7) of 'high' array and store it in 'avg_pay_high'. Do the same for 'low' array and store it's mean in 'avg_pay_low'.

high = census[census[:,1]>10]

low = census[census[:,1]<=10]

avg_pay_high = high.mean(axis=0)[7]
print(avg_pay_high)

avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_low)
 



# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder



#Task 1  Loading the data
data=pd.read_csv(path)
#Code starts here
#Subset the dataframe 'data' such that it only contains rows where Rating is less than or equal to 5. 
#Plot a histogram of Rating column again to see the distribution of app ratings
data.plot(kind = "hist", bins = 25)
#sns.distplot(data.Rating)
plt.xlim(0,8)

#Subset the dataframe 'data' such that it only contains rows where Rating is less than or equal to 5. 
#Plot a histogram of Rating column again to see the distribution of app ratings
data = data[data["Rating"]<=5]
sns.distplot(data.Rating)
plt.xlim(0,8)
print(data.shape)


#Check for the Null values. Treat them if any. There should be no null values left in the data.
data.isnull().sum()
data.dropna(inplace = True)
data.isnull().sum()


#Task 2 - Null Value Treatment
# code starts here
#Check for the Null values. Treat them if any. There should be no null values left in the data.
#Check for the Null values. Treat them if any. There should be no null values left in the data.
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
percent_null

missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis =1)
missing_data

data.dropna(inplace = True)

total_null_1 = data.isnull().sum()
percent_null_1 = (total_null/data.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1], keys=['Total','Percent'], axis =1)
missing_data_1
# code ends here

#Task 3 - Category vs Rating

#Code starts here



box = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
plt.title("Rating vs Category [BoxPlot]")
plt.xlabel("Category",rotation=45,horizontalalignment='right')

#Task 4 - Installs vs Ratings
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data["Installs"].value_counts()

data["Installs"] = data["Installs"].str.replace(',', '')
data["Installs"] = data["Installs"].str.replace('+', '')
data["Installs"] = data["Installs"].astype(int)
#data.head()


# Initialize Encoder
le = LabelEncoder()

# Fit-transform on data
data['Installs'] = le.fit_transform(data['Installs'])
data.head()

sns.regplot(x="Installs", y="Rating",data=data)
plt.title("Rating vs Installs [RegPlot]")
#Code ends here


#Task 5 -  Price vs Ratings
#Code starts here

data["Price"].value_counts()


data["Price"] = data["Price"].apply(lambda x: x.strip('$'))

data["Price"] = data["Price"].astype(float)

sns.regplot(x="Price", y="Rating",data=data)
plt.title("Rating vs Price [RegPlot]")
#Code ends here

#Task 6 - Genre vs Rating

#Code starts here

data["Genres"].unique()

data["Genres"].nunique()

data['Genres'] = data['Genres'].str.split(';', 1).str[0]
data.head()

#Group Genres and Rating by Genres pass as_index=False and store its mean in a variable called 'gr_mean'
gr_mean = data.groupby(["Genres"],as_index=False)["Rating"].mean()

#Print the statistics of 'gr_mean' using describe()" function
gr_mean.describe()
#Sort the values of 'gr_mean' by Rating using "sort_values()" function and save it back to 'gr_mean'
gr_mean = gr_mean.sort_values(by = "Rating")
#Code ends here



#Task 7 - Last Updated vs Rating
#Code starts here
#Print and visualize the values of Last Updated column of 'data'
data["Last Updated"].value_counts()
#data["Last Updated"].hist()

#Last Updated is not of the date type.
#Convert Last Updated to DateTime format
data["Last Updated"]= pd.to_datetime(data["Last Updated"])

#Find out the max value in Last Updated column and save it a variable called 'max_date'
max_date = data["Last Updated"].max()
max_date

#Create new column Last Updated Days which is the difference between max_date and values of column Last Updated in days using "dt.days" function
#data["Last Updated Days"] = max_date - data["Last Updated"]
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days 
data["Last Updated Days"]

#Using seaborn, plot the regplot where x="Last Updated Days", y="Rating", data=data
sns.regplot(x="Last Updated Days", y="Rating",data=data)

#Title the plot as Rating vs Last Updated [RegPlot]
plt.title("Rating vs Last Updated [RegPlot]")

#Code ends here















# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Step 1
#Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.The path for the dataset has been stored in a variable pathCreate dataframe bank by passing the path of the fileCreate the variable 'categorical_var' and using 'df.select_dtypes(include = 'object')' check all categorical values.print 'categorical_var'Create the variable 'numerical_var' and using 'df.select_dtypes(include = 'number')' check all categorical values.print 'numerical_var'
#Test Cases
#categorical_var.shape shoule be (614, 8) and numerical_var.shape should be (614, 5).

#Code starts here
#Create dataframe bank by passing the path of the file
bank = pd.DataFrame(bank_data)
#print(list(bank.columns.values))


categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
#print(list(categorical_var.columns.values))


numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)
#print(list(numerical_var.columns.values))


#Step 2
#Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.From the dataframe bank, drop the column Loan_ID to create a new dataframe banksTo see the null values, use "isnull().sum()" function and print it.Calculate mode for the dataframe banks and store in bank_mode.Fill missing(NaN) values of banks with bank_mode and store the cleaned dataframe back in banks.Check if all the missing values (NaN) are filled.
#Test Cases
#banks.shape should be (614 , 12) and banks.isnull().sum().values.sum() should be 0.


#banks = bank.drop(['Loan_ID'],inplace = True, axis=1) #Alternative
banks = bank.drop(columns='Loan_ID')
print(banks.head())

print(banks.isnull().sum())

#bank_mode = banks.mode()  #Wrong All nan values in fillna() are not filled by this. 
bank_mode = banks.mode().iloc[0]  #Alternative
print(bank_mode)

banks.fillna(bank_mode,inplace = True)
print(banks.head())

#Step 3
#Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.We will use previously created dataframe banks for this task.Generate a pivot table with index as 'Gender', 'Married', 'Self_Employed' and values as 'LoanAmount', using mean aggregation.Store the result in a variable called 'avg_loan_amount'
#Test Cases
#Print and check avg_loan_amount['LoanAmount'][1],2 should be 125.27.

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values = 'LoanAmount',aggfunc = 'mean')

print(avg_loan_amount)
print(avg_loan_amount['LoanAmount'][1],2)
# code ends here


#Step 4
#Now let's check the percentage of loan approved based on a person's employment type.We will use the previously created dataframe banks for this task.Create variable 'loan_approved_se' and store the count of results where Self_Employed == Yes and Loan_Status == Y.Create variable 'loan_approved_nse' and store the count of results where Self_Employed == No and Loan_Status == Y.Loan_Status count is given as 614.Calculate the percentage of loan approval for self-employed people and store result in variable 'percentage_se'.Calculate the percentage of loan approval for people who are not self-employed and store the result in variable 'percentage_nse'.
#Test Cases
#percentage_se, rounded off to two places, should be 9.12.
#percentage_nse, rounded off to two places, should be 59.61.

loan_approved_se = banks[(banks['Loan_Status']== 'Y') & (banks['Self_Employed']== 'Yes')]['Loan_Status'].value_counts()  
print(loan_approved_se)

loan_approved_nse = banks[(banks['Loan_Status']== 'Y') & (banks['Self_Employed']== 'No')]['Loan_Status'].value_counts()
print(loan_approved_nse)

type(loan_approved_nse)

percentage_se = (loan_approved_se/614)*100
percentage_se=round(percentage_se[0],2) 
round(percentage_se,2)
print("Approved", percentage_se)

percentage_nse = (loan_approved_nse/614)*100
percentage_nse=round(percentage_nse[0],2) 
print("Not Approved",percentage_nse)




#Step 5
#A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.Use "apply()" function to convert Loan_Amount_Term which is in months to a year and store the result in a variable 'loan_term'.Find the number of applicants having loan amount term greater than or equal to 25 years and store them in a variable called 'big_loan_term'.
#Test Cases:
#big_loan_term should be 554.

# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
print(loan_term)

big_loan_term = len(loan_term.loc[loan_term>=25])

print(big_loan_term)

# code ends here


#Step 6
#Now let's check the average income of an applicant and the average loan given to a person based on their income.Groupby the 'banks' dataframe by Loan_Status and store the result in a variable called 'loan_groupby'Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History'] and store the subsetted dataframe back in 'loan_groupby'Then find the mean of 'loan_groupby' and store the result in a new variable 'mean_values'
#Test Cases: Print and check mean_values.iloc[1,0], 2 should be 5384.07 when rounded off to two palces.

# code starts here
loan_groupby = banks.groupby(['Loan_Status'])

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here




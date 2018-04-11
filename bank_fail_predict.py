import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bank = pd.read_csv(r"C:\Users\63257\Desktop\Designing_Smart_System\Bank failure data.csv")


# # HW3-Q1
# return the row with "Size" field has the maxium value
bank_2009end = bank[bank["Quarter_DT"] == "10/1/2009"]
max_id = bank_2009end["Size"].idxmax()
print(bank_2009end.loc[max_id])



# # HW3-Q2
# plot a line chart showing "Mean Net Chargeoffs of All Banks From 2007Q4 - 2010Q1"
bank_nco = bank.loc[:,["Bank Name","Quarter","Net Chargeoffs"]]
np_time = bank_nco.Quarter.unique() # create a list of unique values in column "Quarter"
means = []
for i in np_time:
    group = bank_nco[bank_nco["Quarter"] == i]
    mean = group["Net Chargeoffs"].mean()
    mean = float(format(mean, '.4f')) # round to 4 decimal points
    means.append(mean)
plt.plot(np_time,means)
plt.xlabel("Time")
plt.ylabel("Net Chargeoffs")
plt.title("Mean Net Chargeoffs of All Banks From 2007Q4 - 2010Q1")
# display y values beside each point on the plot
for i,j in zip(np_time,means):
    plt.text(i, j, str(j))
plt.show()
plt.clf() # Clear the figure
# make a scatter plot of all points
plt.scatter(bank_nco["Quarter"],bank_nco["Net Chargeoffs"])
plt.xlabel("Time")
plt.ylabel("Net Chargeoffs")
plt.title("Scatter Plot of Net Chargeoffs of All Banks From 2007Q4 - 2010Q1")
plt.show()



# # HW3-Q3
# calculate correlation between "Securities" column and "Fail_label"
print("The correlation between 'Security' and Bank Failure is: " + str(bank["Securities"].corr(bank["Fail_label"])))



# # HW3-Q5

# create 2 new csv files "Bank_r.csv" and "Bank_f.csv"
bank_remain = bank[bank["Failed during 2010Q2"] == "No"]
bank_failed = bank[bank["Failed during 2010Q2"] == "Yes"]
bank_remain.to_csv(r"C:\Users\63257\Desktop\Designing_Smart_System\Bank_r.csv")
bank_failed.to_csv(r"C:\Users\63257\Desktop\Designing_Smart_System\Bank_f.csv")

# fill in a csv file(q5.csv) with each bank's latest information for q5 analysis
bank_r = pd.read_csv(r"C:\Users\63257\Desktop\Designing_Smart_System\Bank_r.csv")
each_bank = bank_r.Bank_Name.unique()
for i in each_bank:
    bank_info = bank_r[bank_r["Bank_Name"] == i]
    quarters = bank_info.Quarter_DT.unique()
    latest_date = quarters[-1]
    row = bank_info[bank_info["Quarter_DT"] == latest_date]
    row.to_csv(r"C:\Users\63257\Desktop\Designing_Smart_System\q5.csv", mode='a', header=False)

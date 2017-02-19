# DisplaySortedData
python module that reads data from csv, sorts them and displays results on browser

The repository contains a data.csv file which contains three employee attributes, each one in a separate column : Name, Age, Salary.
It also contains a python module display_sorted.py
When you run display_sorted.py it executes the following:
1. Reads the csv file with pandas
2. Sorts the data by column in ascending order, separately for each column
3. Allows to view the three different sorted tables on web browser, in the following urls:
  http:/localhost:8080/name/
  http:/localhost:8080/age/
  http:/localhost:8080/salary/

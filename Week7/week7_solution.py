Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products.


import csv
import pandas as pd

h=['prod_no','prod_name',' jan',' feb',' mar','apr','may','jun']
l=[]
for i in range(12):
    prod_no=int(input("Enter product number :"))
    prod_name=input("Enter product name :")
    jan=int(input("Enter the sells of january month :"))
    feb=int(input("Enter the sells of febuary month :"))
    mar=int(input("Enter the sells of march month :"))
    apr=int(input("Enter the sells of apr month :"))
    may=int(input("Enter the sells of may month :"))
    jun=int(input("Enter the sells of june month :"))
    t=(prod_no,prod_name,jan,feb,mar,apr,may,jun)
    l.append(t)

Enter product number : 1
Enter product name : tshirt
Enter the sells of january month : 2000
Enter the sells of febuary month : 2500
Enter the sells of march month : 2100
Enter the sells of apr month : 1100
Enter the sells of may month : 2000
Enter the sells of june month : 1300
Enter product number : 2
Enter product name : pent
Enter the sells of january month : 4000
Enter the sells of febuary month : 3300
Enter the sells of march month : 4300
Enter the sells of apr month : 2400
Enter the sells of may month : 3200
Enter the sells of june month : 2100
Enter product number : 3
Enter product name : socks
Enter the sells of january month : 1100
Enter the sells of febuary month : 2100
Enter the sells of march month : 800
Enter the sells of apr month : 1200
Enter the sells of may month : 1800
Enter the sells of june month : 1450
Enter product number : 4
Enter product name : shirt
Enter the sells of january month : 3000
Enter the sells of febuary month : 4500
Enter the sells of march month : 2050
Enter the sells of apr month : 3400
Enter the sells of may month : 2300
Enter the sells of june month : 4500
Enter product number : 5
Enter product name : hancky
Enter the sells of january month : 1000
Enter the sells of febuary month : 800
Enter the sells of march month : 1400
Enter the sells of apr month : 2300
Enter the sells of may month : 1200
Enter the sells of june month : 2300
Enter product number : 6
Enter product name : dress
Enter the sells of january month : 4500
Enter the sells of febuary month : 5000
Enter the sells of march month : 3400
Enter the sells of apr month : 2300
Enter the sells of may month : 5000
Enter the sells of june month : 4500
Enter product number : 7
Enter product name : kurti
Enter the sells of january month : 2300
Enter the sells of febuary month : 5000
Enter the sells of march month : 4500
Enter the sells of apr month : 3400
Enter the sells of may month : 4600
Enter the sells of june month : 4500
Enter product number : 8
Enter product name : choli
Enter the sells of january month : 6000
Enter the sells of febuary month : 7000
Enter the sells of march month : 5800
Enter the sells of apr month : 7050
Enter the sells of may month : 7800
Enter the sells of june month : 9000
Enter product number : 9
Enter product name : sadi
Enter the sells of january month : 4000
Enter the sells of febuary month : 5600
Enter the sells of march month : 4500
Enter the sells of apr month : 3400
Enter the sells of may month : 4000
Enter the sells of june month : 3400
Enter product number : 10
Enter product name : nightdress
Enter the sells of january month : 3000
Enter the sells of febuary month : 4000
Enter the sells of march month : 2300
Enter the sells of apr month : 4000
Enter the sells of may month : 3400
Enter the sells of june month : 3500
Enter product number : 11
Enter product name : googles
Enter the sells of january month : 3000
Enter the sells of febuary month : 2300
Enter the sells of march month : 4500
Enter the sells of apr month : 3400
Enter the sells of may month : 2300
Enter the sells of june month : 4500
Enter product number : 12
Enter product name : shoes
Enter the sells of january month : 3000
Enter the sells of febuary month : 3400
Enter the sells of march month : 3500
Enter the sells of apr month : 4500
Enter the sells of may month : 3000
Enter the sells of june month : 2300

Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products.
-->
	import csv
	with open('C:\\22bca62\\python\\product.csv','w',newline='')as f:
                 obj=csv.writer(f)
                 obj.writerow(h)
                 obj.writerows(l)

Perform following operations.

1. Add 12 Records. Take input from user.
2. Create dataframe.
-->
	import pandas as pd
	df=pd.read_csv('C:\\22bca62\\python\\product.csv')
	df
	
3. Change Column Name Product No, Product Name, January, February, March, April, May, June.
-->
	df.columns = ["Product No", "Product Name", "January", "February", "March", "April", "May", "June"]

4. Add column "Total Sell" to count total of all month and "Average Sell"
-->
	df["Total Sell"] = df.iloc[:, 2:].sum(axis=1)
	df["Average Sell"] = df.iloc[:, 2:8].mean(axis=1)

5. Add 2 row at the end.
-->
	df = df.append({"Product No": "13", "Product Name": "abc", "January": 100, "February": 200, "March": 300,
                "April": 400, "May": 500, "June": 600, "Total Sell": 2100, "Average Sell": 350}, ignore_index=True)
	df = df.append({"Product No": "14", "Product Name": "def", "January": 700, "February": 800, "March": 900,
                "April": 1000, "May": 1100, "June": 1200, "Total Sell": 5700, "Average Sell": 950}, ignore_index=True)

6. Add 2 row after 3rd row.
-->
	row3 = pd.Series(["08", "ghi", 50, 60, 70, 80, 90, 100, 500, 75],
                 index=["Product No", "Product Name", "January", "February", "March", "April", "May", "June",
                        "Total Sell", "Average Sell"])
	df = pd.concat([df.iloc[:3], row3, df.iloc[3:]]).reset_index(drop=True)

7. Print first 5 row.
-->
	df.head()
8. Print Last 5 row.
-->
	df.tail()

9. Print row 6 to 10.
-->
	df.iloc[5:10]
	
10. Print only product name.
-->
	df["Product Name"]

11. Print sell of January month with product id and product name.
-->
	df[["Product No", "Product Name", "January"]]

12. Print only those product id , product name where january sell is > 5000 and February sell is >8000
-->
	print(df[(df["January"] > 5000) & (df["February"] > 8000)][["Product No", "Product Name"]])

13. Print record in sorting order of Product name.
-->
	df.sort_values("Product Name")

14. Display only odd index number column record.
-->
	df.iloc[:,1::2]

15. Display alternate row.
-->
	df.iloc[::2]


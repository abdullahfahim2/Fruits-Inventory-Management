import csv
f = open("inventoryfruits.csv","w+",newline="")
w = csv.writer(f)
header = ['Fruits Name','Unit Price','Quantity','Total Price']
w.writerow(header)
data = []
while True:
    try:
        n = int(input("How many Item You want to insert? "))
    except ValueError:
        print("Fruits Record are Number.Please Enter Correctly!")
        continue
    else:
        break
for i in range(n):
    print("Enter Fruit Record:",i+1)
    fruitsname = input("Enter Fruits Name: ")
    while True:
        try:
            unitprice = float(input("Enter Unit Price: "))
        except ValueError:
            print("Invalid Unit Price.Please Enter a Correct Price!")
            continue
        else:
            break
    while True:
        try:
            Quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Invalid Quantity.Please Enter Again!")
            continue
        else:
            break
    totalprice = unitprice * Quantity
    rec = [fruitsname,unitprice,Quantity,totalprice]
    data.append(rec)
w.writerows(data)
f.close()

print("Print Fruits items Summary Data From Stored CSV File!")
fh = open("inventoryfruits.csv","r")
r = csv.reader(fh)
for i in r:
    print(i)
fh.close()
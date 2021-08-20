import csv
rows = []
fields = []
with open('tables/MOTable.csv','r') as csvfile:
    csvreader= csv.reader(csvfile)
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
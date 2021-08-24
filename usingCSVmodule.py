import csv
def write():
    p = open("example.csv",'w')
    w = csv.writer(p)
    title= ["Name","Class","Roll"]
    details= ["Sarthak","11","25"]
    w.writerows(title)
    w.writerows(details)
    for i in details:
        w.writerows(i)
    p.close
write()

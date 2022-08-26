import csv
import pandas as pd


#with open('makes.csv','r') as csv_file:
#    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
#
with open('newoutput.csv', 'w') as new_file:
#        fieldnames = ['yearStart','yearEnd','make','model']
#
#        csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore',delimiter='\t')
#
#        csv_writer.writeheader()
#
#        count = 0

#You can also get fieldnames from the DictReader object as csv_reader.fieldnames so you don't have to hardcode it.
        

        #for line in csv_reader:
        #    count += 1
        #    del line['yearStart']
        #    del line['yearEnd']
        #    del line['model']
        #    csv_writer.writerow(line)   
        # df  = pd.read_csv(...)
    #csv_writer=df.to_csv(new_file.csv')
    df= pd.read_csv('makes.csv')
    d=[]
    p=[]
    for k,g in df.groupby('make'):
        d.append([k])
        print(g)
        for _,r in g.iterrows():
            p.append([f'  {r["model"]} ({r["yearStart"]-2000:02d}-{r["yearEnd"]-2000:02d})'])
            print(f'  {r["model"]} ({r["yearStart"]-2000:02d}-{r["yearEnd"]-2000:02d})')
    
    df1=pd.DataFrame(d)
    #df2=pd.DataFrame(p)
    df1.to_csv('newoutput.csv')
    #df2.to_csv('newoutput.csv')

print(f1.readlines())
#for line in csv_reader:
 #           count += 1
 #          print(f'line {count}: {line}')  
#f2.writelines(f1)


#f1=open("makes.txt","r")
#f2= open("changed.txt", "w")



#print(f1.readlines())

#f2.writelines(f1)

#Lines=f1.readlines()

#count=0



#for line in Lines:
#    count += 1
#    print((line.strip()))


#print(count)

#f1.close()
#f2.close()





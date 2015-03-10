import csv
import matplotlib.pyplot as plt
import numpy as np



#### block-maker function:
##def chunks(l,n):
##        for i in range(0,len(l),n):
##	    print(l[i:i+n])
data_list = []
time_list = []
## going to read the data from the csv, and strip only the first value. 
with open('firstdata.csv',newline='\n') as data_file:
    data_reader = csv.reader(data_file,delimiter= ',')
    for row in data_reader:
        if ( len(row) != 1 ):
            data_list.append(row[0])
            time_list.append(row[1][row[1].find(' ')+1:-3])


## The data_list comes out as a list of strings, so we cast them as floats
data_list = [ float(x) for x in data_list]

## When we chart things, we need to tell the graph where to put things horizontally. So we just
x_list = range(0,len(time_list))

## The graphs need to be spaced out a bit
plt.subplots_adjust(hspace=.6)


plt.subplot(211)
plt.plot(x_list,data_list,'b-')
plt.xlabel('Time')
plt.ylabel('Recorded Temperature (C)')
step = int(0.07 * len(data_list))

## Where to make the marks bewow the graph
time_ticks = [ time_list[i] for i in range(0,len(data_list),step)]
plt.xticks(np.arange(0,len(data_list),step),time_ticks,rotation='90')



def data_averager(l,interval):    
    avg_list = []
    for i in range(0,len(l),interval):
        avg_list.append(l[i:i+interval])
    return avg_list

## This will be the list of average temperatures.
avg_temp_list = []        
for i in range(0,len(data_list),step):
    avg_temp = np.average(data_list[i:i+step])
    avg_temp_list.append(avg_temp)

## The graph with the averages
plt.subplot(212)
plt.bar(np.arange(0,len(data_list),step),avg_temp_list,width=10,color='r')
plt.xlabel('Time (hour #)')
plt.ylabel('Average Temperature In Hour (C)')
plt.xticks(np.arange(0,len(data_list),step)+step/4,time_ticks,rotation='90')
plt.ylim(50,80)



plt.show()







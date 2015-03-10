import numpy as np

## Need to add null data
filename = 'random.csv'

def data_reader():
        
    f = open(filename,'r')
    read = f.read()
    f.close()
    num_data = int(read[:read.find('\n')])
    data = read[read.find('\n')+1:]

    x_list=[]
    y_list=[]
    for i in range(num_data):
        x_list.append(float(data[:data.find(',')]))
        y_list.append(float(data[data.find(',')+1:data.find('\n')]))
        data=data[data.find('\n')+1:]
    return x_list,y_list

def data_writer(xl,yl):
    num_data = len(xl)
    to_write = str(num_data)+'\n'
    for i in range(num_data):
        to_write += str(xl[i])+','+str(yl[i])+'\n'
##    print(to_write)
    f = open(filename,'w')
    f.write(to_write)
    f.close()

def add_to_data(xl,yl):
    new_x = np.amax(xl)+1
    new_y = np.random.randn()
    xl.append(new_x)
    yl.append(new_y)
    return xl,yl


for i in range(100):    
    x_list,y_list = data_reader()
    temp1,temp2 = add_to_data(x_list,y_list)
    data_writer(temp1,temp2)





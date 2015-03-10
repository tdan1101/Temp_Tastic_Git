#import libraries
import graphics 
import math
import time
import random


def get_temp():
    #do stuff using pip
    #to find the current temp
    current_temp =  random.randint(50, 90)
    its_cold = False
    its_hot = False
    if current_temp >= 75.0:
        its_hot = True
    elif current_temp <= 65.0:
        its_cold = True
    #if its_cold:
        #Turn on Blue LED
    #if its_hot:
        #Turn on Red LED
    return current_temp

def read_file(usr_file):
    file_data = usr_file.read()
    num_data_points = int(file_data[:file_data.find('\n')])
    file_data = file_data[file_data.find('\n')+1:]
    temp_array = []
    date_time_array = []
    if num_data_points != 0:
        for i in range(num_data_points):
            temp_reading = file_data[:file_data.find(',')]
            temp_array.append(float(temp_reading))
            date_time = file_data[file_data.find(',')+1:file_data.find('\n')] 
            date_time_array.append(date_time)
            file_data = file_data[file_data.find('\n')+1:]   
    return temp_array, date_time_array
    
def write_file(file_name, temp_array, date_time_array):
    num_data_points = 0
    to_write = ''
    for datum in temp_array: #-1??????
        to_write = to_write + str(datum)+','+str(date_time_array[num_data_points]+'\n')
        num_data_points += 1
    to_write = str(num_data_points)+'\n'+to_write
    usr_file = open(file_name, 'w')
    usr_file.write(to_write)
    usr_file.close() 
    
    
def Temp_Tastic_Nigga_Licious():
    current_tempt = get_temp()
    #ask for previous data file name as input from user?
    #file_name = input("file name?")
    file_name = 'data'
    if file_name.find('.') == -1:
            file_name = file_name + '.csv'    
    try:
        usr_file = open(file_name, 'r')
        usr_file.close()
    except:
        #no data recorded yet
        #null_data = '1\n65~~03/05/15 22:46:52'
        null_data = '0\n'
        usr_file = open(file_name, 'w')
        usr_file.write(null_data)
        usr_file.close()
    usr_file = open(file_name, 'r')
    temp_array, date_time_array = read_file(usr_file)
    usr_file.close()  
    print('Continuously recording temperatures now. \nTo stop, hit CTRL C.')
    stop = False
    while not stop:
        try:
            temp_avg = 0
            #find temp avg for an hour 
            for i in range(6):
            #for i in range(120): 
                current_temp = get_temp()
                temp_avg += current_temp
                time.sleep(0.5)
                #time.sleep(30)
            temp_avg = temp_avg/6 #CHANGE TO 120!!!  
            #temp_avg = temp_avg/120          
            date_time = str(time.strftime("%x"))+" "+str(time.strftime("%X"))
            print(round(temp_avg,1), '  ', date_time)
            temp_array.append(round(temp_avg,1))
            date_time_array.append(date_time)
            write_file(file_name, temp_array, date_time_array)
        except KeyboardInterrupt:
            stop = True
    cont = 'y'
    print('finished sucessfully recording temperatures\n')
    while cont == 'y':
        cont = input('start recording again? (y/n)')
        if cont == 'y':
            Temp_Tastic_Nigga_Licious()
        elif cont == 'n':
            cont = 'n'
            print('Have a Nigga Tastic Day Home-Skillet!!!!! \nHit enter to close')
            input()
        else:
            print('Dawg....... How much dope you been smokin??\nClearly \''+str(cont)+'\' isn\'t a \'y\' or \'n\'. \nLets try that again.\n')
            cont = 'y'
    
            
            
            
            
            

#print(str(time.strftime("%x"))+" "+str(time.strftime("%X")))

Temp_Tastic_Nigga_Licious()

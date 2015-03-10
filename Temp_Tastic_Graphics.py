#import libraries
from graphics import *
import math
import time
import random
#from pip import *

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
         
    return current_temp, its_cold, its_hot

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
    for datum in temp_array:
        to_write = to_write + str(datum)+','+str(date_time_array[num_data_points]+'\n')
        num_data_points += 1
    to_write = str(num_data_points)+'\n'+to_write
    usr_file = open(file_name, 'w')
    usr_file.write(to_write)
    usr_file.close() 


    
def Temp_Tastic_Nigga_Licious():
    win = GraphWin('Temp Tastic Nigga Licious', 500, 500)
    win.setCoords(0,0,500,500)
    title = Text(Point(250,450), 'Temp Tastic Nigga Licious')
    title.draw(win)      
    current_temp, its_cold, its_hot = get_temp()
    highest_temp = current_temp
    lowest_temp = current_temp
    Temp = Text(Point(250,150), 'Current Temp is\n' + str(current_temp) + ' Degrees   ' + str(time.strftime("%x"))+" "+str(time.strftime("%X")))
    Temp.draw(win)
    high_low_temps = Text(Point(250,300), 'Highest Recorded Temp\n'+str(highest_temp)+' Degrees\n\nLowest Recorded Temp\n'+str(lowest_temp)+' Degrees')
    high_low_temps.draw(win)     
    cold_message = Text(Point(250,50), 'DAMNNNNN NIGGA!!!!! ITS COLD!!!!')   
    hot_message = Text(Point(250,50), 'DAMNNNNN NIGGA!!!!! ITS HOT!!!!')
    if its_hot:
        hot_message.draw(win)
        time.sleep(2)
        hot_message.undraw()
    elif its_cold:
        cold_message.draw(win)
        time.sleep(2)
        cold_message.undraw()
    else:
        time.sleep(2)
    Temp.undraw()
    high_low_temps.undraw()

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
        null_data = '0\n'
        usr_file = open(file_name, 'w')
        usr_file.write(null_data)
        usr_file.close()
    usr_file = open(file_name, 'r')
    temp_array, date_time_array = read_file(usr_file)
    usr_file.close()  
    
    stop = False
    #for i in range(5):
    while not stop:
        try:
            temp_avg = 0
            #find temp avg for an hour 
            for i in range(6):
            #for i in range(120): 
                current_temp, its_cold, its_hot = get_temp()
                Temp = Text(Point(250,150), 'Current Temp is\n' + str(current_temp) + ' Degrees   ' + str(time.strftime("%x"))+" "+str(time.strftime("%X")))
                Temp.draw(win)                
                if current_temp > highest_temp:
                    highest_temp = current_temp
                if current_temp < lowest_temp:
                    lowest_temp = current_temp
                high_low_temps = Text(Point(250,300), 'Highest Recorded Temp\n'+str(highest_temp)+' Degrees\n\nLowest Recorded Temp\n'+str(lowest_temp)+' Degrees')
                high_low_temps.draw(win)                
                temp_avg += current_temp
                if its_cold:
                    cold_message = Text(Point(250,50), 'DAMNNNNN NIGGA!!!!! ITS COLD!!!!')
                    cold_message.draw(win)
                    time.sleep(0.5)
                    cold_message.undraw()
                elif its_hot:
                    hot_message = Text(Point(250,50), 'DAMNNNNN NIGGA!!!!! ITS HOT!!!!')
                    hot_message.draw(win)
                    time.sleep(0.5)
                    hot_message.undraw()
                else:
                    time.sleep(0.5)
                Temp.undraw()
                high_low_temps.undraw()
            temp_avg = temp_avg/6 #CHANGE TO 120!!!  
            #temp_avg = temp_avg/120       
            date_time = str(time.strftime("%x"))+" "+str(time.strftime("%X"))
            temp_array.append(round(temp_avg,1))
            date_time_array.append(date_time)
            write_file(file_name, temp_array, date_time_array)
        except KeyboardInterrupt:
            stop = True

    closemsg = Text(Point(250,250), 'click to close')
    closemsg.draw(win)
    win.getMouse()
    win.close()        
            
            
            

#print(str(time.strftime("%x"))+" "+str(time.strftime("%X")))

Temp_Tastic_Nigga_Licious()
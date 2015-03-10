#####################################
           ## NOTES ##
##IF USING in Raspberry PI (WINDOWS GENERATES RANDOM DATA)
##  *UNCOMMENT LINES: 21-30(setup GPIO),43-71(LED Commands), 269(GPIO Cleanup)
##  *Choose correct temperature driver:
#      -Trevor
TemperatureDriver = '/sys/bus/w1/devices/28-000006248f0d/w1_slave'
#      -Taylor
#TemperatureDriver = '/sys/bus/w1/devices/     ?????     /w1_slave'

## Define GPIO PIN# in BCM format NOT BOARD format
red = 25
green = 23
blue = 24

#####################################
      ## SETTINGS ##
##FileNAME (ASK FOR INPUT?)
FILE_NAME = 'data'
##How long to wait to take measurement
Secs_Between_measurements = 0.5
##find AVG Between how many num of Recordings
NumTemps_to_AVG = 5
##What is the MAX temp till it starts feeling hot?
HOT = 71
##What is the MAX temp till it starts feeling cold?
COLD = 70
######################################

#import libraries
from graphics import *
import math
import time
import random

#######################
###SET UP GPIO FOR LEDS##
#import RPi.GPIO as gpio
#gpio.setmode(gpio.BCM)
#gpio.setwarnings(False)
#gpio.setup(red,gpio.OUT)
#gpio.output(red,0)
#gpio.setup(green,gpio.OUT)
#gpio.output(green,0)
#gpio.setup(blue,gpio.OUT)
#gpio.output(blue,0)
############################

def get_temp():
    its_cold = False
    its_hot = False 
    current_temp =  random.randint(50, 90)
    ######################################
    #temp_file = open(TemperatureDriver)
    #data = temp_file.read()
    #temp_file.close()
    #current_temp = 1.8*(float(data[data.find('t=')+2:-1])/1000)+32
    #for i in range(3):
        #gpio.output(blue,0)
        #gpio.output(red,1)
        #gpio.output(green,0)
        #time.sleep(0.1)
        #gpio.output(blue,0)
        #gpio.output(red,0)
        #gpio.output(green,1)
        #time.sleep(0.1)
        #gpio.output(blue,1)
        #gpio.output(red,0)
        #gpio.output(green,0)
        #time.sleep(0.1)
    #if current_temp <= COLD:
        #gpio.output(blue,1)
        #gpio.output(red,0)
        #gpio.output(green,0)#Turn on Blue LED
    #elif current_temp >= HOT:
        #gpio.output(blue,0)
        #gpio.output(red,1)
        #gpio.output(green,0)#Turn on Red LED
    #else:
        #gpio.output(blue,0)
        #gpio.output(red,0)
        #gpio.output(green,1)
    ######################################
    if current_temp >= HOT:
            its_hot = True
    elif current_temp <= COLD:
            its_cold = True    
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


    
def Temp_Tastic_Nigga_Licious_Graphics(win):
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
        time.sleep(Secs_Between_measurements)
        hot_message.undraw()
    elif its_cold:
        cold_message.draw(win)
        time.sleep(Secs_Between_measurements)
        cold_message.undraw()
    else:
        time.sleep(Secs_Between_measurements)
    Temp.undraw()
    high_low_temps.undraw()
    file_name = FILE_NAME
    if file_name.find('.') == -1:
            file_name = file_name + '.csv'    
    try:
        usr_file = open(file_name, 'r')
        usr_file.close()
    except:
        ##no data recorded yet CREATE FILE##
        null_data = '0\n'
        usr_file = open(file_name, 'w')
        usr_file.write(null_data)
        usr_file.close()
    usr_file = open(file_name, 'r')
    temp_array, date_time_array = read_file(usr_file)
    usr_file.close()  
    ###Begin continuous loop##
    stop = False
    while not stop:
        try:
            temp_avg = 0
            for i in range(NumTemps_to_AVG): 
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
                    time.sleep(Secs_Between_measurements)
                    cold_message.undraw()
                elif its_hot:
                    hot_message = Text(Point(250,50), 'DAMNNNNN NIGGA!!!!! ITS HOT!!!!')
                    hot_message.draw(win)
                    time.sleep(Secs_Between_measurements)
                    hot_message.undraw()
                else:
                    time.sleep(Secs_Between_measurements)
                Temp.undraw()
                high_low_temps.undraw()
            temp_avg = temp_avg/NumTemps_to_AVG        
            date_time = str(time.strftime("%x"))+" "+str(time.strftime("%X"))
            temp_array.append(round(temp_avg,1))
            date_time_array.append(date_time)
            write_file(file_name, temp_array, date_time_array)
            print("recorded ", round(temp_avg,1), '  ', date_time,'\nto the file ', file_name)
        except KeyboardInterrupt:
            ## EXIT CONT LOOP ON CTRL+C##
            stop = True
    win.close()
    
    
def Temp_Tastic_Nigga_Licious_No_Graphics():
    current_temp, its_cold, its_hot = get_temp()  
    file_name = FILE_NAME
    if file_name.find('.') == -1:
            file_name = file_name + '.csv'    
    try:
        usr_file = open(file_name, 'r')
        usr_file.close()
    except:
        ##no data recorded yet CREATE FILE##
        null_data = '0\n'
        usr_file = open(file_name, 'w')
        usr_file.write(null_data)
        usr_file.close()
    usr_file = open(file_name, 'r')
    temp_array, date_time_array = read_file(usr_file)
    usr_file.close()  
    print('\nContinuously recording temperatures now. \nTo stop, hit CTRL C.')
    stop = False
    while not stop:
        try:
            temp_avg = 0
            for i in range(NumTemps_to_AVG):
                current_temp, its_cold, its_hot = get_temp()
                date_time = str(time.strftime("%x"))+" "+str(time.strftime("%X"))
                print(round(current_temp,1), '  ', date_time)
                temp_avg += current_temp
                time.sleep(Secs_Between_measurements)
            temp_avg = temp_avg/NumTemps_to_AVG   
            date_time = str(time.strftime("%x"))+" "+str(time.strftime("%X"))
            print("recorded ", round(temp_avg,1), '  ', date_time,'\nto the file ', file_name)
            temp_array.append(round(temp_avg,1))
            date_time_array.append(date_time)
            write_file(file_name, temp_array, date_time_array)
        except KeyboardInterrupt:
            stop = True
    print('\nFinished recording them temps nigga! \n')

         


def main():
    print('HEY NIGGGGAAAA!!!! \nYou look like your in need of some temperature recordings.\nAm i right Dawg?')
    cont = 'y'
    while cont == 'y':
        cont = input('Begin recording? (y/n) ')
        if cont == 'y':
            graphics = input('Do you want graphics? (y/n) ')
            if graphics == 'y':
                try:
                    print('Continuously recording temperatures now. \nOpening Graphics Window.\nTo stop, Close Graphics window.\n')                 
                    win = GraphWin('Temp Tastic Nigga Licious', 500, 500)
                    win.setCoords(0,0,500,500)
                    title = Text(Point(250,450), 'Temp Tastic Nigga Licious')
                    title.draw(win) 
                    Temp_Tastic_Nigga_Licious_Graphics(win)
                    win.close()
                except:
                    win.close()
                    print('\nFinished recording them temps nigga! \n')
            elif graphics == 'n':
                Temp_Tastic_Nigga_Licious_No_Graphics()
            else:
                print('Dawg....... How much dope you been smokin???\nClearly your input of \''+str(graphics)+'\' isn\'t a \'y\' or \'n\'. \nLets try that again.......\n')                
        elif cont == 'n':
            cont = 'n'
            print('Have a Nigga Tastic Day Home-Skillet!!!!! \nHit enter to close')
            input()
        else:
            print('Dawg....... How much dope you been smokin???\nClearly your input of \''+str(cont)+'\' isn\'t a \'y\' or \'n\'. \nLets try that again.......\n')
            cont = 'y'    
    
main()
#########################
#gpio.cleanup()
#########################

import tkinter
import subprocess
import customtkinter
import json
import screen_brightness_control as sbc
import sys
import os
hourlist = ['none','00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', "23"]
minustlist = ['none','00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
ardict= {
    "hours": None,
    "min" : None,
    "bright" : 100,
    "pythonpath":sys.executable,
    "defaultbright": None,
    "path" : os.getcwd()+"\\"+"changerbopener.bat",
}
#---------------------------------------------------------------script part------------------------------------------------------------------------------------------------------
def changebr(i): #function for change brightness 
    int(i)
    sbc.set_brightness(i)
    sliderlabel.configure(text=i)
   # print(sbc.get_brightness())

#---------------------------------------------------------------schtasklist------------------------------------------------------------------------------------------------------
# def arlistbuttonfunc():
#         new_window = customtkinter.CTkToplevel(mainw)
#         new_window.title("list of autorun")
#         new_window.geometry("600x600")
#         new_window.resizable(False,False)
#         schtaskcombobox = customtkinter.CTkComboBox(new_window, 400 , 50 , 10 , values )
#         schtaskcombobox.pack()

def arbuttonrfunc():
    with open("arparametr" , "w") as file : 
        new_json=json.dump(ardict ,file , indent= 2 )
    print("wrote")
    with open("arparametr", "r", encoding="utf-8") as arparametr:
        gigi = json.load(arparametr)
    hours = gigi["hours"]
    minutes = gigi["min"]
    bright = gigi["bright"]
    defaultbright = gigi["defaultbright"]
    path = gigi["path"]
    pythonpath = gigi["pythonpath"]

    time= f"{hours}" + ":" + f"{minutes}"
    data = {
        "hours":str(hours),
        "min":str(minutes),
        "bright":str(bright),
        "defaultbright":defaultbright,
        "path":path
    }
    print(time)
    
    command = f'schtasks /Create /tn "dvegbrightness" /tr {path}  /sc DAILY /st {time} /f' ### /f for ignor agree on rewrite
    subprocess.call(command, shell=True)


def drophbox(value): ### def for  hour dropbox
    print(value , " hours")
    ardict['hours'] = str(timehbox.get())


def dropmbox(value): ### def for minuts dropbox
    #timembox.get()
    print(value , " min")
    ardict['min'] = str(timembox.get())

def arcslider(value):
    int(value)
    arcsliderlabel.configure(text = value)
    ardict['bright'] = value

##### gui part   >
mainw = customtkinter.CTk() ### main window

mainw.iconbitmap(default="lightblub.ico")

mainw.title("BrightnessControl by dveg") ### title

mainw.geometry("400x600") ### size of window

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("blue")

mainw.resizable(False, False) ### prohibition to stretch the screen width and height , change to True, True
###for unlock
#------------------------------------------------------------main-menu-gui-part------------------------------------------------------------------------------------------------#
#--------------------------------------------------------slider of brightness change-------------------------------------------------------------------------------------------#



slidertitle = customtkinter.CTkLabel(mainw , text="BRIGHTNESS SLIDER",
                                     font=("Palui SP", 18))
slidertitle.place(relx = 0.25 , rely = 0.01)
slider = customtkinter.CTkSlider(mainw, from_=0, to=100, command=changebr , number_of_steps=100)
slider.set(100) #### default pos of slider
slider.place(relx = 0.23 , rely = 0.1)###cord x and y

sliderlabel = customtkinter.CTkLabel(mainw , text="100" )###default text before he will changed by brightness func
sliderlabel.place(relx = 0.24, rely = 0.13)


#--------------------------------------------------------------redeem button--------------------------------------------------------------------------------------------------#

arbutton = customtkinter.CTkButton(mainw , 180 , 50 , 10 , text="redeem" , command=arbuttonrfunc)
arbutton.place(relx = 0.28 , rely = 0.75)


#-------------------------------------------------------------combobox timer--------------------------------------------------------------------------------------------------#


hlabel = customtkinter.CTkLabel(mainw, 50 , 50 , 10 , text="hours")
hlabel.place(relx = 0.089 , rely = 0.475)
timehbox = customtkinter.CTkComboBox(mainw , 100 , 20 , 10 , values=hourlist, command=drophbox)
timehbox.place(relx = 0.22 , rely = 0.5)


mlabel = customtkinter.CTkLabel(mainw, 50 , 50 , 10 , text="min")
mlabel.place(relx = 0.47 , rely = 0.475)
timembox = customtkinter.CTkComboBox(mainw , 100 , 20 , 10 , values=minustlist, command=dropmbox)
timembox.place(relx = 0.58 , rely = 0.5 )

labelautorun = customtkinter.CTkLabel(mainw, 10 , 10 , 10 , text="AUTO RUN TIME",font=("Palui SP",18))
labelautorun.place(relx=0.31 , rely = 0.43)

labelchangeto = customtkinter.CTkLabel(mainw,10 , 10 , 10 , text="change brightness to",font=("Palui SP",12))
labelchangeto.place(relx = 0.34 , rely=0.56)
#-----------------------------------------------------autorun slider for changebrightness--------------------------------------------------------------------------------------#
arslider = customtkinter.CTkSlider(mainw, from_=1 , to=100 , command=arcslider)
arslider.set(100)
arslider.place(relx = 0.23 , rely=0.6)


arcsliderlabel = customtkinter.CTkLabel(mainw , 1 , 1 , 1 , text="100" )
arcsliderlabel.place(relx=0.24 , rely=0.63)

#--------------------------------------------------------------list-button-----------------------------------------------------------------------------------------------------#
# arlistbutton = customtkinter.CTkButton(mainw , 120 , 25 , 5 , text="list" , command=arlistbuttonfunc)
# arlistbutton.place(relx = 0.35 , rely = 0.84)
mainw.mainloop() #### loop tk for run window
#####

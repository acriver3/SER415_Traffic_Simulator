# SER415 Traffic Simulator - Team 6
# Manolito Ramirez, Jessica Gilbert, Mike Wagner,
# Carlos Franco, Arthur Rivera, and Ryan Kirmis
# Version 1.1.1

import tkinter as tk
import tkinter.ttk
import numpy as np
import math
import time

root = tkinter.Tk()

#-------------------------------------------------------------------------------
# GLOBALS:
flowRateScalar = 1;     # used to change flow rate for specific scenarios

#-------------------------------------------------------------------------------
# GUI SETUP:

# ---Canvas---
top = tk.Canvas(root, width=739, height=535, bg="#C0C5C6")
top.pack();
top.create_text((20, 10), text="Traffic Simulator", font="MSGothic 20 bold", fill="#065535", anchor="nw")
top.create_text((500, 50), text="Cycle Timing", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((555, 290), text="Scenarios", font="MSGothic 15 bold", fill="#065535", anchor="nw")

root.geometry("739x535+503+155")
root.minsize(120, 1)
root.maxsize(1924, 1061)
root.resizable(0, 0)
root.title("Traffic Simulator GUI")
root.configure(background="#d9d9d9")

main_bg = tk.PhotoImage(file="../resources/intersection.png")


# ---Frames---
# Timing value input frame
fTiming = tk.Frame(top, bg="#707070", highlightbackground="#065535", highlightthickness=3)
fTiming.place(relx=0.67, rely=0.15, relheight=0.215, relwidth=0.277)


# ---Labels---
# Intersection image
lIntersection = tk.Label(top, image=main_bg)
lIntersection.place(relx=0.13, rely=0.2, height=341, width=371)

# Timing value input labels
lTimeNS = tk.Label(fTiming, text="N-S", bg="#707070", anchor="nw")
lTimeNSGrnArr = tk.Label(fTiming, text="N-S Green Arrow", bg="#707070", anchor="nw")
lTimeWE = tk.Label(fTiming, text="E-W", bg="#707070", anchor="nw")
lTimeWEGrnArr = tk.Label(fTiming, text="E-W Green Arrow", bg="#707070", anchor="nw")

lTimeNS.place(relx=0.05, rely=0.05, height=20, width=100)
lTimeNSGrnArr.place(relx=0.05, rely=0.275, height=20, width=100)
lTimeWE.place(relx=0.05, rely=0.5, height=20, width=100)
lTimeWEGrnArr.place(relx=0.05, rely=0.725, height=20, width=100)


# ---Text fields---
# 'Number of cars' text fields
tCarsInW = tk.Text(top)
tCarsInN = tk.Text(top)
tCarsInE = tk.Text(top)
tCarsInS = tk.Text(top)
tCarsOutW = tk.Text(top, state="disabled")
tCarsOutN = tk.Text(top, state="disabled")
tCarsOutE = tk.Text(top, state="disabled")
tCarsOutS = tk.Text(top, state="disabled")

# 'Cycle times' text fields
tTimeNS = tk.Text(fTiming)
tTimeNSGrnArr = tk.Text(fTiming)
tTimeWE = tk.Text(fTiming)
tTimeWEGrnArr = tk.Text(fTiming)

tCarsInW.place(relx=0.05, rely=0.57, relheight=0.045, relwidth=0.06)
tCarsInN.place(relx=0.3, rely=0.135, relheight=0.045, relwidth=0.06)
tCarsInE.place(relx=0.65, rely=0.43, relheight=0.045, relwidth=0.06)
tCarsInS.place(relx=0.404, rely=0.86, relheight=0.045, relwidth=0.06)
tCarsOutW.place(relx=0.05, rely=0.43, relheight=0.045, relwidth=0.06)
tCarsOutN.place(relx=0.404, rely=0.135, relheight=0.045, relwidth=0.06)
tCarsOutE.place(relx=0.65, rely=0.57, relheight=0.045, relwidth=0.06)
tCarsOutS.place(relx=0.3, rely=0.86, relheight=0.045, relwidth=0.06)

tTimeNS.place(relx=0.65, rely=0.05, height=20, width=45)
tTimeNSGrnArr.place(relx=0.65, rely=0.275, height=20, width=45)
tTimeWE.place(relx=0.65, rely=0.5, height=20, width=45)
tTimeWEGrnArr.place(relx=0.65, rely=0.725, height=20, width=45)

currScenario = tk.StringVar(top)
currScenario.set("None") # set default scenario to 'None'

# 'Scenarios' drop down menu
scenarios = tk.OptionMenu(top, currScenario, "None", "Construction", "Weather", "Accident")
scenarios.place(relx=0.75, rely=0.6, height=25, width=125)

# ---Buttons---
# 'Run Simulation' button
bRunSim = tk.Button(top, text="Run Simulation", bg = "#90EE90")

bRunSim.place(relx=0.054, rely=0.11, height=34, width=97)

# ---Boolean Indicators---
rbSimRunning = tk.Radiobutton(top, text ="")
rbSimRunning.place(relx=0.2, rely=0.11, height=25, width=25)
rbSimRunning.deselect()

#-------------------------------------------------------------------------------
# CALLBACK FUNCTIONS

# Starts simulation when user clicks 'Run Simulation' button
def startSim(event):
    testCycleLength = 15 # test cycle length of 15 seconds
    testNumCars = 20 # test number of cars during cycle

    startTime = time.time()
    currTime = time.time() - startTime
    currSecond = 0;

    while(currTime < testCycleLength):
        if (currTime > currSecond):
            currRate = (math.tanh(currTime-3) + 1)
            testNumCars -= currRate
            currSecond += 1
            print(testNumCars)
        currTime = time.time() - startTime
    #print(tTimeNS.get("1.0", "end-1c"))

# Updates flow rate scalar based on scenario selection
def scenarioChange(*args):
    # change based on selected scenario
    if (currScenario.get() == "None"):
        flowRateScalar = 1 #UPDATE
    elif (currScenario.get() == "Construction"):
        flowRateScalar = 1 #UPDATE
    elif (currScenario.get() == "Weather"):
        flowRateScalar = 1 #UPDATE
    elif (currScenario.get() == "Accident"):
        flowRateScalar = 1 #UPDATE

# CALLBACK BINDINGS
bRunSim.bind("<Button-1>", startSim)

currScenario.trace('w', scenarioChange)

#-------------------------------------------------------------------------------
# HELPER FUNCTIONS

root.mainloop()

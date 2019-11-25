# SER415 Traffic Simulator - Team 8
# Manolito Ramirez, Jessica Gilbert, Mike Wagner,
# Carlos Franco, Arthur Rivera, and Ryan Kirmis
# Version 1.1.1

import tkinter as tk
import tkinter.ttk
import math
import time

root = tkinter.Tk()

#-------------------------------------------------------------------------------
# GLOBALS:
flowRateScalar = 1;     # used to change flow rate for specific scenarios
sampleDelay = 1000;     # delay between samples

#-------------------------------------------------------------------------------
# GUI SETUP:

# ---Canvas---
top = tk.Canvas(root, width=739, height=535, bg="#C0C5C6")
top.pack();
top.create_text((20, 10), text="Traffic Simulator", font="MSGothic 20 bold", fill="#065535", anchor="nw")
top.create_text((500, 50), text="Cycle Timing", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((555, 290), text="Scenarios", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((147, 57), text="Time (s)", font="MSGothic 8 bold", fill="#065535", anchor="nw")

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

# Current Time Indicator
lCurrTime = tk.Label(top, anchor="nw")
lCurrTime.place(relx=0.2, rely=0.135, height=20, width=30)


# ---Text fields---
# 'Number of cars' text fields
tCarsInW = tk.Text(top)
tCarsInN = tk.Text(top)
tCarsInE = tk.Text(top)
tCarsInS = tk.Text(top)
tCarsOutW = tk.Text(top, state="disabled", bg = "#C8E2BB")
tCarsOutN = tk.Text(top, state="disabled", bg = "#C8E2BB")
tCarsOutE = tk.Text(top, state="disabled", bg = "#C8E2BB")
tCarsOutS = tk.Text(top, state="disabled", bg = "#C8E2BB")

# 'Cycle times' text fields
tTimeNS = tk.Text(fTiming)
tTimeNSGrnArr = tk.Text(fTiming)
tTimeWE = tk.Text(fTiming)
tTimeWEGrnArr = tk.Text(fTiming)

tTimeNS.insert('1.0', '0')
tTimeNSGrnArr.insert('1.0', '0')
tTimeWE.insert('1.0', '0')
tTimeWEGrnArr.insert('1.0', '0')

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

# Lane percentages
tRightW = tk.Text(lIntersection, bg="#90EEBF")
tStraightW = tk.Text(lIntersection, bg="#90EEBF")
tLeftW = tk.Text(lIntersection, bg="#90EEBF")

tRightN = tk.Text(lIntersection, bg="#90EEBF")
tStraightN = tk.Text(lIntersection, bg="#90EEBF")
tLeftN = tk.Text(lIntersection, bg="#90EEBF")

tRightE = tk.Text(lIntersection, bg="#90EEBF")
tStraightE = tk.Text(lIntersection, bg="#90EEBF")
tLeftE = tk.Text(lIntersection, bg="#90EEBF")

tRightS = tk.Text(lIntersection, bg="#90EEBF")
tStraightS = tk.Text(lIntersection, bg="#90EEBF")
tLeftS = tk.Text(lIntersection, bg="#90EEBF")

tRightW.place(relx=0.06, rely=0.663, height=20, width=20)
tStraightW.place(relx=0.06, rely=0.589, height=20, width=20)
tLeftW.place(relx=0.06, rely=0.513, height=20, width=20)

tRightN.place(relx=0.305, rely=0.04, height=20, width=20)
tStraightN.place(relx=0.374, rely=0.04, height=20, width=20)
tLeftN.place(relx=0.442, rely=0.04, height=20, width=20)

tRightE.place(relx=0.89, rely=0.29, height=20, width=20)
tStraightE.place(relx=0.89, rely=0.366, height=20, width=20)
tLeftE.place(relx=0.89, rely=0.438, height=20, width=20)

tRightS.place(relx=0.645, rely=0.915, height=20, width=20)
tStraightS.place(relx=0.577, rely=0.915, height=20, width=20)
tLeftS.place(relx=0.51, rely=0.915, height=20, width=20)

tRightW.insert('1.0', '.2')
tStraightW.insert('1.0', '.7')
tLeftW.insert('1.0', '.1')

tRightN.insert('1.0', '.2')
tStraightN.insert('1.0', '.7')
tLeftN.insert('1.0', '.1')

tRightE.insert('1.0', '.2')
tStraightE.insert('1.0', '.7')
tLeftE.insert('1.0', '.1')

tRightS.insert('1.0', '.2')
tStraightS.insert('1.0', '.7')
tLeftS.insert('1.0', '.1')


# Scenarios
currScenario = tk.StringVar(top)
currScenario.set("None") # set default scenario to 'None'

# Drop down menu
scenarios = tk.OptionMenu(top, currScenario, "None", "Construction", "Weather", "Accident")
scenarios.place(relx=0.75, rely=0.6, height=25, width=125)

# ---Buttons---
# 'Run Simulation' button
bRunSim = tk.Button(top, text="Run Simulation", bg = "#90EE90")

bRunSim.place(relx=0.054, rely=0.11, height=34, width=97)

# ---Boolean Indicators---
#rbSimRunning = tk.Radiobutton(top, text ="")
#rbSimRunning.place(relx=0.2, rely=0.11, height=25, width=25)
#rbSimRunning.deselect()

#-------------------------------------------------------------------------------
# CALLBACK FUNCTIONS

testCycleLength = 15
cycleLengths = [0, 0, 0, 0] # test cycle length of 15 seconds
numCars = [] # test number of cars during cycle

startTime = 0
currTime = 0
currSecond = 0
currCycle = 0

# Starts simulation when user clicks 'Run Simulation' button
def startSim(event):
    global currTime, startTime, currSecond, testCycleLength, testNumCars

    cycleLengths[0] = int(tTimeNS.get("1.0", "end-1c"));
    cycleLengths[1] = int(tTimeNSGrnArr.get("1.0", "end-1c"));
    cycleLengths[2] = int(tTimeWE.get("1.0", "end-1c"));
    cycleLengths[3] = int(tTimeWEGrnArr.get("1.0", "end-1c"));

    testNumCars = 20 # test number of cars during cycle

    startTime = time.time()
    currTime = time.time() - startTime
    currSecond = 0
    root.after(0, cycle)

def cycle():
    global currTime, startTime, currSecond, currCycle, testCycleLength, testNumCars

    lCurrTime["text"] = round(currTime)
    if (currTime < cycleLengths[currCycle]):
        if (currTime > currSecond):
            currRate = (math.tanh(currTime-3) + 1)
            if (testNumCars < 0):
                testNumCars = 0
            else:
                testNumCars -= currRate
            currSecond += 1
        currTime = time.time() - startTime
        root.after(sampleDelay, cycle)
    else:
        if (currCyle == 3):
            currCycle = 0
        else:
            currCycle += 1
            root.after(0, startSim)

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

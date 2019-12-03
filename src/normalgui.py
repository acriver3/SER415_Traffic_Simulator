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
flowRateScalar = 1      # scalar to change max flow rate for specific scenarios
flowDelayScalar = 1     # scalar to decrease or decrease time to max flow rate
maxFlowRate = 1         # scalar to scale max flow rate (default flow rate = 2)
sampleDelay = 500       # delay between samples
simActive = False       # boolean for checking if simulation is active

cycleLengths = [0, 0, 0, 0] # cycle lengths (in s)

startTime = 0           # start time of one traffic cycle
currTime = 0            # currenct time during traffic cycle
currSecond = 0          # current second during traffic cycle
currCycle = 0           # current traffic cycle

carsInW = 0             # cars waiting from West direction
carsInN = 0             # cars waiting from North direction
carsInE = 0             # cars waiting from East direction
carsInS = 0             # cars waiting from South direction
carsOutW = 0            # cars waiting from West direction
carsOutN = 0            # cars waiting from North direction
carsOutE = 0            # cars waiting from East direction
carsOutS = 0            # cars waiting from South direction


#-------------------------------------------------------------------------------
# GUI SETUP:

# ---Canvas---
top = tk.Canvas(root, width=850, height=625, bg="#C0C5C6")
top.pack();
top.create_text((20, 10), text="Traffic Simulator", font="MSGothic 20 bold", fill="#065535", anchor="nw")
top.create_text((570, 98), text="Cycle Timing", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((660, 347), text="Scenarios", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((660, 400), text="Days", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((660, 450), text="Time of Day", font="MSGothic 15 bold", fill="#065535", anchor="nw")
top.create_text((660, 280), text="Max Outflow Rate", font="MSGothic 10 bold", fill="#065535", anchor="nw")
top.create_text((703, 303), text="cars/sec", font="MSGothic 8", fill="#065535", anchor="nw")
top.create_text((340, 54), text="Cycle", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((434, 54), text="Time (s)", font="MSGothic 8 bold", fill="#065535", anchor="nw")

# 'Cars In/Cars' Out text labels from West
top.create_text((43, 354), text="Cars In", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((43, 296), text="Cars Out", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((43, 396), text="Inflow Rate", font="MSGothic 8 bold", fill="#065535", anchor="nw")

# 'Cars In/Cars Out' text labels from North
top.create_text((236, 141), text="Cars In", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((309, 141), text="Cars Out", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((236, 100), text="Inflow Rate", font="MSGothic 8 bold", fill="#065535", anchor="nw")

# 'Cars In/Cars' Out text labels from East
top.create_text((497, 279), text="Cars In", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((497, 368), text="Cars Out", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((497, 321), text="Inflow Rate", font="MSGothic 8 bold", fill="#065535", anchor="nw")

# 'Cars In/Cars Out' text labels from South
top.create_text((309, 532), text="Cars In", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((237, 532), text="Cars Out", font="MSGothic 8 bold", fill="#065535", anchor="nw")
top.create_text((309, 573), text="Inflow Rate", font="MSGothic 8 bold", fill="#065535", anchor="nw")

root.geometry("850x625+503+155")
root.minsize(120, 1)
root.maxsize(1924, 1061)
root.resizable(0, 0)
root.title("Traffic Simulator GUI")
root.configure(background="#D9D9D9")

main_bg = tk.PhotoImage(file="../resources/intersection.png")

# Intersection Canvas
intersection = tk.Canvas(top, width=341, height=371)
intersection.place(relx=0.13, rely=0.3, height=341, width=371)
intersection.create_image(2, -11, image=main_bg, anchor="nw")

# Red lights, green lights
greenLight = tk.PhotoImage(file="../resources/green_light.png")
redLight = tk.PhotoImage(file="../resources/red_light.png")

# Lights from West entrance
greenLightW = intersection.create_image(109, 167, image=greenLight, anchor="nw", state="hidden")
redLightW = intersection.create_image(127, 167, image=redLight, anchor="nw", state="hidden")

# Lights from North entrance
greenLightN = intersection.create_image(180, 95, image=greenLight, anchor="nw", state="hidden")
redLightN = intersection.create_image(180, 113, image=redLight, anchor="nw", state="hidden")

# Lights from East entrance
greenLightE = intersection.create_image(252, 167, image=greenLight, anchor="nw", state="hidden")
redLightE = intersection.create_image(234, 167, image=redLight, anchor="nw", state="hidden")

# Lights from South entrance
greenLightS = intersection.create_image(180, 238, image=greenLight, anchor="nw", state="hidden")
redLightS = intersection.create_image(180, 221, image=redLight, anchor="nw", state="hidden")


# ---Frames---
# Timing value input frame
fTiming = tk.Frame(top, bg="#707070", highlightbackground="#065535", highlightthickness=3)
fTiming.place(relx=0.67, rely=0.2, relheight=0.215, relwidth=0.277)

# ---Labels---
# Timing value input labels
lTimeNS = tk.Label(fTiming, text="N-S", bg="#707070", anchor="nw")
lTimeNSGrnArr = tk.Label(fTiming, text="N-S Green Arrow", bg="#707070", anchor="nw")
lTimeWE = tk.Label(fTiming, text="W-E", bg="#707070", anchor="nw")
lTimeWEGrnArr = tk.Label(fTiming, text="W-E Green Arrow", bg="#707070", anchor="nw")

# Seconds labels
lSecondsNS = tk.Label(fTiming, text="s", bg="#707070", anchor="nw")
lSecondsNSGrnArr = tk.Label(fTiming, text="s", bg="#707070", anchor="nw")
lSecondsWE = tk.Label(fTiming, text="s", bg="#707070", anchor="nw")
lSecondsWEGrnArr = tk.Label(fTiming, text="s", bg="#707070", anchor="nw")

lTimeNS.place(relx=0.05, rely=0.05, height=20, width=100)
lTimeNSGrnArr.place(relx=0.05, rely=0.275, height=20, width=100)
lTimeWE.place(relx=0.05, rely=0.5, height=20, width=100)
lTimeWEGrnArr.place(relx=0.05, rely=0.725, height=20, width=100)

lSecondsNS.place(relx=0.9, rely=0.05, height=20, width=15)
lSecondsNSGrnArr.place(relx=0.9, rely=0.275, height=20, width=15)
lSecondsWE.place(relx=0.9, rely=0.5, height=20, width=15)
lSecondsWEGrnArr.place(relx=0.9, rely=0.725, height=20, width=15)

# Current Time Indicator
lCurrTime = tk.Label(top, bg = "#C8E2BB", anchor="nw")
lCurrTime.place(relx=0.51, rely=0.11, height=20, width=30)
lCurrTime["text"] = 0

# Current Cycle Indicator
lCurrCycle = tk.Label(top, bg = "#C8E2BB", anchor="nw")
lCurrCycle.place(relx=0.4, rely=0.11, height=25, width=70)
lCurrCycle["text"] = "-"

# ---Text fields---
# 'Number of cars' text fields
tCarsInW = tk.Text(top)
tCarsInN = tk.Text(top)
tCarsInE = tk.Text(top)
tCarsInS = tk.Text(top)
tCarsOutW = tk.Text(top, bg = "#C8E2BB")
tCarsOutN = tk.Text(top, bg = "#C8E2BB")
tCarsOutE = tk.Text(top, bg = "#C8E2BB")
tCarsOutS = tk.Text(top, bg = "#C8E2BB")

# 'Cycle times' text fields
tTimeNS = tk.Text(fTiming)
tTimeNSGrnArr = tk.Text(fTiming)
tTimeWE = tk.Text(fTiming)
tTimeWEGrnArr = tk.Text(fTiming)

tTimeNS.insert('1.0', '20')
tTimeNSGrnArr.insert('1.0', '10')
tTimeWE.insert('1.0', '20')
tTimeWEGrnArr.insert('1.0', '10')

tCarsInW.place(relx=0.05, rely=0.59, relheight=0.035, relwidth=0.06)
tCarsInN.place(relx=0.278, rely=0.25, relheight=0.035, relwidth=0.06)
tCarsInE.place(relx=0.585, rely=0.47, relheight=0.035, relwidth=0.06)
tCarsInS.place(relx=0.363, rely=0.875, relheight=0.035, relwidth=0.06)
tCarsOutW.place(relx=0.05, rely=0.498, relheight=0.035, relwidth=0.06)
tCarsOutN.place(relx=0.363, rely=0.25, relheight=0.035, relwidth=0.06)
tCarsOutE.place(relx=0.585, rely=0.612, relheight=0.035, relwidth=0.06)
tCarsOutS.place(relx=0.278, rely=0.875, relheight=0.035, relwidth=0.06)

tTimeNS.place(relx=0.65, rely=0.05, height=20, width=45)
tTimeNSGrnArr.place(relx=0.65, rely=0.275, height=20, width=45)
tTimeWE.place(relx=0.65, rely=0.5, height=20, width=45)
tTimeWEGrnArr.place(relx=0.65, rely=0.725, height=20, width=45)

tCarsInW.insert('1.0', '30')
tCarsInN.insert('1.0', '30')
tCarsInE.insert('1.0', '30')
tCarsInS.insert('1.0', '30')
tCarsOutW.insert('1.0', '0')
tCarsOutN.insert('1.0', '0')
tCarsOutE.insert('1.0', '0')
tCarsOutS.insert('1.0', '0')

# 'Inflow' rates
tInflowW = tk.Text(top)
tInflowN = tk.Text(top)
tInflowE = tk.Text(top)
tInflowS = tk.Text(top)

tInflowW.place(relx=0.05, rely=0.657, relheight=0.035, relwidth=0.06)
tInflowN.place(relx=0.278, rely=0.185, relheight=0.035, relwidth=0.06)
tInflowE.place(relx=0.585, rely=0.5375, relheight=0.035, relwidth=0.06)
tInflowS.place(relx=0.363, rely=0.940, relheight=0.035, relwidth=0.06)

tInflowW.insert('1.0', '0.2')
tInflowN.insert('1.0', '0.2')
tInflowE.insert('1.0', '0.2')
tInflowS.insert('1.0', '0.2')

# Lane percentages text field
tRightW = tk.Text(intersection, bg="#90EEBF")
tStraightW = tk.Text(intersection, bg="#90EEBF")
tLeftW = tk.Text(intersection, bg="#90EEBF")

tRightN = tk.Text(intersection, bg="#90EEBF")
tStraightN = tk.Text(intersection, bg="#90EEBF")
tLeftN = tk.Text(intersection, bg="#90EEBF")

tRightE = tk.Text(intersection, bg="#90EEBF")
tStraightE = tk.Text(intersection, bg="#90EEBF")
tLeftE = tk.Text(intersection, bg="#90EEBF")

tRightS = tk.Text(intersection, bg="#90EEBF")
tStraightS = tk.Text(intersection, bg="#90EEBF")
tLeftS = tk.Text(intersection, bg="#90EEBF")

tRightW.place(relx=0.06, rely=0.657, height=20, width=20)
tStraightW.place(relx=0.06, rely=0.584, height=20, width=20)
tLeftW.place(relx=0.06, rely=0.511, height=20, width=20)

tRightN.place(relx=0.305, rely=0.04, height=20, width=20)
tStraightN.place(relx=0.372, rely=0.04, height=20, width=20)
tLeftN.place(relx=0.44, rely=0.04, height=20, width=20)

tRightE.place(relx=0.89, rely=0.29, height=20, width=20)
tStraightE.place(relx=0.89, rely=0.364, height=20, width=20)
tLeftE.place(relx=0.89, rely=0.438, height=20, width=20)

tRightS.place(relx=0.641, rely=0.915, height=20, width=20)
tStraightS.place(relx=0.575, rely=0.915, height=20, width=20)
tLeftS.place(relx=0.508, rely=0.915, height=20, width=20)

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

# 'Max flow rate' input text fields
tMaxFlowRate = tk.Text(top)
tMaxFlowRate.place(relx=0.775, rely=0.48, height=25, width=40)
tMaxFlowRate.insert('1.0', '2.0')

# Scenarios
currScenario = tk.StringVar(top)
currScenario.set("None") # set default scenario to 'None'

currDay = tk.StringVar(top)
currDay.set("Monday")

currDayTime = tk.StringVar(top)
currDayTime.set("Morning")

# Drop down menu
scenarios = tk.OptionMenu(top, currScenario, "None", "Construction", "Rainy Weather", "Accident")
scenarios.place(relx=0.775, rely=0.6, height=25, width=125)

days = tk.OptionMenu(top, currDay, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
days.place(relx=0.775, rely=0.68, height=25, width=125)

dayTime = tk.OptionMenu(top, currDayTime, "Morning", "Afternoon", "Evening", "Night")
dayTime.place(relx=0.775, rely=0.76, height=25, width=125)

# ---Buttons---
# 'Run Simulation' button
bRunSim = tk.Button(top, text="Run Simulation", bg="#90EE90")
bRunSim.place(relx=0.054, rely=0.11, height=34, width=97)

bStopSim = tk.Button(top, text="Stop", bg="#FFCCCB", state="disabled")
bStopSim.place(relx=0.18, rely=0.11, height=34, width=40)

bResetSim = tk.Button(top, text="Reset", bg="#FFBA00", state="normal")
bResetSim.place(relx=0.24, rely=0.11, height=34, width=40)


#-------------------------------------------------------------------------------
# FUNCTIONS

"""
description- Starts simulation when user clicks 'Run Simulation' button.
parameters-
    event- event object for callback binding
return- void
"""
def startSim(event=None):
    global currTime, startTime, currSecond, currCycle, simActive
    global greenLightW, greenLightN, greentLightE, greenLightS
    global redLightW, redLightN, redLightE, redLightS
    global carsInW, carsInN, carsInE, carsInS

    # disable text fields
    disableEdits()

    # get cycle length user inputs
    cycleLengths[0] = int(tTimeNS.get("1.0", "end-1c"));
    cycleLengths[1] = int(tTimeNSGrnArr.get("1.0", "end-1c"));
    cycleLengths[2] = int(tTimeWE.get("1.0", "end-1c"));
    cycleLengths[3] = int(tTimeWEGrnArr.get("1.0", "end-1c"));

    # set simulation to active
    simActive = True
    bRunSim["state"] = "disabled"
    bStopSim["state"] = "normal"

    # set up cycle timing
    startTime = time.time()
    currTime = time.time() - startTime
    currSecond = 0

    carsInW = float(tCarsInW.get("1.0", "end-1c"))
    carsInN = float(tCarsInN.get("1.0", "end-1c"))
    carsInE = float(tCarsInE.get("1.0", "end-1c"))
    carsInS = float(tCarsInS.get("1.0", "end-1c"))

    if (currCycle == 0): # North/South green cycle
        intersection.itemconfig(greenLightW, state="hidden")
        intersection.itemconfig(redLightW, state="normal")
        intersection.itemconfig(greenLightN, state="normal")
        intersection.itemconfig(redLightN, state="hidden")
        intersection.itemconfig(greenLightE, state="hidden")
        intersection.itemconfig(redLightE, state="normal")
        intersection.itemconfig(greenLightS, state="normal")
        intersection.itemconfig(redLightS, state="hidden")

        root.after(0, cycleNS)
    elif (currCycle == 1): # North/South green arrow cycle
        intersection.itemconfig(greenLightW, state="hidden")
        intersection.itemconfig(redLightW, state="normal")
        intersection.itemconfig(greenLightN, state="normal")
        intersection.itemconfig(redLightN, state="hidden")
        intersection.itemconfig(greenLightE, state="hidden")
        intersection.itemconfig(redLightE, state="normal")
        intersection.itemconfig(greenLightS, state="normal")
        intersection.itemconfig(redLightS, state="hidden")

        root.after(0, cycleNSGrnArr)
    elif (currCycle == 2): # East/West green cycle
        intersection.itemconfig(greenLightW, state="normal")
        intersection.itemconfig(redLightW, state="hidden")
        intersection.itemconfig(greenLightN, state="hidden")
        intersection.itemconfig(redLightN, state="normal")
        intersection.itemconfig(greenLightE, state="normal")
        intersection.itemconfig(redLightE, state="hidden")
        intersection.itemconfig(greenLightS, state="hidden")
        intersection.itemconfig(redLightS, state="normal")

        root.after(0, cycleWE)
    elif (currCycle == 3): # East/West green arrow cycle
        intersection.itemconfig(greenLightW, state="normal")
        intersection.itemconfig(redLightW, state="hidden")
        intersection.itemconfig(greenLightN, state="hidden")
        intersection.itemconfig(redLightN, state="normal")
        intersection.itemconfig(greenLightE, state="normal")
        intersection.itemconfig(redLightE, state="hidden")
        intersection.itemconfig(greenLightS, state="hidden")
        intersection.itemconfig(redLightS, state="normal")

        root.after(0, cycleWEGrnArr)
    else: # if not cycle 0-3, stop simulation
        simActive = False
        bRunSim["state"] = "normal"
        bStopSim["state"] = "disabled"
        lCurrCycle["text"] = "-"
        lCurrTime["text"] = 0
        currCycle = 0

"""
description- Cycles through North/South green state.
parameters- none
return- void
"""
def cycleNS():
    global currTime, startTime, currSecond, currCycle, cycleLengths, simActive
    global carsInN, carsInS, carsOutS, carsOutW, carsOutN, carsOutE

    # if simulation is active
    if (simActive):
        # if start of cycle (first second sample)
        if (currSecond == 0):
            # retrieve user inputs
            carsInN = float(tCarsInN.get("1.0", "end-1c"))
            carsInS = float(tCarsInS.get("1.0", "end-1c"))

            carsOutS = float(tCarsOutS.get("1.0", "end-1c"))
            carsOutW = float(tCarsOutW.get("1.0", "end-1c"))
            carsOutN = float(tCarsOutN.get("1.0", "end-1c"))
            carsOutE = float(tCarsOutE.get("1.0", "end-1c"))

            lCurrCycle["text"] = "N/S"

        # if time has not expired
        if (currTime < cycleLengths[currCycle]):
            if (currTime > currSecond):
                inflowCars()

                lCurrTime["text"] = currSecond + 1

                # calculate current rate
                currRate = calculateCurrRate(currTime)

                tCarsInN.configure(state = 'normal')
                tCarsOutS.configure(state = 'normal')
                tCarsOutW.configure(state = 'normal')

                tCarsInN.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInN >= 0):
                    tCarsOutS.delete("1.0", tk.END)
                    tCarsOutW.delete("1.0", tk.END)

                    # calculate cars in each lane
                    rightLaneCars = currRate * float(tRightN.get("1.0", "end-1c"))
                    straightLaneCars = currRate * float(tStraightN.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInN - (rightLaneCars + straightLaneCars)) <= 0):
                        # scale down right lane cars to match with actual cars waiting
                        rightLaneCars = round(carsInN * (rightLaneCars / (rightLaneCars + straightLaneCars)), 2)
                        # scale down straight lane cars
                        straightLaneCars = carsInN - rightLaneCars

                    carsInN -= (rightLaneCars + straightLaneCars)
                    carsOutS += straightLaneCars
                    carsOutW += rightLaneCars

                    tCarsInN.insert("1.0", math.floor(carsInN))
                    tCarsOutS.insert("1.0", math.floor(carsOutS))
                    tCarsOutW.insert("1.0", math.floor(carsOutW))

                    tCarsInN.configure(state = 'disabled')
                    tCarsOutS.configure(state = 'disabled')
                    tCarsOutW.configure(state = 'disabled')

                tCarsInS.configure(state = 'normal')
                tCarsOutN.configure(state = 'normal')
                tCarsOutE.configure(state = 'normal')

                tCarsInS.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInS >= 0):
                    tCarsOutN.delete("1.0", tk.END)
                    tCarsOutE.delete("1.0", tk.END)

                    # calculate cars in each lane
                    rightLaneCars = currRate * float(tRightS.get("1.0", "end-1c"))
                    straightLaneCars = currRate * float(tStraightS.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInS - (rightLaneCars + straightLaneCars)) <= 0):
                        # scale down right lane cars to match with actual cars waiting
                        rightLaneCars = round(carsInS * (rightLaneCars / (rightLaneCars + straightLaneCars)), 2)
                        # scale down straight lane cars
                        straightLaneCars = carsInS - rightLaneCars

                    carsInS -= (rightLaneCars + straightLaneCars)
                    carsOutN += straightLaneCars
                    carsOutE += rightLaneCars

                    tCarsInS.insert("1.0", math.floor(carsInS))
                    tCarsOutN.insert("1.0", math.floor(carsOutN))
                    tCarsOutE.insert("1.0", math.floor(carsOutE))

                    tCarsInS.configure(state = 'disabled')
                    tCarsOutN.configure(state = 'disabled')
                    tCarsOutE.configure(state = 'disabled')

                currSecond += 1
            currTime = time.time() - startTime
            root.after(sampleDelay, cycleNS)
        else:
            currCycle += 1
            root.after(0, startSim)

"""
description- Cycles through North/South green arrow state.
parameters- none
return- void
"""
def cycleNSGrnArr():
    global currTime, startTime, currSecond, currCycle, cycleLengths, simActive
    global carsInN, carsInS, carsOutE, carsOutW

    # if simulation is active
    if (simActive):
        # if start of cycle (first second sample)
        if (currSecond == 0):
            # retrieve user inputs
            carsInN = float(tCarsInN.get("1.0", "end-1c"))
            carsInS = float(tCarsInS.get("1.0", "end-1c"))

            carsOutE = float(tCarsOutE.get("1.0", "end-1c"))
            carsOutW = float(tCarsOutW.get("1.0", "end-1c"))

            lCurrCycle["text"] = "N/S Arrow"

        # if time has not expired
        if (currTime < cycleLengths[currCycle]):
            if (currTime > currSecond):
                inflowCars()

                lCurrTime["text"] = currSecond + 1

                # calculate current rate
                currRate = calculateCurrRate(currTime)

                tCarsInN.configure(state = 'normal')
                tCarsOutE.configure(state = 'normal')

                tCarsInN.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInN >= 0):
                    tCarsOutE.delete("1.0", tk.END)

                    # calculate cars in left lane
                    leftLaneCars = currRate * float(tLeftN.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInN - leftLaneCars) <= 0):
                        # scale down left lane cars to match with actual cars waiting
                        leftLaneCars = carsInN

                    carsInN -= leftLaneCars
                    carsOutE += leftLaneCars

                    tCarsInN.insert("1.0", math.floor(carsInN))
                    tCarsOutE.insert("1.0", math.floor(carsOutE))

                    tCarsInN.configure(state = 'disabled')
                    tCarsOutE.configure(state = 'disabled')

                tCarsInS.configure(state = 'normal')
                tCarsOutW.configure(state = 'normal')

                tCarsInS.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInS >= 0):
                    tCarsOutW.delete("1.0", tk.END)

                    # calculate cars in left lane
                    leftLaneCars = currRate * float(tLeftS.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInS - leftLaneCars) <= 0):
                        # scale down left lane cars to match with actual cars waiting
                        leftLaneCars = carsInS

                    carsInS -= leftLaneCars
                    carsOutW += leftLaneCars

                    tCarsInS.insert("1.0", math.floor(carsInS))
                    tCarsOutW.insert("1.0", math.floor(carsOutW))

                    tCarsInS.configure(state = 'disabled')
                    tCarsOutW.configure(state = 'disabled')

                currSecond += 1
            currTime = time.time() - startTime
            root.after(sampleDelay, cycleNSGrnArr)
        else:
            currCycle += 1
            root.after(0, startSim)

"""
description- Cycles through West/East green state.
parameters- none
return- void
"""
def cycleWE():
    global currTime, startTime, currSecond, currCycle, cycleLengths, simActive
    global carsInW, carsInE, carsOutE, carsOutS, carsOutW, carsOutN

    # if simulation is active
    if (simActive):
        # if start of cycle (first second sample)
        if (currSecond == 0):
            # retrieve user inputs
            carsInW = float(tCarsInW.get("1.0", "end-1c"))
            carsInE = float(tCarsInE.get("1.0", "end-1c"))

            carsOutE = float(tCarsOutE.get("1.0", "end-1c"))
            carsOutS = float(tCarsOutS.get("1.0", "end-1c"))
            carsOutW = float(tCarsOutW.get("1.0", "end-1c"))
            carsOutN = float(tCarsOutN.get("1.0", "end-1c"))

            lCurrCycle["text"] = "W/E"

        # if time has not expired
        if (currTime < cycleLengths[currCycle]):
            if (currTime > currSecond):
                inflowCars()

                lCurrTime["text"] = currSecond + 1

                # calculate current rate
                currRate = calculateCurrRate(currTime)

                tCarsInW.configure(state = 'normal')
                tCarsOutE.configure(state = 'normal')
                tCarsOutS.configure(state = 'normal')

                tCarsInW.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInW >= 0):
                    tCarsOutE.delete("1.0", tk.END)
                    tCarsOutS.delete("1.0", tk.END)

                    # calculate cars in each lane
                    rightLaneCars = currRate * float(tRightW.get("1.0", "end-1c"))
                    straightLaneCars = currRate * float(tStraightW.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInW - (rightLaneCars + straightLaneCars)) <= 0):
                        # scale down right lane cars to match with actual cars waiting
                        rightLaneCars = round(carsInW * (rightLaneCars / (rightLaneCars + straightLaneCars)), 2)
                        # scale down straight lane cars
                        straightLaneCars = carsInW - rightLaneCars

                    carsInW -= (rightLaneCars + straightLaneCars)
                    carsOutE += straightLaneCars
                    carsOutS += rightLaneCars

                    tCarsInW.insert("1.0", math.floor(carsInW))
                    tCarsOutE.insert("1.0", math.floor(carsOutE))
                    tCarsOutS.insert("1.0", math.floor(carsOutS))

                    tCarsInW.configure(state = 'disabled')
                    tCarsOutE.configure(state = 'disabled')
                    tCarsOutS.configure(state = 'disabled')

                tCarsInE.configure(state = 'normal')
                tCarsOutW.configure(state = 'normal')
                tCarsOutN.configure(state = 'normal')

                tCarsInE.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInE >= 0):
                    tCarsOutW.delete("1.0", tk.END)
                    tCarsOutN.delete("1.0", tk.END)

                    # calculate cars in each lane
                    rightLaneCars = currRate * float(tRightE.get("1.0", "end-1c"))
                    straightLaneCars = currRate * float(tStraightE.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInE - (rightLaneCars + straightLaneCars)) <= 0):
                        # scale down right lane cars to match with actual cars waiting
                        rightLaneCars = round(carsInE * (rightLaneCars / (rightLaneCars + straightLaneCars)), 2)
                        # scale down straight lane cars
                        straightLaneCars = carsInE - rightLaneCars

                    carsInE -= (rightLaneCars + straightLaneCars)
                    carsOutW += straightLaneCars
                    carsOutN += rightLaneCars

                    tCarsInE.insert("1.0", math.floor(carsInE))
                    tCarsOutW.insert("1.0", math.floor(carsOutW))
                    tCarsOutN.insert("1.0", math.floor(carsOutN))

                    tCarsInE.configure(state = 'disabled')
                    tCarsOutW.configure(state = 'disabled')
                    tCarsOutN.configure(state = 'disabled')

                currSecond += 1
            currTime = time.time() - startTime
            root.after(sampleDelay, cycleWE)
        else:
            currCycle += 1
            root.after(0, startSim)

"""
description- Cycles through West/East green arrow state.
parameters- none
return- void
"""
def cycleWEGrnArr():
    global currTime, startTime, currSecond, currCycle, cycleLengths, simActive
    global carsInW, carsInE, carsOutN, carsOutS

    # if simulation is active
    if (simActive):
        # if start of cycle (first second sample)
        if (currSecond == 0):
            # retrieve user inputs
            carsInW = float(tCarsInW.get("1.0", "end-1c"))
            carsInE = float(tCarsInE.get("1.0", "end-1c"))

            carsOutN= float(tCarsOutN.get("1.0", "end-1c"))
            carsOutS = float(tCarsOutS.get("1.0", "end-1c"))

            lCurrCycle["text"] = "W/E Arrow"

        # if time has not expired
        if (currTime < cycleLengths[currCycle]):
            if (currTime > currSecond):
                inflowCars()

                lCurrTime["text"] = currSecond + 1

                # calculate current rate
                currRate = calculateCurrRate(currTime)

                tCarsInW.configure(state = 'normal')
                tCarsOutN.configure(state = 'normal')

                tCarsInW.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInW >= 0):
                    tCarsOutN.delete("1.0", tk.END)

                    # calculate cars in left lane
                    leftLaneCars = currRate * float(tLeftW.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInW - leftLaneCars) <= 0):
                        # scale down left lane cars to match with actual cars waiting
                        leftLaneCars = carsInW

                    carsInW -= leftLaneCars
                    carsOutN += leftLaneCars

                    tCarsInW.insert("1.0", math.floor(carsInW))
                    tCarsOutN.insert("1.0", math.floor(carsOutN))

                    tCarsInW.configure(state = 'disabled')
                    tCarsOutN.configure(state = 'disabled')

                tCarsInE.configure(state = 'normal')
                tCarsOutS.configure(state = 'normal')

                tCarsInE.delete("1.0", tk.END)

                # if cars are waiting
                if (carsInE >= 0):
                    tCarsOutS.delete("1.0", tk.END)

                    # calculate cars in left lane
                    leftLaneCars = currRate * float(tLeftE.get("1.0", "end-1c"))

                    # if 'cars in' will be negative
                    if ((carsInE - leftLaneCars) <= 0):
                        # scale down left lane cars to match with actual cars waiting
                        leftLaneCars = carsInE

                    carsInE -= leftLaneCars
                    carsOutS += leftLaneCars

                    tCarsInE.insert("1.0", math.floor(carsInE))
                    tCarsOutS.insert("1.0", math.floor(carsOutS))

                    tCarsInE.configure(state = 'disabled')
                    tCarsOutS.configure(state = 'disabled')

                currSecond += 1
            currTime = time.time() - startTime
            root.after(sampleDelay, cycleWEGrnArr)
        else:
            currCycle = 0
            root.after(0, startSim)

"""
description- Inflow cars waiting at intersection based on user input.
parameters- none
return- void
"""
def inflowCars():
    global carsInW, carsInN, carsInE, carsInS

    carsInW += float(tInflowW.get("1.0", "end-1c"))
    carsInN += float(tInflowN.get("1.0", "end-1c"))
    carsInE += float(tInflowE.get("1.0", "end-1c"))
    carsInS += float(tInflowS.get("1.0", "end-1c"))

    tCarsInW.configure(state = 'normal')
    tCarsInN.configure(state = 'normal')
    tCarsInE.configure(state = 'normal')
    tCarsInS.configure(state = 'normal')

    tCarsInW.delete("1.0", tk.END)
    tCarsInN.delete("1.0", tk.END)
    tCarsInE.delete("1.0", tk.END)
    tCarsInS.delete("1.0", tk.END)

    tCarsInW.insert("1.0", math.floor(carsInW))
    tCarsInN.insert("1.0", math.floor(carsInN))
    tCarsInE.insert("1.0", math.floor(carsInE))
    tCarsInS.insert("1.0", math.floor(carsInS))

    tCarsInW.configure(state = 'disabled')
    tCarsInN.configure(state = 'disabled')
    tCarsInE.configure(state = 'disabled')
    tCarsInS.configure(state = 'disabled')

"""
description- Stops the simulation if running.
parameters-
    event- event object for callback binding
return- void
"""
def stopSim(event=None):
    global simActive
    global tCarsOutE, tCarsOutN, tCarsOutS, tCarsOutW
    global carsInN, carsInS, carsInW, carsInE
    simActive = False
    # enable user inputs
    enableEdits()
    bRunSim["state"] = "normal"
    bStopSim["state"] = "disabled"

"""
description- Resets the simulation if running.
parameters-
    event - event object for callback binding
return- void
"""
def resetSim(event=None):
    global simActive
    global tCarsOutE, tCarsOutN, tCarsOutS, tCarsOutW
    global carsInN, carsInS, carsInW, carsInE
    simActive = False
    # enable user inputs
    enableEdits()
    bRunSim["state"] = "normal"
    bStopSim["state"] = "disabled"

    # reset fields to defaults
    tCarsOutS.delete('1.0', tk.END)
    tCarsOutW.delete('1.0', tk.END)
    tCarsOutN.delete('1.0', tk.END)
    tCarsOutE.delete('1.0', tk.END)

    tCarsOutW.insert('1.0', '0')
    tCarsOutN.insert('1.0', '0')
    tCarsOutE.insert('1.0', '0')
    tCarsOutS.insert('1.0', '0')

    tCarsInS.delete('1.0', tk.END)
    tCarsInW.delete('1.0', tk.END)
    tCarsInN.delete('1.0', tk.END)
    tCarsInE.delete('1.0', tk.END)

    tCarsInW.insert('1.0', '30')
    tCarsInN.insert('1.0', '30')
    tCarsInE.insert('1.0', '30')
    tCarsInS.insert('1.0', '30')

"""
description- Returns the traffic flow rate at a specific time since GREEN light activated.
parameters-
    t- current time (second) since green light activated
return-
    flowRate- flow rate at specific time
"""
def calculateCurrRate(t):
    global maxFlowRate, flowRateScalar, flowDelayScalar
    # divide flow rate by 2
    maxFlowRate = float(tMaxFlowRate.get("1.0", "end-1c")) / 2
    # calculate y offset
    offsetY = maxFlowRate * flowRateScalar

    # calculate flow rate
    flowRate = (flowRateScalar * (maxFlowRate * (math.tanh((flowDelayScalar * t) - math.pi) + offsetY)))

    # In rare cases where flow rate drops below zero, make flow rate zero
    # (this may occur due to increased precision and the fact that floats
    # only store 32 bits. Thus, the negative value is very small but would cause
    # program to drop one car since the number of cars is rounded down, or floored)
    if (flowRate <= 0):
        flowRate = 0

    return flowRate

"""
description- Updates flow rate/flow delay scalars based on scenario selection.
parameters-
    args
return- void
"""
def scenarioChange(*args):
    global flowRateScalar, flowDelayScalar

    # change based on selected scenario
    if (currScenario.get() == "None"):
        flowRateScalar = 1
        flowDelayScalar = 1
    elif (currScenario.get() == "Construction"):
        flowRateScalar = 0.5
        flowDelayScalar = 0.5
    elif (currScenario.get() == "Rainy Weather"):
        flowRateScalar = 0.85
        flowDelayScalar = 0.75
    elif (currScenario.get() == "Accident"):
        flowRateScalar = 0.4
        flowDelayScalar = 0.5

"""
description- Updates flow rate/flow delay scalars based on day selection.
parameters-
    args
return- void
"""
def dayChange(*args):
    global flowRateScalar, flowDelayScalar

    # change based on selected day of week
    if(currDay.get() == "Monday" or currDay.get() == "Wednesday" or currDay.get() == "Friday"):
        flowRateScalar = 1
        flowDelayScalar = 1
    elif (currDay.get() == "Tuesday" or currDay.get() == "Thursday"):
        flowRateScalar = 0.6
        flowDelayScalar = 0.6
    elif(currDay.get() == "Saturday" or currDay.get() == "Sunday"):
        flowRateScalar = 1.2
        flowDelayScalar = 1

"""
description- Updates flow rate/flow delay scalars based on time of day selection.
parameters-
    args
return- void
"""
def timeChange(*args):
    global flowRateScalar, flowDelayScalar

    # change based on selected time of day
    if(currDayTime.get() == "Morning" or currDayTime.get() == "Evening"):
        flowRateScalar = 0.5
        flowDelayScalar = 0.4
    elif(currDayTime.get() == "Afternoon"):
        flowRateScalar = 1
        flowDelayScalar = 1
    elif(currDayTime.get() == "Night"):
        flowRateScalar = 1.5
        flowDelayScalar = 1

"""
description- Disables all text boxes so that user cannot modify them.
parameters- none
return- void
"""
def disableEdits():
	tCarsInW.configure(state = 'disabled')
	tCarsInN.configure(state = 'disabled')
	tCarsInE.configure(state = 'disabled')
	tCarsInS.configure(state = 'disabled')
	tCarsOutW.configure(state = 'disabled')
	tCarsOutN.configure(state = 'disabled')
	tCarsOutE.configure(state = 'disabled')
	tCarsOutS.configure(state = 'disabled')
	tTimeNS.configure(state = 'disabled')

	tTimeNSGrnArr.configure(state = 'disabled')
	tTimeWE.configure(state = 'disabled')
	tTimeWEGrnArr.configure(state = 'disabled')

	tInflowW.configure(state = 'disabled')
	tInflowN.configure(state = 'disabled')
	tInflowE.configure(state = 'disabled')
	tInflowS.configure(state = 'disabled')

	tRightW.configure(state = 'disabled')
	tStraightW.configure(state = 'disabled')
	tLeftW.configure(state = 'disabled')

	tRightN.configure(state = 'disabled')
	tStraightN.configure(state = 'disabled')
	tLeftN.configure(state = 'disabled')

	tRightE.configure(state = 'disabled')
	tStraightE.configure(state = 'disabled')
	tLeftE.configure(state = 'disabled')

	tRightS.configure(state = 'disabled')
	tStraightS.configure(state = 'disabled')
	tLeftS.configure(state = 'disabled')

	tMaxFlowRate.configure(state = 'disabled')

"""
description- Enables all text boxes so that users can modify them.
parameters- none
return- void
"""
def enableEdits():
	tCarsInW.configure(state = 'normal')
	tCarsInN.configure(state = 'normal')
	tCarsInE.configure(state = 'normal')
	tCarsInS.configure(state = 'normal')
	tCarsOutW.configure(state = 'normal')
	tCarsOutN.configure(state = 'normal')
	tCarsOutE.configure(state = 'normal')
	tCarsOutS.configure(state = 'normal')
	tTimeNS.configure(state = 'normal')

	tTimeNSGrnArr.configure(state = 'normal')
	tTimeWE.configure(state = 'normal')
	tTimeWEGrnArr.configure(state = 'normal')

	tInflowW.configure(state = 'normal')
	tInflowN.configure(state = 'normal')
	tInflowE.configure(state = 'normal')
	tInflowS.configure(state = 'normal')

	tRightW.configure(state = 'normal')
	tStraightW.configure(state = 'normal')
	tLeftW.configure(state = 'normal')

	tRightN.configure(state = 'normal')
	tStraightN.configure(state = 'normal')
	tLeftN.configure(state = 'normal')

	tRightE.configure(state = 'normal')
	tStraightE.configure(state = 'normal')
	tLeftE.configure(state = 'normal')

	tRightS.configure(state = 'normal')
	tStraightS.configure(state = 'normal')
	tLeftS.configure(state = 'normal')

	tMaxFlowRate.configure(state = 'normal')

# CALLBACK BINDINGS
bRunSim.bind("<Button-1>", startSim)
bStopSim.bind("<Button-1>", stopSim)
bResetSim.bind("<Button-1>", resetSim)

currScenario.trace('w', scenarioChange)
currDay.trace('w', dayChange)
currDayTime.trace('w', timeChange)

#-------------------------------------------------------------------------------

# start main loop
root.mainloop()

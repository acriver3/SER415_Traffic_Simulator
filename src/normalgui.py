# SER415 Traffic Simulator - Team 6
# Manolito Ramirez, Jessica Gilbert, Mike Wagner,
# Carlos Franco, Arthur Rivera, and Ryan Kirmis
# Version 1.1.1

import tkinter as tk
import tkinter.ttk

root = tkinter.Tk()

top = tk.Canvas(root, width=739, height=535, bg="#C0C5C6")
top.pack();
top.create_text((20, 10), text="Traffic Simulator", font="MSGothic 20 bold", fill="#065535", anchor="nw")
top.create_text((500, 50), text="Cycle Timing", font="MSGothic 15 bold", fill="#065535", anchor="nw")

root.geometry("739x535+503+155")
root.minsize(120, 1)
root.maxsize(1924, 1061)
root.resizable(0, 0)
root.title("Traffic Simulator GUI")
root.configure(background="#d9d9d9")

main_bg = tk.PhotoImage(file="../resources/intersection.png")

# ---Frames---
fTiming = tk.Frame(top,  bg="#707070", highlightbackground="#065535", highlightthickness=3)
f2 = tk.Frame(top)
f3 = tk.Frame(top)

fTiming.place(relx=0.67, rely=0.15, relheight=0.215, relwidth=0.277)
f2.place(relx=0.785, rely=0.411, relheight=0.215, relwidth=0.169)
f3.place(relx=0.447, rely=0.019, relheight=0.084, relwidth=0.223)


# ---Labels---
lIntersection = tk.Label(top, image=main_bg)
lIntersection.place(relx=0.13, rely=0.2, height=341, width=371)


# ---Text fields---
# 'Number of cars' text fields
tCarsW = tk.Text(top)
tCarsN = tk.Text(top)
tCarsE = tk.Text(top)
tCarsS = tk.Text(top)

# 'Cycle times' text fields
tTimeNS = tk.Text(fTiming)
tTimeNSGrnArr = tk.Text(fTiming)
tTimeWE = tk.Text(fTiming)
tTimeWEGrnArr = tk.Text(fTiming)

tCarsW.place(relx=0.05, rely=0.57, relheight=0.045, relwidth=0.06)
tCarsN.place(relx=0.3, rely=0.135, relheight=0.045, relwidth=0.06)
tCarsE.place(relx=0.65, rely=0.43, relheight=0.045, relwidth=0.06)
tCarsS.place(relx=0.404, rely=0.86, relheight=0.045, relwidth=0.06)

tTimeNS.place(relx=0.5, rely=0.05, height=20, width=45)
tTimeNSGrnArr.place(relx=0.5, rely=0.275, height=20, width=45)
tTimeWE.place(relx=0.5, rely=0.5, height=20, width=45)
tTimeWEGrnArr.place(relx=0.5, rely=0.725, height=20, width=45)

# ---Buttons---
# 'Run Simulation' button
bRunSim = tk.Button(top, text="Run Simulation", bg = "#90EE90")

bRunSim.place(relx=0.054, rely=0.11, height=34, width=97)

#-------------------------------------------------------------------------------
# CALLBACK FUNCTIONS
def startSim(event):
    print("Running simulation")

# CALLBACK BINDINGS
bRunSim.bind("<Button-1>", startSim)

#-------------------------------------------------------------------------------

root.mainloop()

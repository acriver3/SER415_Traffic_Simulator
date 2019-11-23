import tkinter as tk
import tkinter.ttk

top = tkinter.Tk()

top.geometry("739x535+503+155")
top.minsize(120, 1)
top.maxsize(1924, 1061)
top.resizable(1, 1)
top.title("Traffic Simulator GUI")
top.configure(background="#d9d9d9")

main_bg = tk.PhotoImage(file="../resources/test.png")

# Code to add widgets will go here...
t1 = tk.Text(top)
t2 = tk.Text(top)
t3 = tk.Text(top)
t4 = tk.Text(top)
t5 = tk.Text(top)
t6 = tk.Text(top)
t7 = tk.Text(top)
t8 = tk.Text(top)

l1 = tk.Label(top, image=main_bg)



t1.place(relx=0.041, rely=0.374, relheight=0.045, relwidth=0.06)
t2.place(relx=0.041, rely=0.43, relheight=0.045, relwidth=0.06)
t3.place(relx=0.406, rely=0.766, relheight=0.045, relwidth=0.06)
t4.place(relx=0.487, rely=0.766, relheight=0.045, relwidth=0.06)
t5.place(relx=0.704, rely=0.336, relheight=0.045, relwidth=0.06)
t6.place(relx=0.704, rely=0.411, relheight=0.045, relwidth=0.06)
t7.place(relx=0.23, rely=0.019, relheight=0.045, relwidth=0.073)
t8.place(relx=0.338, rely=0.019, relheight=0.045, relwidth=0.073)

l1.place(relx=0.162, rely=0.112, height=341, width=371)

top.mainloop()
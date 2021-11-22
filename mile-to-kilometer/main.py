from tkinter import *

def mile_to_kilometer():
    miles=float(miles_input.get())
    km=miles * 1.609
    kilometer.config(text=f"{km}")

window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

equal=Label(text="is equels to label")
equal.grid(column=0,row=1)

kilometer=Label(text="0")
kilometer.grid(column=1,row=1)

kilometer_label=Label(text="KM")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=mile_to_kilometer)
calculate_button.grid(column=1,row=2)



window.mainloop()
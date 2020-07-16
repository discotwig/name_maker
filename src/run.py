"""
    A string concatonater app. 
Is a gui with two columns [Strings, Cities] and two buttons [Reset, Concat]. Creates phrases usings the same defined strings for each city.
"""

import tkinter as tk
from tkinter import ttk


class City:
    def __init__(self):
        self.entry_for_city = None
        self.label_for_city = None

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.grid()        
         
        self.string_lbl = tk.Label(self.root, text="String:")
        self.string_lbl.grid(row=0, column=0)

        self.keyword_lbl = tk.Label(self.root, text="Keyword:")
        self.keyword_lbl.grid(row=1, column=0)

        self.string_ent = tk.Entry(self.root)
        self.string_ent.grid(row=0, column=1)

        self.keyword_ent = tk.Entry(self.root)
        self.keyword_ent.grid(row=1, column=1)

        

    def run(self):
        self.root.mainloop()






# def main():
#     city = City()


#     cities = []

#     # The Entry box, into which the user can enter a temperature.
#     # We store it in the Temperature object so that we can later
#     # get its contents.
#     city_entry = ttk.Entry(frame, width=8)
#     city_entry.grid()


# def add_city(City):
#     entry = city.entry_for_temperature
#     contents_of_entry_box = entry.get()

    

#     # Convert that STRING to a floating point NUMBER.
#     # Use the number to compute the corresponding Celsius temperature.
#     fahrenheit = float(contents_of_entry_box)
#     celsius = (5 / 9) * (fahrenheit - 32)

#     # Display the computed Celsius temperature in the Label
#     # provided for it.
#     format_string = '{:0.2f} Fahrenheit is {:0.2f} Celsius'
#     answer = format_string.format(fahrenheit, celsius)
#     temperature.label_for_temperature['text'] = answer



app = App()
app.run()

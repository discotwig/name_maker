"""
    A string concatonater app. 
Is a gui with two columns [Strings, Cities] and two buttons [Reset, Concat]. Creates phrases usings the same defined strings for each city.
"""

import tkinter as tk
from tkinter import ttk


class City:
    def __init__(self, entry):
        self.entry_for_city = entry
        self.label_for_city = None

class Keystring:
    def __init__(self, entry):
        self.entry_for_keystring = entry
        self.label_for_keystring = None

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Phrase Maker")

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.grid()

        # Left Phrase Label
        self.phrase_lbl = ttk.Label(self.frame, text="Phrase:")
        self.phrase_lbl.grid(row=0, column=0)

        # Left Phrase Entry
        self.phrase_ent = ttk.Entry(self.frame)
        self.phrase_ent.grid(row=0, column=1)

        # Right City Label
        self.city_lbl = ttk.Label(self.frame, text="City:")
        self.city_lbl.grid(row=0, column=2)

        # Right City Entry
        self.city_ent = ttk.Entry(self.frame)
        self.city_ent.grid(row=0, column=3)

        # Left Keyword Label
        self.keyword_lbl = ttk.Label(self.frame, text="Keyword:")
        self.keyword_lbl.grid(row=1, column=0)

        # Left Keyword Entry
        self.keyword_ent = ttk.Entry(self.frame)
        self.keyword_ent.grid(row=1, column=1)

        # Right Add Button
        self.add_btn = ttk.Button(self.frame, text='Add')
        self.add_btn.grid(row=1, column=2)
        self.add_btn['command'] = lambda: self.add_city(self.city_ent)
        
        # Right Delete Button
        self.delete_btn = ttk.Button(self.frame, text='Clear')
        self.delete_btn.grid(row=1, column=3)
        self.delete_btn['command'] = lambda: self.delete()        

        # Left Reset Button
        self.reset_btn = ttk.Button(self.frame, text='Reset')
        self.reset_btn.grid(row=2, column=0)
        self.reset_btn['command'] = lambda: self.reset_app()

        # Left Create Button
        self.create_btn = ttk.Button(self.frame, text='Create')
        self.create_btn.grid(row=2, column=1)
        self.create_btn['command'] = lambda: self.create_txt()        

        # Right Listbox
        self.city_lbx = tk.Listbox(self.frame)
        self.city_lbx.grid(row=2, column=2, columnspan=2)

        # Right Clear Button
        self.clear_btn = ttk.Button(self.frame, text='Clear')
        self.clear_btn.grid(row=3, column=3)
        self.clear_btn['command'] = lambda: self.clear()

    def add_city(self, city):
        #self.city_lbx.insert(END, item)        
        pass

    def create_txt(self):
        pass

    def clear(self):
        pass

    def reset_app(self):
        pass

    def delete(self):
        pass    

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

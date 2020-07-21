"""
    A string concatonater app. 
Is a gui with two columns [Strings, Cities] and two buttons [Reset, Concat]. Creates phrases usings the same defined strings for each city.
"""

import sys
import os
import datetime as dt

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import re


class App (ttk.Frame):
    def __init__(self, master=None):
        """On Start."""
        ttk.Frame.__init__(self, master=None, padding=20)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """Creates the GUI with grid."""

        # Phrase Label
        self.phrase_lbl = ttk.Label(self, text="Phrase:", style="TLabel")
        self.phrase_lbl.grid(row=0, column=0)

        # Phrase Entry
        self.phrase_ent = ttk.Entry(self)
        self.phrase_ent.grid(row=0, column=1)

        # City Label
        self.city_lbl = ttk.Label(self, text="City:")
        self.city_lbl.grid(row=0, column=2)

        # City Entry
        self.city_ent = ttk.Entry(self)
        self.city_ent.grid(row=0, column=3)

        # Keyword Label
        self.keyword_lbl = ttk.Label(self, text="Keyword:")
        self.keyword_lbl.grid(row=1, column=0)

        # Keyword Entry
        self.keyword_ent = ttk.Entry(self)
        self.keyword_ent.grid(row=1, column=1)

        # Add Button
        self.add_btn = ttk.Button(self, text="Add")
        self.add_btn.grid(row=1, column=2)
        self.add_btn["command"] = lambda: self.addCity(self.city_ent.get())
        
        # Delete Button
        self.delete_btn = ttk.Button(self, text="Delete")
        self.delete_btn.grid(row=1, column=3)
        self.delete_btn["command"] = lambda: self.deleteCity()        

        # Reset Button
        self.reset_btn = ttk.Button(self, text="Reset")
        self.reset_btn.grid(row=2, column=0)
        self.reset_btn["command"] = lambda: self.resetApp()

        # Create Button
        self.create_btn = ttk.Button(self, text="Create")
        self.create_btn.grid(row=2, column=1)
        self.create_btn["command"] = lambda: self.createTXT()        

        # Listbox
        self.city_lbx = tk.Listbox(self)
        self.city_lbx.grid(row=2, column=2, columnspan=2)
        
        # Directory Button
        self.dir_btn = ttk.Button(self, text="Select Folder")
        self.dir_btn.grid(row=3, column=0)
        self.dir_btn["command"] = lambda: self.getDir()

        # Directory Label
        self.dir_lbl = ttk.Label(self, text="No Folder Selected")
        self.dir_lbl.grid(row=3, column=1)        

        # Clear Button
        self.clear_btn = ttk.Button(self, text="Clear")
        self.clear_btn.grid(row=3, column=3)
        self.clear_btn["command"] = lambda: self.clearCities()

    def addCity(self, city):
        """From entry add city to listbox."""
        if city:
            self.city_lbx.insert(0, str(city).strip())
            self.city_ent.delete(0, "end")
            self.city_ent.focus()

    def phraseMaker(self):
        """Replaces desired word in phrase with each city."""
        phrase_lst = []
        phrase = str(self.phrase_ent.get())
        keyword = str(self.keyword_ent.get())
        for i in range(self.city_lbx.size()):
            city = str(self.city_lbx.get(i))
            new_phrase = re.sub(keyword, city, phrase)
            phrase_lst.append(new_phrase)
        return phrase_lst

    def createTXT(self):
        """Creates txt file containing all of the desired phrases."""
        now = dt.datetime.now().strftime("%Y_%m_%d %H_%M_%S")
        try:
            desired_list = self.phraseMaker()
            with open(f"{self.folder}/{now}.txt", "w") as f:
                for i in desired_list:
                    f.write(f"{i}\n")

        except Exception as e:
            self.dir_lbl["text"] = e

    def clearCities(self):
        """Removes all city entries from listbox."""
        self.city_lbx.delete(0, "end")

    def resetApp(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def deleteCity(self):
        """Remove last city entry from listbox."""
        self.city_lbx.delete(0)

    def getDir(self):
        """Get specified directory from user."""
        self.folder = filedialog.askdirectory()
        self.dir_lbl["text"] = self.folder

    def run(self):
        """Runs the app."""
        self.mainloop()


app = App()
app.run()

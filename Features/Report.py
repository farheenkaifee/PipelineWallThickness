import csv
import pandas as pd
from tkinter import filedialog
import random
from PyQt5.QtWidgets import QMessageBox


<<<<<<< HEAD
def report(Measured_Minimum_Thickness_for_Test_Pressure_t1, Depth, fy, fu, fcb, Pt, Plt, Pe, Pb_t1, Pmpt ):
        print(f"\n\tSaving file....!!!")
        try:
                
                filepath = filedialog.asksaveasfilename(
                # os.getenv('home'),
                        initialdir= "C:/Users/DELL/Desktop",
                        title= "Save As",
                        defaultextension= "*.csv",
                        filetypes=(
                                ("csv file","*.csv"),
                                ("HTML file","*.html"),
                                ("text file","*.txt"),
                                ("All file","*.*")
                        )
                )
        except:
                print(f"error code:{random.random()}>>>>>>Error in saving file while opening to write..$$%%^^&&&")
        try:
                if filepath is None:
                        return
                else:
                        with open(filepath, 'w'):
                                df = pd.DataFrame({"SL no" : [1,2,3,4,5,6,7,8,9,10], "INPUTS": ["Measured_Minimum_Thickness_for_Test_Pressure_t1","Depth", "fy", "fu", "fcb", "Pt", "Plt", "Pe", "Pb_t1", "Pmpt" ], "Values": [Measured_Minimum_Thickness_for_Test_Pressure_t1, Depth, fy, fu, fcb, Pt, Plt, Pe, Pb_t1, Pmpt ]})
                                df.to_csv(filepath)
        except:
            print(f"error code:{random.random()}>>>>>>ERROR in saving your file...!!")
            QMessageBox.warning(None, "Warning", 'File is not saved..!!!!')



=======


def report(variable):
    print(f"Hello there your report is being prepared..!!!\n\t\t{variable}")
    try:
                
        filepath = filedialog.asksaveasfilename(
        # os.getenv('home'),
                initialdir= "C:/Users/DELL/Desktop",
                title= "Save As",
                defaultextension= "*.csv",
                filetypes=(
                        ("csv file","*.csv"),
                        ("HTML file","*.html"),
                        ("text file","*.txt"),
                        ("All file","*.*")
                )
        )
        print(filepath)
    except:
        print(f"error code:{random.random()}>>>>>>Error in saving file while opening to write..$$%%^^&&&")
    try:
        if filepath is None:
                return
        else:
            with open(filepath, 'w'):
                    df = pd.DataFrame({"Values": variable})
                    df.to_csv(filepath)
    except:
        print(f"error code:{random.random()}>>>>>>ERROR in saving your file...!!")
        QMessageBox.warning(None, "Warning", 'File is not saved..!!!!')
>>>>>>> 5e881c98f0cf228e1c38b85c40d016d007a6bf46

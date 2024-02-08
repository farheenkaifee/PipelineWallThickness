import csv
import pandas as pd
from tkinter import filedialog
import random
from PyQt5.QtWidgets import QMessageBox




def report(variable):
    print(f"Hello there your report is being prepared..!!!\n\t\t{variable}")
    try:
                
        filepath = filedialog.asksaveasfilename(
        # os.getenv('home'),
                initialdir= "C:/Users/DELL/Desktop",
                title= "Report",
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
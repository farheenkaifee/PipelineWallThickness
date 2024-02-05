import pandas as pd
from tkinter import filedialog

def fileread(open_List):
    print(f"\n\t Opening your file please wait..!!")
    filepath = filedialog.askopenfilename(
            initialdir="C:/Users/DELL/Desktop",
            title= "Open csv file...!!",
            defaultextension= "*.csv",
            filetypes=(
                ("csv file","*.csv"),
                ("HTML file","*.html"),
                ("text file","*.txt"),
                ("All file","*.*")
            )
        )
    try:
            if filepath is None:
                return
            else:
                with open(filepath,'r'):
                    df = pd.read_csv(filepath)
                    column_To_Read = df["Values"].tolist()
                    open_List.clear()
                    open_List.extend(column_To_Read)
    except:
            print("ERROR in opening your file...!!")
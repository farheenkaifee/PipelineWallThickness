# Save a string to a file
# with open("myfile.txt", "w") as f:
#     f.write("Hello, world!")

# Save a list to a file
# with open("myfile.txt", "w") as f:
#     f.writelines(["Hello", "world!"])

# # Save a dictionary to a file
# import json

# with open("myfile.json", "w") as f:
    
#     json.dump({"name": "John Doe", "age": 30}, f)

# # Save a NumPy array to a file
# import numpy as np

# np.save("myfile.npy", np.array([1, 2, 3]))

# # Save a Pandas DataFrame to a file
import pandas as pd

df = pd.DataFrame({"name": ["John Doe", "Jane Doe"], "age": [30, 25]})
df.to_csv("myfile.csv")
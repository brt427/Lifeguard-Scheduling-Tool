import pandas as pd



# Assuming the Excel file is named "staff_data.xlsx" and the data is in a sheet named "Sheet1"
excel_file = "hayward.xlsx"
sheet_name = "s4"

# Read the data from the Excel file into a pandas DataFrame
data_frame = pd.read_excel(excel_file, sheet_name=sheet_name)

# Convert the DataFrame to a list of lists (staff_data_list)
staff_data_list = data_frame.values.tolist()

# If the Excel file has column headers, you can skip the first row in the list
# staff_data_list = data_frame.values.tolist()[1:]

#print(staff_data_list)


class Staff:
    def __init__(self, name, co, to, lg, nickname):
        self.name = name
        self.nickname = nickname
        self.co = co
        self.to = to
        self.lg = lg
        self.eligible = True
        self.score = 0
    def __str__(self):
        
        return("%s"%(self.name))
        #return("%s; CO: %s; TO: %s" %(self.name,self.co, self.to))



# List of staff data in the format [name, username, shift, is_active]
"""
staff_data_list = [
    ["Thomas", "CharlieF", "3-6", False],
    ["John", "JohnDoe", "9-5", True],
    ["Alice", "Wonderland", "2-10", True],
    # Add more staff data here if needed
]
"""
# Assuming self.items is an empty list to start with
master_list = []

# Loop through the staff_data_list and create Staff objects
for data in staff_data_list:
    name, co, to, lg , nickname = data
    staff_obj = Staff(name, co, to, lg, nickname)
    master_list.append(staff_obj)

for thing in master_list:
    
    #print(thing.name,thing.co,thing.to,thing.lg,thing.score,thing.eligible)
    pass

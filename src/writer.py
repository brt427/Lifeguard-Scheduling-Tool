import pandas as pd

class Staff:
    def __init__(self, name, partner, time_slot, is_available):
        self.name = name
        self.partner = partner
        self.time_slot = time_slot
        self.is_available = is_available

def create_excel_from_staff_data(staff_list, output_file):
    # Extract the data from the Staff objects
    data = [[staff.name, staff.partner, staff.time_slot, staff.is_available] for staff in staff_list]

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=["Name", "Partner", "Time Slot", "Is Available"])

    # Write the DataFrame to an Excel file
    df.to_excel(output_file, index=False)
        


    output_excel_path = "writer.xlsx"  # Replace this with the desired path for the output Excel file

    create_excel_from_staff_data(staff_objects, output_excel_path)

    # Read the Excel file back into a DataFrame
read_df = pd.read_excel("writer.xlsx")

# Display the DataFrame contents
print(read_df)


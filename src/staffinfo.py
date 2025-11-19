from staff import Staff
import reader


class Staffinfo:

    def __init__(self):
        self.items=[]
        
    def initialize(self):

        self.items.append(reader.master_list)
        
        
        
        """
        #Example Format 
        
        #self.items.append(Staff("Blake Thomas",None,"0-2",True))
       
        
        """


    def __str__(self):
        """
        Returns formatted string of all of the objects in the inventory 
        with index numbers
        Inputs: None
        Outputs: A formatted inventory string 
        """

        
        
        inventory = ""
        for i in range(len(self.items)):
            inventory = inventory + str(i+1) + "-" + str(self.items[i]) + "\n"
        
        return inventory

        


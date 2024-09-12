from staffinfo import Staffinfo
import reader


#Creates and instantiates a new object with the inventory
"""
staff_list = Staffinfo()
staff_list.initialize()
"""

staff_list=reader.master_list

#Requirements
gaurds_needed = 7
EO_needed = 6

#Current Standards
gaurds_on = 0
EO_on = 0

days = 0



def on_camp(member):
    #Checks if person is on camp
    to_start, to_end = member.to.replace("(", "").replace(")", "").split("-")
        
        #CHECKS IF ON CAMP
    if (days <= int(to_start) or days > int(to_end)) and member.eligible == True:
        return True
        

def solo(member):
    #Checks if person is solo 
    #RETURNS FALSE IF THEY ARE SOLO
    co = member.co
    
    if member.co == "None":
        return True
    

    for people in staff_list:
        if people.name == co:
            return on_camp(people)

def add_lg():

    #ADDS GAURDS
    gaurds_on = 0
    z=0

    staff_list.sort(key=lambda x: x.score)
    
    for member in staff_list:
        if gaurds_on >= gaurds_needed and gaurds_on <(gaurds_needed + 2) :
            if (solo(member) == True) and (on_camp(member) == True ) and member.eligible == True and member.lg == True:
                        member.eligible = False
                        #member.score +=1
                        gaurds_on+=1
                        z+=1
                        print("BACKUP:",member)
        if gaurds_on >= (gaurds_needed + 2):
            if z <2:
             print("Choose Resource or Solo LG")
            return 0
        if member.eligible == True and member.lg == True:

            
            if (solo(member) == True) and (on_camp(member) == True ):
                        member.eligible = False
                        member.score +=1
                        gaurds_on+=1 
                        z+=1
                        print(member)
            
def add_eo():
    #ADDS EYES ON 
    EO_on = 0
    staff_list.sort(key=lambda x: x.score)

    for member in staff_list:
        
        if EO_on >= EO_needed and EO_on <(EO_needed + 2) :
            if (solo(member) == True) and (on_camp(member) == True ):
                        member.eligible = False
                        #member.score +=1
                        EO_on+=1 
                        print("BACKUP:",member)
        if EO_on >= (EO_needed + 2):
            return 0
        
        if member.eligible == True: #and member.lg != True:

            
            if (solo(member) == True) and (on_camp(member) == True ):
                        member.eligible = False
                        member.score +=1
                        EO_on += 1 
                        print(member)









#Assign LGs 
while days < 12:
    s = 0
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    print("Day:",week[days])

    print("Aug",4+days)
    
    '''
    if days <8:
        print("June",(23+days))
    else:
        print("July",(23+days-30))
    '''
    

    print()
    #assign LGs

    #add LG
    print("LG:")
    
    add_lg()
    

    print()

    #Add EO
    print("EO / BB: ")
    
    add_eo()
    
    print()
    #Add BB
    
                
    for member in staff_list:
        member.eligible = True
            
    days +=1 





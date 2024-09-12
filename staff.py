class Staff:

    def __init__(self, name, co, to, lg):
        self.name = name
        self.co = co
        self.to = to
        self.lg = lg
        self.eligible = True
        self.score = 0
    def __str__(self):
        
        return("Name: %s; CO: %s; TO: %s, LG: %s, Times Worked: %s" %(self.name,self.co, self.to, self.lg,self.score))

    
    


def main():
    book1=Staff("Blake Thomas","Eddie","1-2",True)
    print(book1)

if __name__=="__main__":
    main()
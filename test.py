
def add_info():
    #storage a string in afile line by line
    #by using "a" to open file,
    #i am able to write or append new data
    #and keep my old data undisturbed
    Type=''
    Username=''
    password=''
    a=True

    with open('storage.txt', 'a') as f:

    
        while a==True:

            Type=str(input("enter a type"))
            if Type=='exit':
                a=False
            else:
                Username=str(input('enter a Username: '))
                password=str(input('enter a password: '))
                f.write(f"{Type}\t{Username}\t{password}")
                f.write('\n')
                print('''enter a type to continue
                or enter exit to exit the program''')
                        
            
def returninfo():
    var =str(input('enter a type'))
    with open('storage.txt', 'r') as f:
        reader= f.readlines()    #list of all the line
        for line in reader: #access to ever line
            if var in line: # check the type you want to print
                print(line)

def updating_password():
    pass
def info():
    pass
def remove():
    pass

if __name__ == '__main__':
    print('''welcome to my program
    *to obtain your password type return
    *to add passwords type add
    ''')
    command=''
    while command!='exit':
        command=input('enter command : ')
        if command=='exit':
            break 
        if command=='add':
            add_info()
            break           
        elif command=="return":
            returninfo()
            break
        else:
            print('wrong command, try again ')
            command=input('enter command : ') 
            

        
        
        

        
    
            
            

       
       
       
       
  



    
    
    


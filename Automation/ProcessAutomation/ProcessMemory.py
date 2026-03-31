import psutil

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            # vms => virtual memory size
            pinfo['vms'] = proc.memory_info().vms / ( 1024 * 1024 )     # convert into MB
            
            listprocess.append(pinfo)
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor with memory usage")
    
    listprocess = ProcessDisplay()

    # icnt = 0
    for elem in listprocess:
        # icnt += 1
        print(elem)

    # print( "Number of running processes are : ", icnt)
    print( "Number of running processes are : ", len( listprocess ) )

if __name__=="__main__":
    main()
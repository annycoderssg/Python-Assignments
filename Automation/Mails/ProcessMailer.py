import os
import time
import psutil
# import urllib2
from urllib.request import urlopen
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        html = urlopen("http://www.google.com/").read()
        if html:
            return True
    except urllib.URLError as err:
        return False
    # try:
    #     urllib.urlopen("http://google.com", timeout=1)
    #     return True
    # except urllib.URLError as err:
    #     return False

def MailSender(filename, time):
    try:
        fromAddr = "annycoder.s@gmail.com"
        toAddr = "anand.shinde1989@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystems
        Please find attached document which contains log of running process.
        Log file is created at: %s

        This is auto generated mail.

        Thanks & Regards,
        Annycoder.S
        """%(toAddr, time)


        subject = """
        Process log generated at : %s
        """%(time)

        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment; filename= %s" %filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(fromAddr,"Shree@123")

        text = msg.as_string()

        s.sendmail(fromAddr, toAddr, text)

        s.quit()

        print("Log file successfully sent through mail:")

    except Exception as E:
        print("Unable to send mail.", E)

def ProcessLog( log_dir = "Logs"):
    listProcess = []

    if not os.path.exists( log_dir ):
        try:
            os.mkdir( log_dir )
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join( log_dir, "ProcessLog%s.log" %(time.time()))
    f = open(log_path, 'w')
    f.write( separator + '\n' )
    f.write( "My Process Logs: " + time.ctime() + "\n" )
    f.write( separator + '\n' )
    f.write( '\n' )

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms / ( 1024 * 1024 )
            pinfo['vms'] = vms

            listProcess.append( pinfo )
        except( psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess ):
            pass

    for element in listProcess:
        f.write("%s\n" %element)

    print("Log file is successfully generated at location %s" %log_path)

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender( log_path, time.ctime())
        endTime = time.time()

        print("Took %s seconds to send mail", (endTime - startTime))

    else:
        print("There is no internet connection")

def main():
    print("===============Automation Started==============")

    print("Automation name", argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This script is used to record of running processes")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script AbsolutePath_of_Directory")
        print("Example : ProcessMailer.py Logs")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error: invalid datatype of input")

    except Exception as E:
        print("Error: invalid input", E)

if __name__ == "__main__":
    main()

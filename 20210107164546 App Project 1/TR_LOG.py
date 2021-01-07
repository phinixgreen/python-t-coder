import time

ts = time.time()

TR_LOG = open("TR_DBS.csv","a")     ## define TR_LOG as open text.txt and append

print ("Welcome to Transaction Logger.")


name = input ("Please enter your Name in ALL CAPITAL : ") 
date = input ("Enter today in YYYY-MM-DD : ")

print ("Hello, "+name + ". The transactions will be entered as on "+ date)

x = 0
y = input ("How many transcations do you want to enter? ") 


while x < int(y): 
        transactiontype = input ("Enter whether DEBIT or CREDIT in ALL CAPITAL : ")
        transactionamount = input ("Enter your amount in number : ")
        TR_LOG.write( "\n" + str(ts) + ","+ date + "," + name + ","+ transactiontype + "," + transactionamount)          ## write to TR_LOG including input received from val  
        x += 1

else: TR_LOG.close()
pass

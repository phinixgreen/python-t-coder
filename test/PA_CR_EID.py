import time

ts = time.time()

PA_CR_EID = open("PA_DB_EID.csv","a")     ## define PA_CR_EID as open text.txt and append

x = 0
y = input ("How many transcations to you want to enter? ") 

while x < int(y):
        name = input ("Enter the your Name in ALL CAPITAL : ") 
        transactiontype = input ("Enter the your DEBIT or CREDIT in ALL CAPITAL : ")
        transactionamount = input ("Enter the your amount in number : ")
        PA_CR_EID.write( "\n" + str(ts) + ","+ name + ","+ transactiontype + "," + transactionamount)          ## write to PA_CR_EID including input received from val  
        x += 1

else: PA_CR_EID.close()
pass

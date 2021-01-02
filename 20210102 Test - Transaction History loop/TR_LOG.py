import time

ts = time.time()

TR_LOG = open("TR_DBS.csv","a")     ## define TR_LOG as open text.txt and append

x = 0
y = input ("How many transcations to you want to enter? ") 

while x < int(y):
        name = input ("Enter the your Name in ALL CAPITAL : ") 
        transactiontype = input ("Enter the your DEBIT or CREDIT in ALL CAPITAL : ")
        transactionamount = input ("Enter the your amount in number : ")
        TR_LOG.write( "\n" + str(ts) + ","+ name + ","+ transactiontype + "," + transactionamount)          ## write to TR_LOG including input received from val  
        x += 1

else: TR_LOG.close()
pass

import time;
ts = time.time()

PA_CR_LN = open("PA_DB_LN.csv","a")     ## define PA_CR_EID as open text.txt and append
     ## define PA_CR_EID as open text.txt and append

lastName = input ("Enter the Last Name of the Employee: ") 

PA_CR_LN.write("\n" + str(ts) + "," + lastName)          ## write to PA_CR_EID including input received from val  
PA_CR_LN.close()

PA_CR_FN = open("PA_DB_FN.csv","a")     ## define PA_CR_EID as open text.txt and append
     ## define PA_CR_EID as open text.txt and append

firstName = input ("Enter the First Name of the Employee: ") 

PA_CR_FN.write("\n" + str(ts) + "," + firstName)          ## write to PA_CR_EID including input received from val  
PA_CR_FN.close()

print("Command Successful")
import time;             # import time
ts = time.time()         # define ts as time.time()

PA_CR_LN = open("PA_DB_LN.csv","a")     ## define PA_CR_LN as PA_CR_LN.csv and append

lastName = input ("Enter the Last Name of the Employee: ")  ## enters the last name

PA_CR_LN.write("\n" + str(ts) + "," + lastName)          ## write to PA_CR_LN with lastname and ts  
PA_CR_LN.close()                                         ## PA_CR_LN close   

PA_CR_FN = open("PA_DB_FN.csv","a")     ## define PA_CR_FN as PA_CR_FN.csv and append

firstName = input ("Enter the First Name of the Employee: ") ## enters the first name

PA_CR_FN.write("\n" + str(ts) + "," + firstName)          ## write to PA_CR_FN with firstname and ts 

print("Command Successful")                               ## prints command successful
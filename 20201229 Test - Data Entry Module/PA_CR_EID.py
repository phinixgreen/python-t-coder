PA_CR_EID = open("PA_DB_EID.csv","a")     ## define PA_CR_EID as open text.txt and append
EID = input ("Enter a Unique number: ")
lastName = input ("Enter the Last Name of the Employee: ") 
PA_CR_EID.write("\n"+ EID +"," + lastName)          ## write to PA_CR_EID including input received from val  
PA_CR_EID.close()                ## close PA_CR_EID


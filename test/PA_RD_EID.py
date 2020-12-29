PA_RD_EID = open("PA_DB_EID.csv","rt") ## define PA_RD_EID as open PA_DB_EID.txt file and read text with rt
contents = PA_RD_EID.read()       ## define contents as reading PA_RD_EID
PA_RD_EID.close()                 ## close PA_RD_EID after reading
print(contents)                ## print contents
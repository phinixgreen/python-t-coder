
import pandas as pd

username = input ("Enter User Name in CAPITAL: ")   # username inputs for crosschecking name in TR_DBS
tr_type_filter = input ("Do you want a Transaction Filter? Y/N: ")

def tr_check_n():
    
    usersum = pd.read_csv('TR_DBS.csv')                 # usersum reads TR_DBS.csv
    is_user = usersum['USER']==username                 # is_user checks whther TR_DBS data has USER column that has username data input similarity                        
    usersum_username = usersum[is_user]                 # usersum_username prints array in usersum which meets is_user condition
    print (usersum_username.head())                     # prints usersum_username dataframe


def tr_check_y():
    
    usersum = pd.read_csv('TR_DBS.csv')                 # usersum reads TR_DBS.csv
    is_user = usersum['USER']==username                 # is_user checks whther TR_DBS data has USER column that has username data input similarity                        
    is_type = usersum['TRANSACTIONTYPE']==tr_type       # is_type checks whether TR_DBS data has TRANSACTIONTYPE coloumn that has tr_type data input similarity
    usersum_username = usersum[is_user & is_type]       # usersum_username prints array in usersum which meets is_user & is_type condition
    print (usersum_username.head())                     # prints usersum_username dataframe


if tr_type_filter == 'Y':

    tr_type = input ("Enter your Transaction Type in all CAPITAL: ")  # asks transaction type entry
    tr_check_y()                                                      # calls function tr_check_y         

else:

    tr_check_n()                                                      # calls function tr_check_n
    
    

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:27:15 2021

@author: Hitesh
"""

import pandas as pd
from db_conn import hana_conn
#from datetime import date

# st_date = date.today()
# ed_date = date.today()
    
class operations:
    
    def __init__(self, CUST_ID, FIRST_NAME, LAST_NAME, REGION, ID_PROOF_TYPE, START_DATE, END_DATE, STATUS):
        self.CUST_ID = CUST_ID
        self.FIRST_NAME = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.REGION = REGION
        self.ID_PROOF_TYPE = ID_PROOF_TYPE
        self.START_DATE = 'current_date'
        self.END_DATE = 'current_date'
        self.STATUS = STATUS
        self.conn=hana_conn() 
        
    
    def read(self):
        cursor = self.conn.cursor()  
        #cursor.execute("SELECT TOP 10 "CUST_ID","FIRST_NAME","LAST_NAME","REGION","ID_PROOF_TYPE","START_DATE","END_DATE","STATUS" FROM CUSTOMER_DATA;", {})      
        cursor.execute("SELECT TOP 10 * FROM CUSTOMER;", {})      
        data = cursor.fetchall()
        print("Connection to SAP HANA Service successful.")
        
        df = pd.DataFrame(data, columns=['CUST_ID','FIRST_NAME','LAST_NAME','REGION','ID_PROOF_TYPE','START_DATE','END_DATE','STATUS'])
        print(df)
        return df
	
    
    def create(self):
    #if variable=='Read'
        
        #cursor = self.conn.cursor()  
        # val = (self.CUST_ID,self.FIRST_NAME,self.LAST_NAME,self.REGION,self.ID_PROOF_TYPE,self.START_DATE,self.END_DATE,self.STATUS)
        # sql="INSERT INTO CUSTOMER (CUST_ID,FIRST_NAME,LAST_NAME,REGION,ID_PROOF_TYPE,START_DATE,END_DATE,STATUS) VALUES"
        # final_sql= (sql, val) 
        # print(final_sql)
        # cursor.execute(final_sql, {})
        cursor = self.conn.cursor() 
        cursor.execute("INSERT INTO CUSTOMER (CUST_ID,FIRST_NAME,LAST_NAME,REGION,ID_PROOF_TYPE,START_DATE,END_DATE,STATUS) VALUES('12345', 'Sidney', 'Hauke', 'New Jersey', 'Driving License', 'current_date', 'current_date', 'Active')", {})  
        print("Customer got created" )
        
        return "Customer created"
    
    def delete(self):       
        cursor = self.conn.cursor()  
        cursor.execute("DELETE FROM CUSTOMER WHERE CUST_ID ="+str(self.CUST_ID), {})
        # res=cursor.fetchall() 
        # print(res)
        print("Customer got removed" )
        #return res
        return "Customer got removed" 
        
        cursor.close()
        hana_conn.close()        


#unit testing           
# test = operations('12345','Sidney','Hauke','New Jersey','Driving License','s','e','Active')
# test.delete()

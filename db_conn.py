# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:31:41 2021

@author: Hitesh
"""

from hdbcli import dbapi

def hana_conn():
    #address='fced79e4-d9ec-4819-a6bc-723570ac80b7.hana.trial-us10.hanacloud.ondemand.com'
    address='2cde67eb-e7c5-4de4-975b-6170c3b75764.hana.trial-us10.hanacloud.ondemand.com'
    port=int('443')
    user='DBADMIN' 
    #password='RajaHuli@12'
    password='Sap@12345'

    conn = dbapi.connect(address, port, user, password)
    
    return conn

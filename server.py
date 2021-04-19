import os
# from datetime import date
from flask import Flask, render_template
app = Flask(__name__)
from customerapp import operations as op
#from db_conn import hana_conn

# st_date = print(date.today())
# ed_date = print(date.today())
port = int(os.environ.get('PORT', 5000))
#p1=  op('12345','Sidney','Hauke','New Jersey','Driving License','s','e','Active') 
p1= op(12345,'Sidney','Hauke','New Jersey','Driving License','01-Jan-17','01-Dec-99','Active')


@app.route('/Customer/')
def exaapp():
    #print("customer details!!!")
    return render_template('index.html')
    #return print("customer details!!!")

@app.route('/Customer/read/')
def read():
    print ('I got clicked!')
    df = p1.read()
    #print(df) 
    return str(df)

@app.route('/Customer/create/')
def create():
    print ('I got clicked!')
    res = p1.create()
    return res

@app.route('/Customer/delete/')
def delete():
    print ('I got clicked!')
    res = p1.delete()
    return res


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port =port)

        
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,jsonify,request

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello India'
    
@app.route('/india')
# ‘/’ URL is bound with hello_world() function.
def India():
    return 'Hello India'
    
@app.route('/japan')
# ‘/’ URL is bound with hello_world() function.
def Japan():
    return 'Hello Japan'

@app.route('/sweden')
# ‘/’ URL is bound with hello_world() function.
def Sweden():
    return 'Hello Sweden'
    
@app.route('/germany')
# ‘/’ URL is bound with hello_world() function.
def Germany():
    return 'Hello Germany'

@app.route('/singapore')
def Singapore():
    return 'Hello Singapore'

@app.route('/cybersecurity')
def Cybersecurity():
    data = { 
            "manuitems" : [
            {
                "itemid" : "c1",
                "itemtext" : "Products"            
            },
            {
                "itemid" : "c2",
                "itemtext" : "Services"
            }
            ]
        } 
    return jsonify(data) 
    
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
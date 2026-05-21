from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def home(): 
    return "Dress Delivery Service - Order Tracking System" 

if __name__ == "__main__": 
    app.run(debug=True) 

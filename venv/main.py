from flask import Flask,jsonify
from flask_cors import CORS


app=Flask(__name__)
cors=CORS(app,orgins='*')

@app.route("/api/users/",methods=["GET"])
def users():
    a=1+2
    return jsonify(
        {
            "users":[
                a
            ]
        }
    )

if __name__=="__main__":
    app.run()

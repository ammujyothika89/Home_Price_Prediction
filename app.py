from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib, json, numpy as np

app        = Flask(__name__)
CORS(app)

model      = joblib.load("model/xgb_model.pkl")
le_city    = joblib.load("model/le_city.pkl")
le_loc     = joblib.load("model/le_loc.pkl")
le_furnish = joblib.load("model/le_furnish.pkl")
FEATURES   = joblib.load("model/features.pkl")
META       = json.load(open("model/meta.json"))

LOCS = {
    "Bangalore" : ["Whitefield","Koramangala","Indiranagar","HSR Layout","Hebbal"],
    "Mumbai"    : ["Bandra","Andheri","Powai","Thane","Kurla"],
    "Hyderabad" : ["Gachibowli","Jubilee Hills","Madhapur","Kondapur","HITEC City"],
    "Chennai"   : ["Anna Nagar","T Nagar","Velachery","OMR","Adyar"],
    "Pune"      : ["Wakad","Hinjewadi","Kothrud","Baner","Viman Nagar"],
    "Delhi NCR" : ["Noida Sector 62","Gurugram","Dwarka","Faridabad","Greater Noida"]
}

@app.route("/")
def index():
    return render_template("index.html", meta=META, locs=LOCS)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        d  = request.json
        ce = int(le_city.transform([d["city"]])[0])
        le = int(le_loc.transform([d["locality"]])[0])
        fe = int(le_furnish.transform([d["furnishing"]])[0])
        row = np.array([[
            float(d["area"]),  float(d["bhk"]),   float(d["bath"]),
            float(d["age"]),   float(d["floor"]),  float(d["total_floors"]),
            float(d["parking"]),float(d["gym"]),   float(d["pool"]),
            fe, ce, le
        ]])
        price = float(model.predict(row)[0])
        return jsonify({
            "price" : round(price, -3),
            "low"   : round(price*0.968, -3),
            "high"  : round(price*1.032, -3),
            "ppsf"  : round(price/float(d["area"])),
            "r2"    : META["r2"],
            "mape"  : META["mape"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("\n🚀 HomeLens AI  →  http://127.0.0.1:5000\n")
    app.run(debug=False, port=5000)
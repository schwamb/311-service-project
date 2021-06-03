from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS
from joblib import load
import pandas as pd
from sqlalchemy import create_engine, func

app = Flask(__name__)
CORS(app)

engine = create_engine("sqlite:///db_311.sqlite")

reg = load("model")
print(reg)
scaler = load("scaler")

@app.route("/api/v1.0/311_data")
def srvc_data(): 
    sr_info = pd.read_sql('SELECT * FROM service_requests', engine)

    return Response(sr_info.to_json(orient = "records"),mimetype="application/json")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    srType = request.args.get("srType")
    ward = request.args.get("ward")
    month = request.args.get("month")
    hour = request.args.get("hour")

    datum ={
"WARD":ward,
"CREATED_MONTH":month,
"CREATED_DAY_OF_WEEK":0,
"CREATED_HOUR":hour,
"SR_TYPE_Abandoned Vehicle Complaint":0,
"SR_TYPE_Alley Light Out Complaint":0,
"SR_TYPE_Alley Pothole Complaint":0,
"SR_TYPE_Alley Sewer Inspection Request":0,
"SR_TYPE_Animal In Trap Complaint":0,
"SR_TYPE_Bee/Wasp Removal":0,
"SR_TYPE_Bicycle Request/Complaint":0,
"SR_TYPE_Building Violation":0,
"SR_TYPE_Bungalow/Vintage Home Information Request":0,
"SR_TYPE_Business Complaints / Reopening Issue":0,
"SR_TYPE_Cab Feedback":0,
"SR_TYPE_Cable TV Complaint":0,
"SR_TYPE_City Vehicle Sticker Violation":0,
"SR_TYPE_Clean Vacant Lot Request":0,
"SR_TYPE_Clean and Green Program Request":0,
"SR_TYPE_Commercial Fire Safety Inspection Request":0,
"SR_TYPE_Consumer Fraud Complaint":0,
"SR_TYPE_Consumer Retail Store Complaint":0,
"SR_TYPE_Coyote Interaction Complaint":0,
"SR_TYPE_Dead Animal Pick-Up Request":0,
"SR_TYPE_Dead Bird":0,
"SR_TYPE_Fly Dumping Complaint":0,
"SR_TYPE_Garbage Cart Maintenance":0,
"SR_TYPE_Graffiti Removal Request":0,
"SR_TYPE_Home Buyer Program Info Request":0,
"SR_TYPE_Ice and Snow Removal Request":0,
"SR_TYPE_Inaccurate Fuel Pump Complaint":0,
"SR_TYPE_Inaccurate Retail Scales Complaint":0,
"SR_TYPE_Lead Inspection Request":0,
"SR_TYPE_Licensed Pharmaceutical Representative Complaint":0,
"SR_TYPE_Liquor Establishment Complaint":0,
"SR_TYPE_Low Water Pressure Complaint":0,
"SR_TYPE_Missed Garbage Pick-Up Complaint":0,
"SR_TYPE_No Building Permit and Construction Violation":0,
"SR_TYPE_No Solicitation Complaint":0,
"SR_TYPE_No Water Complaint":0,
"SR_TYPE_Nuisance Animal Complaint":0,
"SR_TYPE_Open Fire Hydrant Complaint":0,
"SR_TYPE_Outdated Merchandise Complaint":0,
"SR_TYPE_Paid Sick Leave Violation":0,
"SR_TYPE_Pavement Cave-In Inspection Request":0,
"SR_TYPE_Pet Wellness Check Request":0,
"SR_TYPE_Petcoke Dust Complaint":0,
"SR_TYPE_Porch Inspection Request":0,
"SR_TYPE_Pothole in Street Complaint":0,
"SR_TYPE_Protected Bike Lane - Debris Removal":0,
"SR_TYPE_Public Vehicle/Valet Complaint":0,
"SR_TYPE_Pushcart Food Vendor Complaint":0,
"SR_TYPE_Recycling Inspection Request":0,
"SR_TYPE_Renters and Foreclosure Complaint":0,
"SR_TYPE_Report an Injured Animal":0,
"SR_TYPE_Restaurant Complaint":0,
"SR_TYPE_Ridesharing Complaint":0,
"SR_TYPE_Rodent Baiting/Rat Complaint":0,
"SR_TYPE_Sanitation Code Violation":0,
"SR_TYPE_Sewer Cave-In Inspection Request":0,
"SR_TYPE_Sewer Cleaning Inspection Request":0,
"SR_TYPE_Shared Housing/Vacation Rental Complaint":0,
"SR_TYPE_Sidewalk Cafe Complaint":0,
"SR_TYPE_Sidewalk Inspection Request":0,
"SR_TYPE_Sign Repair Request - All Other Signs":0,
"SR_TYPE_Sign Repair Request - Do Not Enter Sign":0,
"SR_TYPE_Sign Repair Request - One Way Sign":0,
"SR_TYPE_Sign Repair Request - Stop Sign":0,
"SR_TYPE_Smokeless Tobacco at Sports Event Complaint":0,
"SR_TYPE_Snow - Object/Dibs Removal Request":0,
"SR_TYPE_Snow Removal - Protected Bike Lane or Bridge Sidewalk":0,
"SR_TYPE_Snow – Uncleared Sidewalk Complaint":0,
"SR_TYPE_Stray Animal Complaint":0,
"SR_TYPE_Street Cleaning Request":0,
"SR_TYPE_Street Light On During Day Complaint":0,
"SR_TYPE_Street Light Out Complaint":0,
"SR_TYPE_Street Light Pole Damage Complaint":0,
"SR_TYPE_Street Light Pole Door Missing Complaint":0,
"SR_TYPE_Tobacco - General Complaint":0,
"SR_TYPE_Tobacco - Sale to Minors Complaint":0,
"SR_TYPE_Traffic Signal Out Complaint":0,
"SR_TYPE_Tree Debris Clean-Up Request":0,
"SR_TYPE_Tree Planting Request":0,
"SR_TYPE_Tree Removal Request":0,
"SR_TYPE_Tree Trim Request":0,
"SR_TYPE_Vacant/Abandoned Building Complaint":0,
"SR_TYPE_Viaduct Light Out Complaint":0,
"SR_TYPE_Vicious Animal Complaint":0,
"SR_TYPE_Wage Complaint":0,
"SR_TYPE_Water On Street Complaint":0,
"SR_TYPE_Water Quality Concern":0,
"SR_TYPE_Water in Basement Complaint":0,
"SR_TYPE_Weed Removal Request":0,
"SR_TYPE_Wire Basket Request":0,
"SR_TYPE_Yard Waste Pick-Up Request":0}

    datum[f"SR_TYPE_{srType}"]=1
    print(reg.predict(pd.DataFrame([datum]))[0])
    X = pd.DataFrame([datum])
    X_scaled = scaler.transform(X)
    inDays = (reg.predict(X_scaled)[0][0])
    print(inDays)
    output = (round(inDays, 2))
    print(output)
    return render_template("index.html",prediction_text='Your projected turnaround time is: {} days'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
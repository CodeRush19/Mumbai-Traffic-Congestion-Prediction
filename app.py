from flask import Flask, render_template, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# --- FULL STATION DATA ---
congestion_data = [
    {"area": "Churchgate", "lat": 18.9402, "lng": 72.8356},
    {"area": "Marine Lines", "lat": 18.9514, "lng": 72.8252},
    {"area": "Charni Road", "lat": 18.9570, "lng": 72.8230},
    {"area": "Grant Road", "lat": 18.9711, "lng": 72.8145},
    {"area": "Mumbai Central", "lat": 18.9694, "lng": 72.8196},
    {"area": "Mahalaxmi", "lat": 18.9922, "lng": 72.8204},
    {"area": "Lower Parel", "lat": 19.0029, "lng": 72.8284},
    {"area": "Elphinstone", "lat": 19.011, "lng": 72.8315},
    {"area": "Dadar", "lat": 19.0189, "lng": 72.8487},
    {"area": "Malad", "lat": 19.1823, "lng": 72.8404},
    {"area": "Andheri", "lat": 19.1196, "lng": 72.8477},
    {"area": "Kandivali", "lat": 19.2054, "lng": 72.8419},
    {"area": "Mira Road", "lat": 19.2838, "lng": 72.8559},
    {"area": "Vasai", "lat": 19.4103, "lng": 72.8376},
    {"area": "Virar", "lat": 19.478, "lng": 72.7921},
    {"area": "CSMT", "lat": 18.9418, "lng": 72.8345},
    {"area": "Masjid", "lat": 18.95, "lng": 72.8287},
    {"area": "Sandhurst Road", "lat": 18.9626, "lng": 72.8343},
    {"area": "Byculla", "lat": 18.9934, "lng": 72.8362},
    {"area": "Dadar Central", "lat": 19.02808, "lng": 72.8483},
    {"area": "Kurla", "lat": 19.066, "lng": 72.887},
    {"area": "Vidyavihar", "lat": 19.07, "lng": 72.9194},
    {"area": "Ghatkopar", "lat": 19.086, "lng": 72.9273},
    {"area": "Vikhroli", "lat": 19.1263, "lng": 72.9436},
    {"area": "Kanjur Marg", "lat": 19.155, "lng": 72.9607},
    {"area": "Bhandup", "lat": 19.165, "lng": 72.9557},
    {"area": "Mulund", "lat": 19.1823, "lng": 72.9565},
    {"area": "Thane", "lat": 19.2163, "lng": 73.01},
    {"area": "Diva", "lat": 19.2113, "lng": 73.0525},
    {"area": "Kalyan", "lat": 19.242, "lng": 73.13},
]

routes = [
    [[18.9402, 72.8356], [18.9514, 72.8252], [18.9570, 72.8230], [18.9711, 72.8145], [18.9694, 72.8196]],
    [[18.9694, 72.8196], [19.1196, 72.8477], [19.2054, 72.8419], [19.2838, 72.8559], [19.4103, 72.8376], [19.4780, 72.7921]],
    [[18.9418, 72.8345], [19.066, 72.887], [19.2163, 73.01], [19.2420, 73.13]],
]

@app.route('/')
def home():
    return 'Server Running'

@app.route('/map')
def map():
    return render_template('map_with_routes.html')

@app.route('/api/get_congestion')
def get_congestion():
    day = request.args.get('day')
    hour = request.args.get('hour')
    base = 40
    peak = 30
    for s in congestion_data:
        val = base + random.randint(0, 20)
        if day in ['Monday','Tuesday','Wednesday','Thursday','Friday'] and hour and int(hour) in range(7,10):
            val += peak
        s['congestion'] = min(val, 90)
    return jsonify(congestion_data)

@app.route('/api/get_routes')
def get_routes():
    return jsonify(routes)

@app.route('/api/congestion_trend')
def trend():
    labels = [(datetime.now()-timedelta(days=6-i)).strftime('%a') for i in range(7)]
    values = [random.randint(40, 90) for _ in range(7)]
    return jsonify({'labels': labels, 'data': values})

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/map
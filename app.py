# app.py
from flask import Flask, render_template

app = Flask(__name__)

# ======================
# EDITABLE CONTENT AREA
# ======================
# Everything you need to edit is in this section

profile_info = {
    "name": "Xavier Hack",
    "age": "16",
    "title": "High school student and Acountant",
    "bio": "I Am a high school student with a passion for technology and finance, I always enjoy finding new technology.",
    "email": "No@thankyou.com",
    "location": "ontario, Canada",
}

projects = [
    {
        "title": "E-Commerce Dashboard",
        "description": "A comprehensive dashboard for online stores with real-time analytics.",
        "code": """from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    
@app.route('/dashboard')
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)""",
        "language": "python"
    },
    {
        "title": "A simple sales calculator",
        "description": "A calculator program that calculates sales for businesses.",
        "code": """""""""""
sales calculator program 
this progam claculataes sales for a buisness by:
1. calculating the total cost of a purchase 
2. allows for discounts to be applied 
3. prints out receipts
""""""
while True:
    try:
        price = float(input("enter the item price "))
        quantity = int(input("enter the quantity"))
        break
    except ValueError:
        print("invalid input")

subtotal = price * quantity

while True:
    try:
        discount = float
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

operation = input("enter a operation? Choose: +,-,x,/ ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "x":
    result = num1 * num2
elif operation == "/":
    if num2 != 0 :
        result = num1 / num2
    else: result = "error: dont divide by zero"
else: 
    result = "please enter one of the operations"

print("the result is: ", result)""",
        "language": "python"
    },
    {
        "title": "Detectify NOSE EDITION!!!!",
        "description": "This is a program that was given to me by my teacher to track cascades, I modified it to track noses.",
        "code": """import cv2
import time

# Load the Haar Cascade for nose detection
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

frame_count = 0
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if not check:
        break

    frame_count += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect noses in the frame
    noses = nose_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around detected noses
    for (x, y, w, h) in noses:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Nose Detection', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):  # Quit the program
        break
    elif key == ord('s'):  # Save a screenshot
        screenshot_filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(screenshot_filename, frame)
        print(f"Screenshot saved as {screenshot_filename}")

print("Total frames processed:", frame_count)

video.release()
cv2.destroyAllWindows()""",
        "language": "python"
    },
    {
        "title": "MAPIFY!",
        "description": "A simple program that uses data to show locations of volcanoes and population",
        "code": """import folium
import pandas

# Read volcano data
data = pandas.read_csv("volcano_data.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Function to determine color based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Create map object with updated zoom behavior
map = folium.Map(
    location=[43.5212, -79.6473],
    zoom_start=4,
    control_scale=True,  # Adds a scale bar to the map
    zoom_control=True    # Enables the default zoom control
)

# Feature group for schools and volcano markers
fg = folium.FeatureGroup(name="School & Volcano Markers")

# Feature group for population
fgp = folium.FeatureGroup(name="Population")

# Load and style GeoJson population data
fgp.add_child(
    folium.GeoJson(
        data=open('global_pop_data.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {
            'fillColor': 'green' if x['properties']['POP2005'] < 10000000
            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
            else 'red'
        }
    )
)

# Add school markers
for coordinates in [[-43.52, -79.64], [-42.31, -78.41], [-43.01, -79.12]]:
    fg.add_child(folium.Marker(location=coordinates, popup="School", icon=folium.Icon(color='red')))

# Volcano circle markers (colored by elevation)
fgv = folium.FeatureGroup(name="Volcano Circles")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=10,
        popup="Elevation: " + str(el) + " m",
        fill_color=color_producer(el),
        color='grey',
        fill_opacity=0.7
    ))

# Specific school marker with updated color
fg.add_child(folium.Marker(location=[43.5212, -79.6473], popup="Iona CSS", icon=folium.Icon(color='purple')))

# New layer for rivers
fgr = folium.FeatureGroup(name="Rivers")
fgr.add_child(
    folium.GeoJson(
        data=open('rivers_data.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {
            'color': 'blue',
            'weight': 2
        }
    )
)

# Add all feature groups to map
map.add_child(fg)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgr)  # Add the new rivers layer
map.add_child(folium.LayerControl())

# Save map
map.save("mapify.html")""",
        "language": "python"
    },
    {
        "title": "Workout buddy",
        "description": "A short and simple gym tracker to log workouts and track progress.",
        "code": """class Exercise:
    \"\"\"Represents an exercise with its name and workout sessions.\"\"\"
    def __init__(self, name):
        self.name = name
        self.sessions = []  # Stores tuples of (sets, reps, weight)

    def add_session(self, sets, reps, weight):
        \"\"\"Logs a new workout session.\"\"\"
        self.sessions.append((sets, reps, weight))

    def show_progress(self):
        \"\"\"Displays all logged sessions for this exercise.\"\"\"
        print(f"Progress for {self.name}:")
        for i, (sets, reps, weight) in enumerate(self.sessions, 1):
            print(f"Session {i}: {sets} sets of {reps} reps at {weight} kg")

    def __str__(self):
        return self.name


class GymTracker:
    \"\"\"Tracks multiple exercises and their workout sessions.\"\"\"
    def __init__(self):
        self.exercises = {}

    def add_exercise(self, name):
        \"\"\"Adds a new exercise to track.\"\"\"
        if name in self.exercises:
            print("Exercise already exists.")
        else:
            self.exercises[name] = Exercise(name)
            print(f"Added exercise: {name}")

    def log_workout(self, name, sets, reps, weight):
        \"\"\"Logs a workout session for an existing exercise.\"\"\"
        if name in self.exercises:
            self.exercises[name].add_session(sets, reps, weight)
            print(f"Logged {sets} sets of {reps} reps at {weight} kg for {name}")
        else:
            print("Exercise not found. Add it first.")

    def view_progress(self):
        \"\"\"Displays progress for all exercises.\"\"\"
        if not self.exercises:
            print("No exercises tracked yet.")
        else:
            for exercise in self.exercises.values():
                exercise.show_progress()


# Main program loop
tracker = GymTracker()

while True:
    print("\\n Gym Tracker Options:")
    print("1. Add Exercise")
    print("2. Log Workout")
    print("3. View Progress")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter exercise name: ").strip().capitalize()
        tracker.add_exercise(name)

    elif choice == "2":
        name = input("Enter exercise name: ").strip().capitalize()
        sets = int(input("Enter number of sets: "))
        reps = int(input("Enter number of reps: "))
        weight = float(input("Enter weight in kg: "))
        tracker.log_workout(name, sets, reps, weight)

    elif choice == "3":
        tracker.view_progress()

    elif choice == "4":
        print("Stay strong! 💪 Exiting Gym Tracker.")
        break

    else:
        print("Invalid choice. Try again.")""",
        "language": "python"
    },
    {
        "title": "Weather App",
        "description": "Real-time weather application with 5-day forecasts.",
        "code": """import requests
from flask import Flask, render_template, request

app = Flask(__name__)
API_KEY = "your_api_key_here"

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return render_template('weather.html', data=data)
    return render_template('weather.html')""",
        "language": "python"
    }
]

timeline_posts = [
    {
        "date": "March 10, 2025",
        "title": "Coded The weather app",
        "content": "Decided to start my journey with a challange as I learned how to code a weather app using an open source api!"
    }
    
    ,{
        "date": "April 20, 2025",
        "title": "E-commerce Dashboard, commence",
        "content": "I began working on an e-commerce dashboard project. The goal is to create a dashboard for online stores that uses analytics in real time to provide insights!"
    },    
    
    {
        "date": "April 20, 2025",
        "title": "E-commerce Dashboard, game set",
        "content": "The dashboard is finished, for the time I had and the amount of knowlage I had alongside some assistance I feel it turned out great, It was a great experience!"
    },

    {
        "date": "May 13, 2025",
        "title": "Read moneyball by Michael Lewis",
        "content": "Just finished this fascinating book on how data analytics transformed baseball. It’s a must-read for anyone interested in sports and statistics."
    },
    
    {
        "date": "May 27, 2025",
        "title": "Finished zero to one by Peter Thiel",
        "content": "This book offers a unique perspective on startups and innovation. "
    },
    {
        "date": "May 30, 2025",
        "title": "Thinking, Fast and Slow by Daniel Kahneman",
        "content": "A deep dive into the psychology of decision-making."
    }
    
]

# ======================
# END OF EDITABLE CONTENT
# ======================

@app.route('/')
def home():
    return render_template('index.html', profile=profile_info)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/timeline')
def timeline_page():
    return render_template('timeline.html', posts=timeline_posts)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# Home route for the irrigation website
@app.route('/')
def home():
    return render_template('index.html')

# Route to get irrigation status or trigger irrigation
@app.route('/irrigate', methods=['POST'])
def irrigate():
    # Simulate irrigation based on user input
    area = request.form['area']
    water_needed = calculate_water_needed(area)
    return render_template('index.html', water_needed=water_needed)

# Function to calculate the water required based on area
def calculate_water_needed(area):
    try:
        area = float(area)
        water_needed = area * 1.5  # example: 1.5 liters of water per square meter
        return f'{water_needed} liters'
    except ValueError:
        return 'Invalid input. Please enter a valid number.'

if __name__ == '__main__':
    app.run(debug=True)

#from flask import Flask, render_template, request, jsonify
#from utils import calculate_monthly_payment, calculate_total_cost

from flask import Flask, request, jsonify, render_template
from health_utils import calculate_bmi, calculate_bmr
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()  # Load environment variables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.get_json()
        height = float(data['height'])  # height in meters
        weight = float(data['weight'])  # weight in kg
        
        if height <= 0 or weight <= 0:
            return jsonify({'error': 'Height and weight must be positive numbers'}), 400
            
        bmi_value = calculate_bmi(height, weight)
        
        return jsonify({
            'bmi': round(bmi_value, 2),
            'category': get_bmi_category(bmi_value)
        })
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.get_json()
        height = float(data['height'])  # height in cm
        weight = float(data['weight'])  # weight in kg
        age = int(data['age'])         # age in years
        gender = data['gender'].lower() # 'male' or 'female'
        
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({'error': 'Height, weight, and age must be positive numbers'}), 400
        if gender not in ['male', 'female']:
            return jsonify({'error': 'Gender must be either "male" or "female"'}), 400
            
        bmr_value = calculate_bmr(height, weight, age, gender)
        
        return jsonify({
            'bmr': round(bmr_value, 2)
        })
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', True)
    )





# app = Flask(__name__)

#@app.route('/')
#def home():
#    return render_template('home.html')

#@app.route('/calculate', methods=['POST'])
#def calculate():
#    loan_amount = float(request.form['loan_amount'])
#    duration_years = int(request.form['duration'])
#    annual_interest_rate = float(request.form['interest_rate'])

#    monthly_payment = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
#    total_cost = calculate_total_cost(monthly_payment, duration_years)

#    return jsonify({
#        'monthly_payment': monthly_payment,
#        'total_cost': total_cost
#    })

#if __name__ == '__main__':
#    app.run(debug=True)

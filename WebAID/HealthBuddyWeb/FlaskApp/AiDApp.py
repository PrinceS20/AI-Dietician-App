from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/gd')
def gd():
    return render_template('gd.html')

@app.route('/generate_diet_plan', methods=['GET','POST'])
def generate_diet_plan():
    age = int(request.form['age'])
    gender = request.form['gender']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    activity_level = request.form['activity_level']
    goal = request.form['goal']
    
    # Perform AI algorithm or calculations to generate the diet plan based on user input
    # You can use the input variables (age, gender, weight, height, activity_level, goal) to generate a personalized plan
    # For the sake of simplicity, we will create a basic diet plan manually here
    
    diet_plan = ""
    if goal == "weight_loss":
        diet_plan = "Your diet plan for weight loss:\n- Consume a calorie deficit of 500-1000 calories per day.\n- Include more fruits, vegetables, lean proteins, and whole grains.\n- Limit intake of processed foods and sugary drinks.\n- Stay hydrated and monitor portion sizes."
    elif goal == "muscle_gain":
        diet_plan = "Your diet plan for muscle gain:\n- Consume a slight calorie surplus of 250-500 calories per day.\n- Focus on consuming sufficient protein to support muscle growth.\n- Include lean meats, dairy, eggs, legumes, and protein-rich plant-based foods.\n- Incorporate complex carbohydrates and healthy fats.\n- Stay hydrated and fuel your body before and after workouts."
    elif goal == "maintenance":
        diet_plan = "Your diet plan for weight maintenance:\n- Consume a balanced diet that meets your daily calorie needs.\n- Include a variety of nutrient-dense foods from all food groups.\n- Monitor portion sizes and practice mindful eating.\n- Make healthy choices and limit excessive intake of processed foods, sugary snacks, and drinks.\n- Stay hydrated and listen to your body's hunger and fullness cues."

    return render_template('result.html', diet_plan=diet_plan)

if __name__ == '__main__':
    app.run(debug=True)
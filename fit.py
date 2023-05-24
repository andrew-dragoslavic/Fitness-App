from flask import Flask,render_template
app = Flask(__name__, template_folder= "templates", static_folder='styles')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/self-care')
def about():
    return render_template('sc.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/workouts')
def workout():
    return render_template('workouts.html')

if __name__ == '__main__':
    app.run(debug = True)
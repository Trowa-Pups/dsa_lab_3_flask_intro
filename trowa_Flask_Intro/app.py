from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('work.html')

@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/toUpperCase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def circle():
    try:
        radius = float(request.form.get('radius', 0))
        circle_area = 3.14159 * (radius **2)

    except ValueError:
        circle_area = "Invalid Input!"
    
    return render_template('areaofcircle.html', result=circle_area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def triangle():
    try:
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        triangle_area = 0.5 * base * height 

    except ValueError:
        triangle_area = "Invalid Input!"
    
    return render_template('areaoftriangle.html', result=triangle_area)

if __name__ == "__main__":
    app.run(debug=True)

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

@app.route('/converttoPostfix', methods=['GET', 'POST'])
def stack():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class Stack:
        def __init__(self):
            self.top = None

        def push(self, data):
            new_node = Node(data)
            if self.top:
                new_node.next = self.top
            self.top = new_node

        def pop(self):
            if self.top is None:
                return None
            
            else:
                popped_node = self.top
                self.top = self.top.next
                popped_node.next = None
                return popped_node.data

        def peek(self):
            if self.top:
                return self.top.data
            
            else:
                return None

        def print_stack(self):
            if self.top is None:
                print("Stack is empty")

            else:
                current = self.top
                print("Stack elements (top → bottom):")
                while current:
                    print(current.data)
                    current = current.next

    precedence = {'+': 1, '-': 1, '*': 2,'/': 2,'^': 3}

    def is_operator(c):
        return c in precedence

    def infix_to_postfix(expr):
        stack = Stack()
        output = []

        for token in expr:
            if token.isalnum(): #Checks if alphanumeric (letters or numbers)
                output.append(token)

            elif is_operator(token):
                while (stack.peek() is not None and is_operator(stack.peek()) and precedence[stack.peek()] >= precedence[token]):
                    output.append(stack.pop())
                stack.push(token)

            elif token == '(':
                stack.push(token)

            elif token == ')':
                while stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()  #Remove '('

        while stack.peek() is not None:
            output.append(stack.pop())

        return " ".join(output)
    
    result = None
    if request.method == 'POST':
        expr = request.form['expression']
        result = infix_to_postfix(expr)

    return render_template('converttopostfix.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)

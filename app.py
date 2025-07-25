from flask import Flask, request, render_template

app = Flask(__name__)

# Simple HTML form template
# html_form = """

# """

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            operation = request.form['operation']

            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    error = "Cannot divide by zero."
                else:
                    result = a / b
            else:
                error = "Invalid operation selected."
        except Exception as e:
            error = str(e)

    return render_template("calculator.html", result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
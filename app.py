from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.form.get('a', 0))
            b = float(request.form.get('b', 0))
            operation = request.form.get('operation', '')

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

        # Return JSON if 'Accept: application/json' is in header
        if request.headers.get('Accept') == 'application/json':
            return jsonify({"result": result, "error": error})
    
    # Fallback to HTML render
    return render_template("calculator.html", result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
 
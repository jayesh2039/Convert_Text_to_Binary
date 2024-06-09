from flask import Flask, render_template_string, request

app = Flask(__name__)

def char_to_binary(char):
    """Convert a single character to its binary representation."""
    return format(ord(char), '08b')

def convert_string_to_binary(s):
    """Convert a string of characters to their binary representations."""
    return ' '.join(char_to_binary(char) for char in s)

def binary_to_char(binary):
    """Convert a single binary representation to its character."""
    return chr(int(binary, 2))

def convert_binary_to_string(binary_string):
    """Convert a binary string (space-separated) to its character representation."""
    binary_values = binary_string.split(' ')
    return ''.join(binary_to_char(binary) for binary in binary_values)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Binary Converter</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f7f9fc;
                color: #333;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #444;
                margin-bottom: 30px;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            label {
                font-weight: bold;
                margin: 10px 0;
                color: #555;
            }
            input[type="text"], select {
                width: 100%;
                max-width: 400px;
                padding: 10px;
                margin-top: 5px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
            p {
                text-align: center;
                font-size: 18px;
            }
            a {
                display: block;
                text-align: center;
                margin-top: 20px;
                text-decoration: none;
                color: #007bff;
                font-size: 16px;
                transition: color 0.3s;
            }
            a:hover {
                color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Simple Binary Converter</h1>
            <form action="/convert" method="post">
                <label for="operation">Select Operation:</label>
                <select name="operation" id="operation">
                    <option value="string_to_binary">String to Binary</option>
                    <option value="binary_to_string">Binary to String</option>
                </select>
                <label for="text">Enter Text:</label>
                <input type="text" id="text" name="text" required>
                <input type="submit" value="Convert">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/convert', methods=['POST'])
def convert():
    operation = request.form['operation']
    text = request.form['text']
    
    if operation == 'string_to_binary':
        result = convert_string_to_binary(text)
    elif operation == 'binary_to_string':
        try:
            result = convert_binary_to_string(text)
        except ValueError:
            result = "Invalid binary input."
    else:
        result = "Invalid operation."

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Conversion Result</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f7f9fc;
                color: #333;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #444;
                margin-bottom: 30px;
            }
            p {
                text-align: center;
                font-size: 18px;
            }
            a {
                display: block;
                text-align: center;
                margin-top: 20px;
                text-decoration: none;
                color: #007bff;
                font-size: 16px;
                transition: color 0.3s;
            }
            a:hover {
                color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Conversion Result</h1>
            <p>{{ result }}</p>
            <a href="/">Back to Converter</a>
        </div>
    </body>
    </html>
    ''', result=result)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')

from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/get_version', methods=['GET'])
def get_version():
    return jsonify({"version": "1.0.0"})

@app.route('/check_prime/<string:number>', methods=['GET'])
def check_prime(number):
    try:
        number = int(number)
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

    if number < 0:
        return jsonify({"error": "Negative numbers are not allowed"}), 400
    if number <= 1:
        return jsonify({"number": number, "is_prime": False})
    
    for i in range(2, number):
        if number % i == 0:
            return jsonify({"number": number, "is_prime": False})
    
    return jsonify({"number": number, "is_prime": True})

if __name__ == '__main__':
    app.run(debug=True)

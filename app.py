from flask import Flask, jsonify
app = Flask(__name__)

# Route để lấy version của ứng dụng
@app.route('/get_version', methods=['GET'])
def get_version():
    return jsonify({"version": "1.0.0"})

# Route để kiểm tra số nguyên tố
@app.route('/check_prime/<int:number>', methods=['GET'])
def check_prime(number):
    if number <= 1:
        return jsonify({"number": number, "is_prime": False})
    for i in range(2, number):
        if number % i == 0:
            return jsonify({"number": number, "is_prime": False})
    return jsonify({"number": number, "is_prime": True})

if __name__ == '__main__':
    app.run(debug=True)


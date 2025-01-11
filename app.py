# Interactive Visual Data Structures Learning Tool (Browser-Based Version)
# Updated Code Architecture

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Example data structures for visualization
linked_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_node', methods=['POST'])
def add_node():
    data = request.json
    value = data.get('value')
    if value is not None:
        linked_list.append(value)
        return jsonify({'status': 'success', 'linked_list': linked_list})
    return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

@app.route('/delete_node', methods=['POST'])
def delete_node():
    data = request.json
    value = data.get('value')
    if value in linked_list:
        linked_list.remove(value)
        return jsonify({'status': 'success', 'linked_list': linked_list})
    return jsonify({'status': 'error', 'message': 'Value not found'}), 400

@app.route('/get_linked_list', methods=['GET'])
def get_linked_list():
    return jsonify({'linked_list': linked_list})

if __name__ == '__main__':
    app.run(debug=True)


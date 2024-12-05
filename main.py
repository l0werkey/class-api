from flask import Flask, request, jsonify
import re

app = Flask(__name__)

classes = {}

def format_name(name):
    return re.sub(r'\s+', '_', name.strip().lower())

@app.route('/classes', methods=['GET'])
def get_classes():
    classes_list = [{'id': key, **value} for key, value in classes.items()]
    return jsonify(classes_list)

@app.route('/classes', methods=['POST'])
def add_class():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Class name is required"}), 400

    formatted_name = format_name(data['name'])
    if formatted_name in classes:
        return jsonify({"error": "Class already exists"}), 400

    classes[formatted_name] = {'id': formatted_name, 'name': data['name'], 'students': []}
    return jsonify(classes[formatted_name]), 201

@app.route('/class/<string:class_id>', methods=['GET'])
def get_class(class_id):
    class_data = classes.get(class_id)
    if not class_data:
        return jsonify({"error": "Class not found"}), 404
    return jsonify(class_data)

@app.route('/class/<string:class_id>', methods=['POST'])
def add_student(class_id):
    class_data = classes.get(class_id)
    if not class_data:
        return jsonify({"error": "Class not found"}), 404

    data = request.json
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Student name and age are required"}), 400

    student = {'name': data['name'], 'age': data['age']}
    class_data['students'].append(student)
    return jsonify(student), 201

if __name__ == '__main__':
    app.run(debug=True)

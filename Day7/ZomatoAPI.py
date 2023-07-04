from flask import Flask, jsonify, request

app = Flask(__name__)

menu = [
    {
        'id': 1,
        'name': 'Margherita Pizza',
        'price': 10,
        'availability': True
    },
    {
        'id': 2,
        'name': 'Chicken Tikka Masala',
        'price': 15,
        'availability': True
    },
    {
        'id': 3,
        'name': 'Pasta Alfredo',
        'price': 12,
        'availability': False
    }
]

orders = []

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route('/menu', methods=['POST'])
def add_dish():
    new_dish = request.get_json()
    
    # Check if required fields are present in the request data
    if 'name' not in new_dish or 'price' not in new_dish:
        return jsonify({'message': 'Invalid dish data. Missing name or price.'}), 400
    
    dish_id = len(menu) + 1
    new_dish['id'] = dish_id
    new_dish['availability'] = True
    menu.append(new_dish)
    
    return jsonify({'message': 'Dish added successfully', 'dish': new_dish}), 201


@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            return jsonify({'message': 'Dish removed successfully'})
    return jsonify({'message': 'Dish not found'})

# Add other routes for updating availability, taking orders, and updating order status

if __name__ == '__main__':
    app.run(debug=True)

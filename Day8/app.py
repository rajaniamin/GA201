from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data
dishes = [
    {"id": 1, "name": "Pizza", "price": 10, "availability": True},
    {"id": 2, "name": "Burger", "price": 5, "availability": True},
    {"id": 3, "name": "Pasta", "price": 8, "availability": False},
]

orders = [
    {"id": 1, "customer_name": "John Doe", "dish_ids": [1, 2], "status": "Received"},
    {"id": 2, "customer_name": "Jane Smith", "dish_ids": [2, 3], "status": "Preparing"},
    {"id": 3, "customer_name": "David Johnson", "dish_ids": [1, 3], "status": "Ready for Pickup"},
]


@app.route("/")
def index():
    return render_template("index.html", dishes=dishes, orders=orders)


@app.route("/add_dish", methods=["POST"])
def add_dish():
    dish_id = len(dishes) + 1
    dish_name = request.form.get("dish_name")
    dish_price = float(request.form.get("dish_price"))
    dish_availability = True if request.form.get("dish_availability") == "on" else False

    dish = {
        "id": dish_id,
        "name": dish_name,
        "price": dish_price,
        "availability": dish_availability
    }

    dishes.append(dish)

    return redirect("/")


@app.route("/edit_dish", methods=["POST"])
def edit_dish():
    dish_id = int(request.form.get("dish_id"))
    dish_name = request.form.get("dish_name")
    dish_price = float(request.form.get("dish_price"))
    dish_availability = True if request.form.get("dish_availability") == "on" else False

    for dish in dishes:
        if dish["id"] == dish_id:
            dish["name"] = dish_name
            dish["price"] = dish_price
            dish["availability"] = dish_availability
            break

    return redirect("/")


@app.route("/delete_dish", methods=["POST", "GET"])

def delete_dish():
    dish_id = request.form.get("dish_id")
    
    if dish_id:
        dish_id = int(dish_id)

        for dish in dishes:
            if dish["id"] == dish_id:
                dishes.remove(dish)
                break

    return redirect("/")



@app.route("/take_order", methods=["POST"])
def take_order():
    order_id = len(orders) + 1
    customer_name = request.form.get("customer_name")
    dish_ids = [int(dish_id) for dish_id in request.form.getlist("dish_ids[]")]
    status = "Received"

    order = {
        "id": order_id,
        "customer_name": customer_name,
        "dish_ids": dish_ids,
        "status": status
    }

    orders.append(order)

    return redirect("/")


@app.route("/update_order", methods=["POST"])
def update_order():
    order_id = int(request.form.get("order_id"))
    status = request.form.get("status")

    for order in orders:
        if order["id"] == order_id:
            order["status"] = status
            break

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    customer_name = ""
    order_id = ""
    dress_type = ""
    delivery_status = ""
    message = ""

    if request.method == "POST":
        customer_name = request.form.get("customer_name", "")
        order_id = request.form.get("order_id", "")
        dress_type = request.form.get("dress_type", "")
        delivery_status = request.form.get("delivery_status", "")

        message = f"Hello {customer_name}, your {dress_type} order {order_id} is currently {delivery_status}."

    return render_template(
        "index.html",
        customer_name=customer_name,
        order_id=order_id,
        dress_type=dress_type,
        delivery_status=delivery_status,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
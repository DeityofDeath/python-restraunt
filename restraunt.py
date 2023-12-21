from flask import Flask, render_template, request

app = Flask(__name__)

order_queue = []
completed_orders = []


@app.route('/')
def index():
    return render_template('restindex.html', order_queue=order_queue, completed_orders=completed_orders)


@app.route('/enqueue', methods=['POST'])
def enqueue_order():
    order = request.form.get('order')
    if order:
        order_queue.append(order)
    return render_template('restindex.html', order_queue=order_queue, completed_orders=completed_orders)


@app.route('/dequeue', methods=['POST'])
def dequeue_order():
    if order_queue:
        completed_order = order_queue.pop(0)
        completed_orders.append(completed_order)
    return render_template('restindex.html', order_queue=order_queue, completed_orders=completed_orders)


@app.route('/review_history', methods=['POST'])
def review_history():
    if completed_orders:
        completed_order = completed_orders.pop()
        print(f"Reviewed Order: {completed_order}")
    return render_template('restindex.html', order_queue=order_queue, completed_orders=completed_orders)


app.run(debug=True)

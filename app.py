from flask import Flask, render_template

app = Flask(__name__)

# Sample data for transactions (replace with your actual data)
transactions = [
    {"id": 1, "name": "ABC Corp", "status": "Pre-Approved", "amount": 45000},
    {"id": 2, "name": "XYZ LLC", "status": "Offer Accepted", "amount": 50000},
    {"id": 3, "name": "TEST Inc.", "status": "Capital on its Way", "amount": 25000},
    {"id": 4, "name": "FOOD Kitchen", "status": "No Offers", "amount": "-"}
    # Add more transactions here
]

@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)

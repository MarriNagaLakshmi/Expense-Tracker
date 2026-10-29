from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# v1 Database: In-memory list to store recorded expenses
EXPENSES = [
    {"id": 1, "description": "Notebooks", "amount": 150.0},
    {"id": 2, "description": "Coffee", "amount": 90.0}
]

# Dashboard HTML Interface Layout
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Expense Tracker v1</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f7f6; }
        .container { max-width: 600px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h1, h2 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 10px; background: #eee; margin-bottom: 5px; border-radius: 4px; display: flex; justify-content: space-between; }
        .total { font-weight: bold; background: #d4edda; color: #155724; padding: 10px; border-radius: 4px; margin-top: 20px; font-size: 18px; }
        input[type="text"], input[type="number"] { padding: 8px; width: 35%; margin-right: 5px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📉 Expense Tracker v1</h1>
        
        <!-- v1 Feature: Add - Record expense form -->
        <h2>Add – Record expense</h2>
        <form action="/add" method="POST">
            <input type="text" name="description" placeholder="Description (e.g., Dinner)" required>
            <input type="number" step="0.01" name="amount" placeholder="Amount (₹)" required>
            <button type="submit">Record</button>
        </form>

        <!-- v1 Feature: View - Show expenses -->
        <h2>View – Show expenses</h2>
        <ul>
            {% for expense in expenses %}
            <li>
                <span>{{ expense.description }}</span>
                <strong>₹{{ expense.amount }}</strong>
            </li>
            {% endfor %}
        </ul>

        <!-- v1 Feature: Total - Calculate sum -->
        <h2>Total – Calculate sum</h2>
        <div class="total">Total Spending: ₹{{ total }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    # v1 Feature: Total – Calculate sum
    total_sum = sum(item["amount"] for item in EXPENSES)
    # v1 Feature: View – Show expenses
    return render_template_string(HTML_TEMPLATE, expenses=EXPENSES, total=total_sum)

@app.route("/add", methods=["POST"])
def add_expense_form():
    # v1 Feature: Add – Record expense
    description = request.form.get("description")
    amount = request.form.get("amount")
    if description and amount:
        EXPENSES.append({
            "id": len(EXPENSES) + 1, 
            "description": description, 
            "amount": float(amount)
        })
    return "<script>window.location.href='/';</script>"

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

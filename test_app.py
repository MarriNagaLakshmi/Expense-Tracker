from app import app, EXPENSES

def test_add_record_expense():
    client = app.test_client()
    initial_count = len(EXPENSES)
    response = client.post("/add", data={"description": "Lunch", "amount": "250.0"})
    assert response.status_code == 200
    assert len(EXPENSES) == initial_count + 1

def test_view_and_total_calculation():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Total Spending" in response.data

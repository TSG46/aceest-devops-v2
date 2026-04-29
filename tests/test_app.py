from app import app

# Create test client
client = app.test_client()

# ✅ Test 1 - Home page
def test_home():
    response = client.get("/")
    assert response.status_code == 200

# ✅ Test 2 - Members API
def test_members():
    response = client.get("/members")
    assert response.status_code == 200
    assert b"Ravi" in response.data

# ✅ Test 3 - Health check
def test_health():
    response = client.get("/health")
    assert response.status_code == 200

# ✅ Test 4 - Negative test (extra marks)
def test_invalid_url():
    response = client.get("/invalid")
    assert response.status_code == 404
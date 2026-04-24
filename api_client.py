# api_client.py - API client utilities

import json
import time
from datetime import datetime


class APIClient:
    """Simple API client simulator"""

    def __init__(self, base_url="https://api.example.com"):
        self.base_url = base_url
        self.requests_log = []

    def get(self, endpoint, params=None):
        """Simulate GET request"""
        self._log_request("GET", endpoint, params)

        # Simulate API response
        response = {
            "status": 200,
            "data": {
                "endpoint": endpoint,
                "params": params,
                "timestamp": datetime.now().isoformat(),
                "message": "Success"
            }
        }
        return response

    def post(self, endpoint, data=None):
        """Simulate POST request"""
        self._log_request("POST", endpoint, data)

        response = {
            "status": 201,
            "data": {
                "endpoint": endpoint,
                "body": data,
                "timestamp": datetime.now().isoformat(),
                "id": int(time.time())
            }
        }
        return response

    def _log_request(self, method, endpoint, payload):
        """Log all requests"""
        self.requests_log.append({
            "method": method,
            "endpoint": endpoint,
            "payload": payload,
            "timestamp": datetime.now()
        })

    def get_logs(self):
        """Get all request logs"""
        return self.requests_log

    def clear_logs(self):
        """Clear request logs"""
        self.requests_log = []
        return "Logs cleared"


def fetch_user_data(user_id):
    """Fetch user data by ID"""
    # Simulate user database
    users = {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
        3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    }
    return users.get(user_id, {"error": "User not found"})


def save_to_json(data, filename):
    """Save data to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        return f"Data saved to {filename}"
    except Exception as e:
        return f"Error: {e}"


def load_from_json(filename):
    """Load data from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": f"{filename} not found"}
    except Exception as e:
        return f"Error: {e}"


# Test functions
if __name__ == "__main__":
    # Test APIClient
    client = APIClient()
    print(client.get("/users", {"id": 1}))
    print(client.post("/users", {"name": "New User"}))

    # Test fetch_user_data
    print(f"User data: {fetch_user_data(1)}")

    # Test JSON operations
    test_data = {"name": "Test", "value": 123}
    print(save_to_json(test_data, "test.json"))
    print(load_from_json("test.json"))

    # Show logs
    print(f"Request logs: {client.get_logs()}")
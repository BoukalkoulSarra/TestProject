# view_request_logs.py - View and manage API request logs

from api_client import APIClient


def demonstrate_logging():
    """Show how request logging works"""
    client = APIClient()

    # Make several requests
    print("Making API requests...")
    client.get("/users")
    client.get("/products", {"category": "books"})
    client.post("/orders", {"item": "laptop", "quantity": 1})
    client.get("/profile/123")

    # View logs
    print(f"\nTotal requests made: {len(client.get_logs())}")
    print("\nRequest Logs:")
    for i, log in enumerate(client.get_logs(), 1):
        print(f"{i}. {log['method']} {log['endpoint']} at {log['timestamp']}")

    # Clear logs
    print(f"\n{client.clear_logs()}")
    print(f"Logs after clearing: {len(client.get_logs())}")


if __name__ == "__main__":
    demonstrate_logging()
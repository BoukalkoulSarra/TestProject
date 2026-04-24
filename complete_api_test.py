# complete_api_test.py - Complete testing of all API functions

from api_client import (
    APIClient,
    fetch_user_data,
    save_to_json,
    load_from_json
)


class CompleteAPITest:
    """Test all api_client.py functions"""

    def __init__(self):
        self.client = APIClient()
        self.test_results = []

    def test_get_method(self):
        """Test GET method"""
        print("\n1. Testing GET method...")
        response = self.client.get("/test", {"key": "value"})
        assert response['status'] == 200
        self.test_results.append("✅ GET method works")
        return response

    def test_post_method(self):
        """Test POST method"""
        print("2. Testing POST method...")
        response = self.client.post("/test", {"data": "test"})
        assert response['status'] == 201
        self.test_results.append("✅ POST method works")
        return response

    def test_fetch_user(self):
        """Test fetch_user_data function"""
        print("3. Testing fetch_user_data...")
        user = fetch_user_data(1)
        assert user['name'] == "Alice"
        self.test_results.append("✅ fetch_user_data works")
        return user

    def test_json_operations(self):
        """Test JSON save/load functions"""
        print("4. Testing JSON operations...")
        test_data = {"test": "data", "number": 42}
        save_to_json(test_data, "test_output.json")
        loaded = load_from_json("test_output.json")
        assert loaded == test_data
        self.test_results.append("✅ JSON save/load works")
        return loaded

    def test_logging(self):
        """Test request logging"""
        print("5. Testing request logging...")
        initial_logs = len(self.client.get_logs())
        self.client.get("/log-test")
        self.client.post("/log-test", {})
        new_logs = len(self.client.get_logs())
        assert new_logs == initial_logs + 2
        self.test_results.append("✅ Logging works")

    def run_all_tests(self):
        """Run all tests"""
        print("=" * 50)
        print("RUNNING COMPLETE API CLIENT TESTS")
        print("=" * 50)

        self.test_get_method()
        self.test_post_method()
        self.test_fetch_user()
        self.test_json_operations()
        self.test_logging()

        print("\n" + "=" * 50)
        print("TEST RESULTS SUMMARY")
        print("=" * 50)
        for result in self.test_results:
            print(result)

        print(f"\n✅ All tests passed! ({len(self.test_results)}/5)")
        print(f"📊 Total API calls logged: {len(self.client.get_logs())}")


# Run complete test suite
if __name__ == "__main__":
    tester = CompleteAPITest()
    tester.run_all_tests()
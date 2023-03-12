import time
import threading
import requests
import unittest

from app import app

class TestProductService(unittest.TestCase):
    def test_get_products_performance(self):
        #Define the number of requests to send per second
        requests_per_second = 2500
        # Define the number of seconds to run the test
        test_duration_seconds = 10
        # Start the Product service
        app_thread = threading.Thread(target=app.run)
        app_thread.start()
        # Define the URL to send requests to
        url = 'http://localhost:5001/products'
        # Keep track of the number of successful requests
        response = requests.get(url)
        print(response)



        #num_successes = 0
        # Calculate the number of requests to send
        #total_requests = requests_per_second * test_duration_seconds
        # Send requests at the specified rate
        #start_time = time.time()
        #for i in range(total_requests):
        #    response = requests.get(url)
        #    if response.status_code == 200:
        #        num_successes += 1
        #    time_elapsed = time.time() - start_time
        #    expected_num_successes = int(time_elapsed * requests_per_second)
        #    if num_successes < expected_num_successes:
        #        time.sleep(expected_num_successes / requests_per_second - time_elapsed)

        # Stop the Product service
        # Verify that the number of successful requests meets the threshold
        #self.assertGreaterEqual(num_successes, requests_per_second * test_duration_seconds * 0.9)
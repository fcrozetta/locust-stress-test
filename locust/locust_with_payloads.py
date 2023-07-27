from locust import HttpUser, task, between

correct_payload = {"name": "Jon", "age": 30}
incorrect_payload = {"invalid": "payload"}


class User1(HttpUser):
    wait_time = between(1, 5)

    @task(5)
    def success_simple_call(self):
        self.client.get("/simple-get")

    @task(5)
    def success_long_call(self):
        self.client.get("/long-wait")

    @task(2)
    def error_call(self):
        self.client.get("/error")

    @task(5)
    def post_correct_payload(self):
        self.client.post("/input-process", json=correct_payload)

    @task(2)
    def incorrect_payload(self):
        self.client.post("/input-process", json=incorrect_payload)

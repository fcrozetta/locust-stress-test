from locust import HttpUser, task


class UserTasks(HttpUser):
    @task(5)
    def get_random_failure(self):
        self.client.get("/random-failure")

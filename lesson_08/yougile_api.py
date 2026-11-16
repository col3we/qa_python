import requests


class YougileProjectsApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, data):
        return requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id, data):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=data,
            headers=self.headers
        )

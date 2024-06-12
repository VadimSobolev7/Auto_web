import pytest
import yaml
import requests

with open("C:\Python_web_test\Seminar_1\DZ\config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    print(res1.content)
    return res1.json()["token"]

@pytest.fixture()
def test_text_1():
    return 'Test_text_1'
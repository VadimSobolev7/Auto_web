import yaml
import requests

with open("C:\Python_web_test\Seminar_1\DZ\config.yaml", "r") as f:
    data = yaml.safe_load(f)

def test_step_1(login, test_text_1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner":"notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert test_text_1 in listres, "Test 1 failed"

def test_step_2(login):
    header = {"X-Auth-Token": login}
    res1 = requests.post(data["address"] + "api/posts", params={"title":"Python", "description":"Python", "content":"Python"}, headers=header)
    res2 = requests.get(data["address"] + "api/posts", params={"description":"Python"}, headers=header)
    assert res1 and res2, "test2 FAIL (HW)"
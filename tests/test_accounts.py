import pytest
from jose import jwt
from app.schemas import account_schema, token_schema
from app.core.configs import settings
from .conftest import SQLALCHEMY_DATABASE_URL

def test_example():
    print(SQLALCHEMY_DATABASE_URL)
    assert 7 == 3 + 4


# def test_create_account(client):
#     res = client.post("/accounts/", json={"email": "johnwick@test.mail", "password": "password123", "name": "John"})
#     new_account = account_schema.AccountOut(**res.json())
#     assert new_account.email == "johnwick@test.mail"
#     assert res.status_code == 201
#
#
# def test_account_login(client, test_account):
#     res = client.post("/login", data={"username": test_account["email"], "password": test_account["password"]})
#     res_body = token_schema.Token(**res.json())
#     payload = jwt.decode(res_body.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#     id = payload.get("id")
#     assert id == test_account["id"]
#     assert res_body.token_type == "bearer"
#     assert res.status_code == 200
#
#
# @pytest.mark.parametrize("email, password, status_code", [
#     ("wrongemail@test.com", "password123", 401),
#     ("turtles@test.com", "wtfisgoingon", 401),
#     (None, "somethingwrong", 422),
#     ("turtles@test.com", None, 422)
# ])
# def test_invalid_login(test_account, client, email, password, status_code):
#     res = client.post("/login", data={"username": email, "password": password})
#     assert res.status_code == status_code

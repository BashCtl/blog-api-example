import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.configs import settings
from app.models import Base
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.run import app
from app.models import post_model, post_like_model, account_model, comments_model, comment_like_model

SQLALCHEMY_DATABASE_URL = (f"postgresql+psycopg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_URI}"
                           f":{settings.DB_PORT}/{settings.DB_NAME}_test")



engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @pytest.fixture
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @pytest.fixture
# def client(session):
#     def override_get_db():
#         try:
#             yield session
#         finally:
#             session.close()
#
#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)
#
#
# @pytest.fixture
# def test_account(client):
#     account_data = {"email": "turtles@test.com",
#                     "name": "ninja",
#                     "password": "qwerty1234"}
#     res = client.post("/accounts/", json=account_data)
#     assert res.status_code ==201
#     new_account = res.json()
#     new_account["password"] = account_data["password"]
#     return new_account

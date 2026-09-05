"""
=============================================================================
Automated API & Service Tests (pytest)
TokyoApps Global Technologies - NULOGIC_CORE
=============================================================================
"""

import pytest
from fastapi.testclient import TestClient
from main import app
from modules.database import SessionLocal, Base, engine

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["system"] == "NULOGIC_CORE"
    assert response.json()["compliance"] == "GDPR/LFPDPPP Active"

def test_register_user_success():
    payload = {
        "email": "api.test@tokyoapps.com",
        "password": "securepassword123",
        "gdpr_accepted": True,
        "lfpdppp_accepted": True
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "api.test@tokyoapps.com"
    assert data["status"] == "registered_with_consent"

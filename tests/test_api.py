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

def test_create_transaction_success():
    # 1. Registrar usuario previo
    user_payload = {
        "email": "fintech.user@tokyoapps.com",
        "password": "securepassword123",
        "gdpr_accepted": True,
        "lfpdppp_accepted": True
    }
    user_res = client.post("/users/", json=user_payload)
    user_id = user_res.json()["id"]

    # 2. Crear transacción asociada
    tx_payload = {
        "user_id": user_id,
        "gateway": "okx_v5",
        "amount": 250.50,
        "currency": "USDT",
        "reference_id": "TX_TEST_OKX_12345"
    }
    response = client.post("/transactions/", json=tx_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["reference_id"] == "TX_TEST_OKX_12345"
    assert data["status"] == "completed"

"""
=============================================================================
FastAPI Enterprise Endpoints & System Initialization
TokyoApps Global Technologies - NULOGIC_CORE
=============================================================================
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from modules.database import get_db, engine, Base
from modules.models import User, Transaction
from services.user_service import UserService
from pydantic import BaseModel, EmailStr

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NULOGIC_CORE Enterprise API",
    version="1.0.0",
    description="Fintech-compliant ecosystem with strict GDPR and LFPDPPP governance."
)

class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str
    gdpr_accepted: bool
    lfpdppp_accepted: bool

class TransactionRequest(BaseModel):
    user_id: int
    gateway: str
    amount: float
    currency: str = "USDT"
    reference_id: str

@app.get("/")
def health_check():
    return {
        "system": "NULOGIC_CORE",
        "status": "operational",
        "compliance": "GDPR/LFPDPPP Active",
        "author": "José Arturo Orozco Jaime (TokyoApps)"
    }

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreateRequest, db: Session = Depends(get_db)):
    try:
        user = UserService.create_user_with_consent(
            db=db,
            email=payload.email,
            hashed_password=payload.password,
            gdpr=payload.gdpr_accepted,
            lfpdppp=payload.lfpdppp_accepted,
            ip_address="127.0.0.1"
        )
        return {"id": user.id, "email": user.email, "status": "registered_with_consent"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.post("/transactions/", status_code=status.HTTP_201_CREATED)
def create_transaction(payload: TransactionRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Usuario con ID {payload.user_id} no encontrado."
        )
    
    try:
        tx = UserService.add_transaction(
            db=db,
            user_id=payload.user_id,
            gateway=payload.gateway,
            amount=payload.amount,
            currency=payload.currency,
            reference_id=payload.reference_id
        )
        return {"transaction_id": tx.id, "reference_id": tx.reference_id, "status": tx.status}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

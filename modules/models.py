"""
=============================================================================
Enterprise ORM Models (Users, Consents, Transactions)
TokyoApps Global Technologies - NULOGIC_CORE
=============================================================================
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from modules.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    consents = relationship("UserConsent", back_populates="user", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")

class UserConsent(Base):
    __tablename__ = "user_consents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    consent_version = Column(String, nullable=False, default="v1.0")
    gdpr_accepted = Column(Boolean, default=False, nullable=False)
    lfpdppp_accepted = Column(Boolean, default=False, nullable=False)
    ip_address = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="consents")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    gateway = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="USDT", nullable=False)
    status = Column(String, default="pending", nullable=False)
    reference_id = Column(String, unique=True, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="transactions")

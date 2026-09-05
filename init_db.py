"""
=============================================================================
Database Initialization Script
TokyoApps Global Technologies - NULOGIC_CORE
=============================================================================
"""

from modules.database import engine, Base
from modules.models import User, UserConsent, Transaction

def init_db():
    print("==================================================")
    print("  NULOGIC_CORE DATABASE INITIALIZATION & MIGRATION")
    print("  TokyoApps Global Technologies")
    print("==================================================")
    print("[*] Creando tablas relacionales en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("[SUCCESS] Todas las tablas (users, user_consents, transactions) creadas exitosamente.")

if __name__ == "__main__":
    init_db()

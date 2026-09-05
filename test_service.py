"""
=============================================================================
Service Verification Script
TokyoApps Global Technologies - NULOGIC_CORE
=============================================================================
"""

from modules.database import SessionLocal, engine, Base
from services.user_service import UserService
from modules.models import User

def run_test():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        print("==================================================")
        print("  VERIFICACIÓN DE SERVICIOS DE NEGOCIO")
        print("==================================================")
        
        test_email = "test.enterprise@tokyoapps.com"
        user = db.query(User).filter(User.email == test_email).first()
        
        if not user:
            try:
                user = UserService.create_user_with_consent(
                    db=db,
                    email=test_email,
                    hashed_password="secure_hashed_password_sample",
                    gdpr=True,
                    lfpdppp=True,
                    ip_address="127.0.0.1"
                )
            except ValueError as ve:
                print(f"[INFO] {ve}")
                user = db.query(User).filter(User.email == test_email).first()
        else:
            print(f"[INFO] El usuario {test_email} ya existe en la base de datos.")

        if user:
            UserService.add_transaction(
                db=db,
                user_id=user.id,
                gateway="okx_v5",
                amount=150.00,
                currency="USDT",
                reference_id="TX_OKX_987654321"
            )
            
        print("[SUCCESS] Pruebas de lógica de servicios completadas sin errores.")
        
    finally:
        db.close()

if __name__ == "__main__":
    run_test()

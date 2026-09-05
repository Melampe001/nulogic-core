"""
=============================================================================
Business Logic Services (User Management, Consents, Transactions)
TokyoApps Global Technologies - NULOGIC_CORE
=============================================================================
"""

from sqlalchemy.orm import Session
from modules.models import User, UserConsent, Transaction

class UserService:
    @staticmethod
    def create_user_with_consent(
        db: Session, 
        email: str, 
        hashed_password: str, 
        gdpr: bool, 
        lfpdppp: bool, 
        ip_address: str = None
    ) -> User:
        """Crea un usuario y registra su consentimiento auditable GDPR/LFPDPPP."""
        
        # Verificar si el usuario ya existe
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise ValueError(f"El usuario con el correo {email} ya se encuentra registrado.")

        # Crear instancia de usuario
        db_user = User(email=email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # Registrar el consentimiento normativo
        db_consent = UserConsent(
            user_id=db_user.id,
            consent_version="v1.0",
            gdpr_accepted=gdpr,
            lfpdppp_accepted=lfpdppp,
            ip_address=ip_address
        )
        db.add(db_consent)
        db.commit()

        print(f"[SUCCESS] Usuario {email} registrado con consentimiento GDPR/LFPDPPP verificado.")
        return db_user

    @staticmethod
    def add_transaction(
        db: Session,
        user_id: int,
        gateway: str,
        amount: float,
        currency: str,
        reference_id: str
    ) -> Transaction:
        """Registra una transacción financiera para el usuario."""
        db_tx = Transaction(
            user_id=user_id,
            gateway=gateway,
            amount=amount,
            currency=currency,
            status="completed",
            reference_id=reference_id
        )
        db.add(db_tx)
        db.commit()
        db.refresh(db_tx)
        
        print(f"[SUCCESS] Transacción {reference_id} registrada por {amount} {currency} ({gateway}).")
        return db_tx

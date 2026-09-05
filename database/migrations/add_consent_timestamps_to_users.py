# Migración automatizada para cumplimiento normativo (LFPDPPP / GDPR)
# Añade marcas de tiempo y aceptación obligatoria de Términos de Servicio y Privacidad

from datetime import datetime

def upgrade_database_schema(db_connection):
    cursor = db_connection.cursor()
    cursor.execute('''
        ALTER TABLE users ADD COLUMN IF NOT EXISTS terms_accepted BOOLEAN NOT NULL DEFAULT 0;
    ''')
    cursor.execute('''
        ALTER TABLE users ADD COLUMN IF NOT EXISTS terms_accepted_at TIMESTAMP NULL;
    ''')
    cursor.execute('''
        ALTER TABLE users ADD COLUMN IF NOT EXISTS privacy_policy_accepted BOOLEAN NOT NULL DEFAULT 0;
    ''')
    cursor.execute('''
        ALTER TABLE users ADD COLUMN IF NOT EXISTS privacy_policy_accepted_at TIMESTAMP NULL;
    ''')
    db_connection.commit()
    print("[OK] Esquema de base de datos actualizado con registros de consentimiento y timestamps.")
__import__('sys').modules[__name__] = upgrade_database_schema

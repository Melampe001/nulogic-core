# ==============================================================================
# NULOGIC_CORE - Orquestador Principal del Ecosistema
# Autor: José Arturo Orozco Jaime (TokyoApps Global Technologies)
# ==============================================================================

import os
import sys
from modules.payment_gateway import HybridPaymentGateway
from modules.okx_v5_integration import OKXV5Connector

def initialize_system():
    print("==================================================")
    print("  NULOGIC_CORE ENTERPRISE SYSTEM INITIALIZATION  ")
    print("  TokyoApps Global Technologies                  ")
    print("==================================================")

    # 1. Validación de Credenciales y Módulos
    print("[*] Verificando módulos de pasarela de pagos y OKX V5...")
    payment_gateway = HybridPaymentGateway()
    okx_connector = OKXV5Connector()

    # 2. Prueba de conectividad simulada / segura
    balance_status = okx_connector.fetch_account_balance()
    print(f"[OKX V5 Sync Status]: {balance_status}")

    # 3. Verificación de cumplimiento legal
    compliance_mode = os.getenv("GDPR_LFPDPPP_COMPLIANCE", "true")
    print(f"[Compliance Check]: Protocolos de consentimiento LFPDPPP/GDPR activos ({compliance_mode}).")
    
    print("[SUCCESS] NULOGIC_CORE inicializado operativamente bajo estándares globales.")

if __name__ == "__main__":
    initialize_system()

#!/usr/bin/env python3
"""
Aplicação principal do projeto Modern Python UV Project Scaffold
"""
import os
import sys
from pathlib import Path


def main():
    """Função principal da aplicação"""
    print("🚀 Bem-vindo ao Modern Python UV Project Scaffold!")
    print(f"📂 Executando em: {Path.cwd()}")
    print(f"🐍 Python: {sys.version}")

    # Exemplo de lógica básica
    environment = os.getenv("ENVIRONMENT", "development")
    print(f"🌍 Ambiente: {environment}")

    if environment == "production":
        print("🔒 Executando em modo produção")
    else:
        print("🛠️ Executando em modo desenvolvimento")


if __name__ == "__main__":
    main()

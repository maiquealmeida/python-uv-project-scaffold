#!/bin/bash
# Script para executar em modo produção

export ENVIRONMENT=production
echo "🔒 Executando em modo produção..."
uv run python -m src.main

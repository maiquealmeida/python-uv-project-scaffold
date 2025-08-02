#!/bin/bash
# Script para executar em modo desenvolvimento

export ENVIRONMENT=development
echo "🛠️ Executando em modo desenvolvimento..."
uv run python -m src.main

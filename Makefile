# Makefile para projeto Modern Python UV Project Scaffold

.PHONY: help install dev start prod run test test-watch lint format type-check check clean

help: ## Mostra esta ajuda
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instala as dependências do projeto
	uv sync

dev: ## Executa a aplicação em modo desenvolvimento
	ENVIRONMENT=development uv run python -m src.main

start: dev ## Alias para dev

prod: ## Executa a aplicação em modo produção
	ENVIRONMENT=production uv run python -m src.main

run: prod ## Alias para prod

test: ## Executa os testes
	uv run pytest

test-watch: ## Executa os testes com watch mode
	uv run pytest --watchdog-timeout=60 -s

lint: ## Executa linting do código
	uv run flake8 src tests

format: ## Formata o código com black
	uv run black src tests

type-check: ## Executa type checking com mypy
	uv run mypy src

check: lint type-check test ## Executa todas as verificações (lint, type-check, test)

clean: ## Remove caches e arquivos temporários
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -name "*.pyc" -delete

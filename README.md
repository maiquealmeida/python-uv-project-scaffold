# Modern Python UV Project Scaffold

Projeto Python inicializado com UV, estruturado com código fonte em `/src`.

## Estrutura do Projeto

```
Modern Python UV Project Scaffold/
├── src/
│   ├── __init__.py
│   └── main.py          # Aplicação principal
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Testes unitários
├── scripts/
│   ├── dev.sh           # Script de desenvolvimento
│   └── prod.sh          # Script de produção
├── pyproject.toml       # Configuração do projeto
├── Makefile             # Scripts make
├── README.md
└── .gitignore
```

## Instalação

Clone este repositório. Disponibilizei uma ferramenta para facilitar a criação de novos projetos com base neste e outros repositórios:

```bash
npx @maiquealmeida/git-template maiquealmeida/python-uv-project-scaffold ./nome-do-projeto
```

Acesse o diretório criado para o projeto e enstale as dependências do projeto:

```bash
cd nome-doprojeto

uv sync
```

## Scripts Disponíveis

### Via Makefile (Recomendado)

- **Desenvolvimento**: `make dev` ou `make start`
- **Produção**: `make prod` ou `make run`
- **Testes**: `make test`
- **Testes com watch**: `make test-watch`
- **Linting**: `make lint`
- **Formatação**: `make format`
- **Type checking**: `make type-check`
- **Verificação completa**: `make check`
- **Ajuda**: `make help`

### Via Scripts Shell

- **Desenvolvimento**: `./scripts/dev.sh`
- **Produção**: `./scripts/prod.sh`

### Via UV (Direto)

- **Desenvolvimento**: `ENVIRONMENT=development uv run python -m src.main`
- **Produção**: `ENVIRONMENT=production uv run python -m src.main`

## Exemplos de Uso

```bash
# Instalar dependências
uv sync

# Executar em modo desenvolvimento
make dev

# Executar em modo produção
make prod

# Executar testes
make test

# Formatar código
make format

# Verificar qualidade do código
make check

# Ver todos os comandos disponíveis
make help
```

## Desenvolvimento

O projeto está configurado com as seguintes ferramentas de desenvolvimento:

- **pytest**: Framework de testes
- **black**: Formatação de código
- **flake8**: Linting
- **mypy**: Type checking

## Variáveis de Ambiente

- `ENVIRONMENT`: Define o ambiente de execução (`development` ou `production`)
  - Padrão: `development`

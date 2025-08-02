"""
Main module tests
"""

import sys
import os
from pathlib import Path
from unittest.mock import patch
from io import StringIO

# Adiciona o diretório src ao path para imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import main  # noqa: E402


def test_main_development_environment():
    """Testa a execução da função main em ambiente de desenvolvimento"""
    with patch.dict(os.environ, {"ENVIRONMENT": "development"}):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            assert "🚀 Bem-vindo ao Modern Python UV Project Scaffold!" in output
            assert "🛠️ Executando em modo desenvolvimento" in output
            assert "🌍 Ambiente: development" in output


def test_main_production_environment():
    """Testa a execução da função main em ambiente de produção"""
    with patch.dict(os.environ, {"ENVIRONMENT": "production"}):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            assert "🚀 Bem-vindo ao Modern Python UV Project Scaffold!" in output
            assert "🔒 Executando em modo produção" in output
            assert "🌍 Ambiente: production" in output


def test_main_default_environment():
    """Testa a execução da função main sem definir ambiente.

    Deve usar development como padrão.
    """
    # Remove a variável de ambiente se existir
    env_copy = os.environ.copy()
    if "ENVIRONMENT" in env_copy:
        del env_copy["ENVIRONMENT"]

    with patch.dict(os.environ, env_copy, clear=True):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            assert "🚀 Bem-vindo ao Modern Python UV Project Scaffold!" in output
            assert "🛠️ Executando em modo desenvolvimento" in output
            assert "🌍 Ambiente: development" in output

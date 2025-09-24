#!/bin/bash
# Script de Chamada para a Calculadora Python - EBAC

echo "Iniciando o Script de Chamada..."

# Define o nome do seu arquivo Python principal
# *** MUDE 'calculadora_express.py' para o NOME REAL do seu arquivo Python ***
PYTHON_SCRIPT="calculadora_express.py"

# --- Verificações de Segurança (Boa Prática) ---
# Verifica se o arquivo Python existe
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Erro: O arquivo Python da calculadora ('$PYTHON_SCRIPT') não foi encontrado."
    echo "Certifique-se de que ele está na mesma pasta que 'calculadora.sh'."
    exit 1 # Sai do script com erro
fi

# Verifica se o arquivo Python tem permissão de execução
if [ ! -x "$PYTHON_SCRIPT" ]; then
    echo "Erro: O arquivo Python da calculadora ('$PYTHON_SCRIPT') não tem permissão de execução."
    echo "Use 'chmod u+x $PYTHON_SCRIPT' para corrigir e tente novamente."
    exit 1 # Sai do script com erro
fi
# --- Fim das Verificações ---

# Executa o seu script Python
./"$PYTHON_SCRIPT"

echo "Fim do Script de Chamada."
# Script de Chamada para a Calculadora Python - EBAC

echo "Iniciando o Script de Chamada..."

# Define o nome do seu arquivo Python principal
# *** MUDE 'minha_calc.py' para o NOME REAL do seu arquivo Python ***
PYTHON_SCRIPT="calculadora_express.py"

# --- Verificações de Segurança (Boa Prática) ---
# Verifica se o arquivo Python existe
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Erro: O arquivo Python da calculadora ('$PYTHON_SCRIPT') não foi encontrado."
    echo "Certifique-se de que ele está na mesma pasta que 'calculadora.sh'."
    exit 1 # Sai do script com erro
fi

# Verifica se o arquivo Python tem permissão de execução
if [ ! -x "$PYTHON_SCRIPT" ]; then
    echo "Erro: O arquivo Python da calculadora ('$PYTHON_SCRIPT') não tem permissão de execução."
    echo "Use 'chmod u+x $PYTHON_SCRIPT' para corrigir e tente novamente."
    exit 1 # Sai do script com erro
fi
# --- Fim das Verificações ---

# Executa o seu script Python
./"$PYTHON_SCRIPT"

echo "Fim do Script de Chamada."

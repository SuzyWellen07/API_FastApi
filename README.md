# API_FastApi

Atividade realizada na matéria de Desenvolvimento Web IV no IFPR.

```bash
# Ex. 1 - Criar um endpoint que identificar se um número é par ou ímpar "PAR" ou "IMPAR"

# Ex. 2 - Informar 3 horarios, de acordo com a cidade que usuário especificar na url (brasilia, tokyo, londres)
GET localhost:8000/hora/tokyo

# Ex. 3 - retorna o nome do dia da semana (seg, terça, ...) de acordo com o dia atual
Endpoint: /diasemana
```

## Executando a API

```bash
# 1. criar ambiente virtual
python3 -m venv env
# 2. ativar ambiente virtual
source env/bin/activate
# 3. instalar dependências
pip install requirements.txt
# 4. iniciar FastApi
uvicorn main:app --reload
```

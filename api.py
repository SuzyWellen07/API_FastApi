from fastapi import FastAPI
from datetime import datetime
import pytz
import locale

# Defina o idioma local para exibir datas em português
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Crie uma instância do FastAPI
app = FastAPI()

# Mapeamento de cidades para fusos horários
fusos_horarios = {
    'BRASILIA': 'America/Sao_Paulo',
    'TOKYO': 'Asia/Tokyo',
    'LONDON': 'Europe/London'
}

# Ex. 1 - Criar um endpoint que identifica se um número é par ou ímpar "PAR" ou "IMPAR"
@app.get("/tipo/{num}")
def tipo(num: int):
    resultado = "par" if num % 2 == 0 else "ímpar"  # Modificação: corrigir a palavra "ímpar"
    return {"numero": num, "tipo": resultado}

# Ex. 2 - Informar 3 horários, de acordo com a cidade especificada na URL (brasilia, tokyo, londres)
# É necessário ter a biblioteca pytz instalada (pip install pytz)
@app.get("/hora/{cidade}")
def hora(cidade: str):
    cidade = cidade.upper()
    
    if cidade not in fusos_horarios:
        return {"error": "Cidade não encontrada ou nome incorreto."}  # Modificação: retornar um dicionário com uma chave "error"

    fuso_horario = pytz.timezone(fusos_horarios[cidade])
    data_atual = datetime.now(fuso_horario)
    
    horarios = {
        "Brasilia": data_atual.strftime("%d/%m/%Y %H:%M:%S"),
        "Tokyo": data_atual.strftime("%d/%m/%Y %H:%M:%S"),
        "London": data_atual.strftime("%d/%m/%Y %H:%M:%S")
    }
    
    return horarios

# Ex. 3 - Retorna o nome do dia da semana (seg, terça, ...) de acordo com o dia atual
@app.get("/diasemana")
def dia():
    # Obter a data atual
    data = datetime.now()
    # Formatar a data como o nome do dia da semana
    dia_semana = data.strftime("%A")
    
    # Verificar se é sábado ou domingo e adicionar "-feira" para os outros dias
    return {"dia": dia_semana if dia_semana in ['sábado', 'domingo'] else dia_semana + "-feira"}

# Endpoint para a raiz
@app.get("/")
def root():
    return {"message": "Bem-vindo à API FastAPI"}

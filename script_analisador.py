from pathlib import Path
from datetime import datetime
import re



limite = 3
suspeitos = {}

caminho = Path('logs/log.txt')
contagem = {}
def ler_arquivo(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
            return 'Arquivo não encontrado'
    except PermissionError:
            return 'Permissão negada'

conteudo = ler_arquivo(caminho)
ips = re.findall(r"\d+\.\d+\.\d+\.\d+",conteudo)
for ip in ips:
    if ip in contagem:
       contagem[ip] += 1
    else:
       contagem[ip] = 1

for ip, quantidade in contagem.items():
    if quantidade > limite:
        suspeitos[ip] = quantidade
        
        
def salvar_relatorio(suspeitos):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open('relatorio.txt', 'w') as arquivo:
        arquivo.write('Relatorio de Seguranca\n')
        arquivo.write(f'Gerado em: {data}\n')
        arquivo.write('-' * 30 + '\n')
        for ip, quantidade in suspeitos.items():
            arquivo.write(f'{ip} - {quantidade} tentativas\n')

salvar_relatorio(suspeitos)
    

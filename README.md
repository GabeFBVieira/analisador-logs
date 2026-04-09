# Analisador de Logs de Segurança

Script Python que analisa logs de acesso, identifica IPs suspeitos
e gera um relatório automaticamente.

## Funcionalidades
- Lê arquivos de log
- Extrai IPs com regex
- Conta tentativas por IP
- Gera relatório com IPs suspeitos

## Como usar
1. Coloque seu log.txt na pasta logs/
2. Execute o script
3. O relatório será gerado em relatorio.txt

## Tecnologias
- Python 3
- pathlib
- re (regex)
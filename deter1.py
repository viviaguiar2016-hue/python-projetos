from datetime import datetime

agora_completo = datetime.now()

hora = agora_completo.hour
minuto = agora_completo.minute
day = agora_completo.day
mes = agora_completo.month  
ano = agora_completo.year   


print(f"Hoje {hora}:{minuto}:{day}:{mes}:{ano}")
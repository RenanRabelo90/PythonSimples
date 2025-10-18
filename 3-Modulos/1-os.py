import os

#Biblioteca de Sistema Operacional

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
os.system("ver")

# 4 - Configurações da Máquina
os.system("systeminfo")

# 5 - Limpar a tela do terminal
os.system("cls")

# 6 - Desligar o computador em um minuto
#os.system("shutdown /s")

# Desligar o computador imediatamente
#os.system("shutdown /s /t 0")

#cancelar desligamento
#os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

def turn_off_half_hour():
    os.system("shutdown /s /t 1800")

def cancel_shutdown():
    os.system("shutdown /a")

cancel_shutdown()
import os

# 1- Desligar o computador
os.system("shutdown /s") # Desliga o computador em 60s
#os.system("shutdown /s /t 0") #Desliga o compuador imediatamente
#os.system("shutdown now") - Linux

#2 - Cancelar Desligamento
#os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")
    
def turn_off_half_hour():
    os.system("shutdown /s /t 1800")
    
def cancel_shutdown():
    os.system("shutdown /a")
    
#turn_off_one_hour()
#cancel_shutdown()
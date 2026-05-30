# Criar um lembrete frequente

import time
from plyer import notification

def alert():
    notification.notify(
        title = "NOTIFICAÇÃO",
        message = "Hora de apontar horas",
        app_name = "Notificações",
        timeout = 10
    )

while True:
    alert()
    time.sleep(15)
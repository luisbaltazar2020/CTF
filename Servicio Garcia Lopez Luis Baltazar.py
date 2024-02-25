import psutil
import sys
from datetime import datetime
import threading


def tiempo():
    now = datetime.now()
    return now

def killed():
     while True:
        locked(target)

def argumentos():
    if len(sys.argv)==1:
        print("El programa necesita argumentos")
        sys.exit(0)

def locked(target):
    for proc in psutil.process_iter():
        if proc.name().lower()==target.lower():
            proc.kill()
            print("la aplicacion fue detectada y detenida en: "+ str(tiempo()))

pasa=threading.Thread(target=killed)

argumentos()
target=sys.argv[1]
pasa.start()


print("exito!")
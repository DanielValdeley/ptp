import sys, time
import poller
from serial import Serial

class CallbackSend(poller.Callback):

    def __init__(self, serial: Serial, timeout:float):
        poller.Callback.__init__(self, sys.stdin, timeout)
        self._s = serial

    def handle(self):
        msg = sys.stdin.readline(128)
        self._s.write(msg.encode('ascii'))
        print(f'enviou: {msg}')



####################################################
class CallbackReceived(poller.Callback):

    def __init_(self, serial: Serial, timeout:float):
        poller.Callback.__init_(self, serial, timeout)
        self._s = serial
        
    
    def handle_idle(self, msg):
        pass

    def handle_prep(self, msg):
        pass

    def handle_rx(self, msg):
        pass
    def handle_esc(self, msg):
        pass

    def handle(self):
        msg = self._s.read(128)
        print(f'recebeu: {msg}')
        self._current_handler(msg)

    def handle_timeout(self):
        'O tratador de envento timeout'
        'Desativa o timeout deste callback, e também evento de envio de pacote!'
        self.disable_timeout()
        self.disable()

##########################################

try:
  porta = sys.argv[1]
except:
  print('Uso: %s porta_serial' % sys.argv[0])
  sys.exit(0)

try:
  p = Serial(porta, 9600, timeout=10)
except Exception as e:
  print('Não conseguiu acessar a porta serial', e)
  sys.exit(0)

cs = CallbackSend(p, timeout=10)

sched = poller.Poller()

sched.adiciona(cs)

sched.despache()

print('compilou!')



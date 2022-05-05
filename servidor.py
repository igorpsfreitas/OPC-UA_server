import socket
from opcua import Server

class Servidor():
    def __init__(self, ip = None, port = '4840'):
        self._ip = ip if ip != None else self._ipBase()
        self._port = port 
        
        self._servidor = Server()
        self._set_Endpoint(self._ip, self._port)
        self.set_NomeServidor('Server HUB - Sensnor')
        
        
        # Refatorar....
        self.space = self._servidor.register_namespace('Sensores')
        
        self.objects = self._servidor.get_objects_node()
        
        self.grupoObjetos = self.objects.add_object(self.space, 'Grupo 1')
        
        self.var1 = self.objects.add_variable(self.space, 'Variavel 1', 100)
        
        self.var1.set_writable()
        ###
        
    # Setter nome do Servidor:
    def set_NomeServidor(self, nome):
        self._servidor.name = nome
    
    def _set_Endpoint(self,ip, port):
        self._servidor.set_endpoint(f'opc.tcp://{ip}:{port}')
    
    # Auto set para IP do Servidor:    
    def _ipBase(self):
        ipSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ipSocket.connect(('8.8.8.8', 80))
        ip = str(ipSocket.getsockname()[0])
        ipSocket.close()
        return ip
    
    # Setter IP servidor:
    def setIp(self, value = str()):
        self._ip = value
    
    
    def iniciaServidor(self):
        self._servidor.start()
        
    def finalizaServidor(self):
        self._servidor.stop()

            


# Testes: 

Serv = Servidor()
Serv.iniciaServidor()

while True:
    t = input()
    if t == '0':
        Serv.finalizaServidor()
        break
    else:
        
        
        
        
        
        #         
        # Setter valor variavel
        Serv.var1.set_value(t)
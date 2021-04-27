import json
import os.path
class Transaccion:
    data = {}
    data['transacciones']=[]
    def __init__(self, monto, tipo, tipo_pago):
        self.monto = monto
        self.tipo = tipo
        self.tipo_pago = tipo_pago

    def generarJson(self):
        ## Leyendo archivo data.txt y se asgina a variable data
        if os.path.isfile('data.txt'):
            with open('data.txt') as json_file:
                self.data = json.load(json_file)

        self.data['transacciones'].append({
            'monto':self.monto,
            'tipo':self.tipo,
            'tipo_pago': self.tipo_pago
        })
        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile)

    def imprimirTransacciones(self):
        for p in self.data['transacciones']:
            print('Monto: ' + str(p['monto']))
            print('Tipo: ' + str(p['tipo']))
            print('Tipo_Pago: ' + str(p['tipo_pago']))
            print("--------------")

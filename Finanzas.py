import os.path
import json
from Transaccion import Transaccion

## Menú
def menu():
    print("Finanzas de mi Negocio")
    print("Seleccione entre las siguientes opciones:")
    print("1 - Hacer Transacción")
    print("2 - Mostrar Resumen")
    print("3 - Salir")
    opcion = str(input())
    if opcion == "1":
        pedirTransaccion()
    elif opcion == "2":
        mostrarResumen()
    elif opcion == "3":
        exit()
    else:
        print("Opción inexistente")
        menu()

## Mostrar resumen
def mostrarResumen():
    totalCuenta = 0
    totalEfectivo = 0
    totalTransferencia = 0
    resumen = {}
    if os.path.isfile('data.txt'):
        with open('data.txt') as json_file:
            resumen = json.load(json_file)
            for p in resumen['transacciones']:
                if p['tipo'] == "Ingreso" and p['tipo_pago'] == "Transferencia":
                    totalCuenta = totalCuenta + p['monto']
                    totalTransferencia = totalTransferencia + p['monto']
                elif p['tipo'] == "Egreso" and p['tipo_pago'] == "Transferencia":
                    totalCuenta = totalCuenta - p['monto']
                    totalTransferencia = totalTransferencia - p['monto']
                if p['tipo'] == "Ingreso" and p['tipo_pago'] == "Efectivo":
                    totalCuenta = totalCuenta + p['monto']
                    totalEfectivo = totalEfectivo + p['monto']
                elif p['tipo'] == "Egreso" and p['tipo_pago'] == "Efectivo":
                    totalCuenta = totalCuenta - p['monto']
                    totalEfectivo = totalEfectivo - p['monto']
    
        print("Total en la Cuenta:" + str(totalCuenta))
        print("Total en Cuenta de Banco:" + str(totalTransferencia))
        print("Total en Efectivo:" + str(totalEfectivo))

    else:
        print("No existe ninguna transacción.")
        menu()

#Pedir Monto
def pedirMonto():
    print("Monto:")
    monto = int(input())
    if monto > 0:
        return monto
    else:
        print("El monto no es válido")
        pedirMonto()

#Pedir Tipo
def pedirTipo():
    print("Seleccione Tipo de Transaccion (Ingreso o Egreso):")
    print("Opciones: 1- Ingreso | 2- Egreso")
    tipo = str(input())
    if tipo == "1":
        return "Ingreso"
    elif tipo == "2":
        return "Egreso"
    else:
        print("Opción no existente.")
        pedirTipo()

#Pedir Tipo de Pagp
def pedirTipoPago():
    print("Seleccione Tipo de Pago (Ingreso o Egreso):")
    print("Opciones: 1- Transferencia | 2- Efectivo")
    tipo = str(input())
    if tipo == "1":
        return "Transferencia"
    elif tipo == "2":
        return "Efectivo"
    else:
        print("Opción no existente.")
        pedirTipoPago()

## Pedir Transacción
def pedirTransaccion():
    #Se piden datos
    monto = pedirMonto()
    tipo = pedirTipo()
    tipo_pago = pedirTipoPago()
    #Instancia de Transacción
    transaccion = Transaccion(monto, tipo, tipo_pago)
    transaccion.generarJson()
    print("Transacción completada!")
    transaccion.imprimirTransacciones()

# Programa
menu()

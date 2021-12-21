from AgenteJugador import AgenteJugador
from NonogramEnvironment import NonogramEnvironment

matriz = [[0,0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,1,1,0,0,0,0],[0,0,1,0,1,1,1,1,1,0,0],[0,0,0,1,1,0,1,1,0,1,0],[0,0,0,0,1,1,1,1,0,1,0],[0,0,0,0,1,1,1,1,0,0,0],[0,0,0,0,1,1,1,1,0,1,0],[0,0,0,1,1,0,1,1,0,1,0],[0,0,1,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0]]
pistas = [[[3],[2],[1,5],[2,2,1],[4,1],[4],[4,1],[2,2,1],[1,5],[2],[3]],[[0],[0],[1,1],[1,1],[7],[2,3,2],[11],[1,7,1],[1,1,1,1],[2,2],[0]]]
columnas = len(matriz)
filas = len(matriz[0])
op=999
nonogram = NonogramEnvironment(matriz, pistas)
jugador = AgenteJugador(nonogram)

pistas = jugador.sensors["SensorDePistas"].sense()
ingame = jugador.sensors["SensorDePartida"].sense()
errores = jugador.sensors["SensorDeErrores"].sense()
victoria = jugador.sensors["SensorDeVictoria"].sense()

def Pintar(pX,pY):
    ingame[pX][pY] = "█"
    jugador.actuators["Pintor"].act(pX,pY)

def ActualizarTablero():
    global ingame
    ingame = jugador.sensors["SensorDePartida"].sense()
    return ingame

def ActualizarErrores():
    global errores
    errores = jugador.sensors["SensorDeErrores"].sense()
    return errores

def ActualizarVictoria():
    global victoria
    victoria = jugador.sensors["SensorDeVictoria"].sense()
    return victoria

def Mostrar():
    coma = ""
    líneas = []
    pistasFilas = []
    pistasColumnas = []

    for i in range(filas):
        line = ""
        fila = ""
        columna = ""

        for j in range(columnas):
            line += ingame[j][i]

        for j in range(len(pistas[1][i])):
            if (j+1) < len(pistas[1][i]):
                coma = ", "
            else:
                coma = ""
            fila += str(pistas[1][i][j]) + coma
        fila += "|"

        for j in range(len(pistas[0][i])):
            columna += str(pistas[0][i][j]) + coma
        columna += "_"

        líneas.append(line)
        pistasFilas.append(fila)
        pistasColumnas.append(columna)

    pistasFilasLen = max([len(pistasFilas[x]) for x in range(len(pistasFilas))])
    pistasColumnasLen = max([len(pistasColumnas[x]) for x in range(len(pistasColumnas))])

    space = ""
    for i in range(pistasFilasLen):
        space += " "

    for i in range(len(pistasColumnas)):
        for j in range(pistasColumnasLen - len(pistasColumnas[i])):
            pistasColumnas[i] = " " + pistasColumnas[i]

    for i in range(len(pistasColumnas[0])):
        line = space
        for j in range(len(pistasColumnas)):
            line += pistasColumnas[j][i]
        print(line)

    for i in range(len(pistasFilas)):
        for j in range(pistasFilasLen - len(pistasFilas[i])):
            pistasFilas[i] = " " + pistasFilas[i]
        
        print(pistasFilas[i] + líneas[i])

    print("\n" + "Errores: " + str(errores))

print()
print("------------------------------------------------------------------------------------------------------------------------------------------")
print("                                       ----__--__--__--»:» NONOMANÍA [Parcel edition] ----__--__--__--»:» ")
print("------------------------------------------------------------------------------------------------------------------------------------------")
print()
print("Presione ENTER para iniciar.")
input()

while (op != 0):
    print("\n"+"\n"+"Ingrese una opción para continuar:")
    print()
    print("         1: Pintar un casillero")
    print("         2: Actualizar el tablero")
    print("         3: Mostrar tablero")
    print("         0: Salir")

    op=int(input())

    if(op==1):
        print("\n"+"Ingrese una coordenada X")
        pX = int(input())-1

        print("\n" + "Ingrese una coordenada Y")
        pY = int(input())-1

        if (pX<=11 and pY<=11):
            Pintar(pX,pY)
            print("\n" + "Casilla pintada en: " + str(pX + 1) + "-" + str(pY + 1))

        else: print("\n"+"Coordenadas inválidas. Volviendo al menú principal...")

    if(op==2):
        ActualizarTablero()
        ActualizarErrores()
        ActualizarVictoria()
        print("\n"+"Tablero actualizado!")

    if(op==3):
        print()
        Mostrar()
        if victoria:
            print("\n"+"Felicitaciones, has completado el nonograma!")
            op = 0
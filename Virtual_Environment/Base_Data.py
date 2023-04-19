# Importamos los módulos necesarios:
import cv2
import time
import os
import imutils

# ------------------------------------------------------------
# SE DEBE CREAR UNA CARPETA DENTRO DE LA CARPETA DATA. ESTA CARPETA VA A CONTENER LAS IMAGENES QUE QUEREMOS RECONOCER
# Nombre de la carpeta
personName = 'Jorge'
# Direccion en donde se va a crear la carpeta
dataPath = 'F:\Estudios de ProGramacion\Practicas_Python\Reconocimiento_Facial\Virtual_Environment\Data'
personPath = dataPath + '/' + personName
# Creando la carpeta
if not os.path.exists(personPath):
    print('Carpeta Creada:', personPath)
    os.makedirs(personPath)
# ------------------------------------------------------------
# Crear un contador de imagenes para que cuente cuantas fotos se estan almacenando
# ------------------------------------------------------------
# Creamos un objeto de captura de video usando la cámara predeterminada:
captura = cv2.VideoCapture(0)

# Verificamos si la cámara se ha abierto correctamente:
if not captura.isOpened():
    print("No se puede abrir la cámara")
    exit()

# Iniciamos un bucle while que se ejecutará hasta que se presione la tecla "esc":
while True:
    # En cada iteración del bucle, leemos un nuevo cuadro de la cámara:
    ret, frame = captura.read()

    # Verificamos si el cuadro se ha leído correctamente:
    if not ret:
        print("No se puede recibir el cuadro de la cámara. Saliendo ...")
        break
    
    # Para que la imagen de la cama concuerde con el movimiento realizado. Es decir: si me inclino hacia la derecha, la imagen NO ira a la izquierda
    frame = cv2.flip(frame, 1) 

    # Mostramos el cuadro en una ventana llamada "Visor de Camara":
    cv2.imshow('Visor de Camara', frame)

    # Esperamos 1 milisegundo (aproximadamente) para que se presione una tecla:
    if cv2.waitKey(1) == 27:  # 27 es el valor ASCII para "esc"
        # Cuando se presiona la tecla "esc", salimos del bucle:
        break
    # Agregamos un pequeño retraso de 0.1 segundos para permitir que la cámara capture un nuevo cuadro antes de continuar con la siguiente iteración del bucle:
    time.sleep(0.1)  # Pequeño retraso para permitir que la cámara capture un nuevo cuadro

# Liberamos los recursos de la cámara y cerramos todas las ventanas abiertas:
captura.release()
cv2.destroyAllWindows()
# ------------------------------------------------------------
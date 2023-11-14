# Uso TP2 - Servidor de Procesamiento de Imagenes
En *main.py* se corre el servidor principal, el cliente puede comunicarse con él a través de postman o curl. Deberá enviar el nombre de la imagen (la cual debe estar en la misma carpeta)
que desea procesar junto con el factor de escalado (si es que decide escalar la imagen). Si desea escalar la imagen, debe iniciar el servidor de escalado en *image_scale_server.py*

- Si va a utilizar el escalado debe proporcionar un factor de reducción de la imagen.

# Ejemplo
1- "Inicio de Servidor en main"
python3 main.py -i 0.0.0.0 -p 8083 -m messi.jpg -s 0.8
*_respuesta_* : Soy el proceso padre - PID: 80141
              Servidor de procesamiento de imágenes iniciado en 0.0.0.0:8083

2- "Inicio de Servidor en image_scale_server"
python3 image_scale_server.py
*_respuesta_*: Escuchando en el puerto:  8080

3- "Uso de CURL"
curl -X POST -d "/home/kali/Desktop/UM/Computacion2/TP2/" http://localhost:8083

Luego de esta serie de pasos vamos a poder observar que en la misma carpeta se nos crearon dos imagenes nuevas: una imagen en escala de grises y otra en escala de grises y escalada. 
En el caso que solo queramos la imagen en escala de grises, no debemos enviarle el factor de escalado en los argumentos

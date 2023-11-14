import http.server
import socket
from PIL import Image
from io import BytesIO
import cgi

PORT = 8080

class HTTPServerV6(http.server.HTTPServer):
    address_family = socket.AF_INET6

class ResizeHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        
    #Verificar si estamos recibiendo datos de formulario multipart (es decir, una imagen)
        if ctype == 'multipart/form-data':
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            fields = cgi.parse_multipart(self.rfile, pdict)
            image_data = fields.get('image')[0]
            scale = float(fields.get('scale')[0])
            
            #Convertir los datos de la imagen a una imagen PIL y redimensionar
            image = Image.open(BytesIO(image_data))
            new_size = (int(image.width * scale), int(image.height * scale))
            resized_image = image.resize(new_size)
            
            #Guardar la imagen redimensionada en un objeto BytesIO para enviarla como respuesta
            byte_io = BytesIO()
            resized_image.save(byte_io, 'JPEG')
            byte_io.seek(0)
            
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            self.wfile.write(byte_io.read())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Bad Request: Expected multipart/form-data'.encode())
        

with HTTPServerV6(("::", PORT), ResizeHandler) as httpd:
    print("Escuchando en el puerto: ", PORT)
    httpd.serve_forever()


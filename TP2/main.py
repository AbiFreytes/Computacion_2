from multiprocessing import Event
import multiprocessing
import argparse
import http.server
import socket
import os
from image_utils import convert_to_grayscale
from PIL import Image
import requests
from io import BytesIO

class HTTPServerV6(http.server.HTTPServer):
    address_family = socket.AF_INET6

def run_http_server(ip, port, imagen, scale=None):
    Handler = http.server.SimpleHTTPRequestHandler
    class ConvertGreys(Handler):
        def do_POST(self):
            imag = imagen
            escala = scale

            grayscale_output_path = "grayscale_image.jpg"
            event = Event()
            image_process = multiprocessing.Process(target=convert_to_grayscale, args=(imag, grayscale_output_path, event))

            try:
                image_process.start()
                event.wait()
                image_process.join()
                print("Imagen procesada con exito")

                if scale:
                    with open(grayscale_output_path, 'rb') as f:
                        img_data = f.read()
                        response = requests.post('http://localhost:8080/resize', data={'scale': escala}, files={'image': img_data})

                    if response.status_code == 200:
                        img = Image.open(BytesIO(response.content))
                        img.save('resized_image.jpg')
                        print("Imagen en escala de grises y reescalada lista")

                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b'Connection closed')

            except ValueError as e:
                print(f"Error: {e}")
                self.send_error(400, f"Bad Request: {e}")

            except requests.RequestException as e:
                print(f"Error in HTTP request: {e}")
                self.send_error(500, f"Internal Server Error: {e}")

            except Exception as e:
                print(f"Unexpected error: {e}")
                self.send_error(500, "Internal Server Error")

            except KeyboardInterrupt:
                print("Deteniendo los servidores...")
                image_process.terminate()
            

    with HTTPServerV6(("::", port), ConvertGreys) as httpd:
        print(f"Servidor de procesamiento de imágenes iniciado en {ip}:{port}")
        httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description='Tp2 - Procesado de imágenes')
    parser.add_argument('-i', '--ip', required=True, help='Dirección de escucha')
    parser.add_argument('-p', '--port', type=int, required=True, help='Puerto de escucha')
    parser.add_argument('-m', '--img', required=True, help='Path de la imágen')
    parser.add_argument('-s', '--scale', type=float, required=False, help='Escala')
    args = parser.parse_args()

    if args.scale:
        run_http_server(args.ip, args.port, args.img, args.scale)
    else:
        run_http_server(args.ip, args.port, args.img)

if __name__ == "__main__":
    padre = os.getpid()
    print(f"Soy el proceso padre - PID: {padre}")
    main()
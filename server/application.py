#./server/application.py

import http.server
import socketserver

PORT = 8000

class TestMe():			# класс для демонстрации работы юнит-тестов
    def take_five(self):
        return 4
    def port(self):
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

# веб-сервер отвечающий на любой запрос по дефолту показывает клиенту список файлов в текущем каталоге
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
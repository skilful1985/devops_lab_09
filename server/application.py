"""Добавляем модули"""
import http.server
import socketserver

PORT = 8000

""" класс для демонстрации работы юнит-тестов """
class TestMe():
    """ функция для проверки счета """
    def take_five(self):
        return 4
    """ функция возврата порта """
    def port(self):
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

""" веб-сервер отвечающий на любой запрос по дефолту
показывает клиенту список файлов в текущем каталоге """
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()

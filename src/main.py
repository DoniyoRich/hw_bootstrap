from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):

        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()
        with open('index.html', encoding='utf-8') as html_file:
            start_file = html_file.read()

        self.wfile.write(bytes(start_file, 'utf-8'))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

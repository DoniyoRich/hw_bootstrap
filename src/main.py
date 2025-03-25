from http.server import BaseHTTPRequestHandler, HTTPServer

from src.constants import HTML_DIR

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def get_html_page(self, page_name: str) -> str:
        """ Возвращает страницу html, определенную параметром page_name. """
        with open(HTML_DIR / page_name, encoding='utf-8') as html_file:
            html_file = html_file.read()
        return html_file

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        if self.path == '/' or self.path == '/index.html':
            page_content = self.get_html_page('index.html')
        else:
            page_content = self.get_html_page('contacts.html')

        self.send_response(200)
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()

        self.wfile.write(bytes(page_content, 'utf-8'))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

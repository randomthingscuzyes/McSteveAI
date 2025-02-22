import http.server
import socketserver
import threading
import webbrowser

# Definisci la porta
PORT = 5500

# Crea un semplice server HTTP
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Aggiungi header per evitare problemi di CORS (opzionale)
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Avvia il server
def start_server():
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Server avviato su http://localhost:{PORT}")
        httpd.serve_forever()

# Apri il browser automaticamente
def open_browser():
    webbrowser.open_new_tab(f"http://localhost:{PORT}")

if __name__ == "__main__":
    # Avvia il server in un thread separato
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Apri il browser
    open_browser()

    # Tieni il programma in esecuzione
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nServer arrestato.")
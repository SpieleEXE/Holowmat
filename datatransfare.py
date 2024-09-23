import socket
import os

BUFFER_SIZE = 4096  # Größe der Datenblöcke
DEFAULT_PORT = 12345
ENCODING = 'utf-8'  # Zum Umwandeln von Strings in Bytes und umgekehrt


def send_file(filename, host, port=DEFAULT_PORT):
    """Sendet eine Datei an einen Server."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Die Datei {filename} existiert nicht.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Verbunden mit {host}:{port}. Sende Datei: {filename}")

        with open(filename, 'rb') as file:
            while (data := file.read(BUFFER_SIZE)):
                s.sendall(data)  # Datei in Blöcken senden
        print("Datei erfolgreich gesendet.")


def receive_file(save_as, port=DEFAULT_PORT):
    """Empfängt eine Datei und speichert sie."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"Warte auf Verbindung auf Port {port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Verbindung von {addr} hergestellt. Empfange Datei...")
            with open(save_as, 'wb') as file:
                while (data := conn.recv(BUFFER_SIZE)):
                    if not data:
                        break
                    file.write(data)  # Daten in Datei schreiben
        print(f"Datei empfangen und unter {save_as} gespeichert.")


def send_string(data, host, port=DEFAULT_PORT):
    """Sendet einen String an einen Server."""
    if not isinstance(data, str):
        raise TypeError("Die Daten müssen ein String sein.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Verbunden mit {host}:{port}. Sende String-Daten...")
        data_bytes = data.encode(ENCODING)  # String in Bytes umwandeln
        s.sendall(data_bytes)
        print("String erfolgreich gesendet.")


def receive_string(port=DEFAULT_PORT):
    """Empfängt einen String und gibt ihn zurück."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"Warte auf Verbindung auf Port {port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Verbindung von {addr} hergestellt. Empfange String-Daten...")
            data_bytes = b""
            while True:
                part = conn.recv(BUFFER_SIZE)
                if not part:
                    break
                data_bytes += part  # Empfange Daten in Blöcken
            data = data_bytes.decode(ENCODING)  # Bytes wieder in String umwandeln
        print("String empfangen.")
        return data

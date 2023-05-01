"""
proxy class for two-player games
"""
class Proxy:
    def __init__(self, client):
        self.client = client

    def receive_string(self):
        data = self.client.recv(1024)
        if not data:
            return None
        return data.decode('utf-8')

    def send_string(self, string):
        self.client.send(string.encode('utf-8'))

    def make_guess(self):
        return self.receive_string()

    def get_result(self, guess):
        self.send_string(guess)
        return self.receive_string()

    def receive_result(self, result):
        self.send_string(result)

    def close(self):
        self.client.close()
        

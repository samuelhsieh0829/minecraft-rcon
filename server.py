from mcrcon import MCRcon

class Server:
    def __init__(self, IP, PORT, password) -> None:
        self.IP = IP
        self.PORT = PORT
        self.password = password

    def send(self, command: str):
        with MCRcon(self.IP, self.password, self.PORT) as rcon:
            resp = rcon.command(command)
        return resp
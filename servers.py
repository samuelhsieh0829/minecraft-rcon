from server import Server
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("RCON_PASSWORD")
Servers:dict[str, Server] = {}

#For Docker network
Servers["lobby"] = Server("mc-lobby", 25576, password)
Servers["activity"] = Server("mc-activity", 25577, password)
Servers["survive"] = Server("mc-survive", 25578, password)

# Test
# Servers["lobby"] = Server("localhost", 25576, password)
# Servers["activity"] = Server("localhost", 25577, password)
# Servers["survive"] = Server("localhost", 25578, password)
from mcstatus import MinecraftServer

server = input("Enter the servers IP address: ")
server = MinecraftServer.lookup(server)
latency = server.ping()
print("The server replied in {0} ms".format(latency))
status = server.status()
print("The server has {0}/{1} players online".format(status.players.online, status.players.max))
query = server.query()
print("The server has the following players online: {0}".format(", ".join(query.players.names)))
print("The server has the following plugins installed: {0}".format(", ".join(query.software.plugins)))
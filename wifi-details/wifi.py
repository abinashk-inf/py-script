from pydbus import SystemBus

bus=SystemBus()
nm=bus.get('.NetworkManager')

wi=bus.get('.NetworkManager',nm.ActiveConnections[0])
name = wi.Id
typ=wi.Type
print(name)
print(typ)


from pydbus import SystemBus

bus=SystemBus()
nm=bus.get('.NetworkManager')

wi=bus.get('.NetworkManager',nm.ActiveConnections[0])
name = wi.Id
typ=wi.Type
print(name)
print(typ)

ip4=bus.get('.NetworkManager',con.Ip4Config)
ip4Add=ip4.AddressData
print(ip4Add)

ip6=bus.get('.NetworkManager',con.Ip6Config)
ip6Add=ip6.AddressData
print(ip6Add)

dev=bus.get('.NetworkManager',nm.GetDevices()[1])
mac=dev.HwAddress
print(mac)




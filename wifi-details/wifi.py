from pydbus import SystemBus

bus=SystemBus()
nm=bus.get('.NetworkManager')
active=nm.ActiveConnections
con=bus.get('.NetworkManager',active[0])

wi=bus.get('.NetworkManager',nm.ActiveConnections[0])
name = wi.Id
typ=wi.Type
print('Network: {}'.format(name))
print('Network Type: {}'.format(typ))

ip4=bus.get('.NetworkManager',con.Ip4Config)
ip4Add=ip4.AddressData
print('IpV4 Address: {}'.format(ip4Add))

ip6=bus.get('.NetworkManager',con.Ip6Config)
ip6Add=ip6.AddressData
print('IpV6 Address: {}'.format(ip6Add))

dev=bus.get('.NetworkManager',nm.GetDevices()[1])
mac=dev.HwAddress
print('Physical Address: {}'.format(mac))

pas=bus.get('.NetworkManager',wi.Connection)
secret=pas.GetSecrets(pas.GetSettings()['802-11-wireless']['security'])['802-11-wireless-security']['psk']
print('Network Password: {}'.format(secret))




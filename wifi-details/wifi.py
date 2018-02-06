from pydbus import SystemBus

bus=SystemBus()
nm=bus.get('.NetworkManager')
active=nm.ActiveConnections
if len(active)>0:

    con=bus.get('.NetworkManager',active[0])
    wi=bus.get('.NetworkManager',nm.ActiveConnections[0])
    name = wi.Id
    typ=wi.Type
    print('Network: {}'.format(name))
    print('Network Type: {}'.format(typ))
    pas=bus.get('.NetworkManager',wi.Connection)
    secret=pas.GetSecrets(pas.GetSettings()['802-11-wireless']['security'])['802-11-wireless-security']['psk']
    print('Network Password: {}'.format(secret),end='\n')

    ip4=bus.get('.NetworkManager',con.Ip4Config)
    ip4Add=ip4.AddressData
    ip4Routes=ip4.Routes
    ip4RtData=ip4.RouteData
    ip4Nameserver=ip4.Nameservers
    print('IpV4 Details:')
    print('     Address: {}'.format(ip4Add))
    print('     Routes: {}'.format(ip4Routes))
    print('     Route Data: {}'.format(ip4RtData))
    print('     Nameserver: {}'.format(ip4Nameserver))

    ip6=bus.get('.NetworkManager',con.Ip6Config)
    ip6Add=ip6.AddressData
    ip6Routes=ip6.Routes
    ip6RtData=ip6.RouteData
    ip6Nameserver=ip6.Nameservers
    print('IpV6 Details:')
    print('     Address: {}'.format(ip6Add))
    print('     Routes: {}'.format(ip6Routes))
    print('     Route Data: {}'.format(ip6RtData))
    print('     Nameserver: {}'.format(ip6Nameserver),end='\n')

    dev=bus.get('.NetworkManager',nm.GetDevices()[1])
    mac=dev.HwAddress
    print('Physical Address: {}'.format(mac))
else:
    print('System is not connected. Please connect to a wireless network.')


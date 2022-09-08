import bluetooth
# 选择蓝牙通信对象

def find_address():
    target_name = "Philips TAT2206"
    target_address = None
    nearby_devices = bluetooth.discover_devices()
    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name(bdaddr):
            target_address = bdaddr
            break
    if target_address is not None:
        print(
            "found target bluetooth device with address ",
            target_address)
    else :
        print(
            "could not find target bluetooth device nearby"
        )
        
        
def find_device_services():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        print(" %s - %s" % (addr, name))
        services = bluetooth.find_service()
        for svc in services:
            print("Service Name: %s" % svc["name"])
            print(" Host: %s" % svc["host"])
            print(" Description: %s" % svc[
                "description"])
            print(" Provided By: %s" % svc[
                "provider"])
            print(" Protocol: %s" % svc["protocol"])
            print(" channel/PSM: %s" % svc["port"])
            print(" svc classes: %s " % svc[
                "service-classes"])
            print(" profiles: %s " % svc["profiles"])
            print(" service id: %s " % svc[
                "service-id"])
            print("")
            
def bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)
    client_sock, address = server_sock.accept()
    print ("Accepted connection from ",address)
    data = client_sock.recv(1024)
    print ("received [%s]" % data)  
    client_sock.close()
    server_sock.close()
    
def bluetooth_client():
    bd_addr = "01:23:45:67:89:AB"
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()
    
if __name__ == '__main__':
    # find_address()
    find_device_services()
        
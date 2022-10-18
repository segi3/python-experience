from yeelight import Bulb

bulb = Bulb("192.168.1.9")

while True:
    inp=input("action:")
    if inp == '0':
        print('stop flow')
        bulb.stop_flow()
    elif inp == '1':
        print('start flow')
        bulb.start_flow(flow)
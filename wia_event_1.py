from wia import Wia
import time
import random

wia = Wia()
wia.access_token = "llave_generada_por_wia"
i = 0

while i <20:
    xx = random.randint(0,200)
    wia.Event.publish(name="dato1", data=45*xx)
    wia.Event.publish(name="dato2", data=xx)
    wia.Event.publish(name="dato3", data=4.5*xx)
    wia.Event.publish(name="dato4", data=4502*xx)
    i += 1
    time.sleep(3)

from wia import Wia

wia = Wia()
wia.access_token = "d_sk_B6nhRp8zRbBwrkuzU2hcXeG2"

wia.Event.publish(name="hello-wia", data=45)

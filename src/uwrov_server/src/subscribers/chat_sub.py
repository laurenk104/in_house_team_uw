import rospy
from std_msgs.msg import String
from flask_socketio import SocketIO

from .subscriber import ServerSub

class ChatSub(ServerSub):
    def __init__(self, topic, sio_route, sio):
        super().__init__(topic, String)
        self.sio_route = sio_route
        self.sio = sio

    def callback(self, msg):
        packet = {
            'text': msg.data
        }
        self.sio.emit(self.sio_route, packet, broadcast=True)
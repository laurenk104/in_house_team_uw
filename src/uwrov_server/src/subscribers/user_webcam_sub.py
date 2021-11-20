import rospy
from std_msgs.msg import String
from flask_socketio import SocketIO

from .subscriber import ServerSub
from sensor_msgs.msg import CompressedImage

class UserWebcamSub(ServerSub):
    def __init__(self, topic, sio_route, sio):
        super().__init__(topic, CompressedImage)
        self.sio_route = sio_route
        self.sio = sio

    def callback(self, msg):
        rospy.loginfo(msg.data)
        packet = {
            'user_video': msg.data
        }
        self.sio.emit(self.sio_route, packet, broadcast=True)
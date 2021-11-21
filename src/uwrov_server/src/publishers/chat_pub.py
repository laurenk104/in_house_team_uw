import rospy
from std_msgs.msg import String
from .publisher import ServerPub

class ChatPub(ServerPub):
    """
    Publisher for sending chat message
    """
    
    def __init__(self, topic):
        super().__init__(topic, String)
        self.msg = String()
    
    def publish(self, channel):
        rospy.loginfo(channel)
        self.msg.data = channel
        print(self.msg)
        self.publisher.publish(self.msg)
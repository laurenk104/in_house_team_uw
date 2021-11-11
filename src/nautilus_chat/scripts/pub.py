import rospy
from std_msgs.msg import String
import getpass

"""
Publisher for the text messages in the chat window, publishing in
the following format "username: message"
"""

def main():
    rospy.init_node('chat_publisher', log_level=rospy.DEBUG)
    pub = rospy.Publisher('/nautilus/chat', String, queue_size=10)
    username = getpass.getuser()
    while not rospy.is_shutdown():
        msg = input("Enter message: ")
        pub.publish(username + ": " + msg)

if __name__ == '__main__':
    main()
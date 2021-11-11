import rospy
from std_msgs.msg import String
import getpass

"""
Publisher for the text messages in the chat window, publishing in
the following format "username: message"
"""

def main():
    chat_log = []
    rospy.init_node('chat_publisher', log_level=rospy.DEBUG)
    pub = rospy.Publisher('/nautilus/chat', String, queue_size=10)
    username = getpass.getuser()
    while not rospy.is_shutdown():
        res = ""
        msg = input("Enter message: ")
        if (len(chat_log) == 10):
            chat_log.pop(0)
        chat_log.append(username + ": " + msg + "\n")

        for i in range(len(chat_log)):
            res += chat_log[i]

        pub.publish(res)
        print(res)

if __name__ == '__main__':
    main()
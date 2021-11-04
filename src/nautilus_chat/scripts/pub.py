import rospy
from std_msgs.msg import String

"""
Publisher for the text messages in the chat window, keeping track
of the 20 most recent text messages.
"""
# username: msg|username: msg|username: msg|  ...

def main():
    rospy.init_node('chat_publisher', log_level=rospy.DEBUG)
    pub = rospy.Publisher('/nautilus/chat', String, queue_size=10)
    username = "test_username"
    text_storer = ""
    text_storer_size = 0
    while not rospy.is_shutdown():
        msg = input("Enter message: ")
        if (text_storer.count('\|') == 5):
            idx = text_storer.find('\|')
            text_storer = text_storer[(idx + 2):]
            text_storer_size -= 1
        text_storer = text_storer + username + ": "+ msg + "\|"
        text_storer_size += 1
        pub.publish(text_storer)

if __name__ == '__main__':
    main()
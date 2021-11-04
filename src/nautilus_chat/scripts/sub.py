import rospy
from std_msg import String

def callback(msg):
    return

def main():
    rospy.init_node('text_server', log_level=rospy.DEBUG)
    rospy.Subscriber('/nautilus/chat', String, callback)
    rospy.spin()

if __name__ == '__main__':
  main()
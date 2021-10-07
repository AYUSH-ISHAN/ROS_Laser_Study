#! /usr/bin/env/python

import rospy
import sensor_msgs.msg import LaserScan
from geographic_msgs.msg import Twist

def callback(msg):
    print(msg.ranges[360])
    move.linear.x = 0.1
    if msg.linear[360] < 1:
        move.linear.x = 0
    pub.publish(move)

rospy.init_node("check")
sub = rospy.Subscriber("laser/scan", LaserScan, callback)
pub = rospy.Publisher("/cmd_vel", Twist)
move = Twist()

rospy.spin()
    
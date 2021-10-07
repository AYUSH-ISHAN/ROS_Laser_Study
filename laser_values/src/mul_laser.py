#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print("Values at different degrees: ")
    print("Value at 0 degrees = ")
    print(msg.ranges[0])
    print("Value at 90 degrees = ")
    print(msg.ranges[359])
    print("Value at 0 degrees = ")
    print(msg.ranges[719])

## Two data were their ...   1. Intensity,    2. Ranges

rospy.init_node('scan_values')
sub = rospy.Subscriber('/laser/scan', LaserScan, callback)
rospy.spin()
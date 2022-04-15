#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import PointCloud2


def imu_listener(data):
    imu_publisher.publish(data)


def lidar_listener(data):
    lidar_publisher.publish(data)


def main():
    rospy.init_node('topics_redirect', log_level=rospy.DEBUG)
    rospy.Subscriber("velodyne_points", PointCloud2, callback=lidar_listener)
    rospy.Subscriber("imu/data", Imu, callback=imu_listener)
    rospy.spin()


if __name__ == '__main__':
    lidar_publisher = rospy.Publisher("points_raw", PointCloud2, queue_size=500)
    imu_publisher = rospy.Publisher("imu_raw", Imu, queue_size=500)
    main()

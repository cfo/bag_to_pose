#!/usr/bin/python

import rosbag
import argparse

def extract(bagfile, pose_topic, out_filename):
    n = 0
    f = open(out_filename, 'w')
    f.write('# timestamp tx ty tz qx qy qz qz\n')    
    with rosbag.Bag(bagfile, 'r') as bag:
        for (topic, msg, ts) in bag.read_messages(topics=str(pose_topic)):
            f.write('%.12f %.12f %.12f %.12f %.12f %.12f %.12f %.12f\n' % 
                    (msg.header.stamp.to_sec(),
                     msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z,
                     msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w))
            n += 1
    print('wrote ' + str(n) + ' imu messages to the file: ' + out_filename)
          
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    Extracts IMU messages from bagfile.
    ''')
    parser.add_argument('bag', help='Bagfile')
    parser.add_argument('topic', help='Topic')
    args = parser.parse_args()
    print('Extract pose from bag '+args.bag+' in topic ' + args.topic)
    extract(args.bag, args.topic, 'pose.txt')
#-*-coding:utf8-*-
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--length', default = 11, type = int, help = '长度')
parser.add_argument('--width', default = 11, type = int, help = '宽度')
args = parser.parse_args()
area = args.length * args.width
print('面积={0:*^10}'.format(area))

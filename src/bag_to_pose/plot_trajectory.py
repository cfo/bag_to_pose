#!/usr/bin/python

import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Cardo']})
rc('text', usetex=True)

def plot_trajectory(filename):
    data = np.loadtxt(filename)
    fig = plt.figure()
    ax = fig.add_subplot(111, xlabel='x', ylabel='y')
    ax.plot(data[:,1], data[:,2])
    ax.legend()
    fig.tight_layout()
    fig.savefig('trajectory.pdf')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot poses')
    parser.add_argument('pose_file', help='Bagfile')
    args = parser.parse_args()
    plot_trajectory(args.pose_file)
#!/usr/bin/env python

import rospy
import crazyflie
import time
import uav_trajectory


if __name__ == '__main__':
	rospy.init_node('test_high_level')

	cf = crazyflie.Crazyflie("crazyflie7", "crazyflie7")

	cf.setParam("commander/enHighLevel", 1)
	#cf.setParam("stabilizer/estimator", 2) # Use EKF
	#cf.setParam("stabilizer/controller", 1) # Use mellinger controller
	#cf.setParam("kalman/resetEstimation",1)
	#time.sleep(5.0)
	cf.takeoff(targetHeight = 0.6, duration = 1.0)
	time.sleep(5.0)	
	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
	time.sleep(2.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(4.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=-1.4, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(3.0)

	cf.goTo(goal= [0.0, 0.0, 0.2], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [1.3, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0 , 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(7.0)

	cf.goTo(goal= [0.0, 0.5, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(7.0)

	cf.goTo(goal= [-1.3, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(7.0)

	cf.goTo(goal= [0.0, -0.5, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(5.0)

	cf.goTo(goal= [0.0, 0.0, 0.0], yaw=0.0, duration = 2.0, relative = True)
	time.sleep(7.0)
	
	cf.land(targetHeight = 0.0, duration = 2.0)
	time.sleep(5.0)
	#traj1 = uav_trajectory.Trajectory()
	#traj1.loadcsv("takeoff.csv")

	#traj2 = uav_trajectory.Trajectory()
	#traj2.loadcsv("figure8.csv")

	#print(traj1.duration)

	#cf.uploadTrajectory(0, 0, traj1)
	#cf.uploadTrajectory(1, len(traj1.polynomials), traj2)

	#cf.startTrajectory(0, timescale=1.0)
	#time.sleep(traj1.duration * 2.0)

	#cf.startTrajectory(1, timescale=2.0)
	#time.sleep(traj2.duration * 2.0)

	#cf.startTrajectory(0, timescale=1.0, reverse=True)
	#time.sleep(traj1.duration * 1.0)

	cf.stop()

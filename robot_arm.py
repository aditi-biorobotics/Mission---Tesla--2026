print("My Robotic arm calibration")
joint_angles = [45,90,15]
print("OriginalAngles:" + str(joint_angles))
print("shoulder angle (position 0):" + str (joint_angles[0])+ "°")
print("elbow angle (position 1):" + str(joint_angles[1])+ "°")
print("\n moving Robot to next target")
joint_angles.append(60)
joint_angles.append(200)
print("updated angles with Gripper:"+ str(joint_angles))
print("\n final safety check")
for angle in joint_angles:
	if angle > 180:
		print("ALERT: angle" + str(angle) + "° is UNSAFE!")
	else:
		print("angle" + str(angle) + "° is SAFE.")
		
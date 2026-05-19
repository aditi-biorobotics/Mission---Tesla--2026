# Humanoid Robot Diagnostics using Dictionaries
print("Optimus Diagnostic system")
robot_status = {"left leg": "active", "battery_level": 85, "cpu_temperature": 42.5, "gripper_locked" : True}
print("Battery status: " + str(robot_status["battery_level"]) + "%")
print("CPU Temp:" + str(robot_status["cpu_temperature"]) + "°C")
print("\n Running system update")
robot_status["cpu_temperature"] = 55.0
robot_status["right_leg"] = "active"
print("updated cpu temperature:" + str(robot_status["cpu_temperature"]) + "°C")
print("right leg status:" + robot_status["right_leg"])
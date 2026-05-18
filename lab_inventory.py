print("Bio Robotics lab inventory system")
components=["Heart monitor","Robotics arm","AI brain chip","temperature sensor"]
print("Total item in lab:" + str(len(components)))
print("\n scanning inventory items")
for item in components:
	print("Item detected:" + item + "⚙️")
	print("\n scan completed successfully.")
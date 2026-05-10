# Day 2: Health Monitoring loop
print("Hospital patient monitoring syatem")
count = 1
while count <=5:
	print("Reading number:" +str(count))
	temp = float(input("Enter body temperature (celsius): "))
if temp > 37.5:
	print("Status: fever detected!")
else: 
    print("Status: Normal.") 
count = count + 1
print(" monitoring session finished. All readings recorded.")

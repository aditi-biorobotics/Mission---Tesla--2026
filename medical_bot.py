# Day 2: Medical screening Bot 
print ("Bio- AI Daignostic system")
# Symptoms input 
print ("Enter symptoms as (yes/no)")
fever = input("Is there High fever ?")
pain = input("Is there severe joint pain ?")
weight_loss = input("Is there sudden weight loss ?")
# AI Logic for detection
if fever == "yes" and pain =="yes" :
	print ("Result: High risk of dengue. please check platelet count !")
elif fever == "yes" and weight_loss == "no": 
	print("Result: could be Typhoid or Malaria.check for chills or appetite")
elif weight_loss == "yes":
	print("Result: signs of Immune Deficiency. Consult for HIV/AIDS test. ")
else:
		print("Result: Symptoms unclear . maintain hydration and rest.")
		print("Diagnosis complete")
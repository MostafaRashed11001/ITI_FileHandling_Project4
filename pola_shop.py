# Pola[2Sab shop]
# - Select type
   # - Large
   # - Medium
   # - Small
# - Pay cost
# - store into file
import os
type_select_dic={
		"Large ":30.0, #[Price(L.E)]
		"Medium":25.0,
		"Small ":20.0
}
Quantity_Large=0
Quantity_Medium=0
Quantity_Small=0
name=""
total_cost=0
print("----------Welcome in Pola shop----------")
while True:
	print ("Modes:")
	print ("'1'for pay")
	print ("'2'for Fatora")
	print ("'3'for exit")
	while True:
		try:
			mode =int(input ("Please input mode : "))
			break
		except:
			print ("Enter Valid Number")															#input mode 
	if mode == 1:
		name=input("Please enter your name :")
		while True:
			print ("Select type:")
			print ("'1'for Large")
			print ("'2'for Medium")
			print ("'3'for Small")
			print ("'4'for Total order")
			print ("Any another key for end order")
			while True:
				try:
					type_select =int(input ("Please input size "+ name+" :"))
					break
				except:
					print ("Enter Valid Number")															#input type_select 
			if type_select == 1:
				Quantity_Large+=int(input("What quantity do you want?"))
			elif type_select==2:
				Quantity_Medium+=int(input("What quantity do you want?"))
			elif type_select==3:
				Quantity_Small+=int(input("What quantity do you want?"))
			elif type_select==4:
				print(" Large:",Quantity_Large,"\n Medium:",Quantity_Medium,"\n Small:",Quantity_Small)
			else:
				break;
		Fatora_Save= open("Fatora_Save.txt","a+")
		Fatora_Save= open("Fatora_Save.txt","w")
		Fatora_Save.write("Customer :"+ name+"\n")
		Fatora_Save.write("For large size :" + str(Quantity_Large)+"\n")
		Fatora_Save.write("For Medium size :" + str(Quantity_Medium)+"\n")
		Fatora_Save.write("For Small size :" + str(Quantity_Small)+"\n")
		total_cost=(Quantity_Large*int(type_select_dic["Large "]))+(Quantity_Medium*int(type_select_dic["Medium"]))+(Quantity_Small*int(type_select_dic["Small "]))
		Fatora_Save.write("For Total cost :" + str(total_cost)+"\n")
		Fatora_Save.close()
	elif mode == 2:
		Fatora= open("Fatora.txt","a+")
		Fatora= open("Fatora.txt","w")
		Fatora.write("Customer :"+ name+"\n")
		Fatora.write("For large size :" + str(Quantity_Large)+ "\n")
		Fatora.write("For Medium size :" + str(Quantity_Medium)+"\n")
		Fatora.write("For Small size :" + str(Quantity_Small)+"\n")
		total_cost=(Quantity_Large*int(type_select_dic["Large "]))+(Quantity_Medium*int(type_select_dic["Medium"]))+(Quantity_Small*int(type_select_dic["Small "]))
		Fatora.write("For Total cost :" + str(total_cost)+"\n")
		Fatora= open("Fatora.txt","r")
		print (Fatora.read())
		Fatora.close()
		os.remove("Fatora.txt")
	elif mode == 3:
		print("----------Thank you for choosing Pola shop------------")
		break;
	else:
		print("----------Wrong Mode----------")														#Wrong Mode
		print("Please choose from this modes:")
	
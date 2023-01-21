# ## hint: its a good point to use file as json	  
# System for grocerry shop
# apple[40] -bannaa[30] -cherry[70]
# user take 3 - 2 - 10
# shop      37  28  60
# Cost      3*15 -

# #Welcome to ITI Shop
	# 1- Owner
	# 2- user
	# 3- exit
	# Select Mode For customer press 1 , for owner press two , to exist press 0 :  

# - Customer
    # - To show our products 				press 1         ---> products & cost
    # - To Buy from our products 			press 2     	---> Able to buy
    # - to print the bill 					press 3
# - to exist press 0
# - ITI OWNER
    # - Add new products       press 1
    # - Show Products          press 2
    # - Add Cost			   press 3
    # - Change cost			   press 4
# - to exist press 0
import os
print("----------Welcome in grocerry shop----------")
password_list = ["2022",'g2']
Products_dic={
		"Apple" :[40.0,25.0], #[Quantity(kg):Price(L.E)]
		"Bannaa":[30.0,20.0],
		"Cherry":[70.0,30.0]
}
Customer_Products_dic={
			"Customer_product":["Quantity"]
}
Fired_Employes={
		"Farouk" :[5000], #[salary,phone_number,fired_day]
}
employes_dic={
		"Mostafa_Rashed" :30000, #salary
		"Alaa_Elnaggar": 30000
}
cost=0
#Main loop
while True:
	print ("Modes:")
	print ("'1'for Owner")
	print ("'2'for user")
	print ("'3'for exit")
	print ("'4'for employes")
	while True:
		try:
			mode =int(input ("Please input mode : "))
			break
		except:
			print ("Enter Valid Number")															#input mode 
	if mode == 1:																					#owner_mode
		password=input ("Please enter your password:") 												#input Password
		if password in password_list:																#check password
			while True:
				print ("----------Welcome ITI Owner----------")
				print ("Owner Modes:")
				print ("press '1' for Add new products")
				print ("press '2' for Show Products")
				print ("press '3' for Change Cost")
				print ("press '4' for Change Quantity")
				print ("press '0' to exist to main mode")
				while True:
					try:
						owner_mode=int (input("Please choose mode:"))
						break
					except:
						print ("Enter Valid Number")
				if   owner_mode ==1:																#Add new products	
					name_of_new_product=input("Enter name of new product:")							#input new product
					while True:
						try:
							Quantity_of_new_product=float(input("Enter Quantity:"))					#input Quantity_of_new_product
							break
						except:
							print ("Enter Valid Number")
					while True:
						try:
							Price_of_new_product=float(input("Enter Price:"))						#input Price_of_new_product
							break
						except:
							print ("Enter Valid Number")
					Products_dic[name_of_new_product]=[Quantity_of_new_product,Price_of_new_product]
					#FILE HANDLING
					Products_dic_file= open("Products_dic.txt","a+")
					#Products_dic_file= open("Products_dic.txt","w")
					Products_dic_file.write("name_of_new_product : "+ str(name_of_new_product)+"\n")
					Products_dic_file.write("Quantity_of_new_product:"+str(Quantity_of_new_product)+"\n")
					Products_dic_file.write("Price_of_new_product:"+str(Price_of_new_product)+"\n")
					Products_dic_file.write("/////////////////////END process//////////////////////////"+"\n")
					Products_dic_file.close()
					#FILE HANDLING
					print("products now:")
					print(Products_dic)																#output new products
				elif owner_mode ==2:																#Show Products
					print("products now[Quantity(kg):Price(L.E)]:")
					print(Products_dic)
					#FILE HANDLING
					Products_dic_file= open("Products_dic.txt","a+")
					Products_dic_file= open("Products_dic.txt","r")
					print (Products_dic_file.read())
					Products_dic_file.close()
					#FILE HANDLING
				elif owner_mode ==3:																#Change Cost
					while True:
						name_of_new_product=input("Enter name of product:")							#choose product owner need change cost
						if name_of_new_product in Products_dic:
							break
						else:
							print ("Chosse Product form this list:")
							print(Products_dic)
					while True:
						try:
							Price_of_new_product=float(input("Enter Price:"))						#input new Cost
							break
						except:
							print ("Enter Valid Number")
					Products_dic[name_of_new_product]=[Products_dic[name_of_new_product][0],Price_of_new_product]
					#FILE HANDLING
					Products_dic_file= open("Products_dic.txt","a+")
					#Products_dic_file= open("Products_dic.txt","w")
					Products_dic_file.write("name_of_product : "+ str(name_of_new_product)+"\n")
					Products_dic_file.write("Change_of_Price_product:"+str(Price_of_new_product)+"\n")
					Products_dic_file.write("/////////////////////END process//////////////////////////"+"\n")
					Products_dic_file.close()
					#FILE HANDLING
					print("product now[Quantity(kg):Price(L.E)]:")
					print(Products_dic[name_of_new_product])										#output changeing in product
				elif owner_mode ==4:																#Change Quantity
					while True:
						name_of_new_product=input("Enter name of product:")							#choose product owner need change Quantity
						if name_of_new_product in Products_dic:
							break
						else:
							print ("Chosse Product form this list:")
							print(Products_dic)
					while True:
						try:
							Quantity_of_new_product=float(input("Enter Quantity:"))					#Change Quantity
							break
						except:
							print ("Enter Valid Number")
					Products_dic[name_of_new_product]=[Quantity_of_new_product,Products_dic[name_of_new_product][1]]
					#FILE HANDLING
					Products_dic_file= open("Products_dic.txt","a+")
					#Products_dic_file= open("Products_dic.txt","w")
					Products_dic_file.write("name_of_product : "+ str(name_of_new_product)+"\n")
					Products_dic_file.write("Change_of_Quantity_product:"+str(Quantity_of_new_product)+"\n")
					Products_dic_file.write("/////////////////////END process//////////////////////////"+"\n")
					Products_dic_file.close()
					#FILE HANDLING
					print("product now:")
					print(Products_dic[name_of_new_product])										#output changeing in product
				elif owner_mode ==0:
					break																			#exist to main mode
				else:
					print ("Choose one of this modes")
		else:
			print("----------Wrong password----------")												#Wrong password condtion
			print("Choose '1' again to enter the password")
	elif mode == 2:																					#Customer_mode
		print("----------Welcome in ITI grocerry shop----------")
		while True:
				print ("Customer Modes:")
				print ("press '1' for show our products")
				print ("press '2' for Buy from our products")
				print ("press '3' for Cost")
				print ("press '0' to exist to main mode")
				while True:
					try:
						Customer_mode=int (input("Please choose mode:"))							#input Customer_mode
						break
					except:
						print ("Enter Valid Number")
				if   Customer_mode ==1:																#Customer_mode show our products
					print("products--> 'Name of product': [Quantity(kg):Price(L.E)] : ")
					print(Products_dic)
				elif Customer_mode ==2:
					while True:
						while True:
							name_of_Customer_product=input("Enter name of product:")				#choose product Customer need to buy it
							if name_of_Customer_product in Products_dic:
								break
							else:
								print ("The "+name_of_Customer_product+" is not available in our products:")
								print ("If you need chosse available product form this list:")
								print(Products_dic)
						while True:
							try:
								Quantity_of_Customer_product=float(input("Enter Quantity:"))		#input Quantity Customer need it
								break
							except:
								print ("Enter Valid Number")
						if Products_dic[name_of_Customer_product][0]>=Quantity_of_Customer_product:	#Chack Quantity& output cost
							Customer_Products_dic[name_of_Customer_product]=[Quantity_of_Customer_product]
							cost+=(Quantity_of_Customer_product*Products_dic[name_of_Customer_product][1])
							Products_dic[name_of_Customer_product][0]-=Quantity_of_Customer_product
							print("Price of last product:")
							print((Quantity_of_Customer_product*Products_dic[name_of_Customer_product][1]))
							print("your product:")
							print(Customer_Products_dic)
							print("Total cost ="+ str(cost))
							#FILE HANDLING
							Fatora_file= open("Fatora_file.txt","a+")
							#Fatora_file= open("Fatora_file.txt","w")
							Fatora_file.write("name_of_Customer_product '"+ str(name_of_Customer_product) + "\n")
							Fatora_file.write("Price of last product::"+str((Quantity_of_Customer_product*Products_dic[name_of_Customer_product][1])))
							Fatora_file.write("Customer_Products_dic:"+str(Customer_Products_dic)+"\n")
							Fatora_file.write("Total cost ="+ str(cost)+ "\n")
							Fatora_file.write("/////////////////////END process//////////////////////////"+"\n")
							Fatora_file.close()
							#FILE HANDLING
							break
						else:
							print("Quantity you needed not available at this moment :")
							print("You can found this "+str(Products_dic[name_of_Customer_product][0])+"Quantity")
				elif Customer_mode ==3:
					if cost>0:																		#Cost_Mode
						#print("you orderd '"+ str(len(Customer_Products_dic)) + "' products from our shop")
						#print("your product:")
						#print(Customer_Products_dic)
						#print("Total cost ="+ str(cost))
						#FILE HANDLING
						Fatora= open("Fatora.txt","a+")
						Fatora= open("Fatora.txt","w")
						Fatora.write("you orderd '"+ str(len(Customer_Products_dic)) + "' products from our shop")
						Fatora.write("your product:"+str(Customer_Products_dic))
						cost+=(Quantity_of_Customer_product*Products_dic[name_of_Customer_product][1])
						Fatora.write("Total cost ="+ str(cost))
						Fatora= open("Fatora.txt","r")
						print (Fatora.read())
						Fatora.close()
						os.remove("Fatora.txt")
						#FILE HANDLING
					elif cost==0:
						print("you don't buy any thing")
						print("Choose '1'to show our products and '2' to Buy our products")
				elif Customer_mode ==0:
					Customer_Products_dic.clear()
					break																			#exist to main mode
				else:
					print ("Choose one of this modes:")
					
	elif mode == 3:
		break																						#exit from main program
	elif mode==4:
		print ("----------Welcome ITI Employes----------")
		print ("Employes Modes:")
		print ("press '1' for Add new Employes")
		print ("press '2' for Show Employes")
		print ("press '3' for Fired Employes")
		print ("press '0' to exist to main mode")
		while True:
			try:
				Employes_mode=int (input("Please choose mode:"))
				break
			except:
				print ("Enter Valid Number")
		if   Employes_mode ==1:
			name_of_new_Employe=input("Enter name of new Employe:")							#input new Employe
			while True:
				try:
					Salary_of_new_Employe=float(input("Enter Salary:"))					#input salary_of_new_Employe
					break
				except:
					print ("Enter Valid Number")
			employes_dic[name_of_new_Employe]= Salary_of_new_Employe
			#FILE HANDLING
			employes_dic_file= open("employes_dic.txt","a+")
			#employes_dic_file= open("employes_dic.txt","w")
			employes_dic_file.write("name_of_new_Employe : "+ str(name_of_new_Employe)+"\n")
			employes_dic_file.write("Salary_of_new_Employe:"+str(Salary_of_new_Employe)+"\n")
			employes_dic_file.write("/////////////////////END process//////////////////////////"+"\n")
			employes_dic_file.close()
			#FILE HANDLING
		elif Employes_mode ==2:
			print("employes now salary:")
			#print(employes_dic)
			#FILE HANDLING
			employes_dic_file= open("employes_dic.txt","a+")
			employes_dic_file= open("employes_dic.txt","r")
			print (employes_dic_file.read())
			employes_dic_file.close()
			#FILE HANDLING
		elif Employes_mode ==3:                                                         #Fired_Employes
			name_of_Fired_Employe=input("Enter name of Fired Employe:")							#input fired Employe
			while True:
				try:
					Salary_of_Fired_Employe=float(input("Enter Salary:"))					#input salary_of_fired_Employe
					break
				except:
					print ("Enter Valid Number")
			while True:
				try:
					Phone_number_Fired_Employe=float(input("Enter Phone number:"))					#input phone_number_fired_Employe
					break
				except:
					print ("Enter Valid Number")
			while True:
				try:
					Day_Fired_Employe=float(input("Enter Day(like : 12/3/1987):"))					#input Day_fired_Employe
					break
				except:
					print ("Enter Valid Number")
			Fired_Employes[name_of_Fired_Employe]= [Salary_of_Fired_Employe,Phone_number_Fired_Employe,Day_Fired_Employe]
			#FILE HANDLING
			Fired_Employes_file= open("Fired_Employes.txt","a+")
			#Fired_Employes_file= open("Fired_Employes.txt","w")
			Fired_Employes_file.write("name_of_Fired_Employe : "+ str(name_of_Fired_Employe)+"\n")
			Fired_Employes_file.write("Salary_of_Fired_Employe:"+str(Salary_of_Fired_Employe)+"\n")
			Fired_Employes_file.write("Phone_number_Fired_Employe:"+str(Phone_number_Fired_Employe)+"\n")
			Fired_Employes_file.write("Day_Fired_Employe:"+str(Day_Fired_Employe)+"\n")
			Fired_Employes_file.write("/////////////////////END process//////////////////////////"+"\n")
			Fired_Employes_file.close()
			#FILE HANDLING
			print (Fired_Employes)
		elif Employes_mode ==0:
			break
		else:
			print("----------Wrong Mode----------")														#Wrong Mode
			print("Please choose from this modes:")
	else:
		print("----------Wrong Mode----------")														#Wrong Mode
		print("Please choose from this modes:")
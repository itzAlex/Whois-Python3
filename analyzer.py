# Analyzer of the received information
# Author: @itzAlex

import os
try:
	from prettytable import PrettyTable
except ImportError:
	try:
		os.system("pip install prettytable")
	except:
		print("PrettyTable wasn't found in the system, tried to install it but could not.")


Registrar_Data_Delete = "We will display stored WHOIS data for up to 30 days. Make Private Now "

def analyze():

	center_output = os.get_terminal_size().columns
	read_website = (open("cleaned_website.txt", "r")).read()

	Registrar_Info = read_website[(read_website.find("Registrar Info")+15):(read_website.find("Important Dates")-1)] 
	Important_Dates = read_website[(read_website.find("Important Dates")+16):(read_website.find("Name Servers")-1)]
	Name_Servers = read_website[(read_website.find("Name Servers")+13):(read_website.find("Similar Domains")-1)]
	Similar_Domains = read_website[(read_website.find("Similar Domains")+16):(read_website.find("Registrar Data")-1)]
	Registrar_Data = read_website[(read_website.find("Registrar Data")+15):(read_website.find("Information Updated:")-1)]
	Information_Updated = read_website[read_website.find("Information Updated:"):]


	# Registrar Info ✓

	Name_Registrar_Info = Registrar_Info[Registrar_Info.find("Name"):(Registrar_Info.find("Whois Server")-1)]
	Whois_Server_Registrar_Info = Registrar_Info[Registrar_Info.find("Whois Server"):(Registrar_Info.find("Referral URL")-1)]
	Referral_URL_Registrar_Info = Registrar_Info[Registrar_Info.find("Referral URL"):(Registrar_Info.find("Status")-1)]
	Status_Registrar_Info = Registrar_Info[Registrar_Info.find("Status"):]

	# Important Dates ✓

	Expires_On_Important_Dates = Important_Dates[Important_Dates.find("Expires On"):(Important_Dates.find("Registered On")-1)]
	Registered_On_Important_Dates = Important_Dates[Important_Dates.find("Registered On"):(Important_Dates.find("Updated On")-1)]
	Updated_On_Important_Dates = Important_Dates[Important_Dates.find("Updated On"):]

	# Name Servers ✓

	Table_Name_Servers = PrettyTable(['Domain', 'IP'])
	Name_Servers_Split = Name_Servers.split()

	for i in range(0, len(Name_Servers_Split), 2):
		Row = []
		IPs = Row.append(Name_Servers_Split[i])
		Domains = Row.append(Name_Servers_Split[i+1])
		Table_Name_Servers.add_row(Row)

	# Print everything	

	print("\n", "----------------Registrar Info----------------".center(center_output), "\n\n", Name_Registrar_Info.replace("Name", "Name:", 1), "\n", Whois_Server_Registrar_Info.replace("Whois Server", "Whois server:", 1), "\n", Referral_URL_Registrar_Info.replace("Referral URL", "Referral URL:", 1), "\n", Status_Registrar_Info.replace("Status", "Status:", 1))
	print("\n", "----------------Important Dates----------------".center(center_output), "\n\n", Expires_On_Important_Dates.replace("Expires On", "Expires On:", 1), "\n", Registered_On_Important_Dates.replace("Registered On", "Registered On:", 1), "\n", Updated_On_Important_Dates.replace("Updated On", "Updated On:", 1))
	print("\n", "----------------Name Servers----------------".center(center_output)); print(" "); print(Table_Name_Servers) # Used print() instead of "\n" because of an unknown space in the new line
	print("\n", "----------------Similar Domains----------------".center(center_output), "\n\n", Similar_Domains)
	print("\n", "----------------Registrar Data----------------".center(center_output), "\n"); print(" "); print(Registrar_Data.replace(Registrar_Data_Delete, ""))
	print("\n\n\n", Information_Updated.center(center_output))
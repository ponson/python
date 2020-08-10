#!/usr/bin/python
# -*- coding: UTF-8 -*-

from datetime import datetime
import os, sys

strDataTypesBefore = ["Sales Diagnostic_Detail View_", "Forecast and Inventory Planning_", "Inventory Health_"] 
strDataTypesAfter = ["-Sales Diagnostic_Detail View-Daily_(sp)_", "-Forecast and Inventory Planning-Daily_(sp)_", "-Inventory Health-Daily_(sp)_"]

strCountriesBefore = ["US", "CA", "MX", "BR", "GB", "FR", "ES", "DE", "IT", "JP", "AU", "AE", "IN"]
strCountriesAfter = ["com", "ca", "com.mx", "com.br", "co.uk", "fr", "es", "de", "it", "co.jp", "com.au", "ae", "in"]



# List files
fileList = os.listdir(os.getcwd())

print ('directory: %s' %fileList)

for fileStr in fileList:
	tarCountryIdx = -1
	tarDataTypeIdx = -1
		
	if fileStr.find(".csv") < 0:
		continue
	print ("filename : %s" %fileStr)
	strLen = len(fileStr)
    # Data Type Comparison
	for i in range(len(strDataTypesBefore)):
		#print(strDataTypesBefore[i])
		#print(fileStr.find(strDataTypesBefore[i]))
		if fileStr.find(strDataTypesBefore[i]) >= 0:
			tarDataTypeIdx = i
			break
			
	for j in range(len(strCountriesBefore)):
		#print(strCountriesBefore[j])
		#print(fileStr[strLen-12: strLen-10])
		if fileStr.find(strCountriesBefore[j], strLen-12, strLen-10) >= 0:
			tarCountryIdx = j
			break
	idxStrP = "DataTypeIdx: {}, CountryIdx: {}" 		
	#print (idxStrP.format(tarDataTypeIdx, tarCountryIdx))
	if (tarDataTypeIdx >= 0 and tarCountryIdx >=0):
		#handle date
		dateStr = fileStr[strLen-9:strLen-4]
		dateObj = datetime.strptime("2020-"+dateStr, "%Y-%m-%d").date()
		print("==> "+strCountriesAfter[tarCountryIdx]+strDataTypesAfter[tarDataTypeIdx]+str(dateObj)+"_to_"+str(dateObj)+".csv")
		os.rename(fileStr,strCountriesAfter[tarCountryIdx]+strDataTypesAfter[tarDataTypeIdx]+str(dateObj)+"_to_"+str(dateObj)+".csv")
print("Done.")














# Windows

def reclassify(vul):
	if vul < 0:
		return 'None'
	elif vul >= 0 and vul <=0.2:
		return 'Low'
	elif vul > 0.2 and vul <=0.4:
		return 'Moderately Low'
	elif vul > 0.4 and vul <=0.6:
		return 'Medium'
	elif vul > 0.6 and vul <=0.8:
		return 'Moderately High'
	elif vul > 0.8:
		return 'High'
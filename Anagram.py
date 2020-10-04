from collections import defaultdict

def areAnagram(string1, string2):
	if len(string1)!=len(string2):
		return False
	count_dict = {}
	count_dict= defaultdict(lambda:0,count_dict)
	for i in range(len(string1)):
		count_dict[string1[i]]+=1
		count_dict[string2[i]]-=1
	for key in count_dict:
		if count_dict[key] !=0:
			return False
		else:
			return True

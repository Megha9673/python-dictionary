import json
data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		yn =  input("Did u mean %s instead?Enter Y for yes and N for no:" % get_close_matches(w, data.keys())[0])
		if yn== 'Y':
			return data[w]
		elif yn== 'N':
			return "word doesn't exist"	
		else:
			return "we don't understand your query"
				
	else:
		print("word non existent")

word = raw_input("enter word")
output = translate(word)
if type(output)== list:
	for item in output:
		print(item)
else:
	print(output)		
units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = 'hundred'
thousand = 'thousand'

def convert_to_words(x):
	if x == 1000:
		return 'one thousand'
	result = ''	
	if x >= 100:
		result += units[int(x / 100)] + ' ' + hundred
		x %= 100
	if x != 0:
		if len(result):
			result += ' and '
		if x >= 20:
			result += tens[int(x / 10) - 2]
			x %= 10
			if x != 0:
				result += '-'
		elif x > 10:
			result += teens[x - 11]
			x = 0
		if x > 0:
			result += units[x]
	return result

result = 0
for i in range(1, 1001):
	result += sum([x != ' ' and x != '-' for x in convert_to_words(i)])
print(result)

'''https://www.codewars.com/kata/5ae326342f8cbc72220000d2
Given a string that includes alphanumeric characters ('3a4B2d') return the expansion of that string: The numeric values represent the occurance of each letter preceding that numeric value. There should be no numeric characters in the final string. Empty strings should return an empty string.
The first occurance of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears.
string_expansion('3D2a5d2f') == 'DDDaadddddff'
string_expansion('3abc') == 'aaabbbccc'       # correct
string_expansion('3abc') != 'aaabc'           # wrong
string_expansion('3abc') != 'abcabcabc'       # wrong
If there are two consecutive numeric characters the first one is ignored.
string_expansion('3d332f2a') == 'dddffaa'
If there are two consecutive alphabetic characters then the first character has no effect on the one after it.
string_expansion('abcde') == 'abcde'
Your code should be able to work for both lower and capital case letters.
string_expansion('') == ''
'''
def string_processing(string):
	digit = '1'
	strng = ''
	last = ''
	res = ''
	if len(string) == 0: return ''
	else:
		if string[0].isdigit():
			digit = string[0]
			last = 'd'
		else:
			strng = string[0]
			last = 's'
		for i in range(1, len(string)):
			if string[i].isdigit():
				if last == 's':
					for e in strng:
						res += e * int(digit)
			#			print(res)
					digit = string[i]
					last = 'd'
				else:
					digit = string[i]
					last = 'd'
			else:
				if last == 'd':
					strng = string[i]
					last = 's'
				else:
					strng += string[i]
					last = 's'
		for e in strng:
			res += e * int(digit)
	return res
	
string = '' # should equal 'Mdr'
print(string_processing(string))

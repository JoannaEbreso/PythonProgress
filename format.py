Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '{} is {} years old!'.format('Bill',24)
'Bill is 24 years old!'
>>> {} is {} years old!.format('Bill',24)
SyntaxError: invalid syntax
>>> names = ['Ade', 'Ernest', 'Chima', 'Chimobi', 'Ife']
>>> ages = [16,7,9,25,99]
>>> for index in range(5):
	'{:<10s} is {:<10d} years old'.format ('Bill',24)
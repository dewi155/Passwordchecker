import requests #url/api 
import hashlib #sha1password 
import sys #input password
import os


def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
	return res

def get_password_leaks_count(hashes, hash_to_check): 
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0
		
def pwned_api_check(password): #converts password into SHA1
	sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
	first5_char, tail = sha1password[:5], sha1password[5:] #store password in two parts for security
	response = request_api_data(first5_char)
	return get_password_leaks_count(response, tail)

def main(text):
		my_file = open(r'C:/Users/dewi1/PycharmProjects/passwordchecker/password.txt', mode='r')
		password = my_file.read()	
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times... you should change your password!')
		else:
			print(f'{password} was NOT found. Well done!')	
		return 'done!'		


if __name__ == '__main__':
    sys.exit(main(sys.argv))
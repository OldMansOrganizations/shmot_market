import hashlib

errors_data = {
				'uniq_name': 'name not unique',
				'uniq_login': 'login not unique',
				'uniq_gmail': 'gmail not unique',
				'unique_personal_area': 'personal area ERROR'
			}


def hash_password(password):
	new_password = hashlib.sha256(password.encode('utf-8'))
	new_password = new_password.hexdigest()
	return new_password



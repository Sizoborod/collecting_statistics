from requests import get, post, delete


print(post('http://localhost:5000/api/users', json={'name': 'Mike', 'email': 'smith@mars.org', 'hashed_password': 'physics'}).json())


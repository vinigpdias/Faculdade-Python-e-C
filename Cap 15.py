#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#r.status_code
#200
#r.headers['content-type'] 
#'application/json; charset=utf8'
#r.encoding 
#'utf-8'
#r.text
#'{"type":"User"...'
#r.json()
#{'private_gists': 419, 'total_private_repos': 77, ...}

usuarios = []

user1 = {
    "rm":89114,
    "senha":"kxVTM4BZIS"
}

usuarios.append(user1)

for user in usuarios:
    print(user['senha'])


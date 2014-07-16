from pygithub3 import Github

gh = Github(login='copitux', password='password')

copitux = gh.users.get()
kennethreitz = gh.users.get('kennethreitz')

copitux_repos = gh.repos.list().all()
kennethreitz_repos = gh.repos.list('kennethreitz').all()
print kennethreitz_repos
import git

def pull_covid_data():
	""" Pulls the data from COVID-19 repository using GitPython """
	path = 'COVID-19'
	repository = git.Repo(path)
	r = repository.remotes.origin
	r.pull()

	print(f'Here is the status update of {path}: ')
	print('\n' + repository.git.status())

pull_covid_data() 
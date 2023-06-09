import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pygal.config

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code", r.status_code)

response_dict = r.json()
#print(response_dict.keys())
# print('Total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))

# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#    print(key)
    
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print('Name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])
#     print('\n')

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description'],
		'xlink':repo_dict['html_url']
	}
    plot_dicts.append(plot_dict)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_config.style = LS('#333388', base_style=LCS)
my_config.title = 'Most-Starred Python Projects on GitHub'
my_config.x_labels = names


# visualize
chart = pygal.Bar(my_config)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
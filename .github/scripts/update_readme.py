import requests
import os
import re

ORG_NAME = os.environ['ORG_NAME']
TOKEN = os.environ['GITHUB_TOKEN']

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repos():
    url = f'https://api.github.com/orgs/{ORG_NAME}/repos'
    response = requests.get(url, headers=headers)
    return response.json()

def build_table(repos):
    featured = []
    completed = []

    for repo in repos:
        topics_url = f'https://api.github.com/repos/{ORG_NAME}/{repo["name"]}/topics'
        topics_res = requests.get(topics_url, headers={**headers, 'Accept': 'application/vnd.github.mercy-preview+json'})
        topics = topics_res.json().get('names', [])

        if 'nexalab-featured' in topics:
            featured.append((repo['name'], repo.get('description') or '-', '`In Progress`'))
        elif 'nexalab-completed' in topics:
            completed.append((repo['name'], repo.get('description') or '-', '`Completed`'))

    all_projects = featured + completed

    if not all_projects:
        return '| Project | Description | Status |\n|:--------|:------------|:------:|\n| Coming Soon | Our first project is on the way. | `In Progress` |'

    table = '| Project | Description | Status |\n|:--------|:------------|:------:|\n'
    for name, desc, status in all_projects:
        table += f'| [{name}](https://github.com/{ORG_NAME}/{name}) | {desc} | {status} |\n'

    return table.strip()

def update_readme(table):
    with open('profile/README.md', 'r') as f:
        content = f.read()

    pattern = r'(## Our Projects\n\n)[\s\S]*?(\n\n>)'
    replacement = f'\\1{table}\\2'
    new_content = re.sub(pattern, replacement, content)

    with open('profile/README.md', 'w') as f:
        f.write(new_content)

repos = get_repos()
table = build_table(repos)
update_readme(table)
print("README updated successfully.")

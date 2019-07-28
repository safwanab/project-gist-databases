import requests
import sqlite3
​
def import_gists_to_database(db, username, commit=True):
    api_url = 'https://api.github.com/users/{}/gists'.format(username)
    response = requests.get(api_url)
    
    if response.status_code == 404:
        raise requests.HTTPError()
    
    for gist in response.json():
         cursor = db.execute('''
         INSERT INTO gists
             (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url)
         VALUES
             (:id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, :comments_url)
         ''', gist)

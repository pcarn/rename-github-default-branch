# Rename GitHub Default Branch

If you try to rename the default branch of a repo, when you delete the old branch from the remote, it closes all pull requests that had it as a base.

This python script:
* Renames the branch on your local repo
* Pushes the new branch
* Changes all pull requests with the old branch as a base to the new branch
* Changes the repo's default branch in GitHub
* Deletes the old branch from GitHub

## Install
1. Set up a GitHub Personal Access Token
    * Go to https://github.com/settings/tokens, create a token with permission `repo`
2. Install dependencies
```bash
$ pip install PyGithub
$ pip install gitpython
```
3. Clone this repo

## Usage
```
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to Local Repo
  -t TOKEN, --token TOKEN
                        GitHub Personal Access Token
  -r REPO, --repo REPO  org/repo name
  --old-branch OLD_BRANCH
                        Old Branch Name
  --new-branch NEW_BRANCH
                        New Branch Name
```

## Example
```
$ python change_default_branch.py -p ~/git/my-repo -t token -r pcarn/my-repo --old-branch master --new-branch main
Renamed local branch from main to master
Pushed new branch
Changed PR #2 from base main to master
Changed PR #1 from base main to master
Changed repo's default branch to master
Deleted remote branch main
```

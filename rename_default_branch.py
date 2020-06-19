from git import Repo
from github import Github
import argparse

parser = argparse.ArgumentParser(description='Change the default branch of a github repo')
parser.add_argument('-p', '--path', dest='path', help='Path to Local Repo', required=True)
parser.add_argument('-t', '--token', dest='token', help='GitHub Personal Access Token', required=True)
parser.add_argument('-r', '--repo', dest='repo', help='org/repo name', required=True)
parser.add_argument('--old-branch', help='Old Branch Name', required=True)
parser.add_argument('--new-branch', help='New Branch Name', required=True)

args = parser.parse_args()

local_repo = Repo(args.path)
local_repo.git.branch('-m', args.old_branch, args.new_branch)
print('Renamed local branch from {} to {}'.format(args.old_branch, args.new_branch))
local_repo.git.push('-u origin', args.new_branch)
print('Pushed new branch')

g = Github(args.token)

repo = g.get_repo(args.repo)

pulls = repo.get_pulls(state='open', base=args.old_branch)
if pulls.totalCount == 0:
    print('No Pull Requests found with base {}'.format(args.old_branch))
else:
    for pr in pulls:
        pr.edit(base=args.new_branch)
        print('Changed PR #{} from base {} to {}'.format(pr.number, args.old_branch, args.new_branch))

repo.edit(default_branch=args.new_branch)
print('Changed remote repo\'s default branch to {}'.format(args.new_branch))


repo.get_git_ref('heads/{}'.format(args.old_branch)).delete()
print('Deleted remote branch {}'.format(args.old_branch))

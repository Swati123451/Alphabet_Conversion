mkdir Git2
cd Git2
git init
git status 
touch readfile.txt
git add .
git commit –a –m ‘change 1’
touch abc.css
git add .
git stash
gitbranch MyBranch
git checkout MyBranch
touch readfileMyBranch.txt
touch abcMyBranch.css
git add .
git stash
git stash apply
git commit –a –m ‘All Changes’
git log
git checkout master
git merge MyBranch
git merge MyBranch

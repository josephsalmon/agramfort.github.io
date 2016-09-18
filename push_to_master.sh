#!/usr/bin/env/bash
# rsync -avzh ./output ../agramfort.github.io/
cp  -R ./output/* ../agramfort.github.io/

cd ../agramfort.github.io
git ci -am 'updates'
git commit -m 'rebuild pages' --allow-empty
git push origin master
cd ~/github/agramfort-site

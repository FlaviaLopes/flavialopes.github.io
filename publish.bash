now="$(date +'%d/%m/%Y')"

pelican -o deploy -s publishconf.py

ghp-import deploy -b gh-pages -m "Publicado em $now" --cname="flavialopes.dev"

git push git@github.com:FlaviaLopes/flavialopes.github.io.git gh-pages:master





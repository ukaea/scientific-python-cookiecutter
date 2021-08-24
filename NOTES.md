## Deploying Tutorial to GitHub Pages with GitHub Actions

1. Make sure you have the Sphinx `conf.py` set correctly:
  ```python
  html_baseurl = 'http://ukaea.github.io/scientific-python-cookiecutter/'
  ```
2. Add this action to the GitHub Actions: 
  ```yaml
  - name: Deploy tutorial
    uses: peaceiris/actions-gh-pages@v3
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}
      publish_dir: ./
      publish_branch: gh-pages
  ```
3. Adjust settings of GitHub repo to use the gh-pages branch: `Settings > Pages > Source > Branch: gh-pages > /(root)`

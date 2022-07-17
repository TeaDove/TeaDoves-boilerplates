- `.flake8`
settings for [flake8](https://github.com/pycqa/flake8)
- `.gitignore`
python `.gitignore` with some extras
- `.pre-commit-config.yaml`
[pre-commit hooks](https://pre-commit.com/) config
usage:
```shell
pip3 install pre-commit
# then put .pre-commit-config.yaml in root of repository
pre-commit install
pre-commit run --all-files
```
- `pyproject.toml`
`black` and `isort` settings

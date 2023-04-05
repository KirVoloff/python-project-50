install:
		poetry install

package-install:
		pip install --user dist/*.whl --force-reinstall

lint:
		poetry run flake8 gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

check:		selfcheck test lint

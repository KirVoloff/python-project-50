install:
		poetry install

package-install:
		pip install --user dist/*.whl --force-reinstall

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

build:
		poetry build

publish:
		poetry publish --dry-run

selfcheck:
		poetry check

check:		selfcheck test lint

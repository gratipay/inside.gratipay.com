python := "$(shell { command -v python2.7 || command -v python; } 2>/dev/null)"

# Set the relative path to installed binaries under the project virtualenv.
# NOTE: Creating a virtualenv on Windows places binaries in the 'Scripts' directory.
bin_dir := $(shell $(python) -c 'import sys; bin = "Scripts" if sys.platform == "win32" else "bin"; print(bin)')
env_bin := env/$(bin_dir)
venv := "./vendor/virtualenv-12.0.7.py"

env: requirements.txt requirements_tests.txt
	$(python)  $(venv)\
				--prompt="[inside.gratipay.com] " \
				--never-download \
				--extra-search-dir=./vendor/ \
				./env/
	./$(env_bin)/pip --version
	./$(env_bin)/pip install --no-index --find-links=file:///$(PWD)/vendor -r requirements.txt
	./$(env_bin)/pip install --no-index --find-links=file:///$(PWD)/vendor -r requirements_tests.txt

clean:
	rm -rf env
	find . -name \*.pyc -delete

run: env
	./$(env_bin)/honcho -e defaults.env,local.env run ./env/bin/python \
		./startapp.py --port=8536

test:
	./$(env_bin)/py.test ./tests/

python := "$(shell { command -v python2.7 || command -v python; } 2>/dev/null)"

# Set the relative path to installed binaries under the project virtualenv.
# NOTE: Creating a virtualenv on Windows places binaries in the 'Scripts' directory.
bin_dir := $(shell $(python) -c 'import sys; bin = "Scripts" if sys.platform == "win32" else "bin"; print(bin)')
env_bin := env/$(bin_dir)
venv := "./vendor/virtualenv-1.9.1.py"

env:
	$(python)  $(venv)\
				--unzip-setuptools \
				--prompt="[building.gittip.com] " \
				--never-download \
				--extra-search-dir=./vendor/ \
				--distribute \
				./env/
	./$(env_bin)/pip install -r requirements.txt

clean:
	rm -rf env *.egg *.egg-info
	find . -name \*.pyc -delete

local.env:
	echo "Creating a local.env file ..."
	echo
	cp default.local.env local.env

run: env local.env
	./$(env_bin)/honcho -e default.local.env,local.env start web

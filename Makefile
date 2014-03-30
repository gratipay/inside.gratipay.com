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
	./$(env_bin)/pip install git+https://github.com/erikrose/peep.git@43b8e5790edec7457512b8d10a5f7ffeb666bad4
	./$(env_bin)/peep install -r requirements.txt --no-deps

clean:
	rm -rf env *.egg *.egg-info
	find . -name \*.pyc -delete

run: env local.env
	./$(env_bin)/honcho -e defaults.env,local.env run ./env/bin/aspen \
		--network_address :8536 --www_root=./www/ --project_root=./

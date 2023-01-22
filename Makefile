link-conda-env:
	ln -sf environments-and-requirements/environment-mac.yml environment.yml

link-conda-env-intel:
	ln -sf environments-and-requirements/environment-mac-intel.yml environment.yml

conda-update:
	conda env update

conda-activate:
	pyenv activate anaconda3-2022.05
	conda activate flan-t5-xl3

conda-delete:
	conda env remove -n flan-t5-xl3

conda-lock-env:
	conda env export > env.yml.lock
	conda list --explicit > spec-file.txt

conda-env-export:
	conda env export
	conda list --explicit

conda-history:
	conda env export --from-history

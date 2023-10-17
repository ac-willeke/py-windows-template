.PHONY: codestyle formatting docstring pre-commit clean clean-build clean-pyc clean-linting clean-test clean-log

# --------------------------------------------------------------------------- #
# Style targets
# --------------------------------------------------------------------------- #

codestyle: ## check codestyle (black, isort, ruff)
	isort --settings-path pyproject.toml ./
	black --config pyproject.toml ./
	ruff check ./**

docstring: ## create/ update docstring to restructured text
	pyment -w -o numpydoc /src
# access denied if no admin access 

pre-commit: ## run pre-commit on all files
#pre-commit run -a
	pre-commit run -a --config config/.pre-commit-config.yaml

# --------------------------------------------------------------------------- #
# Cleaning targets
# --------------------------------------------------------------------------- #

clean: clean-build clean-pyc clean-linting clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	for /d /r %%d in (*.egg-info) do rd /s /q "%%d"
	for /d /r %%d in (*.egg) do rd /s /q "%%d"
	for /d /r %%d in (*.eggs) do rd /s /q "%%d"
	for /d /r %%d in (build) do rd /s /q "%%d"
	for /d /r %%d in (dist) do rd /s /q "%%d"

clean-pyc: ## remove Python file and dir artifacts
	for /f "delims=" %%f in ('dir /s /b *.pyc') do del /f /q "%%f" 
	for /f "delims=" %%f in ('dir /s /b *.pyo') do del /f /q "%%f"
	for /d /r %%d in (__pycache__) do rd /s /q "%%d"
	for /d /r %%d in (.ipynb_checkpoints) do rd /s /q "%%d"

clean-linting: ## remove linting artifacts
	rmdir /s /q .ruff_cache
	rmdir /s /q .pytest_cache
	rmdir /s /q .vscode

clean-log: ## remove log files in /log folder
	del /f /q "log\*.log"


# --------------------------------------------------------------------------- #
# Conda targets
# --------------------------------------------------------------------------- #

conda-create: ## create conda environment
	conda env create -f environment.yml

conda-update: ## update conda environment
	conda env update -f environment.yml

conda-export: ## export conda environment
	conda env export > environment.yml

# --------------------------------------------------------------------------- #
# Installation targets using pipx
# --------------------------------------------------------------------------- #

install-global: install-pre-commit install-black install-isort install-ruff install-pyment install-cookiecutter install-pytest## install global tools

install-pre-commit: ## install pre-commit
	pipx install pre-commit --user

install-black: ## install black
	pipx install black

install-isort: ## install isort
	pipx install isort

install-ruff: ## install ruff
	pipx install ruff

install-pyment: ## install pyment
	pipx install pyment

install-cookiecutter: ## install cookiecutter
	pipx install cookiecutter

install-pytest: ## install pytest
	pipx install pytest

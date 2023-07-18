# GET VIRTUAL ENVIRONMENT =============================================
venv_get:
	./bin/get_poetry_env
	poetry run pip3 install --upgrade pip

	poetry run pip3 install torch-scatter -f https://data.pyg.org/whl/torch-2.0.1+cpu.html
	poetry run pip3 install torch-sparse -f https://data.pyg.org/whl/torch-2.0.1+cpu.html
	poetry run pip3 install torch-cluster -f https://data.pyg.org/whl/torch-2.0.1+cpu.html
	poetry run pip3 install torch-spline-conv -f https://data.pyg.org/whl/torch-2.0.1+cpu.html

	# NB! for some obscure reason installation of pyg-lib ruins all other libraries
	# poetry run pip3 install pyg-lib -f https://data.pyg.org/whl/torch-2.0.1+cpu.html

	poetry run python bin/test_poetry_env.py

# REMOVE VIRTUAL ENVIRONMENT ==========================================
venv_remove:
	@echo "===removing virtual environment==="
	rm -rf .venv
	rm poetry.lock
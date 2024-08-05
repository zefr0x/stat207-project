_default:
	@just --list

compile_dep:
	uv pip compile requirements/requirements.txt.in -o requirements/requirements.txt
	uv pip compile requirements/requirements-dev.txt.in -o requirements/requirements-dev.txt

sync_dep:
	uv pip sync requirements/requirements.txt requirements/requirements-dev.txt

dev:
	python3 setup.py build_ext --inplace
test:
	PYTHONPATH=. pytest tests/
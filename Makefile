build: rmdirs
	python setup.py sdist bdist_wheel
rmdirs:
	rm -rd dist build PyGizmo.egg-info
packets:
	pip install -r requirments.txt


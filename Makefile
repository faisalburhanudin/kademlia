PYDOCTOR=pydoctor

test: lint
	py.test --cov-report term-missing --cov=cermin -x

lint:
	flake8 kademlia

install:
	python setup.py install

PYDOCTOR=pydoctor

test:
	py.test --cov-report term-missing --cov=kademlia -x

lint:
	flake8 kademlia

install:
	python setup.py install

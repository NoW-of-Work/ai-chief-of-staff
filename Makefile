.PHONY: build clean check

build:
	python3 build/build.py

check: build
	python3 build/check.py

clean:
	rm -rf dist plugin/skills

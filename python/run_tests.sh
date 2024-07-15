#!/bin/bash

flake8 . && \
mypy . && \
bandit --silent -r -x '**/test_*.py' . && \
pytest --quiet --cov


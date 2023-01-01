#!/bin/bash
pylint nodes.py
pytest tests/ --cov-report=html --cov=nodes --cov-branch

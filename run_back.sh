#!/bin/bash

source ./.venv/bin/activate
uv run fastapi dev ./back/src/endpoints.py
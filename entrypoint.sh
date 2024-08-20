#!/bin/sh

echo "Starting FastAPI server"

uvicorn main:app --reload --host 0.0.0.0

#!/bin/bash

rm ./db.sqlite3
rm -r ./alembic/versions/*
alembic revision --autogen -m "init" && alembic upgrade head

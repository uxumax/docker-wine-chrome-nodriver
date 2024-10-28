#!/bin/bash
source ./ready_checker.sh

check_ready
docker compose build wine


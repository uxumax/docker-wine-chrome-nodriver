# Check arguments existance
source ./ready_checker.sh

check_ready
xhost +local:docker  # for container GUI
docker compose run --rm wine


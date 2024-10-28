# Check arguments existance
if [ $# -lt 2 ]; then
  echo "Error: Missing arguments."
  echo "Usage: $0 <profile_name> <script_name>"
  exit 1
fi

source ./ready_checker.sh

set_container_args() {
    # Set arguments to env file
    echo -e "PROFILE_NAME=$1\nSCRIPT_NAME=$2" > ./args.env
}

run_container() {
    docker compose run --rm wine
}

check_ready
set_container_args $1 $2
xhost +local:docker  # for container GUI
run_container


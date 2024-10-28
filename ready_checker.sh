CHROME_PATH="./chrome/bin/chrome.exe"

is_docker_installed() {
    if command -v docker &> /dev/null; then
        return 0
    else
        return 1
    fi
}

is_chrome_exists() {
    if [ -e $CHROME_PATH ]; then
        return 0
    else
        return 1
    fi
}

check_ready() {
    if ! is_docker_installed; then
        echo "Docker is not installed" >&2
        echo "Please install docker engine before build or run"
        echo "Get more info here https://docs.docker.com/engine/install/"
        exit 1
    fi

    if ! is_chrome_exists; then
        echo "Chrome does not exists" >&2
        echo "Please upload chrome browser dir to chrome/bin"
        echo "Exe file should be available at chrome/bin/chrome.exe"
        exit 1
    fi
}

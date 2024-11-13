#!/bin/sh
set -e

MONO_VERSION="9.3.0"
PYTHON_VERSION="3.11.2"

_download_mono_msi() {
    echo "Download wine-mono $MONO_VERSION msi"
    wget -P $HOME/wine/installers \
        https://dl.winehq.org/wine/wine-mono/$MONO_VERSION/wine-mono-$MONO_VERSION-x86.msi
}

_download_python() {
    wget -P $HOME/wine/installers \
        https://www.python.org/ftp/python/$PYTHON_VERSION/python-$PYTHON_VERSION-amd64.exe
}

is_wine_working() {
    return 0
}

install_mono() {
    mono_msi_file="$HOME/wine/installers/wine-mono-$MONO_VERSION-x86.msi"
    if [ ! -f "$mono_msi_file" ]; then
        echo "Essential wine-mono does not downloaded"
        _download_mono_msi
    fi
    echo "Install wine-mono $MONO_VERSION"
    wine msiexec /i $mono_msi_file
    echo "Mono has been installed"
}

install_python() {
    py_installer=$HOME/wine/installers/python-$PYTHON_VERSION-amd64.exe
    if [ ! -f "$py_installer" ]; then
        echo "Python installer does not downloaded"
        _download_python
    fi
    echo "Install python $PYTHON_VERSION"
    wine $py_installer
    echo "Python has been installed. Install dependencies"
    wine python -m pip install -r $HOME/chrome/requirements.txt
}

reset_wine() {
    echo "Reseting wine..."
    rm -rf "$HOME/wine/prefix" && winecfg
}

is_wine_prefix_exists() {
    if [ ! -d "$HOME/wine/prefix" ]; then
        return 0  # True, directory is empty
    else
        return 1  # False, directory is not empty
    fi
}

run_app() {
    wine python chrome/run.py $PROFILE_NAME $SCRIPT_NAME
}

entry_point() {
    if is_wine_prefix_exists; then
        echo "Creating new wine prefix"
        winecfg || reset_wine
        # Can install mono here if popup of mono instalation doesn't appear
        # install_mono
    fi

    if ! is_wine_working; then
        echo "Wine is not working. Have to reset"
        reset_wine
    fi
    
    # Install python if not installed
    wine python --version || install_python

    run_app
}

entry_point


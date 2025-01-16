FROM debian:12

# Install basic utils
RUN apt-get update && \
    apt-get install -y \
        x11-apps \
        unzip \
        wget \
        vim \
        sudo 

# Add wine repository
RUN mkdir -pm755 /etc/apt/keyringsa && \
    wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key && \
    wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bookworm/winehq-bookworm.sources

# Install wine
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install --install-recommends -y \
        fonts-wine \
        winehq-staging 
        # If set winehq-stable then fonts inside chrome pages will not show 
        # Do not know why but set staging for now

# Clean apt lists
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Wihtout this line winecfg will not work properly
RUN wineboot --init

# Create a user to run Wine
RUN useradd -m wineuser && \
    echo "wineuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to the wineuser
USER wineuser
WORKDIR /home/wineuser

ENV WINEDEBUG="-all"
ENV WINEPREFIX="/home/wineuser/wine/prefix"

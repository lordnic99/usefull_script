#!/bin/bash



# Move to the user's home directory

cd ~
git config --global http.postBuffer 1048576000

git config --global https.postBuffer 1048576000



# Update package lists (recommended before installing dependencies)

sudo apt-get update



# Install required dependencies

echo "Installing dependencies..."

sudo apt-get install -y ninja-build gettext cmake unzip curl build-essential



# Clone the Neovim repository

echo "Cloning Neovim..."

git clone https://github.com/neovim/neovim



# Navigate to the Neovim directory

cd neovim



# Build Neovim with optimizations and debug information

echo "Building Neovim (RelWithDebInfo)..."

make CMAKE_BUILD_TYPE=RelWithDebInfo



# Install Neovim (use sudo with caution)

echo "Installing Neovim (This may require root privileges)..."

sudo make install



# Print a success message

echo "Neovim installation complete!"



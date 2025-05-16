#!/bin/bash

# This script creates a 4 GB swap file on an EC2 instance (e.g., t2.micro)
# Run it as root or with sudo: sudo ./create-swap.sh

set -e

echo "🚧 Creating 4 GB swap file..."

# Step 1: Allocate 4 GB for swap
sudo fallocate -l 4G /swapfile || sudo dd if=/dev/zero of=/swapfile bs=1M count=4096

# Step 2: Set correct permissions
sudo chmod 600 /swapfile

# Step 3: Format the file as swap
sudo mkswap /swapfile

# Step 4: Enable swap immediately
sudo swapon /swapfile

# Step 5: Make swap permanent (add to /etc/fstab if not already there)
if ! grep -q "/swapfile" /etc/fstab; then
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
fi

# Step 6: Adjust swappiness to 10 (default is 60)
sudo sysctl vm.swappiness=10
if ! grep -q "vm.swappiness" /etc/sysctl.conf; then
    echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
fi

# Step 7: Display result
echo "✅ Swap enabled. Current memory usage:"
free -h

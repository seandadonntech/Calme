#!/bin/bash

# Set the target directory for KDE widgets
TARGET_DIR="$HOME/.local/share/plasma/plasmoids/calme"

# Create the target directory
mkdir -p "$TARGET_DIR"

# Copy the necessary files to the target directory
cp -r contents/* "$TARGET_DIR/"

# Notify KDE Plasma to reload the widgets
qdbus org.kde.plasmashell /PlasmaShell reloadConfig

echo "Widget installed successfully!"



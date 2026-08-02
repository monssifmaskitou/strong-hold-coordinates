## Linux Desktop Shortcut Setup
To launch this app from your system menu:
1. Copy `coordinatesapp.desktop` to `~/.local/share/applications/`
2. Open the file and update the `Exec=` line if you install the project somewhere else.
3. Make it executable: `chmod +x ~/.local/share/applications/coordinatesapp.desktop`

The app resolves `icon.png` relative to the script location, so moving the project folder does not require changing the Python code.

The desktop shortcut now launches [launch.sh](/home/monssif/Desktop/coordinatesapp/launch.sh), which locates the repo folder at runtime and uses the project virtual environment if it exists.

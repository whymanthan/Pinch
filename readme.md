# Pinch

Pinch is a Python script that runs in the background on a Linux system (Ubuntu), allowing users to capture selected text from any application and append it to a Markdown file using a global keyboard shortcut (Ctrl+Shift+X). The script uses `xclip` for clipboard operations and provides desktop notifications for user feedback.

## Features

- Capture selected text from any application.
- Append the captured text to a specified Markdown file.
- Add two blank lines between each new text entry.
- Provide desktop notifications for successful operations or errors.
- Run automatically on system startup.

## Requirements

- Python 3
- `xclip`
- `libnotify-bin`
- `pynput`

## Installation

1. **Clone the Repository:**

   - `git clone https://github.com/whymanthan/Pinch.git`
   - `cd pinch`
   
2. **Install Required Packages:**

   - `sudo apt-get install xclip libnotify-bin`
   - `pip3 install pynput`
   
3. **Make the Script Executable:**
   `chmod +x pinch.py`
   
4. **Create a .desktop File for Startup:**

- You can create a .desktop file specifically for the startup application.
  `nano ~/.config/autostart/pinch.desktop`

- If the autostart directory does not exist, create it:
   `mkdir -p ~/.config/autostart`


5. **Add the Following Content to pinch.desktop:**
```
[Desktop Entry]
   Type=Application
   #your_pinchfiledestination
   Exec=python3 ./
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name=Pinch
   Comment=Capture selected text and append to Markdown file
```

- Ensure the Exec line points to the correct path of your pinch.py script.

6. **Save and Close the File:**

- Save the changes and close the text editor (Ctrl+O, Enter, Ctrl+X for nano).

7. **Verify Startup Entry**

- Reboot your system to ensure that the script runs on startup.
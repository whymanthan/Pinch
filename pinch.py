import subprocess
import os
from pynput import keyboard
import notify2

# File to which the text will be appended
MARKDOWN_FILE = os.path.expanduser('~/Documents/Max/pinch.md')

# Initialize the notify2 system
notify2.init('Pinch')

def get_selection():
    try:
        # Use xclip to get the selected text from the primary clipboard
        result = subprocess.run(['xclip', '-selection', 'primary', '-o'], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        notify_user("Error: Unable to access selection")
        return None

def notify_user(message):
    notification = notify2.Notification("Pinch", message)
    notification.show()

def append_to_file(text):
    try:
        with open(MARKDOWN_FILE, 'a') as file:
            file.write('-----'+'\n' + text + '\n')
        notify_user("Text successfully appended to markdown file")
    except Exception as e:
        notify_user(f"Error: {str(e)}")

def on_activate():
    selection_text = get_selection()
    if selection_text:
        append_to_file(selection_text)

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<shift>+x'),
    on_activate
)

listener = keyboard.Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)
)

def main():
    listener.start()
    notify_user("Pinch listener started. Press Ctrl+Shift+X to capture selected text.")
    listener.join()

if __name__ == '__main__':
    main()

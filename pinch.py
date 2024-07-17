import subprocess
from pynput import keyboard

# File to which the text will be appended
MARKDOWN_FILE = '/home/angy/Documents/Max/pinched.md'

# Function to read the current selection using xclip
def get_selection():
    try:
        result = subprocess.run(['xclip', '-selection', 'primary', '-o'], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        notify_user("Error: Unable to access selection")
        return None

# Function to notify user via GUI notification
def notify_user(message):
    subprocess.run(['notify-send', 'Pinch', message])

# Function to append text to the markdown file with two blank lines before the new text
def append_to_file(text):
    try:
        with open(MARKDOWN_FILE, 'a') as file:
            file.write('\n\n' + text + '\n')
        notify_user("Text successfully appended to markdown file")
    except Exception as e:
        notify_user(f"Error: {str(e)}")

# Define the keyboard listener function
def on_activate():
    selection_text = get_selection()
    if selection_text:
        append_to_file(selection_text)

# Define the keyboard shortcut listener
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

# Start the keyboard listener in a background thread
listener.start()
notify_user("Pinch listener started. Press Ctrl+Shift+X to capture selected text.")
listener.join()

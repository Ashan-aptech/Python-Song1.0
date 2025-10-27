import time
import random
import sys
import os

# --- Fix for Windows console encoding ---
if os.name == "nt":
    sys.stdout.reconfigure(encoding="utf-8")
    os.system("chcp 65001 >nul")

# --- Global Toggle for Colors ---
ENABLE_COLORS = False

# --- Terminal Colors ---
if ENABLE_COLORS:
    class Colors:
        HEADER = "\033[95m"
        CYAN = "\033[96m"
        BLUE = "\033[94m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        END = "\033[0m"
        BOLD = "\033[1m"
        MAGENTA = "\033[35m"
        LIGHTCYAN = "\033[96m"
        ORANGE = "\033[33m"
        LIGHTGREEN = "\033[92m"
        PURPLE = "\033[35m"
        LIGHTBLUE = "\033[94m"
else:
    class Colors:
        HEADER = CYAN = BLUE = GREEN = YELLOW = RED = END = BOLD = MAGENTA = LIGHTCYAN = ORANGE = LIGHTGREEN = PURPLE = LIGHTBLUE = ''

# --- Utility: Clear Screen ---
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# --- Utility: Typewriter Effect ---
def type_text(text, min_delay=0.03, max_delay=0.08, color=Colors.END, bounce=False, newline=True):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        if bounce:
            time.sleep(random.uniform(min_delay, max_delay) * random.uniform(0.5, 1.5))
        else:
            time.sleep(random.uniform(min_delay, max_delay))
    if newline:
        print()

# --- Utility: Safe Divider ---
def safe_divider(char="═", length=60):
    try:
        print(Colors.BOLD + Colors.HEADER + char * length + Colors.END)
    except UnicodeEncodeError:
        print(Colors.BOLD + Colors.HEADER + "=" * length + Colors.END)

# --- Animation: Music Notes ---
def music_notes_effect():
    print(Colors.BOLD + Colors.PURPLE + "🎵" + Colors.END, end=" ")
    for _ in range(3):
        notes = ["♪", "♫", "🎶"]
        for note in notes:
            try:
                sys.stdout.write(Colors.LIGHTBLUE + note + " " + Colors.END)
                sys.stdout.flush()
                time.sleep(0.08)
            except UnicodeEncodeError:
                sys.stdout.write(Colors.LIGHTBLUE + "*" + Colors.END)
    print(Colors.BOLD + Colors.PURPLE + "🎵" + Colors.END)

# --- Animation: Pulsing Effect ---
def pulse_effect(text, pulses=3):
    for i in range(pulses):
        if i % 2 == 0:
            sys.stdout.write(Colors.BOLD + Colors.YELLOW + text + Colors.END)
        else:
            sys.stdout.write(Colors.BOLD + Colors.ORANGE + text + Colors.END)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b" * len(text))

# --- Animation: Loading Bar ---
def loading_bar(duration=3, width=30):
    print(Colors.CYAN + "[", end="")
    for i in range(width):
        sys.stdout.write("▰")
        sys.stdout.flush()
        time.sleep(duration / width)
    print("]" + Colors.END)

# --- Lyrics Display Function ---
def play_lyrics():
    lyrics = [
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",
        "Jadon vi tenu dekhan aaya...",
        "Meri akhiyan ne keha...",
        "Tu hi meri jaan, tu hi meri duniya...",
        "Tu hi meri har khushi...",
        "Main taan tere kol rehna...",
        "Tere naal guzarna...",
        "Saari zindagi...",
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",
        "Teri muskurahat dekh ke...",
        "Mera dil dhadakda hai...",
        "Teri baaton mein hai woh jaadu...",
        "Jo mujhe bandh ta hai...",
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",
        "Har din tera intezar...",
        "Har raat teri yaad...",
        "Tere bina adhoori hai...",
        "Meri har ek saans...",
        "Ohhh... Talwiinder...",
        "Meri jaan...",
        "Ohhh... Talwiinder...",
        "Meri duniya...",
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",
        "Talwiinder...",
        "Meri Talwiinder...",
        "Tu milegi...",
        "Haan tu milegi...",
        "Kade na kade..."
    ]

    verse_delays = [2.0, 1.8, 2.2, 2.0, 
                   1.7, 1.5, 2.0, 1.8,
                   1.6, 1.4, 1.2,
                   2.0, 1.8, 2.2, 2.0,
                   1.7, 1.5, 1.8, 1.6,
                   2.0, 1.8, 2.2, 2.0,
                   1.8, 1.6, 1.7, 1.5,
                   2.5, 2.0, 2.5, 2.0,
                   2.0, 1.8, 2.2, 2.0,
                   2.5, 2.0, 1.8, 1.5, 2.0]

    verse_colors = [Colors.LIGHTBLUE, Colors.CYAN, Colors.LIGHTCYAN, Colors.BLUE,
                   Colors.GREEN, Colors.LIGHTGREEN, Colors.YELLOW, Colors.ORANGE,
                   Colors.MAGENTA, Colors.PURPLE, Colors.RED,
                   Colors.LIGHTBLUE, Colors.CYAN, Colors.LIGHTCYAN, Colors.BLUE,
                   Colors.GREEN, Colors.LIGHTGREEN, Colors.YELLOW, Colors.ORANGE,
                   Colors.LIGHTBLUE, Colors.CYAN, Colors.LIGHTCYAN, Colors.BLUE,
                   Colors.MAGENTA, Colors.PURPLE, Colors.RED, Colors.ORANGE,
                   Colors.YELLOW, Colors.LIGHTGREEN, Colors.YELLOW, Colors.LIGHTGREEN,
                   Colors.LIGHTBLUE, Colors.CYAN, Colors.LIGHTCYAN, Colors.BLUE,
                   Colors.PURPLE, Colors.MAGENTA, Colors.LIGHTBLUE, Colors.CYAN, Colors.LIGHTCYAN]

    clear_screen()
    safe_divider()
    type_text("🎶 NOW PLAYING: SANJOY - TU TALWIINDER 🎶", 0.05, 0.1, Colors.HEADER, bounce=True)
    safe_divider()
    print()
    time.sleep(1.5)

    print(Colors.YELLOW + "📻 Loading 'Tu Talwiinder' by Sanjoy..." + Colors.END)
    print(Colors.CYAN + "   Music Status: ", end="")
    pulse_effect("LOADING", 4)
    print()
    loading_bar(2.5)
    print()
    music_notes_effect()
    print()

    for i, line in enumerate(lyrics):
        if i in [0, 4, 8, 11, 15, 19, 23, 28, 32, 36]:
            try:
                print(Colors.BOLD + Colors.PURPLE + "\n┅┅┅┅┅┅┅┅┅┅ ♪ ┅┅┅┅┅┅┅┅┅┅\n" + Colors.END)
            except UnicodeEncodeError:
                print(Colors.BOLD + Colors.PURPLE + "\n---------- ♪ ----------\n" + Colors.END)
            time.sleep(0.7)

        if i in [11, 12, 13, 14, 19, 20, 21, 22, 32, 33, 34, 35]:
            type_text(line, 0.04, 0.08, verse_colors[i], bounce=True)
        elif i in [28, 29, 30, 31]:
            type_text("   " + line, 0.06, 0.12, verse_colors[i])
        elif i in [36, 37, 38, 39]:
            type_text(line, 0.07, 0.15, verse_colors[i])
        else:
            type_text(line, 0.04, 0.09, verse_colors[i])
        time.sleep(verse_delays[i])

    print("\n" + Colors.BOLD + Colors.PURPLE + "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅" + Colors.END)
    print(Colors.BOLD + Colors.GREEN + "🎧 Song Complete - Sanjoy 'Tu Talwiinder' 🎧" + Colors.END)
    
    print("\n" + Colors.LIGHTBLUE + "🎵 ", end="")
    for _ in range(3):
        notes = ["♪", "♫", "🎶"]
        for note in notes:
            try:
                sys.stdout.write(Colors.PURPLE + note + " " + Colors.END)
                sys.stdout.flush()
                time.sleep(0.3)
            except UnicodeEncodeError:
                sys.stdout.write(Colors.PURPLE + "*" + Colors.END)
    print(Colors.BOLD + Colors.LIGHTBLUE + "THE END" + Colors.END)
    print()

if __name__ == "__main__":
    try:
        play_lyrics()
    except KeyboardInterrupt:
        print("\n\n" + Colors.RED + "⏹️  Playback stopped by user" + Colors.END)
        sys.exit(0)

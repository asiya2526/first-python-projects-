import time
import os
import sys

# ASCII number representation for 0-9
DIGITS = {
    '0': ["███", "█ █", "███"],
    '1': ["  █", "  █", "  █"],
    '2': ["███", "  █", "███"],
    '3': ["███", " ██", "███"],
    '4': ["█ █", "███", "  █"],
    '5': ["███", "██ ", "███"],
    '6': ["███", "███", "███"],
    '7': ["███", "  █", "  █"],
    '8': ["███", "███", "███"],
    '9': ["███", "███", "  █"],
    ':': ["   ", " ░ ", "   "]
}

def render_clock():
    sys.stdout.write("\033[2J\033[H")  # Clear screen and move cursor home
    
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            
            # Build clock line by line
            lines = ["", "", ""]
            for char in current_time:
                digit_pattern = DIGITS.get(char, ["   ", "   ", "   "])
                for i in range(3):
                    lines[i] += digit_pattern[i] + "  "
            
            # Print the combined big-text time display
            sys.stdout.write("\033[H")  # Reset cursor position
            sys.stdout.write("\033[96m===========================\n")
            sys.stdout.write("    LIVE DIGITAL CLOCK     \n")
            sys.stdout.write("===========================\033[0m\n\n")
            
            for line in lines:
                sys.stdout.write(f"\033[93m  {line}\033[0m\n")
                
            sys.stdout.write("\n\033[90mPress Ctrl+C to exit...\033[0m\n")
            sys.stdout.flush()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    render_clock()
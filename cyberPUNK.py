import sys
import time
import random

def cyberpunk_typewriter(text, speed=0.04):
    print("\033[92m", end="")  # Set terminal text color to bright green
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Add slight random variation to typing speed for a realistic effect
        time.sleep(speed + random.uniform(-0.01, 0.02))
        
        # System bell sound trigger on spaces (optional mechanical touch)
        if char == " ":
            sys.stdout.write("\a")
            
    print("\033[0m")  # Reset terminal color

def main():
    message = """
=====================================================
[SYSTEM INITIALIZED]
Welcome to the Cyberpunk Terminal Interface!
Status: Connected
User: asiya
age: 100

        you are been hacked by asiya

                 i am virus! 
                      
=====================================================
    """
    cyberpunk_typewriter(message)

if __name__ == "__main__":
    main()
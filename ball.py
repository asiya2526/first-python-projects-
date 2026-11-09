import time
import sys

def run_bouncing_ball():
    width, height = 40, 15
    x, y = 5, 5
    dx, dy = 1, 1  # Direction vector (speed)

    sys.stdout.write("\033[2J\033[H")  # Clear terminal
    
    try:
        while True:
            # Build screen grid
            grid = [[" " for _ in range(width)] for _ in range(height)]
            
            # Move position
            x += dx
            y += dy
            
            # Bounce off vertical walls
            if x <= 0 or x >= width - 1:
                dx *= -1
            
            # Bounce off horizontal walls
            if y <= 0 or y >= height - 1:
                dy *= -1

            # Place ball
            grid[y][x] = "⚽"

            # Render frame
            output = []
            output.append("┌" + "─" * width + "┐")
            for row in grid:
                output.append("│" + "".join(row) + "│")
            output.append("└" + "─" * width + "┘")

            sys.stdout.write("\033[H" + "\n".join(output))
            sys.stdout.flush()
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    run_bouncing_ball()
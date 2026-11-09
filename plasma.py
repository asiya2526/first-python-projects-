import math
import os
import sys
import time

# Gradient character set from dark to bright
PALETTE = " .:-=+*#%@"


def clear_screen():
  # ANSI escape code to clear screen and reset cursor
  sys.stdout.write("\033[2J\033[H")


def run_plasma():
  width, height = 70, 30
  t = 0.0

  try:
    while True:
      output = []
      # Generate plasma frame using sine wave combinations
      for y in range(height):
        row = []
        for x in range(width):
          # Mathematical plasma formulas combining spatial and temporal coordinates
          v1 = math.sin(x * 0.1 + t)
          v2 = math.sin(y * 0.1 + t)
          v3 = math.sin((x + y) * 0.1 + t)
          v4 = math.sin(math.sqrt(x * x + y * y) * 0.1 + t)

          # Combine waves and normalize to palette index
          val = (v1 + v2 + v3 + v4 + 4) / 8.0
          index = int(val * (len(PALETTE) - 1))
          index = max(0, min(index, len(PALETTE) - 1))
          row.append(PALETTE[index] * 2)  # Double characters for square pixel aspect ratio

        output.append("".join(row))

      # Move cursor to top left instead of clearing full screen to prevent flicker
      sys.stdout.write("\033[H" + "\n".join(output))
      sys.stdout.write(
          "\n\033[92m[+] ASCII Plasma Wave Simulator | Press Ctrl+C to Exit\033[0m"
      )
      sys.stdout.flush()

      t += 0.15
      time.sleep(0.03)

  except KeyboardInterrupt:
    sys.stdout.write("\033[0m\nExiting...\n")


if __name__ == "__main__":
  clear_screen()
  run_plasma()
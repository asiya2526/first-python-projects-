import os
import random
import sys
import time

# Cross-platform non-blocking key input handling
if os.name == 'nt':
  import msvcrt

  def get_key():
    if msvcrt.kbhit():
      key = msvcrt.getch()
      if key in (b'\x00', b'\xe0'):  # Arrow keys prefix
        key = msvcrt.getch()
        return {b'H': 'UP', b'P': 'DOWN', b'K': 'LEFT', b'M': 'RIGHT'}.get(
            key, None
        )
      elif key == b'w':
        return 'UP'
      elif key == b's':
        return 'DOWN'
      elif key == b'a':
        return 'LEFT'
      elif key == b'd':
        return 'RIGHT'
      elif key == b'q':
        return 'QUIT'
    return None

else:
  import select
  import termios
  import tty

  def get_key():
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
      key = sys.stdin.read(1)
      if key == '\x1b':  # Arrow key sequence
        sys.stdin.read(1)  # skip '['
        k = sys.stdin.read(1)
        return {'A': 'UP', 'B': 'DOWN', 'D': 'LEFT', 'C': 'RIGHT'}.get(k, None)
      elif key == 'w':
        return 'UP'
      elif key == 's':
        return 'DOWN'
      elif key == 'a':
        return 'LEFT'
      elif key == 'd':
        return 'RIGHT'
      elif key == 'q':
        return 'QUIT'
    return None


def run_snake():
  width, height = 25, 15
  snake = [(5, 5), (4, 5), (3, 5)]
  direction = 'RIGHT'
  score = 0

  # Place initial food
  food = (random.randint(1, width - 2), random.randint(1, height - 2))

  # OS setup for raw input mode on Unix
  old_settings = None
  if os.name != 'nt':
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())

  # Hide cursor
  sys.stdout.write('\033[?25l')

  try:
    while True:
      # Check key input
      new_dir = get_key()
      if new_dir == 'QUIT':
        break
      elif new_dir == 'UP' and direction != 'DOWN':
        direction = 'UP'
      elif new_dir == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
      elif new_dir == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
      elif new_dir == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

      # Move Snake Head
      head_x, head_y = snake[0]
      if direction == 'UP':
        head_y -= 1
      elif direction == 'DOWN':
        head_y += 1
      elif direction == 'LEFT':
        head_x -= 1
      elif direction == 'RIGHT':
        head_x += 1

      new_head = (head_x, head_y)

      # Check collisions with walls
      if head_x <= 0 or head_x >= width - 1 or head_y <= 0 or head_y >= height - 1:
        break
      # Check self collision
      if new_head in snake:
        break

      snake.insert(0, new_head)

      # Check food collision
      if new_head == food:
        score += 10
        food = (random.randint(1, width - 2), random.randint(1, height - 2))
        while food in snake:
          food = (random.randint(1, width - 2), random.randint(1, height - 2))
      else:
        snake.pop()

      # Render Grid
      grid = [[' ' for _ in range(width)] for _ in range(height)]

      # Draw Walls
      for x in range(width):
        grid[0][x] = '█'
        grid[height - 1][x] = '█'
      for y in range(height):
        grid[y][0] = '█'
        grid[y][width - 1] = '█'

      # Draw Food
      grid[food[1]][food[0]] = '🍎'

      # Draw Snake
      for idx, (sx, sy) in enumerate(snake):
        if idx == 0:
          grid[sy][sx] = '🟢'
        else:
          grid[sy][sx] = '🟩'

      # Draw Frame to Terminal
      output = [
          '\033[H\033[92m🐍 CLI SNAKE GAME | Score: '
          + str(score)
          + ' \033[0m'
      ]
      for row in grid:
        output.append(''.join(row))
      output.append(
          '\033[90mControls: WASD or Arrow Keys | Q to Quit\033[0m'
      )

      sys.stdout.write('\n'.join(output))
      sys.stdout.flush()

      time.sleep(0.3)

  finally:
    # Restore terminal settings & show cursor
    sys.stdout.write('\033[?25h\033[0m\n')
    if old_settings:
      termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    print(f'\n💥 GAME OVER! Final Score: {score}')


if __name__ == '__main__':
  run_snake()
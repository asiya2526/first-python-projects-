import math
import os
import random
import sys
import time

# ANSI Color Codes
GREEN = "\033[92m"
BRIGHT_GREEN = "\033[1;92m"
DARK_GREEN = "\033[32m"
RESET = "\033[0m"


def clear_screen():
  sys.stdout.write("\033[2J\033[H")


def run_matrix_cube():
  width, height = 80, 24
  # Matrix rain drops initialization
  drops = [random.randint(-20, 0) for _ in range(width)]

  # 3D Cube Vertices (X, Y, Z)
  vertices = [
      (-1, -1, -1),
      (1, -1, -1),
      (1, 1, -1),
      (-1, 1, -1),
      (-1, -1, 1),
      (1, -1, 1),
      (1, 1, 1),
      (-1, 1, 1),
  ]

  # Cube Edges connecting the vertices
  edges = [
      (0, 1),
      (1, 2),
      (2, 3),
      (3, 0),  # Back face
      (4, 5),
      (5, 6),
      (6, 7),
      (7, 4),  # Front face
      (0, 4),
      (1, 5),
      (2, 6),
      (3, 7),  # Connecting edges
  ]

  angle_x = 0
  angle_y = 0
  angle_z = 0

  clear_screen()

  try:
    while True:
      # 1. Build background matrix rain grid
      screen = [[" " for _ in range(width)] for _ in range(height)]
      for i in range(width):
        drop_row = drops[i]
        for r in range(height):
          if drop_row <= r < drop_row + 8:
            char = chr(random.randint(33, 126))
            screen[r][i] = (
                BRIGHT_GREEN if r == drop_row + 7 else DARK_GREEN
            ) + char
          else:
            if screen[r][i] == " ":
              screen[r][i] = " "
        drops[i] += 1
        if drops[i] > height:
          drops[i] = random.randint(-25, 0)

      # 2. Rotate and Project 3D Cube Vertices to 2D Screen
      projected_points = []
      for vertex in vertices:
        x, y, z = vertex

        # Rotate around X axis
        rad = angle_x
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        y, z = y * cos_a - z * sin_a, y * sin_a + z * cos_a

        # Rotate around Y axis
        rad = angle_y
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        x, z = x * cos_a + z * sin_a, -x * sin_a + z * cos_a

        # Rotate around Z axis
        rad = angle_z
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        x, y = x * cos_a - y * sin_a, x * sin_a + y * cos_a

        # Perspective projection distance scaling
        distance = 3.5
        z += distance
        proj_scale = 14 / z
        proj_x = int(width / 2 + x * proj_scale * 2)  # 2x scale for aspect ratio
        proj_y = int(height / 2 + y * proj_scale)
        projected_points.append((proj_x, proj_y))

      # 3. Draw Edges onto the Screen Grid using Bresenham's line algorithm concept
      for edge in edges:
        p1 = projected_points[edge[0]]
        p2 = projected_points[edge[1]]

        # Simple line drawing interpolation
        steps = max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
        if steps == 0:
          continue
        for s in range(steps + 1):
          t = s / steps
          lx = int(p1[0] + (p2[0] - p1[0]) * t)
          ly = int(p1[1] + (p2[1] - p1[1]) * t)
          if 0 <= lx < width and 0 <= ly < height:
            screen[ly][lx] = f"{GREEN}█{RESET}"

      # 4. Render Frame to Terminal
      output = []
      for row in screen:
        output.append("".join(row))

      sys.stdout.write(
          "\033[H"
          + "\n".join(output)
          + f"\n{BRIGHT_GREEN} 🌌 3D MATRIX CUBE SIMULATOR | Press Ctrl+C to Exit {RESET}"
      )
      sys.stdout.flush()

      # Increment rotation angles
      angle_x += 0.03
      angle_y += 0.04
      angle_z += 0.015
      time.sleep(0.03)

  except KeyboardInterrupt:
    sys.stdout.write(RESET + "\nExiting simulation...\n")


if __name__ == "__main__":
  run_matrix_cube()
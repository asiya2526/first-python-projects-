import sys
import time

def generate_mandelbrot():
    # Terminal screen dimensions
    width, height = 80, 40
    
    # Mathematical boundaries of the complex plane
    xmin, xmax = -2.0, 0.5
    ymin, ymax = -1.25, 1.25
    
    # Shading characters from light (background) to dense (deep inside fractal)
    palette = " .:-=+*#%@"
    max_iter = 60

    sys.stdout.write("\033[2J\033[H")  # Clear screen
    sys.stdout.write("\033[96m[+] Rendering Mandelbrot Fractal using Complex Math...\033[0m\n\n")
    
    output = []
    
    # Loop through every row and column of the terminal grid
    for h in range(height):
        row = []
        zy = ymin + (h / height) * (ymax - ymin)
        
        for w in range(width):
            zx = xmin + (w / width) * (xmax - xmin)
            
            # Complex number c = zx + i*zy
            c = complex(zx, zy)
            z = complex(0, 0)
            iteration = 0
            
            # The Mandelbrot iteration loop: z = z^2 + c
            while abs(z) < 2.0 and iteration < max_iter:
                z = z*z + c
                iteration += 1
                
            # Map iteration count to palette character
            if iteration == max_iter:
                char = "@"  # Inside the set (solid core)
            else:
                char = palette[iteration % len(palette)]
                
            row.append(char * 2)  # Double characters to fix terminal font aspect ratio
            
        output.append("".join(row))
        
    # Print the final generated fractal art
    sys.stdout.write("\n".join(output))
    sys.stdout.write("\n\033[92m[✓] Render Complete! Pure mathematical infinity in your terminal.\033[0m\n")

if __name__ == "__main__":
    generate_mandelbrot()
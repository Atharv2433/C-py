import sys
import pymesh
import numpy as np

def double_array(arr):
    """Double the values in the array."""
    return [x * 2 for x in arr]

def create_cube(size):
    """Create a cube mesh with the given size."""
    # Vertices for a cube centered at the origin
    half_size = size / 2
    vertices = np.array([
        [-half_size, -half_size, -half_size],
        [half_size, -half_size, -half_size],
        [half_size, half_size, -half_size],
        [-half_size, half_size, -half_size],
        [-half_size, -half_size, half_size],
        [half_size, -half_size, half_size],
        [half_size, half_size, half_size],
        [-half_size, half_size, half_size],
    ])
    
    
    faces = np.array([
        [0, 1, 2], [0, 2, 3],  # Bottom
        [4, 5, 6], [4, 6, 7],  # Top
        [0, 1, 5], [0, 5, 4],  # Front
        [1, 2, 6], [1, 6, 5],  # Right
        [2, 3, 7], [2, 7, 6],  # Back
        [3, 0, 4], [3, 4, 7],  # Left
    ])
    
    cube_mesh = pymesh.formats.Mesh(vertex=vertices, faces=faces)
    return cube_mesh

if __name__ == "__main__":
    try:
        input_numbers = list(map(int, sys.argv[1:]))
        doubled_numbers = double_array(input_numbers)
        
        if len(doubled_numbers) > 0:
            size = doubled_numbers[0]
            print(f"Using doubled value {size} to create a cube shape.")

            cube_mesh = create_cube(size)
            cube_mesh.export("output_cube.obj")  

            print("Cube mesh created and saved as output_cube.obj.")
        else:
            print("Error: No valid input provided.", file=sys.stderr)

    except ValueError:
        print("Error: Invalid input. Please provide integers.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

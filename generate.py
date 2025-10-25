import pyrosim.pyrosim as pyrosim

# Base block size
base_length = 1.0
base_width  = 1.0
base_height = 1.0

# Tower/grid configuration
num_rows   = 5
num_cols   = 5
num_levels = 10
shrink     = 0.9

# Spacing between tower centers to prevent overlap
spacing_x = base_length * 1.25
spacing_y = base_width  * 1.25

pyrosim.Start_SDF("boxes.sdf")

for r in range(num_rows):
    for c in range(num_cols):
        cumulative_height = 0.0
        for l in range(num_levels):
            # Size shrinks by 10% each level
            length = base_length * (shrink ** l)
            width  = base_width  * (shrink ** l)
            height = base_height * (shrink ** l)

            # Centered above the previous block: z is half the current height above the stack
            # center the grid around the origin
            x = (c - (num_cols - 1)/2.0) * spacing_x
            y = (r - (num_rows - 1)/2.0) * spacing_y
            z = cumulative_height + (height / 2.0)

            name = f"Box_r{r}_c{c}_l{l}"
            pyrosim.Send_Cube(name=name, pos=[x, y, z], size=[length, width, height])

            # Increase stack height by the full height of the placed block
            cumulative_height += height

pyrosim.End()

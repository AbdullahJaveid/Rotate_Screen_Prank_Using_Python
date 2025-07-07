import rotatescreen
import time

# Get the primary display
screen = rotatescreen.get_primary_display()

# Rotate screen to 90 degrees
screen.rotate_to(90) # type: ignore
time.sleep(2)

# Rotate screen to 180 degrees
screen.rotate_to(180) # type: ignore
time.sleep(2)

# Rotate screen to 270 degrees
screen.rotate_to(270) # type: ignore
time.sleep(2)

# Rotate screen back to normal (0 degrees)
screen.rotate_to(0) # type: ignore

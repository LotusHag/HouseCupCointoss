from functions import team_assigner
from functions import run_tester
# Fill in the amounts for Lapis and Gold
Lapis = 38
Gold = 33

# Function that tells you who the next member should go to
team_assigner(Lapis,Gold)

# Function that showcases team_assigner actually skewing the numbers randomly and correctly
# The first number is the amount of runs you want it to do.
run_tester(10000, Lapis, Gold)
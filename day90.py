# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = int(input())
bc = int(input())

angle_deg = math.degrees(math.atan(ab / bc))

print(str(int(round(angle_deg))) + chr(176))

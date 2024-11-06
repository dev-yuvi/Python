from Weight.util import lbs_to_kg
from Weight.util import kg_to_lbs

try:
    weight=int(input())
    print(f"kg to lbs: {kg_to_lbs(weight)}")
    print(f"lbs to kg: {lbs_to_kg(weight)}")

except ValueError:
    print("To Give Numbers onely")

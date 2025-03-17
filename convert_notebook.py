import os

os.system("jupyter nbconvert --to html damageCalculation.ipynb --output damageCalculation_inclCode")
os.system("jupyter nbconvert --to html --no-input damageCalculation.ipynb --output damageCalculation_exclCode")
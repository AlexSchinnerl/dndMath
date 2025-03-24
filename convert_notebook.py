import os

os.system("jupyter nbconvert --to html damageCalculation.ipynb --output-dir='./output' --output damageCalculation_inclCode")
os.system("jupyter nbconvert --to html --no-input damageCalculation.ipynb --output-dir='./output' --output damageCalculation_exclCode")
os.system("jupyter nbconvert --to html --no-input damageCalculation.ipynb --output-dir='./output' --output index")
from spire.presentation.common import *
from spire.presentation import *
import os
import sys

print("PPT to JPG...")

ppt_name = ""

if (len(sys.argv) > 1):
    ppt_name = "".join(sys.argv[1:])
else:
    print("No file name input")
    os._exit(1)
 
print("Current working directory...")   
print(os.getcwd())

presentation = Presentation()

presentation.LoadFromFile(ppt_name)

for i, slide in enumerate(presentation.Slides):
    jpg_name = f"JPG_{ppt_name}_{str(i)}.png"
    image = slide.SaveAsImage()
    image.Save(jpg_name)
    image.Dispose()
    
presentation.Dispose()
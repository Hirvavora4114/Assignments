from rembg import remove
from PIL import Image
input_path='003_100_4.jpg'
output_path='003_100_4.png'
inp=Image.open(input_path)
output=remove(inp)
output.save(output_path)
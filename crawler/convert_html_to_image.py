from html2image import Html2Image
from PIL import Image

# 创建Html2Image对象
hti = Html2Image()

# 设置输出图片的宽度和高度
image_width = 800
image_height = 1800
html_file_path = ''
output_filename = 'ok20250324.png'

try:
    hti.screenshot(
        html_file=html_file_path,
        save_as=output_filename,
        # size=(image_width, image_height)  # 设置宽度为1080，高度为3000
    )
    print(f"Generated: {output_filename}")  
    # 打印生成的图片尺寸以调试
    img = Image.open(output_filename)
    print(f"Image size: {img.size}")
except Exception as e:
    print(f"Error generating {output_filename}: {e}")  
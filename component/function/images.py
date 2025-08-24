import base64
import io
from PIL import Image


def load_img_html(path):
    image_io = io.BytesIO()
    try:
        Image.open(path).save(image_io, format="PNG")
        image_io.seek(0)
    except FileNotFoundError:
        pass
    
    
    return f"""
    <div style="display:flex; justify-content: center; ">
        <img class="item-image" src="data:image/png;base64, {base64.b64encode(image_io.read()).decode('utf-8')}">
    </div>"""
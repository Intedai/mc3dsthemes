import math
import anvil
from PIL import Image

def block_to_chunk_coords(bx, by, bz):
    return tuple(map(lambda i: math.floor(i / 16), (bx, by, bz)))

def coords_inside_chunk(bx, by, bz):
    return tuple(map(lambda i: (i % 16 + 16) % 16, (bx, by, bz)))

def chunk_to_region_coords(cx, cz):
    return tuple(map(lambda i: math.floor(i / 32), (cx, cz)))

# Copy of get_top_block_img that was changed a bit, will modify these 2 funcs so they will be efficient and also avoid D.R.Y
def get_block_img(overworld_path, bx, by, bz):
    chunk_pos = block_to_chunk_coords(bx, 0, bz)
    region_pos = chunk_to_region_coords(*(chunk_pos[::2]))
    cic = coords_inside_chunk(bx, 0, bz)

    region_file_name = f'{overworld_path}/r.{region_pos[0]}.{region_pos[1]}.mca'

    region = anvil.Region.from_file(region_file_name)
    chunk = anvil.Chunk.from_region(region, chunk_pos[0], chunk_pos[2])

    block = block = chunk.get_block(cic[0], by, cic[2])

    if block.id != "air":
        try:
            return Image.open(f"block/{block.id}.png")
        except FileNotFoundError:
            print(f"Couldn't find the texture \"{block.id}\". Continuing to the next block.")
        except Exception as e:
                print("Exception: {e}. Continuing to next block.")

    return None

def get_top_block_img(overworld_path, bx, bz):
    chunk_pos = block_to_chunk_coords(bx, 0, bz)
    region_pos = chunk_to_region_coords(*(chunk_pos[::2]))
    cic = coords_inside_chunk(bx, 0, bz)

    region_file_name = f'{overworld_path}/r.{region_pos[0]}.{region_pos[1]}.mca'

    region = anvil.Region.from_file(region_file_name)
    chunk = anvil.Chunk.from_region(region, chunk_pos[0], chunk_pos[2])

    for y in range(319, -64 - 1, -1):
        block = block = chunk.get_block(cic[0], y, cic[2])
        if block.id != "air":
            try:
                return Image.open(f"block/{block.id}.png")
            except FileNotFoundError:
                print(f"Couldn't find the texture \"{block.id}\". Continuing to the next block.")
            except Exception as e:
                print("Exception: {e}. Continuing to next block.")
    return None

def render_rectangle_img(overworld_path, start_pos, end_pos):
    width = (abs(start_pos[0] - end_pos[0]) + 1) * 16
    height = (abs(start_pos[1] - end_pos[1]) + 1)* 16

    final = Image.new("RGB", (width, height))
    for row, x in enumerate(range(start_pos[0], end_pos[0] - 1, -1)):
        for col, z in enumerate(range(start_pos[1], end_pos[1] - 1, -1)):
            img = get_top_block_img(overworld_path, x, z)
            if img:
                final.paste(img, (row * 16, col * 16))
    return final

def average_block_color(block_id):
    img = Image.open(f"block/{block_id}.png").convert("RGB")
    width, height = img.size
    data = img.load()
    
    rgb_sum = [0, 0, 0]
    
    for r in range(width):
        for c in range(height):
            for i in range(len(rgb_sum)):
                rgb_sum[i] += data[r, c][i]

    img_size = width * height

    average_color = tuple(value // img_size for value in rgb_sum)

    return average_color
import png
#4 pixels per byte
#256 pixels per tile
#16 pixels per row

RESULT_WIDTH = 1024
TILE_H = 16
TILE_H_BYTES = 4

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def byte_to_pixels(b):
    p4 = (b >> 6) & 0x3
    p3 = (b >> 4) & 0x3
    p2 = (b >> 2) & 0x3
    p1 = b & 0x3
    return [p1, p2, p3, p4]

with open('pspfont.dat', 'rb') as f:
    f.seek(0xEEE8)
    bitmap = f.read()

WIDTH = len(bitmap) // TILE_H_BYTES
bitmap_new = bytearray(WIDTH * TILE_H)
#Loop over each column of pixels
for x_pos, column in enumerate(chunks(bitmap, TILE_H_BYTES)):
    #Convert bytes to pixels
    pixels = []
    for b in column:
        pixels += byte_to_pixels(b)
    #Insert pixels into bitmap
    for h, pixel in zip(range(TILE_H), pixels):
        bitmap_new[x_pos + h * WIDTH] = pixel
#Write an image 16 pixels tall, very wide (>30,000 pixels)
writer = png.Writer(width = WIDTH, height = 16, bitdepth = 2,
                    greyscale = True)
with open('output1.png', 'wb') as f:
    writer.write(f, chunks(list(bitmap_new), WIDTH))

#Compute number of "tile rows"
if WIDTH % RESULT_WIDTH == 0:
    rows = WIDTH // RESULT_WIDTH
else:
    rows = (WIDTH // RESULT_WIDTH) + 1
#Remap to more square bitmap
bitmap_new2 = bytearray(RESULT_WIDTH * rows * TILE_H)
for row in range(rows):
    for h in range(TILE_H):
        #base = position in bitmap_new2
        base = row * RESULT_WIDTH * TILE_H + h * RESULT_WIDTH
        #base2 = position in bitmap_new
        base2 = row * RESULT_WIDTH + h * WIDTH

        #Last tile row
        if (row + 1) * RESULT_WIDTH > WIDTH:
            end = WIDTH - row * RESULT_WIDTH
            bitmap_new2[base:base + end] = \
                bitmap_new[base2:base2 + end]
        #All other tile rows
        else:
            bitmap_new2[base:base + RESULT_WIDTH] = \
                bitmap_new[base2:base2 + RESULT_WIDTH]

#Write the more square image
writer = png.Writer(width = RESULT_WIDTH, height = rows * 16, bitdepth = 2,
                    greyscale = True)
with open('output2.png', 'wb') as f:
    writer.write(f, chunks(list(bitmap_new2), RESULT_WIDTH))
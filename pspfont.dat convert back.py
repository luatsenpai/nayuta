import struct
import png

def unpack_bmp_pixel(b):
    p1 = b & 0xF
    p2 = b >> 4
    return [p2, p1]

def pack_pspfont_pixels(a, b, c, d):
    return (d << 6) + (c << 4) + (b << 2) + a

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

WIDTH = 0x24DB8
REAL_WIDTH = 0x24DB1
width_bytes = WIDTH // 2
#Real width = 0x24DB1
HEIGHT = 0x10
with open('pspfont.bmp', 'rb') as f:
    f.seek(0x8A)
    filedata = f.read()
bitmap = bytearray(len(filedata) * 2)
for row_bmp, row_png in zip(range(HEIGHT), reversed(range(HEIGHT))):
    row_bmp_data = filedata[row_bmp * width_bytes:(row_bmp + 1) * width_bytes]
    l = []
    for b in row_bmp_data:
        l += unpack_bmp_pixel(b)
    bitmap[row_png * WIDTH:(row_png + 1) * WIDTH] = l
bitmap_new = bytearray(REAL_WIDTH * HEIGHT)
for row in range(HEIGHT):
    bitmap_new[row * REAL_WIDTH:(row + 1)* REAL_WIDTH] = \
        bitmap[row * WIDTH:row * WIDTH + REAL_WIDTH]

##writer = png.Writer(width = REAL_WIDTH, height = HEIGHT, greyscale = True,
##                    bitdepth = 2)
##with open('test.png', 'wb') as f:
##    writer.write(f, chunks(bitmap_new, REAL_WIDTH))
pspfont_data = bytearray()
for col in range(REAL_WIDTH):
    l = []
    for row in range(HEIGHT):
        l.append(bitmap_new[col + REAL_WIDTH * row])
    for a, b, c, d in chunks(l, 4):
        pspfont_data.append(pack_pspfont_pixels(a, b, c, d))
        
with open('pspfont.orig', 'rb') as f:
    filedata = bytearray(f.read(0xEEE8))
header_update_data = (
    (15193, 150616, 6),
    (15194, 150624, 6),
    (15195, 150632, 6),
    (15196, 150640, 6),
    (15197, 150648, 5),
    (15198, 150656, 6),
    (15199, 150664, 6),
    (15200, 150672, 6),
    (15201, 150680, 6))
for index, x_pos, width in header_update_data:
    num = struct.pack('<I', (width << 24) + x_pos)
    filedata[0xC4 + 4 * index:0xC4 + 4 * index + 4] = num
with open('pspfont.dat', 'wb') as f:
    f.write(filedata)
    f.write(pspfont_data)
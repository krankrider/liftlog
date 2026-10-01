"""Regenerate icon-180.png and icon-512.png. Standard library only.

    python3 tools/make_icons.py   (run from the repo root)

White barbell on the app's blue (#1f4e79). iOS rounds the corners itself.
"""
import struct
import zlib

BLUE, WHITE = (0x1F, 0x4E, 0x79), (255, 255, 255)


def png(n, rows):
    raw = b"".join(b"\x00" + bytes(v for p in row for v in p) for row in rows)

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", n, n, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9))
            + chunk(b"IEND", b""))


def barbell(cx, cy):
    if 0.10 <= cx <= 0.90 and abs(cy - 0.5) <= 0.04:
        return True
    for x0, half_h in ((0.17, 0.16), (0.27, 0.22), (0.65, 0.22), (0.75, 0.16)):
        if x0 <= cx <= x0 + 0.08 and abs(cy - 0.5) <= half_h:
            return True
    return False


for n in (180, 512):
    rows = [[WHITE if barbell((x + .5) / n, (y + .5) / n) else BLUE for x in range(n)] for y in range(n)]
    with open(f"icon-{n}.png", "wb") as f:
        f.write(png(n, rows))
    print(f"icon-{n}.png")

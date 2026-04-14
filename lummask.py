from PIL import Image
import sys

if len(sys.argv) != 4:
    print(f"usage: {sys.argv[0]} image1 image2 output")
    sys.exit(1)

img1 = Image.open(sys.argv[1]).convert("RGB")
img2 = Image.open(sys.argv[2]).convert("RGB")

# resize larger to smaller
if img1.size[0] * img1.size[1] > img2.size[0] * img2.size[1]:
    img1 = img1.resize(img2.size)
else:
    img2 = img2.resize(img1.size)

px1 = img1.load()
px2 = img2.load()
w, h = img1.size

out = Image.new("L", (w, h))
pxo = out.load()

for y in range(h):
    for x in range(w):
        r1, g1, b1 = px1[x, y]
        r2, g2, b2 = px2[x, y]
        lum1 = 0.299 * r1 + 0.587 * g1 + 0.114 * b1
        lum2 = 0.299 * r2 + 0.587 * g2 + 0.114 * b2
        pxo[x, y] = min(int(abs(lum1 - lum2)), 255)

out.save(sys.argv[3])
print(f"{w}x{h}, saved to {sys.argv[3]}")
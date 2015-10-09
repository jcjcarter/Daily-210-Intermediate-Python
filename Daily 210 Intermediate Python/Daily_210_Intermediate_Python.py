from PIL import Image

W, H = map(int, input().split())
r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())

interpolate = lambda c1, c2, x: c1 + int((c2-c1)*(x/W))

img = Image.new("RGB", (W, 1))

data = img.load()

for x in range(W):
    data[x,0] = (interpolate(r1, r2, x), interpolate(g1, g2, x), interpolate(b1, b2,x))

img = img.resize((W,H))
img.show()
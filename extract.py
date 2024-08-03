import gimpFormats
import sys

g = gimpFormats.GimpDocument(sys.argv[1])
for layer in g.layers:
	print(f"{layer.name}.png")
	layer.image.save(f"fishes/{layer.name}.png")
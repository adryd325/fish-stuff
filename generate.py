#!/usr/bin/env python3

import os
from PIL import Image
import random

backgroundsNormalPath = "./bgs/normal"
backgroundsWeirdPath = "./bgs/weird"
bodiesPath = "./fishes/body"
headsPath = "./fishes/head"
tailsPath = "./fishes/tail"

skeletonPath = "./fish_skeleton.png"
skeleton = Image.open(skeletonPath)

backgroundsNormal = os.listdir(backgroundsNormalPath)
backgroundsWeird = os.listdir(backgroundsWeirdPath)
bodies = os.listdir(bodiesPath)
heads = os.listdir(headsPath)
tails = os.listdir(tailsPath)

def generate():
    backgroundPath = os.path.join(backgroundsNormalPath, random.choice(backgroundsNormal))
    if (random.random() < 0.05):
        backgroundPath = os.path.join(backgroundsWeirdPath, random.choice(backgroundsWeird))

    bodyPath = os.path.join(bodiesPath, random.choice(bodies))
    headPath = os.path.join(headsPath, random.choice(heads))
    tailPath = os.path.join(tailsPath,random.choice(tails))

    final = Image.new("RGBA", (500, 500))

    body = Image.open(bodyPath)
    head = Image.open(headPath)
    tail = Image.open(tailPath)

    final.paste(Image.open(backgroundPath))
    final.paste(skeleton, (0,0), skeleton)
    final.paste(body, (0,0), body)
    final.paste(head, (0,0), head)
    final.paste(tail, (0,0), tail)

    final.save("./out.png", "PNG")

generate()

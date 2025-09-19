import sys
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansPro
from font_intuitive import Intuitive
import requests

print("Lade Daten für Pommes...")

url = "https://raw.githubusercontent.com/LuisErhardt/gibt-es-heute-pommes/refs/heads/master/public/result.txt"
response = requests.get(url)

if response.status_code == 200:
    inhalt = response.text
    print(inhalt)
else:
    print("Fehler beim Laden:", response.status_code)
    sys.exit(1)

print("Schreibe Text auf Display...")

font_small = ImageFont.truetype(SourceSansPro, 44)
font_big = ImageFont.truetype(SourceSansPro, 72)
intuitive_font = ImageFont.truetype(Intuitive, int(72))


def getsize(font, text):
    _, _, right, bottom = font.getbbox(text)
    return (right, bottom)


inky_display = auto()

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

y_top = int(inky_display.height * (5.0 / 10.0))
y_bottom = y_top + int(inky_display.height * (4.0 / 10.0))

for y in range(0, y_top):
    for x in range(0, inky_display.width):
        img.putpixel(
            (x, y),
            inky_display.BLACK if inky_display.colour == "black" else inky_display.RED,
        )

for y in range(y_top, y_bottom):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.WHITE)

for y in range(y_bottom, inky_display.height):
    for x in range(0, inky_display.width):
        img.putpixel(
            (x, y),
            inky_display.BLACK if inky_display.colour == "black" else inky_display.RED,
        )

question_top = "Gibt es heute"
w, h = getsize(font_small, question_top)
x = int((inky_display.width - w) / 2)
y_question = 20
draw.text((x, y_question), question_top, inky_display.WHITE, font_small)

question_bottom = "Pommes?"
w, h = getsize(font_small, question_bottom)
x = int((inky_display.width - w) / 2)
y_question = y_question + 50
draw.text((x, y_question), question_bottom, inky_display.WHITE, font_small)

answer = inhalt
w, h = getsize(intuitive_font, answer)
x = (inky_display.WIDTH - w) / 2
y_answer = int(y_top + ((y_bottom - y_top - h) / 2))
draw.text((x, y_answer), answer, inky_display.BLACK, intuitive_font)

inky_display.set_image(img)
inky_display.show()

print("Fertig!")

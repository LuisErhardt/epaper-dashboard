import sys
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansPro
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

font_small = ImageFont.truetype(SourceSansPro, 36)
font_big = ImageFont.truetype(SourceSansPro, 72)


def getsize(font, text):
    _, _, right, bottom = font.getbbox(text)
    return (right, bottom)


inky_display = auto()

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

draw.rectangle((0, 0, inky_display.WIDTH, inky_display.HEIGHT), fill=inky_display.WHITE)

question = "Gibt es heute Pommes?"
w, h = getsize(font_small, question)
x = (inky_display.WIDTH - w) // 2
y_question = 30
draw.text((x, y_question), question, inky_display.BLACK, font_small)

answer = inhalt
w, h = getsize(font_big, answer)
x = (inky_display.WIDTH - w) // 2
y_answer = y_question + 2 * h
draw.text((x, y_answer), answer, inky_display.BLACK, font_big)

inky_display.set_image(img)
inky_display.show()

print("Fertig!")

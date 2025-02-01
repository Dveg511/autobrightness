import json
import screen_brightness_control as sbc

with open("arparametr", "r", encoding="utf-8") as arparametr:
    gigi = json.load(arparametr)
bright = gigi["bright"]

sbc.set_brightness(bright)
print(f"succes changed to: {bright}")

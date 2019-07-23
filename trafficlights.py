from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25,8,7)
buzzer = Buzzer(15)

while True:
    button.wait_for_press()
    lights.green.on()
    sleep(3)
    lights.green.off()
    lights.amber.on()
    buzzer.on()
    sleep(1.5)
    lights.amber.off()
    buzzer.off()
    lights.red.on()
    sleep(3)
    lights.off()

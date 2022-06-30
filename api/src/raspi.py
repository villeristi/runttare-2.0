from os import getenv
import asyncio
from pydantic import BaseModel
from loguru import logger
import RPi.GPIO as GPIO

PISTON_PIN = int(getenv('RUNTTA_PISTON_PIN', 17))
STATUS_PIN = int(getenv('RUNTTA_STATUS_PIN', 27))
TIMEOUT = int(getenv('RUNTTA_TIMEOUT', 3))

class Raspi(BaseModel):
    piston_pin: int
    status_pin: int

    def init(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.piston_pin, GPIO.OUT)
        GPIO.setup(self.status_pin, GPIO.OUT)

        return self

    async def trigger(self):
        logger.debug("Triggering")
        GPIO.output(self.piston_pint, GPIO.HIGH)
        await asyncio.sleep(TIMEOUT)
        GPIO.output(self.piston_pint, GPIO.LOW)


raspi = Raspi(piston_pin=PISTON_PIN, status_pin=STATUS_PIN).init()

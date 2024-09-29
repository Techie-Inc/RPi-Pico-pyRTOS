#Basic blink example with 3 tasks

import pyRTOS
from machine import Pin

def blink_task(self):
    led = Pin('LED', Pin.OUT)
    while True:
        print('Toggling LED')
        led.value(not led.value())
        yield [pyRTOS.timeout_ms(500)]

def print_task_ms(self):
    while True:
        print('Running Task 2')
        yield [pyRTOS.timeout(1)]
        
def print_task_us(self):
    while True:
        print('Running Task 3')
        yield [pyRTOS.timeout_us(2000000)]

pyRTOS.add_task(pyRTOS.Task(blink_task, name="task1"))
pyRTOS.add_task(pyRTOS.Task(print_task_ms, name="task2"))
pyRTOS.add_task(pyRTOS.Task(print_task_us, name="task3"))

pyRTOS.start()

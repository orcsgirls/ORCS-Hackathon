from gpiozero import Servo
from aiy.pins import PIN_A
from aiy.pins import PIN_B

import time

import ipywidgets.widgets as widgets
import time
from aiy.vision.streaming.server import StreamingServer
from picamera import PiCamera
from IPython.display import display, HTML, IFrame

# Starting streaming camera
camera = PiCamera(sensor_mode=4, resolution=(410, 308))
server = StreamingServer(camera, bitrate=75000)

# Create robot class
class Robot():
    def __init__(self, pin_steer=PIN_A, pin_wheel=PIN_B):
        self.motor_steer = Servo(pin_steer)
        self.motor_wheel = Servo(pin_wheel)
    
    def forward(self, speed=1):
        self.motor_steer.value = 0
        self.motor_wheel.value = speed
        
    def backward(self, speed=1):
        self.motor_steer.value = 0
        self.motor_wheel.value = -speed
        
    def stop(self):
        self.motor_steer.value = 0
        self.motor_wheel.value = 0
    
    def turnleft(self):
        self.motor_steer.value = 0.5
        self.motor_wheel.value = 0.1
        
    def turnright(self):
        self.motor_steer.value = -0.5
        self.motor_wheel.value = 0.1
     
 # make the bot
robot = Robot()

# create video
# create video
video = widgets.HTML(value="<iframe src='http://orcspi-vis.local:4664' width=450 height=380>")
display(video)

# create buttons
button_layout = widgets.Layout(width='100px', height='80px', align_self='center')
stop_button = widgets.Button(description='stop', button_style='danger', layout=button_layout)
forward_button = widgets.Button(description='forward', layout=button_layout)
backward_button = widgets.Button(description='backward', layout=button_layout)
left_button = widgets.Button(description='left', layout=button_layout)
right_button = widgets.Button(description='right', layout=button_layout)
creep_button = widgets.Button(description='creep', layout=button_layout)

# display buttons
middle_box = widgets.HBox([left_button, stop_button, right_button], layout=widgets.Layout(align_self='center'))
controls_box = widgets.VBox([forward_button, middle_box, backward_button, creep_button])
display(controls_box)

def stop(change):
    robot.stop()
    
def step_forward(change):
    robot.forward(1)
    
def step_backward(change):
    robot.backward(0.5)

def step_left(change):
    robot.turnleft()
    
def step_right(change):
    robot.turnright()
    
def creep(change):
    robot.forward(0.1)

# link buttons to actions
stop_button.on_click(stop)
forward_button.on_click(step_forward)
backward_button.on_click(step_backward)
left_button.on_click(step_left)
right_button.on_click(step_right)
creep_button.on_click(creep)

# RPi-WiFi-RC-Car
I repurposed a remote control (RC) car to deploy TensorFlow Lite so that it can follow another vehicle via computer vision. This project is that other vehicle.

To that end, I transformed an off-road RC car chassis so that it could be controlled remotely over SSH by a Raspberry Pi 2. The initial python script was adpated from https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/ for the sake of time, but then modified and refactored to meet the needs of this project.

The RC car has two motors: one for steering, and one for driving. Thus, keyboard commands on the client computer must be able to control the forward/backward and left/right rotations for motor_1 and motor_2 respectively.

Using the arrow-key keypad to the right of most keyboards for intuition's sake, the keys used are as follows:

'4' for left.

'5' for straight.

'6' for right.

'8' for forward.

'2' for backward.

'e' to exit the script and clean up the GPIO pins.

And any other key to stop the drive motors.


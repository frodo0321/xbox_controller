# xbox_controller
A python module for reading data from an xbox controller

<h6>Class Variables:</h6>
<b>Left Analog Stick</b></br>
XBoxController.LAnalogX</br>
XBoxController.LAnalogY</br>
XBoxController.LStick</br>
<b>Right Analog Stick</b></br>
XBoxController.RAnalogX</br>
XBoxController.RAnalogY</br>
XBoxController.RStick</br>
<b>Triggers</b></br>
XBoxController.LT</br>
XBoxController.RT</br>
<b>Bumpers</b></br>
XBoxController.LB</br>
XBoxController.RB</br>
<b>Right Thumb Buttons</b></br>
XBoxController.A</br>
XBoxController.B</br>
XBoxController.X</br>
XBoxController.Y</br>
<b>DPad</b></br>
XBoxController.DUp</br>
XBoxController.DDown</br>
XBoxController.DRight</br>
XBoxController.DLeft</br>
<b>Middle Buttons</b></br>
XBoxController.Guide</br>
XBoxController.Back</br>
XBoxController.Start</br>
</br>


<h6>Usage:</h6>

1. Create an XBoxController object</br>
  c=XBoxController()</br>
  
2. Call XBoxController.update() to refresh buffer:</br>
  c.update()</br>

3. Read from class variables to view input state:</br>
  print c.A</br>

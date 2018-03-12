# OSE Piping library #
This project contains FreeCAD macros to create various pipe, tee, and elbow fittings.
It is made for [Open Source Ecology](http://opensourceecology.org). The project is a very early experemental state.
# Project is discontinued
This project is discontinued. The macros are moved to OSE-piping-workbench.

## Installation ##
Linux:

1. Copy the all files from **macro**  directory to **./FreeCAD** in your home directory.
2. (Optional) Customize **90-deg-elbow.csv**.

## Usage ##

1. Open or create a FreeCAD document.
2. Select **Macro**->**Macros Menu**.
3. Select **create-pipe.FCMacro**, **create-elbow-90.FCMacro** or **create-tee.FCMacro** and click **Execute**.

## Example ##
### 90°-elbow ###
![90°-elbow dialog](doc/pvc-elbow-90-gui-screenshot.png)

creates

![90°-elbow CAD screenshot](doc/pvc-elbow-90-cad-screenshot.png)

### alpha°-Elbow ###
Create an arbitrary elbow with the angle alpha within the range of 0°-180°.

![alpha°-elbow dialog](doc/pvc-elbow-alpha-gui-screenshot.png)

creates

![alpha°-elbow CAD](doc/pvc-elbow-alpha-cad-screenshot.png)


### Coupling ###
Create a centric coupling between two equal or different pipe sizes.

![create coupling dialog](doc/pvc-coupling-gui-screenshot.png)

creates

![coupling CAD](doc/pvc-coupling-cad-screenshot.png)


### Bushing ###
Create a bushing between two different pipe sizes. Not copling and bushings are different.

![create bushing dialog](doc/pvc-bushing-gui-screenshot.png)

creates

![bushing CAD](doc/pvc-bushing-cad-screenshot.png).

### Tee ###
Create an arbitrary elbow with the angle alpha within the range of 0°-180°.

![create-tee dialog](doc/pvc-tee-gui-screenshot.png)

creates

![tee CAD](doc/pvc-tee-cad-screenshot.png)

### Cross ###
Create a cross between equal or different pipes.

![create-cross dialog](doc/pvc-cross-gui-screenshot.png)

creates

![cross CAD](doc/pvc-cross-cad-screenshot.png)

# OSE Piping library #
This project contains FreeCAD macros to create various pipe, tee, and elbow fittings.
It is made for [Open Source Ecology](http://opensourceecology.org). The project is a very early experemental state.

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
![90°-elbow CAD screenshot](doc/pvc-elbow-90-cad-screenshot.png).

### alpha°-elbow ### 
Create an arbitrary elbow with the angle alpha within the range of 0°-180°.
![alpha°-elbow dialog](doc/pvc-elbow-alpha-gui-screenshot.png)
creates
![alpha°-elbow CAD](doc/pvc-elbow-alpha-cad-screenshot.png).

# Plane_derivation-Animation

# Installation

To install click on the exe file below the folder. Click the download button and when finished downloading click the exe file in downloads. Your computer will think that the file is a virus due to it not being signed or whitelisted, and assume the worst. To get around this click more info on the warning popup and run anyway. If you don't feel comfortable opening the file I can show the source code later or you can find it in the folder above the file.

# Explanation

So this program shows an animation of a plane flying 1250 meters over a radar station. The radar station tracks the progress of the plane. 
The initial variables are:<br />
Altitude or Y which equals 1000 meters<br />
Maximum Displacement in the X which equals 1250 meters<br /><sub>Note: This is only the X displacement at an instant, or the max displacement, which is an arbitrary number. This algorithm can extrapolate for longer distances.</sub><br />
Velocity or Dz/Dt which equals 553 m/s <br /><sub>Note: This value was found by taking the time taken by the animated plane to reach the 1250 meters via the equation V = D/T, or V = 1250/2.26 where 2.26 is the time. Due to rounding error and computing differences the time taken for the animation to finish may vary and leave an error</sub><br />
Time the plane takes to reach the maximum displacement 2.26<br />
<br />
Taking a path from the radar station up to the altitude of the plane, continuing along its path until maximum displacement, and then directly back towards the station 
creates a right triangle. This can be used to solve for dx/dt and z. Using the pythagorean theorem we find z as 1600.781 completing the triangle. Using the derived form
of the area of a right triangle we plug in: 2(553)(1600.781) = 2500dX/dT and find dX/dT = 708.185<br />
The next piece we need to solve for is x. The total displacement was found through V = D/T, where 1250 was plugged in for D. This equation can be rearranged to solve for X: X = V * T or X = 553 * T where T is a constant.<br />
With these new values a final equation can be found to find Z at all points along the flight. <br />Z = 2*dX/dT(V * T) / 2(V) or Z = 1416.37(553 * T) / 1106 where T is a constant. <br />
These two equations are used to find X and Z on my program, however, due to rounding error and differences in computer performance which affect the true V of the plane, an error of +-15m is expected.<br />
**_Thanks for taking the time to check out my quick little project. If the docs seem long, it's because I'm practicing writing them. If you have any questions or corrections please let me know_**

# Usage

The program is very simple and will start automatically. When the plane reaches the end press space to reset the animation. The values of X and Z should come out to around:<br />
Z = 1600
X = 1250

# diffdrive

ROS 2 Python package a diff-drive robotok vezérléséhez.

##  Telepítés

1. Klónozd a repository-t a `~/ros2_ws/src` mappába:

   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/Levente0312/lan_h0d.git
2. Navigálj a workspace gyökerébe
   ```bash
   cd ~/ros2_ws
3. build_eld a packaget
   ```bash
   colcon build --packages-select diffdrive --symlink-install
4. Ne felejtsd el source-ölni a workspacet
   ```bash
   source install/setup.bash
## Használat
vezérlő node indítása
   ```bash
   ros2 run diffdrive diffdrive_control
   ```
A terminálban a következő irányítási módok érhetők el:

WASD vagy nyilak: mozgás

Q: kilépés

A node a pygame könyvtárat használja a billentyűzet események kezelésére.

A hírdetet topic ellenőrzése:
   ```bash
   ros2 topic echp /cmd_vel
   ```

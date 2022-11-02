echo OFF
echo Shimyytrov installer v0.1.2.2022.11.02
echo =========================
echo Checking PIP update...
python.exe -m pip install --upgrade pip
echo =========================
echo Installing Pygame from PIP command...
python.exe -m pip install pygame
echo =========================
echo Installing Pillow from PIP command...
python.exe -m pip install pillow
echo =========================
echo Checking...
echo =========================
echo Checking Pygame package...
python.exe -m pip check pygame
echo =========================
echo Checking Pillow package...
python.exe -m pip check pillow
echo =========================
echo Installation completed.
PAUSE
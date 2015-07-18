# project-cool-attic
rpi project to control fan based on temperature

HTU21DF.py - courtesy of dalexgrey via http://forums.adafruit.com/viewtopic.php?f=19&t=58695
  Requires pigpio library : http://abyz.co.uk/rpi/pigpio/download.html
  ```
  wget abyz.co.uk/rpi/pigpio/pigpio.zip
  unzip pigpio.zip
  cd PIGPIO
  make
  make install
  ```
  To check the library
  ```
  sudo ./x_pigpio # check C I/F
  sudo pigpiod    # start daemon

  ./x_pigpiod_if  # check C      I/F to daemon
  ./x_pigpio.py   # check Python I/F to daemon
  ./x_pigs        # check pigs   I/F to daemon
  ./x_pipe        # check pipe   I/F to daemon
  ```
  To compile, link, and run yourprog.c
  ```
  gcc -o yourprog yourprog.c -lpigpio -lrt -lpthread
  sudo ./yourprog
  ```
  To start the pigpio daemon
  ```
  sudo pigpiod
  ```

ambientTemperature requires requests module, see http://docs.python-requests.org/en/latest/user/quickstart/
  ```
  sudo pip install requests
  ```


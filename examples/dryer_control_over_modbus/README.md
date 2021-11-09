## Usage

```bash
python3 control.py <Electrolyser EL 2.1 Modbus IP address> start|stop|reboot
```

In response you will get [Dryer state](https://go.enapter.com/p2Q9o) read 8 times during 10 seconds. You might notice two similar states:

+ `Stopped by User` - stop command was initiated _by user_ in Enapter Cloud, Enapter Mobile App, Electrolyser EL 2.1 Web GUI, by this script or button.
+ `Idle` - stop command was initiated _by Electrolyser EL 2.1_ connected to the same Dryer Control Network.

If you stop Dryer by using this script, Dryer will go to `Stopped by User` state and stay in this state unill you start it manually (button, Enapter Cloud, Enapter Mobile App, Electrolyser Web GUI, Electrolyser Modbus TCP).

**Start Enapter Dryer DRY 2.1:**

```bash
control.py 192.168.42.4 start
```

**Stop Enapter Dryer DRY 2.1:**

```bash
control.py 192.168.42.4 stop
```

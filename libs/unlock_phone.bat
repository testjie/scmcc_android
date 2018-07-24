adb shell echo "down"
adb shell sendevent /dev/input/event0 1 116 1
adb shell sendevent /dev/input/event0 0 0 0
adb shell sendevent /dev/input/event0 1 116 0
adb shell sendevent /dev/input/event0 0 0 0
adb shell echo "up"
adb shell echo "start_unlock"
adb shell input touchscreen  swipe 600 1000 600 300
adb shell echo "end_unlock"
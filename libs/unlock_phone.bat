adb shell echo "down"
adb shell sendevent /dev/input/event0 1 116 1
adb shell sendevent /dev/input/event0 0 0 0
adb shell sendevent /dev/input/event0 1 116 0
adb shell sendevent /dev/input/event0 0 0 0
adb shell echo "up"
adb shell echo "start_unlock"
adb shell input touchscreen  swipe 600 1000 600 300
adb shell sendevent /dev/input/event2: 3 57 1403
adb shell sendevent /dev/input/event2: 1 330 1
adb shell sendevent /dev/input/event2: 1 325 1
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 1102
adb shell sendevent /dev/input/event2: 3 49 6
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 1097
adb shell sendevent /dev/input/event2: 3 48 6
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 54 1078
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 1037
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 978
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 909
adb shell sendevent /dev/input/event2: 3 48 7
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 831
adb shell sendevent /dev/input/event2: 3 48 6
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 749
adb shell sendevent /dev/input/event2: 3 49 5
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 667
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 744
adb shell sendevent /dev/input/event2: 3 54 600
adb shell sendevent /dev/input/event2: 3 48 7
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 545
adb shell sendevent /dev/input/event2: 3 48 6
adb shell sendevent /dev/input/event2: 3 49 6
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 53 638
adb shell sendevent /dev/input/event2: 3 54 502
adb shell sendevent /dev/input/event2: 3 48 7
adb shell sendevent /dev/input/event2: 3 49 7
adb shell sendevent /dev/input/event2: 0 0 0
adb shell sendevent /dev/input/event2: 3 57 4294967295
adb shell sendevent /dev/input/event2: 1 330 0
adb shell sendevent /dev/input/event2: 1 325 0
adb shell sendevent /dev/input/event2: 0 0 0
adb shell echo "end_unlock"
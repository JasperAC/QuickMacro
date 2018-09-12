# Code to check if left or right mouse buttons were pressed
import yaml
import win32api
import time
import pyautogui
from collections import OrderedDict


def init():
    file = open('operation.yml', 'w')
    file.close()


def represent_ordered_dict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


def main():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    file = open('operation.yml', 'a+')

    while True:
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
        operation = OrderedDict()

        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            operation['position'] = list(pyautogui.position())
            operation['button'] = 'left'

            if a < 0:
                print('Left Button Pressed')
                yaml.dump(operation, file, default_flow_style=False)
                print('---', file=file)

            else:
                print('Left Button Released')

        if b != state_right:  # Button state changed
            state_right = b
            print(b)
            operation['position'] = list(pyautogui.position())
            operation['button'] = 'right'

            if b < 0:
                print('Right Button Pressed')
                yaml.dump(operation, file, default_flow_style=False)
                print('---', file=file)
            else:
                print('Right Button Released')

        time.sleep(0.001)


if __name__ == '__main__':
    init()
    yaml.add_representer(OrderedDict, represent_ordered_dict)
    main()

import time
import pyautogui
import yaml


def main():
    operation = yaml.load_all(open("operation.yml"))
    for i in operation:
        pyautogui.click(i['position'], button=i['button'])


if __name__ == '__main__':
    main()
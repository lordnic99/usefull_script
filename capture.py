import win32gui
import win32ui
import win32con
from time import sleep
import ctypes
import sys

def screenshot(hwnd=None):
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    if not hwnd:
        hwnd = win32gui.GetDesktopWindow()
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    h = b - t
    w = r - l

    hDC = win32gui.GetWindowDC(hwnd)
    myDC = win32ui.CreateDCFromHandle(hDC)

    newDC = myDC.CreateCompatibleDC()
    myBitMap = win32ui.CreateBitmap()

    hdc_screen = win32gui.GetDC(0)
    win32gui.ReleaseDC(0, hdc_screen)
    
    scaled_w = int(w * scaleFactor)
    scaled_h = int(h * scaleFactor)

    myBitMap.CreateCompatibleBitmap(myDC, scaled_w, scaled_h)
    newDC.SelectObject(myBitMap)

    win32gui.SetForegroundWindow(hwnd)
    sleep(0.2)
    newDC.BitBlt((0, 0), (scaled_w, scaled_h), myDC, (0, 0), win32con.SRCCOPY)

    myBitMap.SaveBitmapFile(newDC, 'Window_Capture.bmp')

    myDC.DeleteDC()
    newDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hDC)
    win32gui.DeleteObject(myBitMap.GetHandle())
 
def _get_windows_bytitle(title_text, exact = False):
    def _window_callback(hwnd, all_windows):
        all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, title in windows if title_text == title]
    else:
        return [hwnd for hwnd, title in windows if title_text in title]
 
if __name__ == "__main__":
    
    window_title = sys.argv[1]
    
    hwnds = _get_windows_bytitle(window_title.strip(), exact=False)
 
    if hwnds:
        screenshot(hwnds[0])
        print("Check Window_Capture.bmp")
    else:
        print("No window found")
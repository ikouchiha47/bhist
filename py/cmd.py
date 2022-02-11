import platform
import shutil
import  sys

system = platform.system()

darwin_chrome = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"

def chrome():
    if system == 'Darwin':
        return darwin_chrome
    if system == 'Linux':
        return shutil.which('chrome') or shutil.which('google-chrome') or shutil.which('chromium')

    sys.exit('Life sucks, so does your os')


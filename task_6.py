from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_volume():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        return current_volume
    except Exception as e:
        print(f"An error occurred while getting volume: {e}")
        return None

def set_volume(value):
    try:
        value = max(0.0, min(value, 1.0))
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(value, None)
        print(f"Volume set to {value * 100:.0f}%")
    except Exception as e:
        print(f"An error occurred while setting volume: {e}")

if __name__ == "__main__":
    try:
        current_volume = get_volume()
        if current_volume is not None:
            print(f"Current Volume: {current_volume * 100:.0f}%")
        set_volume(0.5)  # Set volume to 50%
    except Exception as e:
        print(f"An error occurred: {e}")

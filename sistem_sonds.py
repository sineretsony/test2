from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL

def set_system_sounds_volume(volume_level: float):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process is None:
            try:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(volume_level, None)
                print(f"[+] Volume set to {volume_level * 100:.0f}% for unnamed session (likely System Sounds)")
                return
            except Exception as e:
                print(f"[!] Error: {e}")
    print("[-] System Sounds session not found.")

set_system_sounds_volume(0.1)

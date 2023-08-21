import os
import platform

def get_os_info():
    system = platform.system()
    release = platform.release()

    if system == "Windows":
        import win32api
        build_number = win32api.GetVersionEx()[3]
        return system, f"{release} (Build {build_number})"
    elif system == "Darwin":
        # For MacOS, the build number can be extracted from uname's version string
        version_str = os.popen('uname -v').read().strip()
        build_number = version_str.split(':')[-1].strip()
        return system, f"{release} ({build_number})"
    else:
        # Linux or other UNIX-based systems
        version = platform.version()
        return system, version

if __name__ == "__main__":
    os_name, os_version = get_os_info()
    print(f"Operating System: {os_name}")
    print(f"Version/Release: {os_version}")


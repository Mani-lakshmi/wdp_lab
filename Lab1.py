
#sams_env_check.py
import sys
import platform
def display_environment_info():
    print("===sams development environment check ===")
    print(f"python version:{platform.python_version()}")
    print(f"platform:{platform.system()}{platform.release()}")
    print(f"executable:{sys.executable}")
    if sys.version_info<(3,11):
        print("warning:sams requires python 3.11 or higher.")
    else:
        print("python version ok for sams development.")
def sams_welcome():
    print("\n welcome to sams-smart academic management system")
    print("edutech solutions pvt.ltd./ skilling lab enviroment")
if __name__ == "__main__":
    display_environment_info()
    sams_welcome()








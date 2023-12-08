import speedtest

speed_test = speedtest.Speedtest()

def bytes_to_bm(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

download_speed = bytes_to_bm(bytes=speed_test.download())
print(download_speed)
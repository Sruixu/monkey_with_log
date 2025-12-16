import subprocess
import datetime
import sys


def main():
    # 原命令
    cmd = sys.argv[1] if len(sys.argv) > 1 else \
        'adb shell monkey -p com.bailunsi.zh_consumer_mall --pct-touch 30 --ignore-crashes --ignore-timeouts --pct-syskeys 0 --throttle 250 -s 2 -v -v -v 10000'

    # 日志文件
    log_file = r'D:\log\monkey_%s.txt' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    print(f"执行: {cmd}")
    print(f"输出: {log_file}")

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

    with open(log_file, 'w', encoding='utf-8') as f:
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                f.write(f'[{timestamp}] {line}')
                f.flush()

    print("完成")


if __name__ == '__main__':
    main()
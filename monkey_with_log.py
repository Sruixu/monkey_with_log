import subprocess
import datetime
import sys


def main():
    # 原命令
    cmd = sys.argv[1] if len(sys.argv) > 1 else \
        'adb shell monkey -p com.bailunsi.zh_consumer_mall --pct-touch 30 --ignore-crashes --ignore-timeouts --pct-syskeys 0 --throttle 250 -s 2 -v -v -v 1000'

    # 日志文件
    log_file = r'D:\log\monkey_%s.txt' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    print(f"执行: {cmd}")
    print(f"输出: {log_file}")

    # 写入开始时间
    start_time = datetime.datetime.now()

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

    with open(log_file, 'w', encoding='utf-8') as f:
        # 写入开始标记
        f.write(f'=== Monkey Test Started at {start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]} ===\n\n')

        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                # 获取当前时间戳
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

                # 写入文件（带有时间戳）
                f.write(f'[{timestamp}] {line}')
                f.flush()

                # 同时输出到控制台（也带有时间戳）
                print(f'[{timestamp}] {line}', end='')

        # 写入结束标记
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        f.write(f'\n=== Monkey Test Finished at {end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]} ===\n')
        f.write(f'=== Duration: {duration.total_seconds():.2f} seconds ===\n')

    print("\n完成")


if __name__ == '__main__':
    main()
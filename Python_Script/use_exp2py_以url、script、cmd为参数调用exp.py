"""
使用示例
python script.py -u http://example.com -f x.py -c "ls -l"
"""
import argparse
import subprocess

def run_command(url, x_script, diy_command):
    # 构建命令字符串，替换url、x_script和diy_command的值
    command = f"python {x_script} {url} '{diy_command}'"
    
    try:
        # 使用subprocess运行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        # 输出命令的标准输出
        print("命令的标准输出：")
        print(result.stdout)
        
        # 输出命令的标准错误（如果有）
        if result.stderr:
            print("命令的标准错误：")
            print(result.stderr)
        
        # 获取命令的返回码
        return_code = result.returncode
        print(f"命令的返回码：{return_code}")
        
    except subprocess.CalledProcessError as e:
        print(f"运行命令时发生错误：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="调用系统命令 'python x.py url 'diy_command''，可通过 -u、-f、-c 参数修改URL、x.py 和 diy_command 的值")
    parser.add_argument("-u", "--url", required=True, help="要传递给 x.py 的 URL")
    parser.add_argument("-f", "--x_script", required=True, help="x.py 的文件名")
    parser.add_argument("-c", "--diy_command", required=True, help="要传递给 diy_command 的命令")
    
    args = parser.parse_args()
    
    # 调用 run_command 函数并传递参数的值
    run_command(args.url, args.x_script, args.diy_command)

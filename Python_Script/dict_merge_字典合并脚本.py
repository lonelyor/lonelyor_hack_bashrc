import os
import mmap

def merge_and_deduplicate_large_text_files(directory_path, output_file):
    # Create a set to store unique lines
    unique_lines = set()

    # 遍历目录下的所有文件
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # 检查文件是否为文本文件（可以根据需要修改此检查）
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    with mmap.mmap(file.fileno(), 0, mmap.MAP_PRIVATE, mmap.PROT_READ) as mmapped_file:
                        for line in iter(mmapped_file.readline, b''):
                            stripped_line = line.strip()
                            if stripped_line != b'':  # 检查剥离后行是否不为空
                                unique_lines.add(stripped_line.decode('utf-8'))

    # # 将独立的行写入输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in sorted(unique_lines):
            outfile.write(line + '\n')

if __name__ == "__main__":
    directory_path = 'dir path'  # 替换为您的目录路径
    output_file = 'xxx.txt'    # 替换为您想要的输出文件名

    merge_and_deduplicate_large_text_files(directory_path, output_file)

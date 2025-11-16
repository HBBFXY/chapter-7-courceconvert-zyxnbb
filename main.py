import keyword

def convert_python_file(source_file, target_file):
    """
    读取Python源文件，将除保留字外的所有小写字母转换为大写字母
    并保存到目标文件中
    """
    try:
        # 读取源文件
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取Python所有保留字
        reserved_words = set(keyword.kwlist)
        
        # 将内容按行分割
        lines = content.split('\n')
        converted_lines = []
        
        for line in lines:
            converted_line = ""
            i = 0
            while i < len(line):
                # 检查当前位置是否是标识符的一部分
                if line[i].isalpha() or line[i] == '_':
                    # 提取完整的单词
                    start = i
                    while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                        i += 1
                    word = line[start:i]
                    
                    # 如果是保留字，保持原样
                    if word in reserved_words:
                        converted_line += word
                    else:
                        # 如果不是保留字，转换为大写
                        converted_line += word.upper()
                else:
                    # 非字母字符保持原样
                    converted_line += line[i]
                    i += 1
            
            converted_lines.append(converted_line)
        
        # 将转换后的内容写入目标文件
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(converted_lines))
        
        print(f"文件转换完成！转换后的文件已保存为: {target_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到源文件 {source_file}")
    except Exception as e:
        print(f"转换过程中发生错误: {e}")

def convert_specific_example():
    """
    转换特定的示例文件（基于图一的内容）
    """
    # 源文件内容（基于图一）
    source_content = """# 这个文件是要转换大小写的文件
import random
ls=[]
random.seed(10)
for i in range(10):
    a=random.randint(0,100)
    ls.append(a)
print(ls)"""
    
    # 将源内容写入临时文件
    source_file = "random_int.py"
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(source_content)
    
    # 转换文件
    target_file = "converted_random_int.py"
    convert_python_file(source_file, target_file)
    
    # 显示转换结果
    print("\n转换前的内容:")
    print(source_content)
    
    print("\n转换后的内容:")
    with open(target_file, 'r', encoding='utf-8') as f:
        print(f.read())

# 主程序
if __name__ == "__main__":
    # 方法1：转换特定示例文件
    print("开始转换示例文件...")
    convert_specific_example()
    
    # 方法2：用户也可以指定其他文件进行转换
    print("\n" + "="*50)
    print("您也可以使用以下方式转换其他文件:")
    print("convert_python_file('源文件.py', '目标文件.py')")
    
    # 演示如何使用函数转换任意文件
    # convert_python_file('input.py', 'output.py')

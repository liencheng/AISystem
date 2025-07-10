import argparse
import csv

def process_files(file_a, file_b, output_file ,output_file2):
    # 读取文件A并提取前两列数据
    # print(file_a)
    
    with open(file_a, 'r', encoding='mbcs') as f_a:
            reader = csv.reader(f_a, delimiter='\t')
            next(reader)  # 跳过标题行
            rows_a = list(reader)  # 读取所有数据，保存在列表中
        
    # 读取文件B并准备将数据写入
    with open(file_b, 'r', encoding='utf-8') as f_b:
            lines_b = f_b.readlines()
        

    # 处理数据并将其写入输出文件
    with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        writer.writerow(lines_b[0].strip().split('\t'))  # 写入文件B的标题行

        for row in rows_a:
            # 获取文件A的第一列和第二列
            id_value = row[0]
            second_column_value = row[1]

            # 将文件A的第一列放入文件B的第一列
            # 文件A的第二列放入文件B的第二列和第三列
            new_row = [id_value, second_column_value, second_column_value]
            writer.writerow(new_row)
    with open(output_file2, 'w', encoding='mbcs', newline='') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        writer.writerow(lines_b[0].strip().split('\t'))  # 写入文件B的标题行

        for row in rows_a:
            # 获取文件A的第一列和第二列
            id_value = row[0]
            second_column_value = row[1]

            # 将文件A的第一列放入文件B的第一列
            # 文件A的第二列放入文件B的第二列和第三列
            new_row = [id_value, second_column_value, second_column_value]
            writer.writerow(new_row)

def main():
    # 创建一个命令行解析器
    parser = argparse.ArgumentParser(description="Process two txt files and merge their data.")
    
    # 添加文件路径参数
    parser.add_argument('file_a', type=str, help="Path to the first input file (file A).")
    parser.add_argument('file_b', type=str, help="Path to the second input file (file B).")
    parser.add_argument('output_file', type=str, help="Path to the output file where merged data will be saved.")
    parser.add_argument('output_file2', type=str, help="Path to the output file where merged data will be saved.")
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用处理文件的函数
    process_files(args.file_a, args.file_b, args.output_file,args.output_file2)

if __name__ == "__main__":
    main()

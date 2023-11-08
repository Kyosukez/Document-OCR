import re
import csv

# Open the input file for reading
input_file_path = 'output.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Remove spaces, slashes, and specific characters from the content
content_without_test = content.replace('test', '')
content_without_sample = content_without_test.replace('sample', '')
# Repeat the same for other content to remove 
# content_without_! = content_without_@('!', '')

print("Spaces, slashes, specific characters, and previous content are deleted.")

# キーワード1とキーワード2で挟まれた部分を正規表現を使用して抽出
keyword1 = "keyword 1"
keyword2 = "keyword 2"

pattern = re.escape(keyword1) + r'(.*?)' + re.escape(keyword2)
# replace the content_without_sample with what ever line comes last 
matches = re.findall(pattern, content_without_sample, re.DOTALL)

# Extracted content
extracted_content = '\n'.join(matches)

# Write the extracted content back to the same input file
with open(input_file_path, 'w', encoding='utf-8') as file:
    file.write(extracted_content)

print('抽出された内容が元のファイルに上書きされました.')

# Now you can read data from the same input file and write it to "output.csv"
output_data = []

with open(input_file_path, 'r', encoding="utf-8") as file:
    first_line = True
    for line in file:
        line = line.strip()

        if first_line:
            widths = [4, 8, 12, 14, 16, 20, 24, 26, 30]
            parts = [line[i:j].strip() for i, j in zip([0] + widths, widths + [None])]
            output_data.append(parts)
            first_line = False
        else:
            widths = [4, 12, 16, 19, 21, 22, 27, 34, 35]
            parts = [line[i:j].strip() for i, j in zip([0] + widths, widths + [None])]
            output_data.append(parts)

# Write the extracted data to "output.csv"
output_file_path = "output.csv"
with open(output_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(output_data)

print(f"CSVファイルに保存しました: {output_file_path}")
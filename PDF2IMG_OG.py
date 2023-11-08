from pdf2image import convert_from_path

convert_from_path(
   "sample.pdf" , #入力PDF Replace with your own
   dpi=300, #解像度
   output_folder='Output Folder PAth', #出力フォルダ Replace with your own 
   output_file='out', #出力ファイルprefix
   fmt='png' #フォーマット
)
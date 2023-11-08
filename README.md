# Document-OCR

Japanese OCR utlizing python inorder to read and export text and data 

* 動作環境
  * OS : Windows10
  * Python : 3.10.0
  * Tesseract : 5.3.3
  * pyocr : 0.8.5
  * PIL : 9.3.0
  * Poppler : 23.11.0

## Usage

You can use this project by cloning this reposetory and running it with your IDE of choice. 

You will need to install the following components inorder to run the code; 

[Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki/)

>I recommend following this tutorial:&nbsp;  [ひつじ](https://hituji-ws.com/code/python/tesseract-ocr/)

Change the Engine for tesseract to the Best version over the Fast version

`※日本語Best版は下から落とす`

https://github.com/tesseract-ocr/tessdata_best/blob/main/jpn.traineddata

https://github.com/tesseract-ocr/tessdata_best/blob/main/jpn_vert.traineddata

`※これをTesseractーOCR＞＞tessdataの中身と上書きする`
![スクリーンショット 2023-11-01 203210](https://github.com/Kyosukez/OCR/assets/52781137/6b280be8-454f-44b2-9aee-5b04c3cf6c07)

```bash
pip install pillow
pip install pyocr
pip install 
```

For the PDF to Image conversion you will need the library Poppler

## Installation 
 >Download Latest Version of Poppler [Here]([https://poppler.freedesktop.org/](https://github.com/oschwartz10612/poppler-windows))

 >Instructions for PATH [here](https://dev.library.kiwix.org/content/stackoverflow_en_nopic_2021-08/questions/18381713/how-to-install-poppler-on-windows)

> [!IMPORTANT]
> This is a prototype at best, do not expect everything to work perfectly.


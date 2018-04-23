import PyPDF2
import numpy as np
import cv2
import matplotlib.pyplot as plt
pdf = PyPDF2.PdfFileReader(open("d:/BaiduYunDownload/test/1.pdf","rb"))
page1=pdf.getPage(1)
obj=page1['/Resources']['/XObject']['/Im21']

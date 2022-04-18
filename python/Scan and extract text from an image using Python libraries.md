
parent: [[Privat ToDo]]
tags:
Reference: [[Python MOC]]
date::
status::
fazit::

---


# Scan and extract text from an image using Python libraries

## Learn how to extract and classify text from an document image using Python libraries such as cv2 and PIL.

[ Save](https://developer.ibm.com/sso/login?d=https%3A%2F%2Fdeveloper.ibm.com%2Ftutorials%2Fdocument-scanner%2F&lang=us_EN)[ Like](https://developer.ibm.com/sso/login?d=https%3A%2F%2Fdeveloper.ibm.com%2Ftutorials%2Fdocument-scanner%2F&lang=us_EN)

By [R K Sharath Kumar](https://developer.ibm.com/profiles/sharrkum)  
Updated July 16, 2018 | Published March 23, 2018

* * *

In this tutorial you will learn how to extract text and numbers from a scanned image and convert a PDF document to PNG image using Python libraries such as [wand](https://pypi.org/project/Wand/), [pytesseract](https://pypi.org/project/pytesseract/), [cv2](https://pypi.org/project/opencv-python/), and [PIL](https://pypi.org/project/PIL/).

You will use a [tutorial from pyimagesearch](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes) for the first part and then extend that tutorial by adding text extraction.

## Learning objectives

Upon completing this tutorial the reader will understand how to:

*   Build a document scanner (based on the prerequisite).
*   Enhance the document scanner to extract text and numbers.

## Prerequisites

This is not beginner’s tutorial and requires knowledge of Python, Open CV & Natural Language Processing. This tutorial builds on a tutorial written by pyimagesearch contributor [Adrian Rosebrock](https://www.pyimagesearch.com/author/adrian/), it details [How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/). It is recommended to read through that tutorial to understand how to scan documents by detecting edges, finding contour and applying transformations.

## Estimated time

Completing this tutorial should take about 30 minutes.

## Steps

### Resizing the image

How are we going to complete our goal of text extraction? First we are going to resize the image using `cv2.resize` with a height value of `1150` and width of `1350` pixels. This image is then saved onto the disk. The code to do this step, and the resized output can be seen below.

    imS = cv2.resize(warped, (1350, 1150))
    cv2.imshow("output",imS)
    cv2.imwrite('Output Image.PNG', imS)
    cv2.waitKey(0)

Show more

### Extracting text from the document

To extract text from the image we can use the `PIL` and `pytesseract` libraries. We currently perform this step for a single image, but this can be easily modified to loop over a set of images. We can enhance the accuracy of the output by fine tuning the parameters but the objective is to show text extraction. The code to do this step, and the text extraction output can be seen below.

    from PIL import Image
    import PIL.Image

    from pytesseract import image_to_string
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
    output = pytesseract.image_to_string(PIL.Image.open('Output Image.PNG').convert("RGB"), lang='eng')
    print output

Show more

### Classifying the document

How do we classify the documents based on its contents? The answer is to extract the text from the document and feed it to a user defined function with a logic of if-then-else and looping functionality to identify the name of the document.

#### Extract number from image

This objective can be achieved using `cv2`. The input document is a bimodal image which means most of the pixels are distributed over two dominant regions. Below is our input image.

`cv2` has a method for OTSU binarization, which would work for bimodal images. It assumes the input intensities distribution to be bi-modal and tries to find the optimal threshold. Otsu binarization automatically calculates a threshold value from image histogram for a bimodal image. The code to do this step, and the Otsu binarization output can be seen below.

    import cv2

    img = cv2.imread("input_image.png", 0)
    ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
    print "Threshold selected : ", ret
    cv2.imwrite("./output_image.png", thresh)

Show more

### Convert pdf to png image

Lastly, we provide a brief snippet of code that uses `wand` to convert a PDF to a PNG.

    from __future__ import print_function

    from wand.image import Image

    with Image(filename='sample_doc.pdf') as img:

        print('width =', img.width)
        print('height =', img.height)
        print('pages = ', len(img.sequence))
        print('resolution = ', img.resolution)

    with img.convert('png') as converted:
         converted.save(filename='sample_doc.png')

Show more

## Summary

This completes the scope to give an overview of document scanning, image recognition, text extraction and classification. Please feel free to explore more on the libraries mentioned here and enhance the code to suit your requirements.
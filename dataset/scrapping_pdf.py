#!/usr/bin/env python3
import os
import requests
import re


def download_pdf_file(url: str) -> bool:
    """Download PDF from given URL to local directory.

    :param url: The url of the PDF file to be downloaded
    :return: True if PDF file was successfully downloaded, otherwise False.
    """

    # Request URL and get response object
    response = requests.get(url, stream=True)

    # isolate PDF filename from URL
    #pdf_file_name = os.path.basename(url)
    pdf_file_name = "".join(re.findall("[^&?]",os.path.basename(url)))+".pdf"
    if response.status_code == 200:
        # Save in current working directory
        filepath = os.path.join(os.getcwd(), pdf_file_name)
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)
            print(f'{pdf_file_name} was successfully saved!')
            return True
    else:
        print(f'Uh oh! Could not download {pdf_file_name},')
        print(f'HTTP response status code: {response.status_code}')
        return False

def getAllPDF() : 
    for annee in range (2018,2024) : 
        if annee==2018:
            inf=20
        else : 
            inf=1
        for semaine in range (inf,53) :
            # URL from which pdfs to be downloaded
            URL = 'https://snepmusique.com/pdf/tops_pdf.php?annee='+str(annee)+'&semaine='+str(semaine)+'&categorie=Top%20Singles'
            download_pdf_file(URL)

if __name__ == '__main__':
    getAllPDF()

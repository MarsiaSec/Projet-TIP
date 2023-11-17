import tabula

def getAllCSV() : 
    for annee in range (2018,2024) : 
        if annee==2018:
            inf=20
        else : 
            inf=1
        if annee==2024:
            sup=45
        else : 
            sup=53
        for semaine in range (inf,sup) :
            # URL from which pdfs will be converted into csv
            URL = 'tops_pdf.phpannee='+str(annee)+'semaine='+str(semaine)+'categorie=Top%20Singles'
            # convert PDF into CSV
            tabula.convert_into(URL+".pdf", URL+".csv", output_format="csv", pages='all')

if __name__ == '__main__':
    getAllCSV()

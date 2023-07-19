import os
from PyPDF2 import PdfMerger  # pip install PyPDF2

def merge_pdfs(cover_folder, draft_folder, output_folder):
    # Create the output folder if it doesn't exist
    # Çıktı klasörü yoksa oluştur
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Get a list of PDFs in the cover and draft folders
    # Kapak ve taslak klasörlerindeki PDF'lerin bir listesini alın
    cover_pdfs = [f for f in os.listdir(cover_folder) if f.endswith('.pdf')]
    draft_pdfs = [f for f in os.listdir(draft_folder) if f.endswith('.pdf')]

    # Iterate through the cover PDFs
    # Kapak PDF'lerini yineleyin
    for pdf in cover_pdfs:
        # Get the numeric key of the PDF
        # PDF'nin sayısal anahtarını alın
        key = pdf.split('.')[0]

        # Find the matching draft PDF with the same key
        # Eşleşen taslak PDF'yi aynı tuşla bulun
        matching_draft = [f for f in draft_pdfs if key in f][0]

        # Create a PdfMerger object
        # Bir PdfMerger nesnesi oluşturun
        merger = PdfMerger()

        # Add the cover and draft PDFs to the merger
        # Kapağı ve taslak PDF'leri birleştirmeye ekleyin
        merger.append(f'{cover_folder}/{pdf}')
        merger.append(f'{draft_folder}/{matching_draft}')

        # Write the merged PDF to the output folder
        # Birleştirilmiş PDF'yi çıktı klasörüne yazın
        merger.write(f'{output_folder}/{matching_draft}')

    print(f'Merged {len(cover_pdfs)} PDFs to {output_folder}')

# Example usage
# Örnek kullanım
merge_pdfs('cover', 'draft', 'output')

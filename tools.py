import pymupdf as pmp
import os
import os.path
from pymupdf import Document

DEBUG = True

def list_pdf() -> list[str]:
    '''
    List pdf file names.
    '''
    if DEBUG: print('list_pdf')
    return os.listdir(os.path.join('.', 'pdfs'))

def _open_pdf(pdf_name:str) -> Document:
    return pmp.open(os.path.join('.', 'pdfs', pdf_name))

def read_pdf(pdf_name:str, page:int) -> str:
    '''
    Open the file at 'pdf_name' and return the page-th (0-index) page.
    '''
    if DEBUG: print(f'read_pdf({pdf_name}, {page})')
    return _open_pdf(pdf_name)[page].get_text() # type: ignore #

def pdf_pages(pdf_name:str) -> int:
    '''
    Open the file at 'pdf_name' and return the number of pages of the doc.
    '''
    if DEBUG: print(f'pdf_pages({pdf_name})')
    return _open_pdf(pdf_name).page_count

def get_pdf_outline(pdf_name: str) -> list:
    '''
    Return the outline (menu/bookmarks) of the given PDF.
    '''
    if DEBUG: print('get_pdf_outline')
    doc = _open_pdf(pdf_name)
    outline = doc.get_toc()  # type: ignore # Table of Contents
    return outline

if __name__ == '__main__':
    import pprint
    DEBUG = True
    pdfs = list_pdf()
    print(pdfs)
    text = read_pdf(pdfs[0], 4)
    print(text)
    for doc in pdfs:
        print(pdf_pages(doc))

    outline = get_pdf_outline(pdfs[0])
    pprint.pprint(outline)
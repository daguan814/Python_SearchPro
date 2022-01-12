# @Time   ： 2021/12/20 12:14 PM
# @Author ： 水镜
# @Do     :

from docx import Document
from docxcompose.composer import Composer


def mdo(files, final_docx):
    new_document = Document()
    composer = Composer(new_document)
    for fn in files:
        composer.append(Document(fn))
    composer.save(final_docx)


mdo(['1.docx', '2.docx'], 'resu.docx')

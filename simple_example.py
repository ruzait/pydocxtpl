from docxtpl import DocxTemplate

document_path ="my.docx"
doc = DocxTemplate(document_path)
context = {"name": "Ruzait"}
doc.render(context)
doc.save("My edit.docx")
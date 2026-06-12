from utils.docx_generator import DocxGenerator

DocxGenerator.create_docx(
    title="Cyber Security",
    content="This is a DOCX export test.",
    filename="test.docx"
)

print(
    "DOCX Created Successfully"
)
from utils.pdf_generator import PdfGenerator

pdf_buffer = (
    PdfGenerator.create_pdf_buffer(
        "Cyber Security",
        "This is a PDF export test."
    )
)

with open(
    "test.pdf",
    "wb"
) as f:

    f.write(
        pdf_buffer.getvalue()
    )

print(
    "PDF Created Successfully"
)
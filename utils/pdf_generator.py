from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PdfGenerator:

    @staticmethod
    def create_pdf_buffer(
        title,
        content
    ):

        buffer = BytesIO()

        doc = SimpleDocTemplate(
            buffer
        )

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                title,
                styles["Title"]
            )
        )

        story.append(
            Spacer(
                1,
                12
            )
        )

        for line in content.split("\n"):

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

        doc.build(
            story
        )

        buffer.seek(0)

        return buffer
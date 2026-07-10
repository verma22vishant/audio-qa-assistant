from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    transcript_1,
    transcript_2,
    comparison,
    output_file="report.pdf"
):
    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Audio QA Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            f"<b>Similarity Score:</b> "
            f"{comparison['similarity']}%",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "<b>Transcript 1</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            transcript_1,
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "<b>Transcript 2</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            transcript_2,
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "<b>Missing Words:</b> "
            + ", ".join(
                comparison["missing_words"]
            ),
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "<b>Extra Words:</b> "
            + ", ".join(
                comparison["extra_words"]
            ),
            styles["Normal"]
        )
    )

    doc.build(story)

    return output_file
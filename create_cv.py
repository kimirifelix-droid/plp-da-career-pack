
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

OUTPUT = "cv/Felix_Kimiri_CV.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=1.6 * cm,
    leftMargin=1.6 * cm,
    topMargin=1.2 * cm,
    bottomMargin=1.2 * cm,
)

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="CandidateName",
    parent=styles["Title"],
    fontSize=20,
    leading=23,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#17365D"),
    spaceAfter=5,
))

styles.add(ParagraphStyle(
    name="ContactDetails",
    parent=styles["Normal"],
    fontSize=8,
    leading=11,
    alignment=TA_CENTER,
    spaceAfter=8,
))

styles.add(ParagraphStyle(
    name="SectionHeading",
    parent=styles["Heading2"],
    fontSize=10.5,
    leading=13,
    textColor=colors.HexColor("#17365D"),
    spaceBefore=6,
    spaceAfter=3,
))

styles.add(ParagraphStyle(
    name="CompactBody",
    parent=styles["BodyText"],
    fontSize=8.5,
    leading=10.5,
    spaceAfter=2,
))

story = []

def add_section(title):
    story.append(Paragraph(title, styles["SectionHeading"]))
    story.append(HRFlowable(
        width="100%",
        thickness=0.6,
        color=colors.HexColor("#9FBAD0"),
        spaceAfter=4,
    ))

def add_bullet(text):
    story.append(Paragraph("&bull; " + text, styles["CompactBody"]))

story.append(Paragraph("FELIX KIMIRI", styles["CandidateName"]))

story.append(Paragraph(
    "Junior Data Analyst | Python | SQL | Data Cleaning | Reporting<br/>"
    "Email: kimirifelix@gmail.com | Phone: 0712343840<br/>"
    "GitHub: github.com/kimirifelix-droid<br/>"
    "LinkedIn: linkedin.com/in/felix-kimiri-0306ab268/",
    styles["ContactDetails"],
))

add_section("PROFESSIONAL SUMMARY")
story.append(Paragraph(
    "Development Studies with IT background, building practical skills in "
    "data analytics through hands-on projects. Familiar with Python, SQL, "
    "pandas, NumPy, exploratory data analysis, data quality checks, and "
    "business reporting. Interested in using evidence and data to support "
    "business decisions, community development, and NGO programmes.",
    styles["CompactBody"],
))

add_section("TECHNICAL SKILLS")
story.append(Paragraph(
    "<b>Programming:</b> Python, SQL<br/>"
    "<b>Data analysis:</b> pandas, NumPy, data cleaning, exploratory data "
    "analysis, KPI analysis, cohort analysis, A/B testing fundamentals<br/>"
    "<b>Visualization and reporting:</b> charts, dashboards, analytical "
    "reports<br/>"
    "<b>Tools:</b> Jupyter Notebook, Git, GitHub, VS Code",
    styles["CompactBody"],
))

add_section("DATA ANALYTICS PROJECTS")

story.append(Paragraph(
    "<b>Retail Sales Analytics — Capstone Project</b>",
    styles["CompactBody"],
))
add_bullet(
    "Cleaned and analysed 4,998 records from a synthetic retail dataset."
)
add_bullet(
    "Calculated KES 304,062,595 in net sales and KES 78,836,895 in gross "
    "profit, with a reported gross margin of 25.93%."
)
add_bullet(
    "Developed eight SQL analyses and three analytical notebooks covering "
    "data cleaning, analysis, and reporting."
)
story.append(Paragraph(
    "Repository: github.com/kimirifelix-droid/plp-capstone-a-felix-kimiri",
    styles["CompactBody"],
))

story.append(Paragraph(
    "<b>PesaPap Growth Analytics</b>",
    styles["CompactBody"],
))
add_bullet(
    "Developed a practice fintech analytics project covering transaction "
    "analysis, customer segmentation, cohort analysis, and A/B testing."
)
story.append(Paragraph(
    "Repository: github.com/kimirifelix-droid/plp-da-a7-pesapap-growth-analytics",
    styles["CompactBody"],
))

story.append(Paragraph(
    "<b>Duka Board Report</b>",
    styles["CompactBody"],
))
add_bullet(
    "Analysed 1,000 synthetic records and reported KES 81,391,500 in "
    "revenue for January to June 2026."
)
add_bullet(
    "Summarised business performance using product, branch, channel, and "
    "period-based metrics."
)
story.append(Paragraph(
    "Repository: github.com/kimirifelix-droid/plp-da-a6-duka-board-report",
    styles["CompactBody"],
))

story.append(Paragraph(
    "<b>Student Performance Exploratory Data Analysis</b>",
    styles["CompactBody"],
))
add_bullet(
    "Explored 1,200 student records and examined the relationship between "
    "study hours and student performance."
)
story.append(Paragraph(
    "Repository: github.com/kimirifelix-droid/plp-da-a5-student-performance-eda",
    styles["CompactBody"],
))

story.append(Paragraph(
    "<b>Mobile Money Agent Data Cleanup</b>",
    styles["CompactBody"],
))
add_bullet(
    "Practised data quality checks and cleaning using generated transaction "
    "and agent records."
)
story.append(Paragraph(
    "Repository: github.com/kimirifelix-droid/plp-da-a4-agent-data-cleanup",
    styles["CompactBody"],
))

add_section("EDUCATION")
story.append(Paragraph(
    "Development Studies with IT<br/>"
   "Institution: Tom Mboya University<br/>"
"Graduated: 2025",
))

add_section("PROFESSIONAL INTERESTS")
story.append(Paragraph(
    "Data analytics, evidence-based decision-making, business intelligence, "
    "community development, and NGO programme support.",
    styles["CompactBody"],
))

add_section("REFERENCES")
story.append(Paragraph(
    "Available on request.",
    styles["CompactBody"],
))

doc.build(story)
print(f"CV created successfully: {OUTPUT}")

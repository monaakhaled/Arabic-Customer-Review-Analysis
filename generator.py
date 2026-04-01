import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import matplotlib.pyplot as plt
import os

# CSV
def save_csv(reviews):
    df = pd.DataFrame({"reviews": reviews})
    path = "reviews.csv"
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return path

# PDF
def save_pdf(text):
    path = "analysis.pdf"
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    font_file = "DejaVuSans.ttf"
    if not os.path.exists(font_file):
        raise FileNotFoundError(f"{font_file} not found in project folder!")
    pdfmetrics.registerFont(TTFont("DejaVu", font_file))
    c.setFont("DejaVu", 10)

    y = height - 40
    lines = text.split("\n")
    for line in lines:
        if y < 40:
            c.showPage()
            c.setFont("DejaVu", 10)
            y = height - 40
        c.drawString(40, y, line)
        y -= 14

    c.save()
    return path

# Chart
def create_chart(reviews):
    lengths = [len(r) for r in reviews]
    plt.figure(figsize=(8,4))
    plt.bar(range(len(lengths)), lengths, color="#4CAF50")
    plt.xlabel("Reviews")
    plt.ylabel("Number of Characters")
    plt.title("Review Length Analysis")
    plt.tight_layout()
    path = "chart.png"
    plt.savefig(path)
    plt.close()
    return path
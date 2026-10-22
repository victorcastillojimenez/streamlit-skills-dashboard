from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import pandas as pd
import numpy as np
from datetime import date, timedelta
import os

from utils.data_loader import generate_mock_data

# Recrear los mismos datos simulados que en el dashboard
def load_data() -> pd.DataFrame:
    return generate_mock_data()

def create_pdf_report(filename="informe_dashboard.pdf"):
    df = load_data()
    
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Título
    title = Paragraph("Informe del Dashboard Analítico", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))
    
    # Resumen
    ventas_totales = df["Ventas"].sum()
    visitas_totales = df["Visitas"].sum()
    ticket_promedio = ventas_totales / visitas_totales if visitas_totales > 0 else 0
    
    story.append(Paragraph("Resumen General", styles['Heading2']))
    
    summary_data = [
        ["Métrica", "Valor"],
        ["Ventas Totales", f"${ventas_totales:,.0f}"],
        ["Visitas Totales", f"{visitas_totales:,.0f}"],
        ["Ticket Promedio", f"${ticket_promedio:.2f}"],
        ["Total de Registros", str(len(df))]
    ]
    
    summary_table = Table(summary_data, colWidths=[200, 200])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Ventas por Categoría
    story.append(Paragraph("Ventas por Categoría", styles['Heading2']))
    df_cat = df.groupby("Categoría")[["Ventas", "Visitas"]].sum().reset_index()
    
    cat_data = [["Categoría", "Ventas", "Visitas"]]
    for _, row in df_cat.iterrows():
        cat_data.append([row['Categoría'], f"${row['Ventas']:,.0f}", f"{row['Visitas']:,.0f}"])
        
    cat_table = Table(cat_data, colWidths=[150, 150, 150])
    cat_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.steelblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(cat_table)
    story.append(Spacer(1, 20))

    # Construir PDF
    doc.build(story)
    return filename

if __name__ == "__main__":
    report_file = create_pdf_report()
    print(f"Report generated: {os.path.abspath(report_file)}")

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from datetime import datetime

def generate_pdf_report(business, audit):
    """
    Generate a PDF report for a business audit
    """
    # Create filename
    filename = f"/tmp/{business.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    # Create PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2E7D32'),
        spaceAfter=30
    )
    story.append(Paragraph(f"Digital Presence Audit Report", title_style))
    story.append(Spacer(1, 12))
    
    # Business Info
    story.append(Paragraph(f"<b>Business Name:</b> {business.name}", styles['Normal']))
    story.append(Paragraph(f"<b>Category:</b> {business.category}", styles['Normal']))
    story.append(Paragraph(f"<b>City:</b> {business.city}", styles['Normal']))
    story.append(Paragraph(f"<b>Audit Date:</b> {audit.audited_at.strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Score Summary
    story.append(Paragraph("<b>Score Summary</b>", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    score_data = [
        ["Metric", "Score"],
        ["Instagram Score", f"{audit.instagram_score}/100"],
        ["Google Maps Score", f"{audit.google_maps_score}/100"],
        ["Website Score", f"{audit.website_score}/100"],
        ["Brand Consistency Score", f"{audit.brand_consistency_score}/100"],
        ["Customer Engagement Score", f"{audit.customer_engagement_score}/100"],
        ["Total Score", f"{audit.total_score}/100"],
        ["Rating", audit.rating]
    ]
    
    score_table = Table(score_data, colWidths=[200, 150])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(score_table)
    story.append(Spacer(1, 20))
    
    # Recommendations
    import json
    recommendations = json.loads(audit.recommendations) if audit.recommendations else {}
    
    story.append(Paragraph("<b>Recommendations</b>", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    for category, recs in recommendations.items():
        if recs:
            story.append(Paragraph(f"<b>{category.replace('_', ' ').title()}:</b>", styles['Heading3']))
            for rec in recs:
                story.append(Paragraph(f"• {rec}", styles['Normal']))
                story.append(Spacer(1, 6))
            story.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(story)
    return filename
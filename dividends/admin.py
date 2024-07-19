from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch
from .models import Dividens


@admin.register(Dividens)
class DividensAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number_of_promotion', 'price_of_promotion', 'total_sum_of_promotions',
                    'percent_of_dividends', 'calculated_dividend', 'holded_dividends', 'payable_dividens')
    actions = ['export_to_excel', 'export_to_pdf']

    def export_to_excel(self, request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="dividends.xlsx"'

        workbook = Workbook()
        worksheet = workbook.active
        worksheet.append(
            ['First Name', 'Last Name', 'Number of Promotion', 'Price of Promotion', 'Total Sum of Promotions',
             'Percent of Dividends', 'Calculated Dividend', 'Holded Dividends', 'Payable Dividens'])

        for obj in queryset:
            worksheet.append([obj.first_name, obj.last_name, obj.number_of_promotion, obj.price_of_promotion,
                              obj.total_sum_of_promotions, obj.percent_of_dividends, obj.calculated_dividend,
                              obj.holded_dividends, obj.payable_dividens])

        column_totals = ['', '', sum(obj.number_of_promotion for obj in queryset),
                         sum(obj.price_of_promotion for obj in queryset),
                         sum(obj.total_sum_of_promotions for obj in queryset),
                         3,
                         sum(obj.calculated_dividend for obj in queryset),
                         sum(obj.holded_dividends for obj in queryset),
                         sum(obj.payable_dividens for obj in queryset)]
        worksheet.append(column_totals)

        workbook.save(response)
        return response

    export_to_excel.short_description = "Export to Excel"

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="dividends.pdf"'

        doc = SimpleDocTemplate(response, pagesize=landscape(letter),
                                leftMargin=0.5 * inch, rightMargin=0.5 * inch,
                                topMargin=0.5 * inch, bottomMargin=0.5 * inch)
        elements = []

        # Table header
        headers = ['First Name', 'Last Name', 'Number', 'Price of Promotion', 'Total Sum',
                   'Percent of Dividends', 'Calculated Dividend', 'Holded Dividends', 'Payable Dividens']
        data = [headers]

        # Table content
        for obj in queryset:
            data.append([
                obj.first_name, obj.last_name, obj.number_of_promotion, obj.price_of_promotion,
                obj.total_sum_of_promotions, obj.percent_of_dividends, obj.calculated_dividend,
                obj.holded_dividends, obj.payable_dividens
            ])

        # Totals row
        data.append([
            '', '', sum(obj.number_of_promotion for obj in queryset),
            sum(obj.price_of_promotion for obj in queryset),
            sum(obj.total_sum_of_promotions for obj in queryset), 
            3.0,
            sum(obj.calculated_dividend for obj in queryset),
            sum(obj.holded_dividends for obj in queryset),
            sum(obj.payable_dividens for obj in queryset)
        ])

        # Create the table
        table = Table(data, colWidths=[0.8 * inch] * 2 + [1 * inch] * 7)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))

        elements.append(table)
        doc.build(elements)

        return response

    export_to_pdf.short_description = "Export to PDF"

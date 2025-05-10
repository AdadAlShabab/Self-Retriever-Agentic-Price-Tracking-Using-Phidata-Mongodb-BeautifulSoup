import pdfkit
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class ReportGenerator:
    def __init__(self, template_dir='src/report/templates'):
        self.env = Environment(loader=FileSystemLoader(template_dir))
    
    def generate_html_report(self, data):
        template = self.env.get_template('report_template.html')
        return template.render(data=data)
    
    def generate_pdf_report(self, data, output_path):
        html = self.generate_html_report(data)
        pdfkit.from_string(html, output_path)
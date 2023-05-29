# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:09:17 2023

@author: caragone
"""

import os
from PyPDF2 import PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

##cambiar a cualquier ruta donde se tiene las boletas
ruta = r'C:\Users\caragone\Downloads\Boletas'

tablita = [] 

encabezados = [
    "Nombres y Apellidos",
    "Cargo",
    "Sueldo",
    "Mes",
    "Dias Trabajados",
    "Dias No trabajados"
]
tablita.append(encabezados)
#%%
archivos_txt = [archivo for archivo in os.listdir(ruta) if archivo.endswith('.txt')]
for archivo in archivos_txt:
    ruta_archivo = os.path.join(ruta, archivo)
    with open(ruta_archivo, 'r') as archivo_txt:
        contenido = archivo_txt.readlines()
        ob = []
        for lineas in contenido:
            if ': ' in lineas:
                ditas = lineas.split(': ')[1]
                ob.append(ditas)
            else:
                ob.append('0')

        nuevo_registro = [
            ob[0],
            ob[1],
            ob[2],
            ob[3],
            ob[4],
            ob[5]
        ]
        tablita.append(nuevo_registro)
#%%
rutapdf= os.path.join(ruta, 'tabla.pdf')
doc = SimpleDocTemplate( rutapdf, pagesize=letter)
table = Table(tablita)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.greenyellow),  
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
    ('FONTSIZE', (0, 0), (-1, 0), 13),  
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  
    ('ALIGNMENT', (0, 0), (0, -1), 'CENTER'),
]))
elements = []
elements.append(table)
doc.build(elements)

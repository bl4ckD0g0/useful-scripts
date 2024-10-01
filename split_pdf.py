import PyPDF2
import os


def split_pdf(input_pdf_path, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Abre el archivo PDF que va a ser dividido en otros
    with open(input_pdf_path, 'rb') as input_pdf:
        reader = PyPDF2.PdfReader(input_pdf)
        num_pages = len(reader.pages)

        # Itera a través de todas las páginas y guarda cada una como un nuevo archivo PDF
        for page_num in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])

            output_pdf_path = os.path.join(output_folder, f'page_{page_num + 1}.pdf')
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)
            print(f'Página {page_num + 1} guardada en: {output_pdf_path}')


# Ejemplo de uso
input_pdf_path = 'C:\\Users\\myUser\\myPDF.pdf'
output_folder = 'C:\\Users\\myUser\\splitPDFs'
split_pdf(input_pdf_path, output_folder)

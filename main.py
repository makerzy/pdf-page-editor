# Install PyPDF2
import PyPDF2

def remove_page(pdf_file, page_number, output_full_path):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()

        for i in range(reader.numPages):
            if i != page_number:
                writer.addPage(reader.getPage(i))

        with open(output_full_path, 'wb') as output_file:
            writer.write(output_file)
            
            
def add_page(pdf_file, page_file, output_full_path):
    writer = PyPDF2.PdfFileWriter()
    
    # Open the input PDF file
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        
        # Add pages from input PDF
        for i in range(reader.numPages):
            writer.addPage(reader.getPage(i))

        # Open the page PDF file
        with open(page_file, 'rb') as page:
            page_reader = PyPDF2.PdfFileReader(page)
            
            # Add the first page from the page PDF
            writer.addPage(page_reader.getPage(0))
            
            # Write the combined PDF to a new file
            with open(output_full_path, 'wb') as output_file:
                writer.write(output_file)


"""
# Example usage:
# Remove page 4 from input.pdf

remove_page("input.pdf", 3, "C:\\...\\new_output_filename.pdf")


# Add a page from 'new_page.pdf' to 'input.pdf'
add_page("input.pdf", "new_page.pdf", "C:\\...\\new_output_filename.pdf")
"""



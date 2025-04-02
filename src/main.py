from Test1.scraper.scraper import PDF

client = PDF("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
# client.ExtrairPDF()
# client.BaixarPDF()
client.CompactarZipCSV()
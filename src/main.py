from Test1.scraper.scraper import PDF
from Test3.main import OperadoraDespesa


client = OperadoraDespesa()
client.ExtrairLinks()
client.BaixarArquivos()

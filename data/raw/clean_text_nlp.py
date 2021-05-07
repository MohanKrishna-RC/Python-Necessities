
from cleantext import clean

text = """
Zürich has a famous website https://www.zuerich.com/ 
WHICH ACCEPTS 40,000 € and adding a random string, :
abc123def456ghi789zero0 for this demo. Also remove punctions ,. 
my phone number is 9876543210 and mail me at satkr7@gmail.com.' """

clean_text = clean(text, fix_unicode=True, 
      to_ascii=True, 
      lower=True, 
      no_line_breaks=True,
      no_urls=True, 
      no_numbers=True, 
      no_digits=True, 
      no_currency_symbols=True, 
      no_punct=True, 
      replace_with_punct="", 
      replace_with_url="<URL>", 
      replace_with_number="<NUMBER>", 
      replace_with_digit="", 
      replace_with_currency_symbol="<CUR>",
      lang='en')

print(clean_text)

# Output: zurich has a famous website <url> which accepts <number> <cur> and adding a random string abcdefghizero for this demo also remove punctions my phone number is <number> and mail me at satkrgmailcom
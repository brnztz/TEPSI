from langchain.utilities import GoogleSerperAPIWrapper 
google_search = GoogleSerperAPIWrapper()
result = google_search.run("Variola do macaco")
print(result)
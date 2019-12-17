Admin panel located here - http://127.0.0.1:8000/admin/
To login use this credentials - User: admin, Password: admin

You can upload files from admin panel or with a POST request to this address - http://127.0.0.1:8000/pdf_scrapper_app/pdf_file/
in case of direct POST request use from-data and "file" as a key for file field

Get all links:
http://127.0.0.1:8000/pdf_scrapper_app/url_link/

Get all links for specific document(example):
http://127.0.0.1:8000/pdf_scrapper_app/url_link/?document=1
(Where 1 is id of document that were previously uploaded)

Get all pdf files that were uploaded:
http://127.0.0.1:8000/pdf_scrapper_app/pdf_file/

Get all links alongside with count of documents that contains links:
http://127.0.0.1:8000/pdf_scrapper_app/get_all_links_and_count_doc/
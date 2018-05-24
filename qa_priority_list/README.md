This script allows us to read/write documents on GOOGLE drive

Configuration:
==============

- Follow instructions on https://pygsheets.readthedocs.io/en/latest/authorizing.html in order to allow python to read/write
  * Select storage Admin
  * Copy the "Service account ID" created
- Share the document with the email created as "Service account ID"
- Store the credentials json file because we need it so python can perform actions on drive.
- Add ENV variables like
  * FILE_KEY is the key
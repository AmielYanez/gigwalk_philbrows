import gspread
from oauth2client.service_account import ServiceAccountCredentials

# TODO: move this to a env var so we can update permisions without deployment
credentials_json = {
  "type": "service_account",
  "project_id": "gigwalk-test",
  "private_key_id": "432343b49cab58a5ec630e55690d46bab6de9bfc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCu9lkRzcLpTp4s\nYNQ1R9TDeJwpDmbU8JFUWg6quS0DpyHnUD2gB6J6YVkZGWIyH++lgbW499wuba05\nFnJUJuBjHKSYi08UCEtOHsDvie5FeDVfKui53q43gH/ggF05Rc9RPaAGZMTdcpWl\nzPyOUX3qZMX0OXmPtu2TliHChniNP2ZD/ilbuihu6EjveDsR93Ng7MsY6VYND5IR\nfo9eo+XcxXNo6b21FIbBruvpVNRvNInKYzIamV+BRurXhTygRSPvv2VXFVfKCsRO\nO/X6CB6ujsycHf9Fhpunt5uB75Du3AJM6QDRzpgnO0cyfszZmMhrj0ROIGNm+c9Y\nExySRuklAgMBAAECggEAJ7XE+Hv9eYt87fCaKW+gtC7bLpxUrY7eRUldW9VEiLg1\nwzTcj8Y708/lc4Nl3J+P+j4K2yzyXd1JvBPCpiPeuNAG8ZJow9CwGs5zFsr09/J1\nFqD8CjemzfUN0QwBXJ7iE3vLprfXULWRjnyMc9a+H+V4YlprIzmvCVjBV8/Ca7gv\nTO6+MNSkxlJVCdyhjxMyaK7ooAQU1hwi5NgnJWi3J9lk0ZpXRbOCaLcj5qG2hq9D\nNSNASefZ+5y91evxxSGQOn7cNmegcofpPX/LxFeoaaiTlArREjpq8bmOWRtfLc+Y\nNqqvhU9U4Snf/qYOrRykRv8Aoyu3aJztdghn6GWn8QKBgQD25nvlCRBYAgtuwUx1\njNqH3Vx9NrehfQta/YHKLdNP2rVAzD/S1UWDkZgfcDNJMCzQTHQXD3/T3E1xfpV6\n61C/4BnIb4qcfw0k1Ge4gDBwOrLT1hj5aPvDzkakED5md2DWKUKeGfu2V5dFjqXm\n2viGMwhhoQhXg5TQH8IUfmB5KQKBgQC1aSAT83lY3QXTHK6Ziw4KqJ8TBAtCXdSl\nEl5oEkJ3wltuZKy5lz5fRQZlHB9mA0CoyDdHoiwtjeq+GegCMaPhvbAvbnWFos+A\nl8iZ5RMoOJ7PQmTvm3pGYeVg1K8astg4sJ/Mn7s7Oqtcej1VkYWrjDV8PnDEGwN6\n5YBI0awjnQKBgQDh9xe1CpKWuWhVOTwM6ZineATJ5GYzugnGgPVkYIRhNT1lzIkt\nIFu6imm7fCiz9w9MpGwrHthSwfFuyfdsxCjnMubl9o/Zor4Y0v0KcufiDxbTocLB\noT+qeQNV7Dfv95n85048/HLO82NTGbbkjcuept4o3ASSc66ivC4YK4GH4QKBgBxs\n3X7izqfS8h+zRdR/SnL3Gv3iy1TZ2QEIkMxj2BBl3ue8VKg7/6Tz7t2W+4CDj/Ui\nci8CRUPaEec5rfXyC0jK7TlxaG7JJRR0NBWRJGBQBupY7/HvfchbfJKgoNNhJKo1\nWsS4XqEYP1OdP9ERnU1VCehu7EJ+LRxrq589Y2itAoGAJ9jezwthR4aaLLBmOYXi\nseiwlhKvF0Ujeikdxg6oWliK+QDNpTNCUvUrTwh+Ifa/q4Bc08vJUt/t2lsZm2Cf\nGMiR6b72uLpyZEnyWoNAFOw+DCpvBe2Y9dBaRRGxIWVw8zXnr9ZeEhJcfwCFCHgg\n+leMBSy6H9nWpkb9QxpG2pE=\n-----END PRIVATE KEY-----\n",
  "client_email": "storage-test@gigwalk-test.iam.gserviceaccount.com",
  "client_id": "102868449285208668417",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/storage-test%40gigwalk-test.iam.gserviceaccount.com"
}


scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive',
  'https://www.googleapis.com/auth/spreadsheets'
]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)

gc = gspread.authorize(credentials)

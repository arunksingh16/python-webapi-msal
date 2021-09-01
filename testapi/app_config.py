import os

CLIENT_ID = "XXXX"
CLIENT_SECRET = "XXXX"
AUTHORITY = "XXXX"
REDIRECT_PATH = "/getAToken"
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"

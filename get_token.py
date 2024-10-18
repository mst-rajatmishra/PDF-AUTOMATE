from google.oauth2 import service_account
import google.auth.transport.requests

# Path to your service account key file
credentials = service_account.Credentials.from_service_account_file(
    '/Users/williamuhl/PDN/PRIVILEGING_look/onecred-pdm-42ae5eee730a.json',
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

# Request the token
auth_request = google.auth.transport.requests.Request()
credentials.refresh(auth_request)

# Print access token
print(credentials.token)

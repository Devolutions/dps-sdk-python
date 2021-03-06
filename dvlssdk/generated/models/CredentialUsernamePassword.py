from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class CredentialUsernamePassword:
    def __init__(self):
        self.AllowClipboard = False
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Domain = ''
        self.MnemonicPassword = ''
        self.PasswordItem = SensitiveItem()
        self.PromptForPassword = False
        self.UserName = ''


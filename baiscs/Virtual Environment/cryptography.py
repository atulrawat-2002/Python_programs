import os
import json
from cryptography.fernet import Fernet
from datetime import datetime


VAUL_FILE = 'notes_vault.json'
FILE_KEY = "vault.key"

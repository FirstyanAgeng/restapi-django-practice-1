from decouple import config

print(os.environ.get('DB_HOST'))
print(os.environ.get('DB_PORT'))
print(os.environ.get('DB_NAME'))
print(os.environ.get('DB_USER'))
print(os.environ.get('DB_PASS'))
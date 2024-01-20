# docker pull couchdb
# docker run -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password -d couchdb
import couchdb
from urllib.parse import quote
#from SensitiveInfo import Sensitive
COUCHDB_USERNAME = 'admin'
COUCHDB_PASSWORD = 'password'
couchdb_username = COUCHDB_USERNAME
couchdb_password = COUCHDB_PASSWORD
encoded_password = quote(couchdb_password)
server_url = f'http://{couchdb_username}:{encoded_password}@127.0.0.1:5984/'
server = couchdb.Server(server_url)


#Create a CouchDB data base
#db = server.create('sample_database')

"""
# Use this to delete the data base
database_name = 'sample_database'

# Check if the database exists before attempting to delete
if database_name in server:
    # Access the database
    db = server[database_name]

    # Delete the database
    del server[database_name]

    print(f"Database '{database_name}' successfully deleted.")
else:
    print(f"Database '{database_name}' does not exist.")
    
"""

# Specify the database name
database_name = 'aasdata01'
db = server[database_name]

"""
# Check if the database exists, and create it if not
if database_name not in server:
    server.create(database_name)

# Access the database
db = server[database_name]

# Data to be inserted into the database
machine_data = {
    'Machine': 'Robot Optical Inspection Machine',
    'MachineNumber': 'RCCESOI1001',
    'Year': 2020,
    'DrawingNumber': 'RCCESOI1001 - ED',
    'VoltageOrFrequency': '230VAC (P+N+PE) 50-60 Hz',
    'Current': '16A',
    'SwitchingCapacity': '10kA'
}

# Insert data into the database
doc_id, doc_rev = db.save(machine_data)

print(f"Data successfully inserted into the database with document ID: {doc_id}")
"""

for doc_id in db:
    doc = db[doc_id]

    # Iterate through each key-value pair in the document
    for key, value in doc.items():
        print(f"{key}: {value}")

    print("\n")  # Add a newline for better readability between documents

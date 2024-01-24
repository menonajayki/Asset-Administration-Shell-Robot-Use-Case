# Here the Asset Administration Shell is Implemented
* BaSyx python SDK is used for the implementation
* Reading CAN Data from Robot
  * PCAN driver leveraged
* couchDB database
* Storing the CAN data into couchDB and retrieved for user presentation through GUI

* Steps of AAS Creation
  1. AAS and Submodels created
  1. AASX Package File Created and Saved
  1. AASX converted to JSON
  1. JSON pushed to couchDB

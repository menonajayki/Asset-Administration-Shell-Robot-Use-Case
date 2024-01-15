# The goal of the program is to  create an Asset Administration Shell usinh Python BASYX Framework
#!/usr/bin/env python3
# This work is licensed under a Creative Commons CCZero 1.0 Universal License.
# See http://creativecommons.org/publicdomain/zero/1.0/ for more information.
"""
Tutorial for the creation of a simple Asset Administration Shell, containing an AssetInformation object and a Submodel
reference
"""
import tkinter as tk
from prettytable import PrettyTable
# Import all Eclipse BaSyx Python SDK classes from model package
from basyx.aas import model

# In this tutorial, you'll get a step-by-step guide on how to create an Asset Administration Shell (AAS) and all
# required objects within. First, you need an AssetInformation object for which you want to create an AAS. After that,
# an Asset Administration Shell can be created. Then, it's possible to add Submodels to the AAS. The Submodels can
# contain SubmodelElements.
#
# Step-by-Step Guide:
# Step 1: create a simple Asset Administration Shell, containing AssetInformation object
# Step 2: create a simple Submodel
# Step 3: create a simple Property and add it to the Submodel


############################################################################################
# Step 1: Create a Simple Asset Administration Shell Containing an AssetInformation object #
############################################################################################
# Step 1.1: create the AssetInformation object
asset_information = model.AssetInformation(
    asset_kind=model.AssetKind.INSTANCE,
    global_asset_id='http://acplt.org/Simple_Asset'
)

# step 1.2: create the Asset Administration Shell
identifier = 'https://acplt.org/Simple_AAS'
aas = model.AssetAdministrationShell(
    id_=identifier,  # set identifier
    asset_information=asset_information
)


#############################################################
# Step 2: Create a Simple Submodel Without SubmodelElements #
#############################################################

# Step 2.1: create the Submodel object
identifier = 'https://acplt.org/Simple_Submodel'
submodel = model.Submodel(
    id_=identifier
)

# Step 2.2: create a reference to that Submodel and add it to the Asset Administration Shell's `submodel` set
aas.submodel.add(model.ModelReference.from_referable(submodel))


# ===============================================================
# ALTERNATIVE: step 1 and 2 can alternatively be done in one step
# In this version, the Submodel reference is passed to the Asset Administration Shell's constructor.
submodel = model.Submodel(
    id_='https://acplt.org/Simple_Submodel'
)
aas = model.AssetAdministrationShell(
    id_='https://acplt.org/Simple_AAS',
    asset_information=asset_information,
    submodel={model.ModelReference.from_referable(submodel)}
)


###############################################################
# Step 3: Create a Simple Property and Add it to the Submodel #
###############################################################

# Step 3.1: create a global reference to a semantic description of the Property
# A global reference consist of one key which points to the address where the semantic description is stored
semantic_reference = model.ExternalReference(
    (model.Key(
        type_=model.KeyTypes.GLOBAL_REFERENCE,
        value='http://acplt.org/Properties/SimpleProperty'
    ),)
)

# Step 3.2: create the simple Property
property_ = model.Property(
    id_short='ExampleProperty',  # Identifying string of the element within the Submodel namespace
    value_type=model.datatypes.String,  # Data type of the value
    value='exampleValue',  # Value of the Property
    semantic_id=semantic_reference  # set the semantic reference
)

# Step 3.3: add the Property to the Submodel
submodel.submodel_element.add(property_)


# =====================================================================
# ALTERNATIVE: step 2 and 3 can also be combined in a single statement:
# Again, we pass the Property to the Submodel's constructor instead of adding it afterward.
submodel = model.Submodel(
    id_='https://acplt.org/Simple_Submodel',
    submodel_element={
        model.Property(
            id_short='ExampleProperty',
            value_type=model.datatypes.String,
            value='exampleValue',
            semantic_id=model.ExternalReference(
                (model.Key(
                    type_=model.KeyTypes.GLOBAL_REFERENCE,
                    value='http://acplt.org/Properties/SimpleProperty'
                ),)
            )
        )
    }
)



# Create a simple Asset Administration Shell
asset_information = model.AssetInformation(
    asset_kind=model.AssetKind.INSTANCE,
    global_asset_id='http://acplt.org/Simple_Asset'
)

aas = model.AssetAdministrationShell(
    id_='https://acplt.org/Simple_AAS',
    asset_information=asset_information
)

# Create a PrettyTable for AAS data
aas_table = PrettyTable(["AAS ID", "Asset Kind", "Global Asset ID"])
aas_table.add_row([aas.id, asset_information.asset_kind, asset_information.global_asset_id])

# Print AAS table
print("Asset Administration Shell:")
print(aas_table)

# Create a hypothetical ModelProvider (replace this with the actual provider if available)
model_provider = ...

# Create a PrettyTable for Submodel data
submodel_table = PrettyTable(["Submodel ID"])

# Add Submodel information to the table
for ref in aas.submodel:
    submodel = ref.resolve(model_provider)  # Adjust based on SDK documentation
    submodel_table.add_row([submodel.id])

# Print Submodel table
print("\nSubmodels:")
print(submodel_table)

# Create a PrettyTable for SubmodelElement data
submodel_element_table = PrettyTable(["Submodel Element ID", "Value Type", "Value"])

# Add SubmodelElement information to the table
for ref in aas.submodel:
    submodel = ref.resolve(model_provider)  # Adjust based on SDK documentation
    for element in submodel.submodel_element:
        submodel_element_table.add_row([element.id_short, element.value_type, element.value])

print("\nSubmodel Elements:")
print(submodel_element_table)

def create_aas():
    # Create a simple Asset Administration Shell
    asset_information = model.AssetInformation(
        asset_kind=model.AssetKind.INSTANCE,
        global_asset_id='http://acplt.org/Simple_Asset'
    )

    aas = model.AssetAdministrationShell(
        id_='https://acplt.org/Simple_AAS',
        asset_information=asset_information
    )

    return aas

def display_aas_table():
    aas = create_aas()

    # Create AAS table
    aas_table = PrettyTable(["AAS ID", "Asset Kind", "Global Asset ID"])
    aas_table.add_row([aas.id, aas.asset_information.asset_kind, aas.asset_information.global_asset_id])

    # Display AAS table in a new window
    window = tk.Tk()
    window.title("AAS Viewer")

    aas_label = tk.Label(window, text="Asset Administration Shell:")
    aas_label.pack()

    aas_text = tk.Text(window, height=100, width=100)
    aas_text.insert(tk.END, str(aas_table))
    aas_text.pack()

    window.mainloop()

# Call the function to display the AAS table
display_aas_table()
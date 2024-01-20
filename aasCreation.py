import tkinter as tk
from prettytable import PrettyTable
from basyx.aas import model

asset_information = model.AssetInformation(
    asset_kind=model.AssetKind.INSTANCE,
    global_asset_id='http://acplt.org/Simple_Asset'
)

identifier = 'https://acplt.org/Simple_AAS'
aas = model.AssetAdministrationShell(
    id_=identifier,  # set identifier
    asset_information=asset_information
)


identifier = 'https://acplt.org/Simple_Submodel'
submodel = model.Submodel(
    id_=identifier
)


aas.submodel.add(model.ModelReference.from_referable(submodel))


submodel = model.Submodel(
    id_='https://acplt.org/Simple_Submodel'
)
aas = model.AssetAdministrationShell(
    id_='https://acplt.org/Simple_AAS',
    asset_information=asset_information,
    submodel={model.ModelReference.from_referable(submodel)}
)


semantic_reference = model.ExternalReference(
    (model.Key(
        type_=model.KeyTypes.GLOBAL_REFERENCE,
        value='http://acplt.org/Properties/SimpleProperty'
    ),)
)


property_ = model.Property(
    id_short='ExampleProperty',
    value_type=model.datatypes.String,
    value='exampleValue',
    semantic_id=semantic_reference
)

submodel.submodel_element.add(property_)

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


asset_information = model.AssetInformation(
    asset_kind=model.AssetKind.INSTANCE,
    global_asset_id='http://acplt.org/Simple_Asset'
)

aas = model.AssetAdministrationShell(
    id_='https://acplt.org/Simple_AAS',
    asset_information=asset_information
)

aas_table = PrettyTable(["AAS ID", "Asset Kind", "Global Asset ID"])
aas_table.add_row([aas.id, asset_information.asset_kind, asset_information.global_asset_id])


print("Asset Administration Shell:")
print(aas_table)


model_provider = ...

submodel_table = PrettyTable(["Submodel ID"])

for ref in aas.submodel:
    submodel = ref.resolve(model_provider)
    submodel_table.add_row([submodel.id])

# Print Submodel table
print("\nSubmodels:")
print(submodel_table)


submodel_element_table = PrettyTable(["Submodel Element ID", "Value Type", "Value"])


for ref in aas.submodel:
    submodel = ref.resolve(model_provider)
    for element in submodel.submodel_element:
        submodel_element_table.add_row([element.id_short, element.value_type, element.value])

print("\nSubmodel Elements:")
print(submodel_element_table)

def create_aas():

    asset_information = model.AssetInformation(
        asset_kind=model.AssetKind.INSTANCE,
        global_asset_id='http://acplt.org/Simple_Asset'
    )

    aas = model.AssetAdministrationShell(
        id_='https://acplt.org/Simple_AAS',
        asset_information=asset_information
    )

    return aas

def display_aas_ui():
    aas = create_aas()


    window = tk.Tk()
    window.title("AAS Viewer")


    aas_id_label = tk.Label(window, text="AAS ID:")
    aas_id_label.grid(row=0, column=0, padx=5, pady=5)

    aas_id_entry = tk.Entry(window, width=50)
    aas_id_entry.insert(0, aas.id)
    aas_id_entry.config(state='readonly')
    aas_id_entry.grid(row=0, column=1, padx=5, pady=5)


    asset_kind_label = tk.Label(window, text="Asset Kind:")
    asset_kind_label.grid(row=1, column=0, padx=5, pady=5)

    asset_kind_entry = tk.Entry(window, width=50)
    asset_kind_entry.insert(0, aas.asset_information.asset_kind)
    asset_kind_entry.config(state='readonly')
    asset_kind_entry.grid(row=1, column=1, padx=5, pady=5)


    global_asset_id_label = tk.Label(window, text="Global Asset ID:")
    global_asset_id_label.grid(row=2, column=0, padx=5, pady=5)

    global_asset_id_entry = tk.Entry(window, width=50)
    global_asset_id_entry.insert(0, aas.asset_information.global_asset_id)
    global_asset_id_entry.config(state='readonly')
    global_asset_id_entry.grid(row=2, column=1, padx=5, pady=5)


    window.mainloop()

display_aas_ui()
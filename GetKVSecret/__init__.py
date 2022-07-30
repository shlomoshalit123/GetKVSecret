import logging
import os
import azure.functions as func
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('secretname')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('secretname')

    logging.info(f'value of name is: {name}.')
    
    if name:
        secretname = name
        TENANT_ID = os.environ["TENANT_ID"]
        CLIENT_ID = os.environ["CLIENT_ID"]
        CLIENT_SECRET = os.environ["CLIENT_SECRET"] 
        KEYVAULT_NAMES = ["VaronisAssignmentKeyv1", "VaronisAssignmentKeyv2", "VaronisAssignmentKeyv3"]

        credential = ClientSecretCredential(
            tenant_id=TENANT_ID,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )

        JsonOutput = ''
        
        for keyvault in KEYVAULT_NAMES:
            logging.info(f'searching in valut {keyvault} for secret: {secretname}.')
            KEYVAULT_URI = 'https://' + keyvault + '.vault.azure.net/'
            secret_client = SecretClient(vault_url=KEYVAULT_URI, credential=credential)
            secret_properties = secret_client.list_properties_of_secrets()
            for secret_property in secret_properties:
                            if secret_property.name == secretname:
                                logging.info(f'found in {keyvault} secret: {secretname}.')
                                secretvalue = secret_client.get_secret(secretname)
                                JsonOutput = {}
                                JsonOutput['Name'] = secret_property.name       
                                JsonOutput['created_on'] = secret_property.created_on.ctime()
                                JsonOutput['keyvault'] = keyvault
                                JsonOutput['Value'] = secretvalue.value
                                if JsonOutput:
                                    logging.info(f'{JsonOutput}')
                                    break
        if JsonOutput != '':
            return func.HttpResponse(f"{JsonOutput}")
        else:
            return func.HttpResponse(
                "Error.",
                status_code=400
            )
    else:
        return func.HttpResponse(
                "Error.",
                status_code=400
        )
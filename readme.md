function to pull secret from azure key vault using app registration

pass one of the following secret names to pull secret details from azure key vault using azure function app:

Paramater: secretname

possible vallues:

VaronisAssignmentSecret1, VaronisAssignmentSecret2, VaronisAssignmentSecret3

function url:

https://azurekeyvaultpython.azurewebsites.net/api/GetKVSecret?code=oNtyIRXCfMIe1L40RZa58qpMfnf1gnCRq3G-JVQbDKLQAzFu9Yj-gg==

example:

https://azurekeyvaultpython.azurewebsites.net/api/GetKVSecret?code=oNtyIRXCfMIe1L40RZa58qpMfnf1gnCRq3G-JVQbDKLQAzFu9Yj-gg==&secretname=VaronisAssignmentSecret2
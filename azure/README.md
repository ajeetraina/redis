# Setting up Redis Enterprise on Azure


```
ajeetraina@Ajeet-Rainas-Macbook-Pro Downloads % az login
You have logged in. Now let us find all the subscriptions to which you have access...
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "86b4ea12-4806-4158-a926-9e3d06286f0f",
    "id": "3d93b920-48e1-401d-a6af-bf48877c94ed",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "86b4ea12-4806-4158-a926-9e3d06286f0f",
    "user": {
      "name": "Ajeet.Raina@Redis212.onmicrosoft.com",
      "type": "user"
    }
  }
]
```


```
ajeetraina@Ajeet-Rainas-Macbook-Pro Downloads % az group create --name myResourceGroup --location centralus
{
  "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup",
  "location": "centralus",
  "managedBy": null,
  "name": "myResourceGroup",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
ajeetraina@Ajeet-Rainas-Macbook-Pro Downloads %
```

```
ajeetraina@Ajeet-Rainas-Macbook-Pro Downloads % az vm create \
  --resource-group "myResourceGroup" \
  --name "myVM" \
  --image "UbuntuLTS" \
  --admin-username "demouser" \
  --admin-password "demouser@123" \
  --location centralus
{
  "fqdns": "",
  "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
  "location": "centralus",
  "macAddress": "00-0D-3A-42-9F-01",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "13.67.135.124",
  "resourceGroup": "myResourceGroup",
  "zones": ""
}
```

```
az vm open-port --port 80 --resource-group myResourceGroup --name myVM
```

```
ajeetraina@Ajeet-Rainas-Macbook-Pro Downloads % az vm open-port --port 80 --resource-group myResourceGroup --name myVM
{
  "defaultSecurityRules": [
    {
      "access": "Allow",
      "description": "Allow inbound traffic from all VMs in VNET",
      "destinationAddressPrefix": "VirtualNetwork",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/defaultSecurityRules/AllowVnetInBound",
      "name": "AllowVnetInBound",
      "priority": 65000,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "VirtualNetwork",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Allow",
      "description": "Allow inbound traffic from azure load balancer",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/defaultSecurityRules/AllowAzureLoadBalancerInBound",
      "name": "AllowAzureLoadBalancerInBound",
      "priority": 65001,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "AzureLoadBalancer",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Deny",
      "description": "Deny all inbound traffic",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/defaultSecurityRules/DenyAllInBound",
      "name": "DenyAllInBound",
      "priority": 65500,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Allow",
      "description": "Allow outbound traffic from all VMs to all VMs in VNET",
      "destinationAddressPrefix": "VirtualNetwork",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Outbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/defaultSecurityRules/AllowVnetOutBound",
      "name": "AllowVnetOutBound",
      "priority": 65000,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "VirtualNetwork",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Allow",
      "description": "Allow outbound traffic from all VMs to Internet",
      "destinationAddressPrefix": "Internet",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Outbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/defaultSecurityRules/AllowInternetOutBound",
      "name": "AllowInternetOutBound",
      "priority": 65001,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Deny",
      "description": "Deny all outbound traffic",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Outbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/defaultSecurityRules/DenyAllOutBound",
      "name": "DenyAllOutBound",
      "priority": 65500,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    }
  ],
  "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
  "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG",
  "location": "centralus",
  "name": "myVMNSG",
  "networkInterfaces": [
    {
      "dnsSettings": null,
      "enableAcceleratedNetworking": null,
      "enableIpForwarding": null,
      "etag": null,
      "hostedWorkloads": null,
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/myVMVMNic",
      "ipConfigurations": null,
      "location": null,
      "macAddress": null,
      "name": null,
      "networkSecurityGroup": null,
      "primary": null,
      "privateEndpoint": null,
      "provisioningState": null,
      "resourceGroup": "myResourceGroup",
      "resourceGuid": null,
      "tags": null,
      "tapConfigurations": null,
      "type": null,
      "virtualMachine": null
    }
  ],
  "provisioningState": "Succeeded",
  "resourceGroup": "myResourceGroup",
  "resourceGuid": "0377639a-f6ca-4b8b-bb67-7a942c7748d9",
  "securityRules": [
    {
      "access": "Allow",
      "description": null,
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "22",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/securityRules/default-allow-ssh",
      "name": "default-allow-ssh",
      "priority": 1000,
      "protocol": "Tcp",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/securityRules"
    },
    {
      "access": "Allow",
      "description": null,
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationApplicationSecurityGroups": null,
      "destinationPortRange": "80",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"c00e3e7a-76c8-456c-a26f-1e56dbf54eaf\"",
      "id": "/subscriptions/3d93b920-48e1-401d-a6af-bf48877c94ed/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG/securityRules/open-port-80",
      "name": "open-port-80",
      "priority": 900,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "myResourceGroup",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourceApplicationSecurityGroups": null,
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/securityRules"
    }
  ],
  "subnets": null,
  "tags": {},
  "type": "Microsoft.Network/networkSecurityGroups"
}
```

# Download Redis Enterprise software

## Please Note:

In case you encounter the below issue:

```
When port 53 is in use, the installation fails. This is known to happen in default Ubuntu 18.04 installations in which systemd-resolved (DNS server) is running. To workaround this issue, change the system configuration to make this port available before running RS installation.
Example steps to resolve the port 53 conflict:
```

```
sudo vi /etc/systemd/resolved.conf
```

```
Add DNSStubListener=no
```

as the last line in the file and save the file.

```
sudo mv /etc/resolv.conf /etc/resolv.conf.orig
sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
sudo service systemd-resolved restart
```






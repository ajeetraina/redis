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


```
Unpacking sntp (1:4.2.8p10+dfsg-5ubuntu7.1) ...
Setting up ntpdate (1:4.2.8p10+dfsg-5ubuntu7.1) ...
Setting up libopts25:amd64 (1:5.18.12-4) ...
Setting up sntp (1:4.2.8p10+dfsg-5ubuntu7.1) ...
Setting up ntp (1:4.2.8p10+dfsg-5ubuntu7.1) ...
Created symlink /etc/systemd/system/network-pre.target.wants/ntp-systemd-netif.path → /lib/systemd/system/ntp-systemd-netif.path.
Created symlink /etc/systemd/system/multi-user.target.wants/ntp.service → /lib/systemd/system/ntp.service.
ntp-systemd-netif.service is a disabled or a static unit, not starting it.
Processing triggers for systemd (237-3ubuntu10.39) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
2020-03-11 18:54:33 [$] executing: 'ntpdate-debian -u'
11 Mar 18:54:43 ntpdate[16477]: adjust time server 206.55.191.142 offset 0.006343 sec
2020-03-11 18:54:43 [!] Note: Log files will be stored on the root file system, in path /var/opt/redislabs/log

RedisLabs rest-api documentation has been deployed in /usr/share/doc/redislabs .

2020-03-11 18:54:45 [!] Installation is complete!
2020-03-11 18:54:45 [$] executing: '/opt/redislabs/bin/rlcheck --retry=10 --suppress-tests=verify_bootstrap_status,verify_processes,verify_pidfiles,verify_tcp_connectivity'
Saving to file: /var/opt/redislabs/log/rlcheck.log
(Remark : Will stop on first failure)
##### Welcome to RedisLabs Enterprise Cluster settings verification utility ####
Skipping test: verify_bootstrap_status
Skipping test: verify_processes
Running test: verify_dmcproxy
		PASS
Running test: verify_port_range
		PASS
Skipping test: verify_pidfiles
Running test: verify_capabilities
		PASS
Running test: verify_existing_sockets
		PASS
Running test: verify_host_settings
		PASS
Skipping test: verify_tcp_connectivity
Summary:
-------
ALL TESTS PASSED.


2020-03-11 18:54:46 [$] executing: 'chown redislabs:redislabs /var/opt/redislabs/log/rlcheck.log'
2020-03-11 18:54:46 [!] Please logout and login again to make sure all environment changes are applied.
2020-03-11 18:54:46 [!] Point your browser at the following URL to continue:
2020-03-11 18:54:46 [!] https://10.0.0.4:8443
2020-03-11 18:54:46 [$] executing: 'chmod 640 /tmp/install.log'
2020-03-11 18:54:46 [$] executing: 'chown redislabs:redislabs /tmp/install.log'
2020-03-11 18:54:46 [$] executing: 'chown redislabs:redislabs /etc/opt/redislabs/redislabs_env_config.sh'
```

You might need to enable 8443 port for accessing Redis Enterprise on Microsoft Azure.





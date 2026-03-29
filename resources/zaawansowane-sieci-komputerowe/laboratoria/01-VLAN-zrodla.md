# VLAN — Źródła do definicji (slajdy 2-6)

**Przedmiot:** Zaawansowane Sieci Komputerowe
**Temat 25:** VLAN — Wirtualne Sieci Lokalne
**Data:** 2026-03-28

---

## Slajd 2 — Definicja VLAN

**Definicja:** "VLAN (Virtual Local Area Network) to logiczne podzielenie jednej fizycznej sieci komputerowej na kilka odrebnych sieci wirtualnych."

**Zrodla:**
- Juniper Networks Documentation — "A VLAN (virtual LAN) abstracts the idea of the local area network (LAN) by providing data link connectivity for a subnet. VLANs make it easy for network administrators to partition a single switched network to match the functional and security requirements of their systems without having to run new cables or make major changes in their current network infrastructure."
  - URL: https://www.juniper.net/documentation/us/en/software/junos/multicast-l2/topics/concept/interfaces-802-1q-vlans-overview.html

- Cisco Documentation — "A Virtual Local Area Network (VLAN) allows you to logically segment a Local Area Network (LAN) into different broadcast domains."
  - URL: https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5653-configure-port-to-vlan-interface-settings-on-a-switch-throug.html

---

## Slajd 3 — Korzysci z VLAN (bezpieczenstwo, wydajnosc, elastycznosc)

**Zrodla:**
- Cisco Documentation — "In scenarios where sensitive data may be broadcast on a network, VLANs can be created to enhance security by designating a broadcast to a specific VLAN. Only users that belong to a VLAN are able to access and manipulate the data on that VLAN."
  - URL: https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5653-configure-port-to-vlan-interface-settings-on-a-switch-throug.html

- Cisco Documentation — "VLANs can also be used to enhance performance by reducing the need to send broadcasts and multicasts to unnecessary destinations. It also eases network configuration by logically connecting devices without physically relocating those devices."
  - URL: https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5653-configure-port-to-vlan-interface-settings-on-a-switch-throug.html

---

## Slajd 4 — Typy VLAN (Data, Native, Management, Voice)

**Zrodla:**
- Cisco Documentation — "VLANs are typically used to isolate endpoints as a workgroup. A basic example is setting up a different VLAN for Voice and a separate VLAN for Data. This ensures that packets for both data types are isolated from each other."
  - URL: https://www.cisco.com/c/en/us/support/docs/smb/switches/Cisco-Business-Switching/kmgmt-2253-assign-an-interface-vlan-as-an-access-or-trunk-port-on-a-swi.html

- Cisco IOS Documentation — "VLAN 1 is the default VLAN on all trunk ports in all Cisco switches."
  - URL: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst1000/software/releases/15_2_7_e/configuration_guides/vlan/b_1527e_vlan_c1000_cg/configuring_vlan_trunks.pdf

---

## Slajd 5 — Access port vs Trunk port

**Definicja Access port:**
- Cisco Documentation — "Access port — A port that carries traffic only to and from the specific VLAN assigned to it." / "Access ports are used primarily for hosts and can only carry traffic for a single VLAN."
  - URL: https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5653-configure-port-to-vlan-interface-settings-on-a-switch-throug.html

**Definicja Trunk port:**
- Cisco Documentation — "Trunk port — A port that is capable of carrying traffic for any or all the VLANs that are accessible by a specific switch." / "Trunk ports are for links between switches or other network devices and are capable of carrying traffic for multiple VLANs."
  - URL: https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5653-configure-port-to-vlan-interface-settings-on-a-switch-throug.html

- Cisco Nexus Documentation — "Trunks carry the traffic of multiple VLANs over a single link and allow you to extend VLANs across the network."
  - URL: https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5000/sw/layer2/503_n2_1/503_n2_1nw/Cisco_n5k_layer2_config_gd_rel_503_N2_1_chapter6.html

---

## Slajd 6 — Standard IEEE 802.1Q

**Zrodla:**
- IEEE Standards Association — oficjalny standard IEEE 802.1Q-2018
  - URL: https://standards.ieee.org/ieee/802.1Q/6844/

- Wikipedia — IEEE 802.1Q — "IEEE 802.1Q, often referred to as Dot1q, is the networking standard that supports virtual local area networking (VLANs) on an IEEE 802.3 Ethernet network. The standard defines a system of VLAN tagging for Ethernet frames."
  - URL: https://en.wikipedia.org/wiki/IEEE_802.1Q

- Wikipedia — "A 12-bit field specifying the VLAN to which the frame belongs. The values of 0 and 4095 are reserved. All other values may be used as VLAN identifiers, allowing up to 4,094 VLANs."
  - URL: https://en.wikipedia.org/wiki/IEEE_802.1Q

---

## Podsumowanie zrodel

| Slajd | Definicja | Zrodlo |
|-------|-----------|--------|
| 2 | Definicja VLAN | Juniper Networks Docs + Cisco Docs |
| 3 | Korzysci (bezpieczenstwo, wydajnosc) | Cisco Documentation |
| 4 | Typy VLAN (Data, Native, Voice) | Cisco Documentation |
| 5 | Access port vs Trunk port | Cisco Documentation (oficjalne) |
| 6 | IEEE 802.1Q, VLAN ID 1-4094 | IEEE Standards + Wikipedia |

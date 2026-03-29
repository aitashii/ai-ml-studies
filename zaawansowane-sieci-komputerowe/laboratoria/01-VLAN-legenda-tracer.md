# VLAN — Legenda do Packet Tracera (tekst do wpisania)

Skopiuj ponizszy tekst do pola tekstowego (Note) w Packet Tracerze.
Edit > Select All > Place Note lub prawy klik na workspace > Add Note.

---

## Tekst do wklejenia w legendzie:

LEGENDA — VLAN Sprint #78
==========================

VLAN 10 - IT (kolor niebieski)
PC-IT-1, IP: 192.168.10.1, port Fa0/5
PC-IT-2, IP: 192.168.10.2, port Fa0/6
-------
VLAN 20 - HR (kolor zielony)
PC-HR-1, IP: 192.168.20.1, port Fa0/3
PC-HR-2, IP: 192.168.20.2, port Fa0/4
-------
VLAN 30 - ZARZAD (kolor czerwony)
PC-ZARZAD-1, IP: 192.168.30.1, port Fa0/1
PC-ZARZAD-2, IP: 192.168.30.2, port Fa0/2

SWITCH: SWITCH-GLOWNY
Model: Cisco Catalyst 2960-24TT
Subnet Mask wszedzie: 255.255.255.0

TEST PING:
OK:    ping 192.168.10.2  (ten sam VLAN)
BLOK:  ping 192.168.20.1  (inny VLAN)

---

## Co mowic przy legendzie (dla kolegi):

Slajd 8 - przy schemacie Packet Tracera powiedz:

"W Cisco Packet Tracer przygotowalismy siec firmy
z jednym switchem i szescioma komputerami w trzech dzialach.

Kazdy dzial ma swoj kolor i swoj VLAN:
- niebieski to dzial IT, VLAN 10, adresy 192.168.10.x
- zielony to dzial HR, VLAN 20, adresy 192.168.20.x
- czerwony to Zarzad, VLAN 30, adresy 192.168.30.x

Kazdy komputer jest podlaczony do portu access na switchu.
Konfiguracje VLAN-ow wpisalismy recznie w CLI switcha.

Sprawdzilismy ze ping dziala miedzy komputerami
w tym samym VLAN-ie, ale nie dziala miedzy roznymi VLAN-ami.
To jest wlasnie cel VLAN — izolacja ruchu miedzy dzialami."

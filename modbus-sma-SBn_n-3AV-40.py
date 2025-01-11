# Supported hardware and firmware:
# SUNNY TRIPOWER 8.0 / SUNNY TRIPOWER 10.0
# Sunny Boy: STP8.0-3AV-40, STP10.0-3AV-40
# Starting with software package: 3.10.15.R


# Full list of readable registers - comment out registers you aren't interested in for faster performance
#
# Descriptions generated by using the following formula in SMA_Modbus-TI-en-26.xlsx - available from SMA web site
#   ="  ['"&A3&" - "&IFERROR(LEFT(B3,FIND(":",B3)-1),B3)&IF(C3<>""," ("&C3&")","")&"',"&A3&",'"&D3&"','"&E3&"'],"

sma_registers = [
  ['30201 - Condition',30201,'U32','ENUM'],
  ['30529 - Total yield (Wh)',30529,'U32','FIX0'],
  ['30531 - Total yield (kWh)',30531,'U32','FIX0'],
  ['30533 - Total yield (MWh)',30533,'U32','FIX0'],
  ['30535 - Daily yield (Wh)',30535,'U32','FIX0'],
  ['30537 - Daily yield (kWh)',30537,'U32','FIX0'],
  ['30539 - Daily yield (MWh)',30539,'U32','FIX0'],
  ['30581 - Total Grid feed-in counter reading (Wh)',30581,'U32','FIX0'],
  # ['30583 - Grid feed-in counter reading (Wh)',30583,'U32','FIX0'],
  ['30865 - Total Power draw from grid (W)',30865,'S32','FIX0'],
  ['31265 - Power draw from grid L1 (W)',31265,'U32','FIX0'],
  ['31267 - Power draw from grid L2 (W)',31267,'U32','FIX0'],
  ['31269 - Power draw from grid L3 (W)',31269,'U32','FIX0'],
  ['31259 - Power supply to grid L1 (W)',31259,'U32','FIX0'],
  ['31261 - Power supply to grid L2 (W)',31261,'U32','FIX0'],
  ['31263 - Power supply to grid L3 (W)',31263,'U32','FIX0'],
  ['31257 - Grid voltage L1 (V)',31257,'U32','FIX2'],
  ['31253 - Grid voltage L2 (V)',31253,'U32','FIX2'],
  ['31255 - Grid voltage L3 (V)',31255,'U32','FIX2'],
  ['30775 - Total PV Power (W)',30775,'S32','FIX0'],
  ['30777 - PV Power L1 (W)',30777,'S32','FIX0'],
  ['30779 - PV Power L2 (W)',30779,'S32','FIX0'],
  ['30781 - PV Power L3 (W)',30781,'S32','FIX0']
]

# scan is not used for SMA inverters but solariot.py expects it to exist
scan = "{}"

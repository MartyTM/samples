import json

ALdb = open('ALdb.json', 'r')
AKdb = open('AKdb.json', 'r')
AZdb = open('AZdb.json', 'r')
ARdb = open('ARdb.json', 'r')
CAdb = open('CAdb.json', 'r')
COdb = open('COdb.json', 'r')
CTdb = open('CTdb.json', 'r')
DEdb = open('DEdb.json', 'r')
FLdb = open('FLdb.json', 'r')
GAdb = open('GAdb.json', 'r')
HIdb = open('HIdb.json', 'r')
IDdb = open('IDdb.json', 'r')
ILdb = open('ILdb.json', 'r')
INdb = open('INdb.json', 'r')
IAdb = open('IAdb.json', 'r')
KSdb = open('KSdb.json', 'r')
KYdb = open('KYdb.json', 'r')
LAdb = open('LAdb.json', 'r')
MEdb = open('MEdb.json', 'r')
MDdb = open('MDdb.json', 'r')
MAdb = open('MAdb.json', 'r')
MIdb = open('MIdb.json', 'r')
MNdb = open('MNdb.json', 'r')
MSdb = open('MSdb.json', 'r')
MOdb = open('MOdb.json', 'r')
MTdb = open('MTdb.json', 'r')
NEdb = open('NEdb.json', 'r')
NVdb = open('NVdb.json', 'r')
NHdb = open('NHdb.json', 'r')
NJdb = open('NJdb.json', 'r') #Best db
NMdb = open('NMdb.json', 'r')
NYdb = open('NYdb.json', 'r')
NCdb = open('NCdb.json', 'r')
NDdb = open('NDdb.json', 'r')
OHdb = open('OHdb.json', 'r')
OKdb = open('OKdb.json', 'r')
ORdb = open('ORdb.json', 'r')
PAdb = open('PAdb.json', 'r')
RIdb = open('RIdb.json', 'r')
SCdb = open('SCdb.json', 'r')
SDdb = open('SDdb.json', 'r')
TNdb = open('TNdb.json', 'r')
TXdb = open('TXdb.json', 'r')
UTdb = open('UTdb.json', 'r')
VTdb = open('VTdb.json', 'r')
VAdb = open('VAdb.json', 'r')
WAdb = open('WAdb.json', 'r')
WVdb = open('WVdb.json', 'r')
WIdb = open('WIdb.json', 'r')
WYdb = open('WYdb.json', 'r')

ALdb_text = open('text/ALdb', 'w')
AKdb_text = open('text/AKdb', 'w')
AZdb_text = open('text/AZdb', 'w')
ARdb_text = open('text/ARdb', 'w')
CAdb_text = open('text/CAdb', 'w')
COdb_text = open('text/COdb', 'w')
CTdb_text = open('text/CTdb', 'w')
DEdb_text = open('text/DEdb', 'w')
FLdb_text = open('text/FLdb', 'w')
GAdb_text = open('text/GAdb', 'w')
HIdb_text = open('text/HIdb', 'w')
IDdb_text = open('text/IDdb', 'w')
ILdb_text = open('text/ILdb', 'w')
INdb_text = open('text/INdb', 'w')
IAdb_text = open('text/IAdb', 'w')
KSdb_text = open('text/KSdb', 'w')
KYdb_text = open('text/KYdb', 'w')
LAdb_text = open('text/LAdb', 'w')
MEdb_text = open('text/MEdb', 'w')
MDdb_text = open('text/MDdb', 'w')
MAdb_text = open('text/MAdb', 'w')
MIdb_text = open('text/MIdb', 'w')
MNdb_text = open('text/MNdb', 'w')
MSdb_text = open('text/MSdb', 'w')
MOdb_text = open('text/MOdb', 'w')
MTdb_text = open('text/MTdb', 'w')
NEdb_text = open('text/NEdb', 'w')
NVdb_text = open('text/NVdb', 'w')
NHdb_text = open('text/NHdb', 'w')
NJdb_text = open('text/NJdb', 'w') #Best db
NMdb_text = open('text/NMdb', 'w')
NYdb_text = open('text/NYdb', 'w')
NCdb_text = open('text/NCdb', 'w')
NDdb_text = open('text/NDdb', 'w')
OHdb_text = open('text/OHdb', 'w')
OKdb_text = open('text/OKdb', 'w')
ORdb_text = open('text/ORdb', 'w')
PAdb_text = open('text/PAdb', 'w')
RIdb_text = open('text/RIdb', 'w')
SCdb_text = open('text/SCdb', 'w')
SDdb_text = open('text/SDdb', 'w')
TNdb_text = open('text/TNdb', 'w')
TXdb_text = open('text/TXdb', 'w')
UTdb_text = open('text/UTdb', 'w')
VTdb_text = open('text/VTdb', 'w')
VAdb_text = open('text/VAdb', 'w')
WAdb_text = open('text/WAdb', 'w')
WVdb_text = open('text/WVdb', 'w')
WIdb_text = open('text/WIdb', 'w')
WYdb_text = open('text/WYdb', 'w')


for line in ALdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    ALdb_text.write(line + '\n')

for line in AKdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    AKdb_text.write(line + '\n')

for line in AZdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    AZdb_text.write(line + '\n')

for line in ARdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    ARdb_text.write(line + '\n')

for line in CAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    CAdb_text.write(line + '\n')

for line in COdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    COdb_text.write(line + '\n')

for line in CTdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    CTdb_text.write(line + '\n')

for line in DEdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    DEdb_text.write(line + '\n')

for line in FLdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    FLdb_text.write(line + '\n')

for line in GAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    GAdb_text.write(line + '\n')

for line in HIdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    HIdb_text.write(line + '\n')

for line in IDdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    IDdb_text.write(line + '\n')

for line in ILdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    ILdb_text.write(line + '\n')

for line in INdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    INdb_text.write(line + '\n')

for line in IAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    IAdb_text.write(line + '\n')

for line in KSdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    KSdb_text.write(line + '\n')

for line in KYdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    KYdb_text.write(line + '\n')

for line in LAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    LAdb_text.write(line + '\n')

for line in MEdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MEdb_text.write(line + '\n')

for line in MDdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MDdb_text.write(line + '\n')

for line in MAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MAdb_text.write(line + '\n')

for line in MIdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MIdb_text.write(line + '\n')

for line in MNdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MNdb_text.write(line + '\n')

for line in MSdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MSdb_text.write(line + '\n')

for line in MOdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MOdb_text.write(line + '\n')

for line in MTdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    MTdb_text.write(line + '\n')

for line in NEdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NEdb_text.write(line + '\n')

for line in NVdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NVdb_text.write(line + '\n')

for line in NHdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NHdb_text.write(line + '\n')

for line in NJdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NJdb_text.write(line + '\n')

for line in NMdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NMdb_text.write(line + '\n')

for line in NYdb:
    try:
        db = json.loads(line)
    except ValueError:
        continue
    else:
        line = db["text"].replace('\n', ' ').encode('utf-8')
        NYdb_text.write(line + '\n')

for line in NCdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NCdb_text.write(line + '\n')

for line in NDdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    NDdb_text.write(line + '\n')

for line in OHdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    OHdb_text.write(line + '\n')

for line in OKdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    OKdb_text.write(line + '\n')

for line in ORdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    ORdb_text.write(line + '\n')

for line in PAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    PAdb_text.write(line + '\n')

for line in RIdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    RIdb_text.write(line + '\n')

for line in SCdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    SCdb_text.write(line + '\n')

for line in SDdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    SDdb_text.write(line + '\n')

for line in TNdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    TNdb_text.write(line + '\n')

for line in TXdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    TXdb_text.write(line + '\n')

for line in UTdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    UTdb_text.write(line + '\n')

for line in VTdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    VTdb_text.write(line + '\n')

for line in VAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    VAdb_text.write(line + '\n')

for line in WAdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    WAdb_text.write(line + '\n')

for line in WVdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    WVdb_text.write(line + '\n')

for line in WIdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    WIdb_text.write(line + '\n')

for line in WYdb:
    db = json.loads(line)
    line = db["text"].replace('\n', ' ').encode('utf-8')
    WYdb_text.write(line + '\n')

ALdb.close()
AKdb.close()
AZdb.close()
ARdb.close()
CAdb.close()
COdb.close()
CTdb.close()
DEdb.close()
FLdb.close()
GAdb.close()
HIdb.close()
IDdb.close()
ILdb.close()
INdb.close()
IAdb.close()
KSdb.close()
KYdb.close()
LAdb.close()
MEdb.close()
MDdb.close()
MAdb.close()
MIdb.close()
MNdb.close()
MSdb.close()
MOdb.close()
MTdb.close()
NEdb.close()
NVdb.close()
NHdb.close()
NJdb.close()
NMdb.close()
NYdb.close()
NCdb.close()
NDdb.close()
OHdb.close()
OKdb.close()
ORdb.close()
PAdb.close()
RIdb.close()
SCdb.close()
SDdb.close()
TNdb.close()
TXdb.close()
UTdb.close()
VTdb.close()
VAdb.close()
WAdb.close()
WVdb.close()
WIdb.close()
WYdb.close()

ALdb_text.close()
AKdb_text.close()
AZdb_text.close()
ARdb_text.close()
CAdb_text.close()
COdb_text.close()
CTdb_text.close()
DEdb_text.close()
FLdb_text.close()
GAdb_text.close()
HIdb_text.close()
IDdb_text.close()
ILdb_text.close()
INdb_text.close()
IAdb_text.close()
KSdb_text.close()
KYdb_text.close()
LAdb_text.close()
MEdb_text.close()
MDdb_text.close()
MAdb_text.close()
MIdb_text.close()
MNdb_text.close()
MSdb_text.close()
MOdb_text.close()
MTdb_text.close()
NEdb_text.close()
NVdb_text.close()
NHdb_text.close()
NJdb_text.close()
NMdb_text.close()
NYdb_text.close()
NCdb_text.close()
NDdb_text.close()
OHdb_text.close()
OKdb_text.close()
ORdb_text.close()
PAdb_text.close()
RIdb_text.close()
SCdb_text.close()
SDdb_text.close()
TNdb_text.close()
TXdb_text.close()
UTdb_text.close()
VTdb_text.close()
VAdb_text.close()
WAdb_text.close()
WVdb_text.close()
WIdb_text.close()
WYdb_text.close()

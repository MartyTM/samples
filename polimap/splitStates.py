rawdb = open('tweetdb.json', 'r')

#individual state databases
ALdb = open('ALdb.json', 'w')
AKdb = open('AKdb.json', 'w')
AZdb = open('AZdb.json', 'w')
ARdb = open('ARdb.json', 'w')
CAdb = open('CAdb.json', 'w')
COdb = open('COdb.json', 'w')
CTdb = open('CTdb.json', 'w')
DEdb = open('DEdb.json', 'w')
FLdb = open('FLdb.json', 'w')
GAdb = open('GAdb.json', 'w')
HIdb = open('HIdb.json', 'w')
IDdb = open('IDdb.json', 'w')
ILdb = open('ILdb.json', 'w')
INdb = open('INdb.json', 'w')
IAdb = open('IAdb.json', 'w')
KSdb = open('KSdb.json', 'w')
KYdb = open('KYdb.json', 'w')
LAdb = open('LAdb.json', 'w')
MEdb = open('MEdb.json', 'w')
MDdb = open('MDdb.json', 'w')
MAdb = open('MAdb.json', 'w')
MIdb = open('MIdb.json', 'w')
MNdb = open('MNdb.json', 'w')
MSdb = open('MSdb.json', 'w')
MOdb = open('MOdb.json', 'w')
MTdb = open('MTdb.json', 'w')
NEdb = open('NEdb.json', 'w')
NVdb = open('NVdb.json', 'w')
NHdb = open('NHdb.json', 'w')
NJdb = open('NJdb.json', 'w') #Best db
NMdb = open('NMdb.json', 'w')
NYdb = open('NYdb.json', 'w')
NCdb = open('NCdb.json', 'w')
NDdb = open('NDdb.json', 'w')
OHdb = open('OHdb.json', 'w')
OKdb = open('OKdb.json', 'w')
ORdb = open('ORdb.json', 'w')
PAdb = open('PAdb.json', 'w')
RIdb = open('RIdb.json', 'w')
SCdb = open('SCdb.json', 'w')
SDdb = open('SDdb.json', 'w')
TNdb = open('TNdb.json', 'w')
TXdb = open('TXdb.json', 'w')
UTdb = open('UTdb.json', 'w')
VTdb = open('VTdb.json', 'w')
VAdb = open('VAdb.json', 'w')
WAdb = open('WAdb.json', 'w')
WVdb = open('WVdb.json', 'w')
WIdb = open('WIdb.json', 'w')
WYdb = open('WYdb.json', 'w')

for line in rawdb:
    if '"name":"Alabama"' in line or ', AL",' in line:
        ALdb.write(line)
    if '"name":"Alaska"' in line or ', AK",' in line:
        AKdb.write(line)
    if '"name":"Arizona"' in line or ', AZ",' in line:
        AZdb.write(line)
    if '"name":"Arkansas"' in line or ', AR",' in line:
        ARdb.write(line)
    if '"name":"California"' in line or ', CA",' in line:
        CAdb.write(line)
    if '"name":"Colorado"' in line or ', CO",' in line:
        COdb.write(line)
    if '"name":"Connecticut"' in line or ', CT",' in line:
        CTdb.write(line)
    if '"name":"Delaware"' in line or ', DE",' in line:
        DEdb.write(line)
    if '"name":"Florida"' in line or ', FL",' in line:
        FLdb.write(line)
    if '"name":"Georgia"' in line or ', GA",' in line:
        GAdb.write(line)
    if '"name":"Hawaii"' in line or ', HI",' in line:
        HIdb.write(line)
    if '"name":"Idaho"' in line or ', ID",' in line:
        IDdb.write(line)
    if '"name":"Illinois"' in line or ', IL",' in line:
        ILdb.write(line)
    if '"name":"Indiana"' in line or ', IN",' in line:
        INdb.write(line)
    if '"name":"Iowa"' in line or ', IA",' in line:
        IAdb.write(line)
    if '"name":"Kansas"' in line or ', KS",' in line:
        KSdb.write(line)
    if '"name":"Kentucky"' in line or ', KY",' in line:
        KYdb.write(line)
    if '"name":"Louisiana"' in line or ', LA",' in line:
        LAdb.write(line)
    if '"name":"Maine"' in line or ', ME",' in line:
        MEdb.write(line)
    if '"name":"Maryland"' in line or ', MD",' in line:
        MDdb.write(line)
    if '"name":"Massachusetts"' in line or ', MA",' in line:
        MAdb.write(line)
    if '"name":"Michigan"' in line or ', MI",' in line:
        MIdb.write(line)
    if '"name":"Minnesota"' in line or ', MN",' in line:
        MNdb.write(line)
    if '"name":"Mississippi"' in line or ', MS",' in line:
        MSdb.write(line)
    if '"name":"Missouri"' in line or ', MO",' in line:
        MOdb.write(line)
    if '"name":"Montana"' in line or ', MT",' in line:
        MTdb.write(line)
    if '"name":"Nebraska"' in line or ', NE",' in line:
        NEdb.write(line)
    if '"name":"Nevada"' in line or ', NV",' in line:
        NVdb.write(line)
    if '"name":"New Hampshire"' in line or ', NH",' in line:
        NHdb.write(line)
    if '"name":"New Jersey"' in line or ', NJ",' in line:
        NJdb.write(line)
    if '"name":"New Mexico"' in line or ', NM",' in line:
        NMdb.write(line)
    if '"name":"New York"' in line or ', NY",' in line:
        NYdb.write(line)
    if '"name":"North Carolina"' in line or ', NC",' in line:
        NCdb.write(line)
    if '"name":"North Dakota"' in line or ', ND",' in line:
        NDdb.write(line)
    if '"name":"Ohio"' in line or ', OH",' in line:
        OHdb.write(line)
    if '"name":"Oklahoma"' in line or ', OK",' in line:
        OKdb.write(line)
    if '"name":"Oregon"' in line or ', OR",' in line:
        ORdb.write(line)
    if '"name":"Pennsylvania"' in line or ', PA",' in line:
        PAdb.write(line)
    if '"name":"Rhode Island"' in line or ', RI",' in line:
        RIdb.write(line)
    if '"name":"South Carolina"' in line or ', SC",' in line:
        SCdb.write(line)
    if '"name":"South Dakota"' in line or ', SD",' in line:
        SDdb.write(line)
    if '"name":"Tennessee"' in line or ', TN",' in line:
        TNdb.write(line)
    if '"name":"Texas"' in line or ', TX",' in line:
        TXdb.write(line)
    if '"name":"Utah"' in line or ', UT",' in line:
        UTdb.write(line)
    if '"name":"Vermont"' in line or ', VT",' in line:
        VTdb.write(line)
    if '"name":"Virginia"' in line or ', VA",' in line:
        VAdb.write(line)
    if '"name":"Washington"' in line or ', WA",' in line:
        WAdb.write(line)
    if '"name":"West Virginia"' in line or ', WV",' in line:
        WVdb.write(line)
    if '"name":"Wisconsin"' in line or ', WI",' in line:
        WIdb.write(line)
    if '"name":"Wyoming"' in line or ', WY",' in line:
        WYdb.write(line)

rawdb.close()
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

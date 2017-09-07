import unirest

ALdb = open('ALdb', 'r')
AKdb = open('AKdb', 'r')
AZdb = open('AZdb', 'r')
ARdb = open('ARdb', 'r')
CAdb = open('CAdb', 'r')
COdb = open('COdb', 'r')
CTdb = open('CTdb', 'r')
DEdb = open('DEdb', 'r')
FLdb = open('FLdb', 'r')
GAdb = open('GAdb', 'r')
HIdb = open('HIdb', 'r')
IDdb = open('IDdb', 'r')
ILdb = open('ILdb', 'r')
INdb = open('INdb', 'r')
IAdb = open('IAdb', 'r')
KSdb = open('KSdb', 'r')
KYdb = open('KYdb', 'r')
LAdb = open('LAdb', 'r')
MEdb = open('MEdb', 'r')
MDdb = open('MDdb', 'r')
MAdb = open('MAdb', 'r')
MIdb = open('MIdb', 'r')
MNdb = open('MNdb', 'r')
MSdb = open('MSdb', 'r')
MOdb = open('MOdb', 'r')
MTdb = open('MTdb', 'r')
NEdb = open('NEdb', 'r')
NVdb = open('NVdb', 'r')
NHdb = open('NHdb', 'r')
NJdb = open('NJdb', 'r')
NMdb = open('NMdb', 'r')
NYdb = open('NYdb', 'r')
NCdb = open('NCdb', 'r')
NDdb = open('NDdb', 'r')
OHdb = open('OHdb', 'r')
OKdb = open('OKdb', 'r')
ORdb = open('ORdb', 'r')
PAdb = open('PAdb', 'r')
RIdb = open('RIdb', 'r')
SCdb = open('SCdb', 'r')
SDdb = open('SDdb', 'r')
TNdb = open('TNdb', 'r')
TXdb = open('TXdb', 'r')
UTdb = open('UTdb', 'r')
VTdb = open('VTdb', 'r')
VAdb = open('VAdb', 'r')
WAdb = open('WAdb', 'r')
WVdb = open('WVdb', 'r')
WIdb = open('WIdb', 'r')
WYdb = open('WYdb', 'r')
results = open('results', 'w')
results.write('State, Trump, Kasich, Cruz, Sanders, Clinton\n')
results.close()

def sentiment(string):
    response = unirest.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
        headers={
            "X-Mashape-Key": "1dRZazo0EnmshMrsoCmY1GSjJ0n9p1YtbedjsnMgJgHfUW66GN",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        },
        params={
            "text": string
        }
    )
    return response.body['type']

def tally(data, state):
    print 'Gathering sentiment data for ' + state
    results = open('results', 'a')
    trumpVotes = 0
    kasichVotes = 0
    cruzVotes = 0
    sandersVotes = 0
    clintonVotes = 0
    for line in data:
        if sentiment(line) == 'positive' or sentiment(line) == 'neutral':
            if 'trump' in line.lower():
                trumpVotes = trumpVotes + 1
            if 'kasich' in line.lower():
                kasichVotes = kasichVotes + 1
            if 'cruz' in line.lower():
                cruzVotes = cruzVotes + 1
            if 'sanders' in line.lower():
                sandersVotes = sandersVotes + 1
            if 'clinton' in line.lower():
                clintonVotes = clintonVotes + 1
        else:
            if 'trump' in line.lower():
                trumpVotes = trumpVotes - 1
            if 'kasich' in line.lower():
                kasichVotes = kasichVotes - 1
            if 'cruz' in line.lower():
                cruzVotes = cruzVotes - 1
            if 'sanders' in line.lower():
                sandersVotes = sandersVotes - 1
            if 'clinton' in line.lower():
                clintonVotes = clintonVotes - 1
    totals = [trumpVotes, kasichVotes, cruzVotes, sandersVotes, clintonVotes]
    data.close()
    results.write(state + ', ' + str(totals).strip('[]') + '\n')
    results.close()

tally(ALdb, 'Alabama')
tally(AKdb, 'Alaska')
tally(AZdb, 'Arizona')
tally(ARdb, 'Arkansas')
tally(CAdb, 'California')
tally(COdb, 'Colorado')
tally(CTdb, 'Connecticut')
tally(DEdb, 'Delaware')
tally(FLdb, 'Florida')
tally(GAdb, 'Georgia')
tally(HIdb, 'Hawaii')
tally(IDdb, 'Idaho')
tally(ILdb, 'Illinois')
tally(INdb, 'Indiana')
tally(IAdb, 'Iowa')
tally(KSdb, 'Kansas')
tally(KYdb, 'Kentucky')
tally(LAdb, 'Louisiana')
tally(MEdb, 'Maine')
tally(MDdb, 'Maryland')
tally(MAdb, 'Massachusetts')
tally(MIdb, 'Michigan')
tally(MNdb, 'Minnesota')
tally(MSdb, 'Mississippi')
tally(MOdb, 'Missouri')
tally(MTdb, 'Montana')
tally(NEdb, 'Nebraska')
tally(NVdb, 'Nevada')
tally(NHdb, 'New_Hampshire')
tally(NJdb, 'New_Jersey')
tally(NMdb, 'New_Mexico')
tally(NYdb, 'New_York')
tally(NCdb, 'North_Carolina')
tally(NDdb, 'North_Dakota')
tally(OHdb, 'Ohio')
tally(OKdb, 'Oklahoma')
tally(ORdb, 'Oregon')
tally(PAdb, 'Pennsylvania')
tally(RIdb, 'Rhode_Island')
tally(SCdb, 'South_Carolina')
tally(SDdb, 'South_Dakota')
tally(TNdb, 'Tennessee')
tally(TXdb, 'Texas')
tally(UTdb, 'Utah')
tally(VTdb, 'Vermont')
tally(VAdb, 'Virginia')
tally(WAdb, 'Washington')
tally(WVdb, 'West_Virginia')
tally(WIdb, 'Wisconsin')
tally(WYdb, 'Wyoming')

import pycirclize

labels=['p.Arg77Ter','p.Gln119Ter','p.Pro133HisfsTer14','p.Tyr134Ter','p.Gln156Ter','p.Leu164SerfsTer24',
'p.Leu164ProfsTer24','p.Ala178HisfsTer63','g.(?_72211317)_(72226125_?)del','p.Ser201Ter','p.Gln213Ter','p.?','p.Tyr218Ter',
'p.?','p.Tyr226Ter','p.Gln259Ter','p.Pro261ArgfsTer105','p.Ala269fsTer97','p.?','g.(?_72156818)_(72234523_?)del',
'g.(?_72111555)_(72268741_?)del','g.(?_72111499)_(72268758_?)del','g.(?_72111575)_(72267140_?)del',
'p.Arg294Ter','p.Arg297Ter','p.Arg308Ter','p.Asn310ThrfsTer56','p.Pro317GlnfsTer49','p.?','p.?',
'g.(?_72181955)_(72184152_?)del','p.Phe325CysfsTer42','g.(?_72181955)_(72182078_?)del',
'p.Ser338CysfsTer27','p.Tyr348Ter','p.?','p.?','g.(?_72111575)_(72246429_?)del',
'p.?','p.Arg361Ter','p.Met362TrpfsTer4','p.Glu363Lys','g.(?_72156818)_(72156947_?)del','p.?','p.Asn395Ter',
'p.Gly396Ter','p.?','p.?','p.Ala413SerfsTer5','p.Asn417Ter','p.Arg425ThrfsTer27','p.Arg437Cys','p.Arg439AspfsTer3',
'p.Arg440Gln','p.Lys442ArgfsTer9','p.Glu443AspfsTer8','p.Asn451GlnfsTer10','p.?','p.?','p.Glu470Ter','p.Ala473GlyfsTer6',
'p.Trp478Ter','p.Ser487Pro','p.?','p.?','p.Val496GlufsTer35','p.Leu499Ter','p.Thr501LeufsTer15','p.Leu505Arg','p.Tyr515Ter',
'p.Glu524ValfsTer10','p.Tys527Asn','p.?','p.?','p.?','p.Gln543Ter','p.Arg547Gly','p.Val549TrpfsTer6',
'g.(?_72123371)_(72123511_?)del','c.(?_1598-56)_(*1968_?)del','p.Leu583Pro']


labels2=['p.','p.','p.','p.','p.','p.',
'p.','p.','g.','p.','p.','p.','p.',
'p.','p.','p.','p.','p.','p.','g.',
'g.','g.','g.',
'p.','p.','p.','p.','p.','p.','p.',
'g.','p.','g.',
'p.','p.','p.','p.','g.',
'p.','p.','p.','p.','g.','p.','p.',
'p.','p.','p.','p.','p.','p.','p.','p.',
'p.','p.','p.','p.','p.','p.','p.','p.',
'p.','p.','p.','p.','p.','p.','p.','p.','p.',
'p.','p.','p.','p.','p.','p.','p.','p.',
'g.','c.','p.']

from pycirclize import Circos

sectors = {"A": 592}
circos =Circos(sectors,space=0)
circos.text(f"EYA1", size=15)
circos.rect(r_lim=(50,60),deg_lim=(195.81,359.39),fc="#A8eeee",ec="black",lw=1,alpha=0.3)

pos_list=[77,119,133,134,156,164,164,178,191,201,213,217,218,222,226,259,261,269,279,279,279,279,279,294,297,308,310,
         317,324,324,324,325,330,338,348,352,352,352,352,361,362,363,370,382,395,396,402,402,413,417,425,
         437,439,440,442,443,451,456,456,470,473,478,487,494,494,496,499,501,505,515,524,527,531,531,531,
         543,547,549,565,566,583]

for sector in circos.sectors:
    sector.axis(fc="none", ls="none", lw=2, ec="black", alpha=0.5)
    track=sector.add_track((60,70))
    track.axis(fc="#00FF0040",ec="none")
    track.xticks_by_interval(interval=30,show_bottom_line=True,outer=False)

track.xticks(
    pos_list,
    labels,
    label_orientation="vertical",
    show_bottom_line=True,
    label_size=6
)     
    

sectors = {"A": 592}
circos =Circos(sectors,space=0)
circos.text(f"EYA1", size=15)
circos.rect(r_lim=(40,50),deg_lim=(195.81,359.39),fc="#A8eeee",ec="black",lw=1,alpha=0.3)
circos.rect(r_lim=(50,60),deg_lim=(0,24.9324),fc="#fdc9c9",ec="black",lw=1,alpha=0.5) #Exon3
circos.rect(r_lim=(50,60),deg_lim=(24.9324,40.74324),fc="#f44f4f",ec="black",lw=1,alpha=0.5) #Exon4
circos.rect(r_lim=(50,60),deg_lim=(40.74324,58.37838),fc="#ffd2a4",ec="black",lw=1,alpha=0.5) #Exon5
circos.rect(r_lim=(50,60),deg_lim=(58.37838,88.17568),fc="#f4a44f",ec="black",lw=1,alpha=0.5) #Exon6
circos.rect(r_lim=(50,60),deg_lim=(88.17568,116.1486),fc="#ffffa4",ec="black",lw=1,alpha=0.5) #Exon7 
circos.rect(r_lim=(50,60),deg_lim=(116.1486,131.9595),fc="#f6ff2a",ec="black",lw=1,alpha=0.5) #Exon8
circos.rect(r_lim=(50,60),deg_lim=(131.9595,169.6622),fc="#d3ffa7",ec="black",lw=1,alpha=0.5) #Exon9
circos.rect(r_lim=(50,60),deg_lim=(169.6622,197.027),fc="#94f44f",ec="black",lw=1,alpha=0.5) #Exon10
circos.rect(r_lim=(50,60),deg_lim=(197.027,214.0541),fc="#a7ffd3",ec="black",lw=1,alpha=0.5) #Exon11
circos.rect(r_lim=(50,60),deg_lim=(214.0541,232.2973),fc="#4ff4c9",ec="black",lw=1,alpha=0.5) #Exon12
circos.rect(r_lim=(50,60),deg_lim=(232.2973,244.4595),fc="#bde0f4",ec="black",lw=1,alpha=0.5) #Exon13
circos.rect(r_lim=(50,60),deg_lim=(244.4595,277.2973),fc="#4fa5f4",ec="black",lw=1,alpha=0.5) #Exon14
circos.rect(r_lim=(50,60),deg_lim=(277.2973,300.4054),fc="#cbbdf4",ec="black",lw=1,alpha=0.5) #Exon15
circos.rect(r_lim=(50,60),deg_lim=(300.4054,322.9054),fc="#9d4ff4",ec="black",lw=1,alpha=0.5) #Exon16
circos.rect(r_lim=(50,60),deg_lim=(322.9054,343.5811),fc="#e8bdf4",ec="black",lw=1,alpha=0.5) #Exon17
circos.rect(r_lim=(50,60),deg_lim=(343.5811,360),fc="#f44fdb",ec="black",lw=1,alpha=0.5) #Exon18


for sector in circos.sectors:
    sector.axis(fc="none", ls="none", lw=2, ec="black", alpha=0.5)
    track=sector.add_track((50,60))
    track.axis(fc="none",ec="none")
    track.xticks_by_interval(interval=30,show_bottom_line=True,outer=False)

track.xticks(
    pos_list,
    labels2,
    label_orientation="vertical",
    show_bottom_line=True,
    label_size=6
)     
    

fig = circos.plotfig()
    
fig = circos.plotfig()
fig.savefig("fig.png",dpi=300)

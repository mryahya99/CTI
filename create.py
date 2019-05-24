#CREATED, CODING, AUTHOR BY: CYBER-TROJAN-INDONESIA/BLACK-CYBER-ANONIM-TEAM
#TEAM SUPPORT: MARIANAS WEB TEAM 2K05
#VERSION: SIMPEL TOOLS FOR CREATE DEFACE #PYTHON PROGRAM
#MAU NGAPAIN LU? MAU NIRU YA? HAHA, PAKAI OTAK LU ANJENG, GINI SIMPEL NYA MASAK NIRU, USE YOUR BRAIN BITCH, FUCK YOU UNTUK ORANG YANG NIRU SC INI

import urllib2 , cookielib , random , re , sys , socket , time , httplib , ssl

if sys.platform == "linux2" or sys.platform == "linux":
	R = ("\033[31m")
	W = ("\033[0;1m")
	B = ("\033[35m")
	G = ("\033[32m")
	glp = ("\033[2m")
	Y = ("\033[33;1m")

	
mess = """\033[31m ________________________________________________________________
   ___  _  _ _ __   __   ___ _____ ___     _   _  _ ___    ___  ___   _   
  / _ \| \| | |\ \ / /  / __|_   _|_ _|   /_\ | \| |   \  | _ )/ __| /_\  
 | (_) | .` | |_\ V /  | (__  | |  | |   / _ \| .` | |) | | _ \ (__ / _ \ 
  \___/|_|\_|____|_|    \___| |_| |___| /_/ \_\_|\_|___/  |___/\___/_/ \_\                                                                                                                                                                                                       a
___________________________________________________________________________________"""

print mess
print "\033[0m 1;36;40m  Created Defacer ^_^"
print "\033[0m 1;32;40m  ============================="
print "\033[33;1m SUPPORT"
print "\033[33;1m BLACK-CYBER-ANONIM"
print "\033[35m FIGHTER OFC BCA"
print "\033[35m CyberTrojanIndonesia"
print "\033[32m FIGHTER OFC CTI"
print "\033[0m 1;32;40m  _______________________________________"

print "Version:"
print "	       1.3"
print "________________________________________"

print " MR.KITSUNE"
print " MR.JHON"
print " MR.BOY"
print " MR.DARKSKY"
print " MR.MISTER-BLACK"
print " ____________             ______________"
print "____________SELAMAT MENCOBA_____________"


print "title "
print "BEBAS"


print "heading "
print "contoh=Mr.DarkSky"



print "imagelink" 
print "Nah kalo ini nyari nya kalo bisa PNG soalnya Backgroundnya transparnt"
print "https://i.ibb.co/6DBMgrY/20190514-174726.png"
print "https://i.ibb.co/rZSdrQT/20190514-173657.png"
print "https://i.ibb.co/bgr86Ct/20190514-173452.png"
print "COPY LALU PASTE OK !!!"



print "bgimage "
print "Nah ini buat Background ......nyarinya yg GIF......SAYA KASIH ^_^"
print "https://media.giphy.com/media/rWY9ySfjytitq/giphy.gif"
print "https://i.gifer.com/embedded/download/3rCL.gif"
print "http://2.bp.blogspot.com/-C8nV9ht6q0g/VimdR0xKhAI/AAAAAAAAAFI/g8wA1nbUShY/s1600/blue-matrix-animated.gif"
print "COPY LALU PASTE OK !!!"



print "message "
print "Nah ini Terserah anda ....!!!!"



print "MACAM textcolor "
print "CONTOH "
print "RED"
print "GREEN"
print "CYAN"
print "BLUE"
print "WHITE"
print "BLACK"



print " TUTORIAL Soundcloud"
print "CONTOH"
print "https://api.soundcloud.com/tracks/298052134/stream?client_id=a3e059563d7fd3372b49b37f00a00bcf"
print "_________________________________|         |_________________________________"


title = raw_input("Judul title: ")
heading = raw_input("Hacked by: ")
imagelink = raw_input("link gambar (tengah): ")
bgimage = raw_input("link gambar (background): ")
message = raw_input("Pesan. gunakan kode <br> untuk text selanjutnya! : ")
textcolor = raw_input("Warna text (contoh=green): ")
youtubeid = raw_input("youtube kode (MUSIK): ")


#Open the index
fo = open("script.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>
<br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Josefin Sans' rel='stylesheet' type='text/css'>
<body bgcolor="#000000" background ="""

messagescript4 = bgimage

messagescript5 = """><div class='CenterDiv'>
<center>
<h1><center><font color=\"red\" face=Orbitron>"""

messagescript6 = heading

messagescript7 = """<h1></font>
<img src=""" 

messagescript8 = imagelink

messagescript9 = """ width=450px height=340px>
<body onload="init()"></body>
<body>
<div id="bulle"></div>"""

messagescript10 = """
<script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font face=Orbitron color="""

messagescript11 = textcolor

messagescript12 = """ size=4>"""

messagescript13 = message 

messagescript14 = """<br><br></font><br></b></div>\"
var ie = (document.all);
var ne = (document.layers); 
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=Orbitron size=1 color=#ffffff><strong>Messenge : '+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script><font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
<a href="/index.php"><img style="position:fixed;bottom:0px;z-index:1000;right:-10px;"  src="http://static1.squarespace.com/static/5706c12007eaa0b82399660d/5706c68bf0bc33987cae6c71/577d5c5d37c581fd0e25c10b/1469717705608/insult-145142_1280.png" type="image/gif" width="150"></a></body>
<!-- CSS --><style>
.CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}
</style>
<br>
<br>
<br>
<iframe width="0" height="0" src="http://www.youtube.com/v/"""

messagescript15 = youtubeid

messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)
print "Script Berhasil Di buat!"
print "Cara Save : $ls"
print "selanjutnya mv -f nama.html /sdcard"
print "cari langsung di internal sesuai nama "
	

fo.close()





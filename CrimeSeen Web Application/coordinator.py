
def main():
    isRunning = True
   
    
    counter = 0
    first = True
    while counter<47:
                if first:
                    garbage= input("space:")
                    first=False
                selected_neighbourhood= input("Neighbourhood:")
                assault=input("Assault:")
                s_assault=input("Sexual Assault:")
                break_enter=input("Break and Enter:")
                robbery=input("Robbery:")
                drugs=input("Drug Charges:")
                vehicle=input("Stolen Vehicle:")
                theft=input("Theft:")
                murder=input("Murder:")
                total_rating=input("Total Rating:")
                longitude=input("Longitude:")
                latitude=input("Latitude:")
                f = open("spreadsheet.txt", "a")

                if float(total_rating)<0.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#ffd56c'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num0\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<1.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#fcb040'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num1\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<2.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#f68e1f'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num2\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<3.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#f26522'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num3\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<4.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#f05622'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num4\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<5.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#ef4c23'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num5\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<6.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#ed1c24'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num6\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<7.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#cf171f'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num7\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<8.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#9c1a1d'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num8\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<9.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#702323'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num9\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)
                elif float(total_rating)<10.5:
                    savedcode = 'var '+ selected_neighbourhood+'=' +'\'<div id="content" class="animated zoomIn" >' +'<div id="siteNotice">' +'</div>' +'<h1 id="firstHeading" class="firstHeading" style="background-color:'+'#5e0000'+'">'+ selected_neighbourhood+'</h1>\'+\n' 
                    f.write(savedcode)
                    savedcode='{position: new google.maps.LatLng('+longitude+','+latitude+'), type: \'num10\',name:\''+selected_neighbourhood+'\'},\n'
                    f.write(savedcode)

                savedcode = '\'<h1 style="padding:0px;">CrimeSeen Rating: '+total_rating+'</h1>' +'<div id="bodyContent" style="text-align:left;padding:0px;margin-top:-20px;" >' +'<ul style="float:left;list-style:none;font-size:16px;padding:0px;padding-right:15px;">' +'<li><img src="Images/assault.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>'+assault+'</li>' +'<li><img src="Images/s_assault.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Sexual Assault: '+s_assault+'</li>' +'<li><img src="Images/break.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Break and Enter: '+break_enter+'</li>' +'<li><img src="Images/robbery.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Robbery: '+robbery+'</li></ul>' +'<ul style="float:left;list-style:none;font-size:16px;padding:0px;">' +'<li><img src="Images/drugs.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Drug Charges: '+drugs+'</li>' +'<li><img src="Images/vehicle.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Stolen Vehicle: '+vehicle+'</li>' +'<li><img src="Images/theft.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Theft: '+theft+'</li>' +'<li><img src="Images/murder.svg" style="vertical-align:middle;width:35px;padding-right:2px;"/>Murder: '+murder+'</li></ul>' +'</div>' +'</div>\'\n'
                f.write(savedcode)

                savedcode = 'var '+selected_neighbourhood+'_pop = new google.maps.InfoWindow({content: '+selected_neighbourhood+'});\n'
                f.write(savedcode)
                


                savedcode = 'else if (feature.name == \''+selected_neighbourhood+'\') {'+selected_neighbourhood+'_pop.open(map, marker);}\n\n\n'
                f.write(savedcode)
                f.close()
                counter += 1

main()

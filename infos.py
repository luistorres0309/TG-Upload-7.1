from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='β'
			else: make_text+='β'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = 'π₯ Descargando... \n\n'
    msg+= 'π Nombre: ' + str(filename)+'\n'
    msg+= 'π TamaΓ±o Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'π Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'πΆ Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'π Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = 'π‘ Descargando Archivo....\n\n'
    msg += 'β€ Archivo: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'β€ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += 'β€ Total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += 'β€ Descargado: '+sizeof_fmt(currentBits)+'\n\n'
    msg += 'β€ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += 'β€ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = 'β« Subiendo A La Nubeβ... \n\n'
    msg+= 'π Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'β« Subiendo: ' + str(filename)+'\n'
    msg+= 'π TamaΓ±o Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'π Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'πΆ Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'π Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = 'β« Subiendo A La Nubeβ...\n\n'
    msg += 'β€ Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'β€ Nombre: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'β€ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += 'β€ Total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += 'β€ Descargado: '+sizeof_fmt(currentBits)+'\n\n'
    msg += 'β€ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += 'β€ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'π Comprimiendo... \n\n'
    msg+= 'π Nombre: ' + str(filename)+'\n'
    msg+= 'π TamaΓ±o Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'π TamaΓ±o Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= 'πΎ Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = 'π Proceso Finalizadoπ\n\n'
    msg+= 'π Nombre: ' + str(filename)+'\n'
    msg+= 'π TamaΓ±o Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'π TamaΓ±o Partes: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= 'π€ Partes Subidas: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= 'π Borrar Archivo: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>π Enlacesπ</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">π' + f['name'] + 'π</a>'
            msg+= "<a href='"+url+"'>π"+f['name']+'π</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = 'π Archivos ('+str(len(evfiles))+')π\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'βοΈ Configuraciones De UsuarioβοΈ\n\n'
    msg+= 'π Nombre: @' + str(username)+'\n'
    msg+= 'π User: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'π³ Password: ' + str(userdata['moodle_password'])+'\n'
    msg+= 'π‘ Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= 'π· RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= 'π· CloudType: ' + str(userdata['cloudtype'])+'\n'
    msg+= 'π UpType: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= 'π Dir: /' + str(userdata['dir'])+'\n'
    msg+= 'π TamaΓ±o de Zips : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'No'
    if isadmin:
        msgAdmin = 'Si'
    msg+= 'π¦Ύ Admin : ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    tokenize = 'NO'
    if userdata['tokenize']!=0:
       tokenize = 'SI'
    msg+= 'π Proxy : ' + proxy + '\n'
    msg+= 'π? Tokenize : ' + tokenize + '\n\n'
    return msg

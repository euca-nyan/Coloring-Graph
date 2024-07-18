# Fungsi penyortiran
def sortir(arr,data,boole):
    global temperm
    i=0
    while len(arr)<data:
        for a in range(len(temperm)):
            temp=temperm[a]
            countArr=[[0]*2 for _ in range(2)]
            count=0
            for b in range(len(arr)):
                br=False
                if arr[b]==temp:
                    br=1
                    break
                else:
                    for c in range(2):
                        for d in range(2):
                            if arr[b][c]==temp[d]:
                                count+=1
                    if boole:
                        arr0=arr[b][0]
                        arr1=arr[b][1]
                        if arr0==temp[1] and arr1==temp[0]:
                            br=1
                            break
                if count>i:
                    break
                else:
                    for c in range(2):
                        if arr[b][0]==temp[c]:
                            countArr[c][0]+=1
                        elif arr[b][1]==temp[c]:
                            countArr[c][1]+=1
            if count<=i and not br and data!=len(arr):
                Arr00=countArr[0][0]
                Arr01=countArr[0][1]
                Arr10=countArr[1][0]
                Arr11=countArr[1][1]
                if Arr00<=Arr01 and Arr10>=Arr11:
                    arr.append(temp)
        i+=1
# Fungsi pengecekan penyortiran
def cek_sortir(sisa,arr,min,max):
    if sisa>0:
        sortir(arr,min,True)
        sortir(arr,max,False)
    else:
        sortir(arr,max,True)
# Inisialisasi awal
from itertools import permutations
Matkul=["Jaringan Komputer", "Pengembangan PL Untuk Agroindustri Modern", "Sistem Basis Data", "Teori Graf", "Algoritma dan Pemrograman II", "Analisis dan Desain Perangkat Lunak", "Arsitektur Komputer", "Matematika Diskrit SI", "Matematika Diskrit IF", "Pemrograman Berbasis Web", "Pemrograman Berorientasi Obyek", "Sistem Operasi", "Datamining", "Desain dan Analisis Algoritma", "Desain Dan Manajemen Jaringan", "Interaksi Manusia dan Komputer", "Keamanan Sistem", "Kecerdasan Komputasional", "Manajemen dan Kewirausahaan", "Manajemen proyek TI", "Parallel Computing", "Pemrograman Antarmuka Aplikasi", "Pemrograman Berbasis Mobile", "Pengantar Rekayasa Perangkat Lunak", "Profesional Issue", "Routing dan Switching", "Sistem Digital", "Sistem Enterprise", "Statistika", "Tata Kelola Teknologi Informasi", "Teori Bahasa dan Otomata"]
Dosen=[["Diah", "Yudha", "Anang", "Dwi"], ["Saiful", "Windi", "Nano", "Anang"], ["Arif", "Priza", "Fajrin", "Gayatri", "Agustin", "Hari"], ["Slamin", "Ariful", "Gama", "Yuyun", "Arif"], ["Maududie", "Istiyadi", "Tio", "Arif"], ["Nano", "Agustin", "Hari"], ["Nova", "Diah"], ["Slamin", "Nova", "Yuyun", "Anton", "Gama"], ["Slamin", "Nova", "Yuyun", "Anton", "Gama", "Sari"], ["Diksi", "Yudha", "Zarkasi", "Hari"], ["Maududie", "Istiyadi", "Tio", "Zarkasi"], ["Yanuar", "Dwi", "Sari"], ["Fajrin", "Gayatri", "Priza", "Nelly"], ["Arif", "Yuyun"], ["Yudha"], ["Fahroby", "Sari", "Anang", "Agustin"], ["Anton", "Diksi", "Yanuar"], ["Ariful", "Tio", "Gayatri", "Nelly", "Yuyun"], ["Nelly", "Karina", "Nano"], ["Beny", "Karina"], ["Zarkasi", "Gama", "Dwi", "Hari"], ["Istiyadi", "Maududie"], ["Priza", "Zarkasi", "Gama", "Dwi"], ["Saiful", "Windi", "Beny"], ["Slamin", "Saiful", "Anton", "Fahroby"], ["Diksi"], ["Diah", "Nova", "Fajrin"], ["Karina", "Agustin", "Oktalia"],  ["Ariful", "Yuyun", "Sari"],  ["Oktalia", "Fajrin"],  ["Anton", "Gama"]]
jmlKls=[6, 6, 6, 6, 4, 4, 4, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
jnsKls=["Kelas A","Kelas B","Kelas C","Kelas D","Kelas E","Kelas F"]
TM=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2]
PR=[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0]
tDs=[]
Mk={}
timatkul={}
for a in range (len(Matkul)):
    Mk[Matkul[a]]={'Dosen':Dosen[a],'jmlKls':jmlKls[a],'sksTM':TM[a],'sksPR':PR[a]}
    timatkul[Matkul[a]]={}
    for b in range (jmlKls[a]):
        timatkul[Matkul[a]][jnsKls[b]]={}

for matkul,data in Mk.items():
    Ds = data['Dosen']
    if len(Ds)==1:
        templist=[]
        for _ in range(data['jmlKls']):
            templist.append(Ds)
    else:
        # Permutasi dibuat hingga menghasilkan daftar permut tim teaching berisi dua orang
        perm = list(permutations(Ds, 2))
        # Ini untuk mengkonversi tuple permutasi menjadi list
        temperm=[[] for x in perm]
        # Ini looping untuk tiap tim dosen di tiap matkul(Sebelum matkul dibagi per kelas)
        for i in list(perm):
            p=perm.index(i)    
            for j in list(i):
                temperm[p].append(j)
        templist=[]
        if data['jmlKls']>len(temperm):
            btsA=data['jmlKls']//len(temperm)
            btsB=data['jmlKls']%len(temperm)
            for _ in range (btsA):
                for i in range (len(temperm)):
                    templist.append(temperm[i])
            # Mulai dari sini untuk mengisi btsB
            if data['jmlKls']!=len(templist):
                lisst=[]
                lisst.append(temperm[0])
                bPerm=len(temperm)/2
                sisa=btsB-bPerm
                cek_sortir(sisa,lisst,bPerm,btsB-1)            
                for x in range (len(lisst)):
                    templist.append(lisst[x])

        elif data['jmlKls']==len(temperm):
            for  i in range(len(temperm)):
                templist.append(temperm[i])
        else:
            templist.append(temperm[0])
            bPerm=len(temperm)/2
            sisa=data['jmlKls']-bPerm
            cek_sortir(sisa,templist,bPerm,data['jmlKls'])
    for y in range(len(templist)):
        timatkul[matkul][jnsKls[y]]['timDosen']=templist[y]
        tDs.append(templist[y])

# Inisialisasi kedua
totalKelas = sum(len(timatkul[matkul]) for matkul in timatkul)
Mx = [[0] * totalKelas for _ in range(totalKelas)]
Der, Mder, idxDer, vColor = ([0 for _ in range(totalKelas)] for _ in range(4))
# INI PENERAPAN WELCH POWELL
for x in range(totalKelas):
    counter=0
    for y in range(totalKelas):
        if x != y:
            for i in range (len(tDs[x])):
                for j in range (len(tDs[y])):
                    if tDs[x][i] == tDs[y][j] and Mx[x][y]!=1:
                        Mx[x][y]=1
                        break 
            if Mx[x][y]==1:
                counter=counter+1
    Der[x]=counter
    Mder[x]=counter
#Mengurutkan Mder
Mder.sort(reverse=True)
#cari posisi urutan Derajat tadinya dimana
for x in range(len(Der)):
    m=x
    for i in range(len(Der)):
        x=m
        if Mder[x]==Der[i]:
            nSama=0;sama=False
            while x>0:
                if Mder[x]==Mder[x-1]:
                    x=x-1
                    nSama=nSama+1
                else:
                    break
            if nSama>0:
                for p in range (1,nSama+1):
                    if i ==idxDer[m-p]:
                        sama=True
            if not sama:
                break
    idxDer[m]=i
##Pewarnaan dimulai dari sini yak
p=idxDer[0]
vColor[p]=1

for x in range (1,len(Der)):
    color=1
    p=idxDer[x]
    for y in range (x):
        q=idxDer[y]
        if Mx[p][q]==1:
            if vColor[q]==color:
                color=color+1
    vColor[p]=color
# Memasukkan vColor ke dictionary timatkul dan membuat array key matkul
p=0
keyMatkul=[]

for mk, kls in timatkul.items():
    for kelas, data in kls.items():
        keyMatkul.append([mk,kelas])
        data['vColor'] = vColor[p]
        p+=1

# Fungsi untuk memproses penjadwalan
def process_jadwal(bbHari,bbSesi,baSesi,tipeFlag,tipeSKS,pengaliSKS):
    global flag,idxHari,hari,ruang,jadwal,timatkul,keyMatkul
    for i in range (bbHari,len(hari)):
        for j in range(bbSesi,baSesi):
            for k in range(len(ruang)):
                if flag[y][tipeFlag]==False:
                    jamkos=jadwal[ruang[k]][hari[i]]['jamkos']
                    sks=Mk[keyMatkul[y][0]][tipeSKS]*pengaliSKS
                    if jamkos>=sks:
                        kosong=True
                        for l in range(j,j+sks):
                            color=jadwal[ruang[k]][hari[i]][l]['vColor']
                            if color!=0:
                                kosong=False
                        if kosong:
                            for l in range(len(ruang)):
                                color=jadwal[ruang[l]][hari[i]][j]['vColor']
                                if color!=x and color!=0:
                                    kosong=False
                            if kosong:
                                for l in range(j,j+sks):
                                    jadwal[ruang[k]][hari[i]][l]={'vColor': timatkul[keyMatkul[y][0]][keyMatkul[y][1]]["vColor"],'matkul':keyMatkul[y][0],'kelas':keyMatkul[y][1],'rincianSKS':tipeSKS}
                                    jadwal[ruang[k]][hari[i]]['jamkos']=jadwal[ruang[k]][hari[i]]['jamkos']-1
                                    idxHari=i
                                    flag[y][tipeFlag]=True
                            else:
                                break
# INISIALISASI UNTUK PENJADWALAN
jadwal={}
maxVColor=max(vColor)
# Insialisasi flag untuk tanda apakah matkul telah dimasukkan ke jadwal
flag= [[False]*2 for _ in range(len(keyMatkul))]
hari=["Senin","Selasa","Rabu","Kamis","Jumat"]
ruang=["Ruang Kuliah A31", "Ruang Kuliah A33", "Ruang Kuliah A35", "Ruang Kuliah A37", "Ruang Kuliah A41", "Ruang Kuliah A42", "Ruang Kuliah A43", "Ruang Kuliah A44", "Ruang Kuliah Aula B1", "Ruang Kuliah Aula B2", "Ruang Kuliah B5"]

for x in range(len(ruang)):
    jadwal[ruang[x]]={}
    for y in range (len(hari)):
        jadwal[ruang[x]][hari[y]]={'jamkos':15}
        for z in range (15):
            jadwal[ruang[x]][hari[y]][z+1]={'vColor': 0,'matkul':"",'kelas':"",'rincianSKS':""}

for x in range(1,maxVColor+1):
    for y in range (len(keyMatkul)):
        idxHari=0
        sksmatkul=Mk[keyMatkul[y][0]]
        matkul=timatkul[keyMatkul[y][0]][keyMatkul[y][1]]
        if sksmatkul['sksPR']>0 and matkul["vColor"]==x:
            process_jadwal(0,1,14,0,'sksTM',1)
            process_jadwal(idxHari+2,1,13,1,'sksPR',3)
for x in range(1,maxVColor+1):
    for y in range(len(keyMatkul)):
        idxHari=0
        sks=Mk[keyMatkul[y][0]]['sksPR']
        if sks==0:
            process_jadwal(0,1,14,0,'sksTM',1)

# ///////////////////////////////////////////////////////////////////////
# # Menampilkan output pada terminal

# from collections import defaultdict
# import pydoc
# from tabulate import tabulate
# # Data penjadwalan mata kuliah
# def format_schedule(schedule):
#     formatted_schedule = defaultdict(lambda: defaultdict(list))
    
#     for room, days in schedule.items():
#         for day, sessions in days.items():
#             current_course = None
#             current_kelas = None
#             start_session = None

#             valid_sessions = {k: v for k, v in sessions.items() if isinstance(k, int)}

#             for session, details in sorted(valid_sessions.items()):
#                 course = details.get('matkul', '')
#                 kelas = details.get('kelas', '')
#                 rincianSKS = details.get('rincianSKS', '')
#                 if course != current_course or kelas != current_kelas:
#                     if current_course is not None and current_kelas is not None:
#                         formatted_schedule[day][room].append((start_session, session - 1, current_course, current_kelas, current_rincianSKS))
#                     current_course = course
#                     current_kelas = kelas
#                     current_rincianSKS = rincianSKS
#                     start_session = session

#             if current_course is not None and current_kelas is not None:
#                 formatted_schedule[day][room].append((start_session, session, current_course, current_kelas, current_rincianSKS))
    
#     return formatted_schedule

# def rincian_sks_format(rincianSKS):
#     if rincianSKS == "sksTM":
#         return "TM"
#     elif rincianSKS == "sksPR":
#         return "PR"
#     else:
#         return rincianSKS

# def tampilkan_jadwal(formatted_schedule):
#     output = []
#     for day, rooms in formatted_schedule.items():
#         for room, entries in rooms.items():
#             for start_session, end_session, course, kelas, rincianSKS in entries:
#                 rincian_sks = rincian_sks_format(rincianSKS)
#                 if start_session == end_session:
#                     output.append([day, room, start_session, start_session, course, kelas, rincian_sks])
#                 else:
#                     output.append([day, room, start_session, end_session, course, kelas, rincian_sks])
    
#     table = tabulate(output, headers=["Hari", "Ruangan", "Mulai", "Selesai", "Mata Kuliah", "Kelas", "SKS"], tablefmt="grid")
#     pydoc.pager(table)

# # Format jadwal berdasarkan data yang diberikan
# formatted_schedule = format_schedule(jadwal)
# # Tampilkan jadwal yang sudah diformat
# tampilkan_jadwal(formatted_schedule)


# ///////////////////////////////////////////////////////////////////////
# Memberikan output csv

# from collections import defaultdict
# import csv

# def format_schedule(schedule):
#     formatted_schedule = defaultdict(lambda: defaultdict(list))
    
#     for room, days in schedule.items():
#         for day, sessions in days.items():
#             current_course = None
#             current_kelas = None
#             start_session = None

#             valid_sessions = {k: v for k, v in sessions.items() if isinstance(k, int)}

#             for session, details in sorted(valid_sessions.items()):
#                 course = details.get('matkul', '')
#                 kelas = details.get('kelas', '')
#                 rincianSKS = details.get('rincianSKS', '')
#                 if course != current_course or kelas != current_kelas:
#                     if current_course is not None and current_kelas is not None:
#                         formatted_schedule[day][room].append((start_session, session - 1, current_course, current_kelas, current_rincianSKS))
#                     current_course = course
#                     current_kelas = kelas
#                     current_rincianSKS = rincianSKS
#                     start_session = session

#             if current_course is not None and current_kelas is not None:
#                 formatted_schedule[day][room].append((start_session, session, current_course, current_kelas, current_rincianSKS))
    
#     return formatted_schedule

# def rincian_sks_format(rincianSKS):
#     if rincianSKS == "sksTM":
#         return "TM"
#     elif rincianSKS == "sksPR":
#         return "PR"
#     else:
#         return rincianSKS
# def get_tim_dosen(course, kelas):
#     if course in timatkul and kelas in timatkul[course]:
#         return ', '.join(timatkul[course][kelas].get('timDosen', []))
#     return ''
# def simpan_jadwal_csv(formatted_schedule, filename):
#     output = []
#     for day, rooms in formatted_schedule.items():
#         for room, entries in rooms.items():
#             for start_session, end_session, course, kelas, rincianSKS in entries:
#                 rincian_sks = rincian_sks_format(rincianSKS)
#                 tim_dosen = get_tim_dosen(course, kelas)
#                 if start_session == end_session:
#                     output.append([day, room, start_session, start_session, course, kelas, rincian_sks, tim_dosen])
#                 else:
#                     output.append([day, room, start_session, end_session, course, kelas, rincian_sks, tim_dosen])

#     # Save the output to a CSV file
#     with open(filename, 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(["Hari", "Ruangan", "Sesi Mulai", "Sesi Selesai", "Mata Kuliah", "Kelas", "Rincian SKS", "Tim Dosen"])
#         csvwriter.writerows(output)

# # Format jadwal berdasarkan data yang diberikan
# formatted_schedule = format_schedule(jadwal)
# # Simpan jadwal yang sudah diformat ke dalam file CSV
# simpan_jadwal_csv(formatted_schedule, 'jadwall.csv')



# ///////////////////////////////////////////////////////////////////////
# Menampilkan CSV dengan data vColor
# from collections import defaultdict
# import csv
# def format_schedule(schedule):
#     formatted_schedule = defaultdict(lambda: defaultdict(list))
    
#     for room, days in schedule.items():
#         for day, sessions in days.items():
#             current_course = None
#             current_kelas = None
#             start_session = None

#             valid_sessions = {k: v for k, v in sessions.items() if isinstance(k, int)}

#             for session, details in sorted(valid_sessions.items()):
#                 course = details.get('matkul', '')
#                 kelas = details.get('kelas', '')
#                 rincianSKS = details.get('rincianSKS', '')
#                 if course != current_course or kelas != current_kelas:
#                     if current_course is not None and current_kelas is not None:
#                         formatted_schedule[day][room].append((start_session, session - 1, current_course, current_kelas, current_rincianSKS))
#                     current_course = course
#                     current_kelas = kelas
#                     current_rincianSKS = rincianSKS
#                     start_session = session

#             if current_course is not None and current_kelas is not None:
#                 formatted_schedule[day][room].append((start_session, session, current_course, current_kelas, current_rincianSKS))
    
#     return formatted_schedule

# def rincian_sks_format(rincianSKS):
#     if rincianSKS == "sksTM":
#         return "TM"
#     elif rincianSKS == "sksPR":
#         return "PR"
#     else:
#         return rincianSKS

# def get_tim_dosen(course, kelas):
#     if course in timatkul and kelas in timatkul[course]:
#         tim_dosen = ', '.join(timatkul[course][kelas].get('timDosen', []))
#         v_color = timatkul[course][kelas].get('vColor', '')
#         return tim_dosen, v_color
#     return '', ''

# def simpan_jadwal_csv(formatted_schedule, filename):
#     output = []
#     for day, rooms in formatted_schedule.items():
#         for room, entries in rooms.items():
#             for start_session, end_session, course, kelas, rincianSKS in entries:
#                 rincian_sks = rincian_sks_format(rincianSKS)
#                 tim_dosen, v_color = get_tim_dosen(course, kelas)
#                 if start_session == end_session:
#                     output.append([day, room, start_session, start_session, course, kelas, rincian_sks, tim_dosen, v_color])
#                 else:
#                     output.append([day, room, start_session, end_session, course, kelas, rincian_sks, tim_dosen, v_color])

#     # Save the output to a CSV file
#     with open(filename, 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(["Hari", "Ruangan", "Sesi Mulai", "Sesi Selesai", "Mata Kuliah", "Kelas", "Rincian SKS", "Tim Dosen", "vColor"])
#         csvwriter.writerows(output)

# # Format jadwal berdasarkan data yang diberikan
# formatted_schedule = format_schedule(jadwal)
# # Simpan jadwal yang sudah diformat ke dalam file CSV
# simpan_jadwal_csv(formatted_schedule, 'jadwalll.csv')
# ///////////////////////////////////////////////////////////////////////

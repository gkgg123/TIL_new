import sys
def input():
    return sys.stdin.readline().rstrip()

station = """1	Seoul	0.0	Y	23	Chupungnyeong	234.7	N
2	Yeongdeungpo	9.1	Y	24	Gimcheon	253.8	Y
3	Anyang	23.9	N	25	Gumi	276.7	Y
4	Suwon	41.5	Y	26	Sagok	281.3	N
5	Osan	56.5	N	27	Yangmok	289.5	N
6	Seojeongri	66.5	N	28	Waegwan	296.0	Y
7	Pyeongtaek	75.0	Y	29	Sindong	305.9	N
8	Seonghwan	84.4	N	30	Daegu	323.1	Y
9	Cheonan	96.6	Y	31	Dongdaegu	326.3	Y
10	Sojeongni	107.4	N	32	Gyeongsan	338.6	N
11	Jeonui	114.9	N	33	Namseonghyeon	353.1	N
12	Jochiwon	129.3	Y	34	Cheongdo	361.8	N
13	Bugang	139.8	N	35	Sangdong	372.2	N
14	Sintanjin	151.9	N	36	Miryang	381.6	Y
15	Daejeon	166.3	Y	37	Samnangjin	394.1	N
16	Okcheon	182.5	N	38	Wondong	403.2	N
17	Iwon	190.8	N	39	Mulgeum	412.4	N
18	Jitan	196.4	N	40	Hwamyeong	421.8	N
19	Simcheon	200.8	N	41	Gupo	425.2	Y
20	Gakgye	204.6	N	42	Sasang	430.3	N
21	Yeongdong	211.6	Y	43	Busan	441.7	Y
22	Hwanggan	226.2	N"""
station_split = list(map(lambda x : x.split('\t'), station.split('\n')))
station_dis = {}

for k in station_split:
    for ind in range(0,len(k)//4):
        num,station,dis,_  = k[ind*4:(ind+1)*4]
        station_dis[station] = float(dis)

station_time = {}
N,Q = map(int,input().split())


for _ in range(N):
    name,ed,st =input().split()
    if ed != '-:-':
        ed = int(ed[:2])*60 + int(ed[3:])
    if st != '-:-':
        st = int(st[:2])*60 + int(st[3:])
    station_time[name] = [ed,st]

for _ in range(Q):
    st,ed = input().split()

    distance = abs(station_dis[ed] - station_dis[st])

    start_time = station_time[st][1]
    end_time = station_time[ed][0]
    if end_time < start_time:
        end_time += 24*60
    answer = distance/(end_time-start_time)*60
    print(answer)
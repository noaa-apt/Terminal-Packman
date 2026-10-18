d=OSError
W=str
V=max
L=int
K=range
J=min
H=len
B=ord
import argparse as e,curses as A,os,random as X,time as M
from collections import deque
os.environ.setdefault('ESCDELAY','25')
Y=['############################','#............##............#','#.####.#####.##.#####.####.#','#o####.#####.##.#####.####o#','#.####.#####.##.#####.####.#','#..........................#','#.####.##.########.##.####.#','#.####.##.########.##.####.#','#......##....##....##......#','######.##### ## #####.######','     #.##### ## #####.#     ','     #.##          ##.#     ','     #.## ###--### ##.#     ','######.## #      # ##.######','      .   #      #   .      ','######.## #      # ##.######','     #.## ######## ##.#     ','     #.##          ##.#     ','     #.## ######## ##.#     ','######.## ######## ##.######','#............##............#','#.####.#####.##.#####.####.#','#.####.#####.##.#####.####.#','#o..##.......  .......##..o#','###.##.##.########.##.##.###','###.##.##.########.##.##.###','#......##....##....##......#','#.##########.##.##########.#','#.##########.##.##########.#','#..........................#','############################']
F,C=H(Y),28
R=[]
for(f,g)in enumerate(Y):
	S=list(g)
	if f in(10,11,12,16,17,18):
		for O in K(C):
			if(O<5 or O>22)and S[O]==' ':S[O]='x'
	R.append(S)
D,E,I,G=(-1,0),(0,-1),(1,0),(0,1)
T=D,E,I,G
Z={A.KEY_UP:D,A.KEY_DOWN:I,A.KEY_LEFT:E,A.KEY_RIGHT:G,B('w'):D,B('s'):I,B('a'):E,B('d'):G,B('W'):D,B('S'):I,B('A'):E,B('D'):G,B('k'):D,B('j'):I,B('h'):E,B('l'):G}
h=23,13
N=11,13
U=17,13
i={(11,12),(11,15),(23,12),(23,15)}
a=[6,5,4,3,2,5,2,2,1,5,2,1,1,3,1,1,0,1]
P=[('CH',100),('ST',300),('OR',500),('OR',500),('AP',700),('AP',700),('ME',1000),('ME',1000),('GA',2000),('GA',2000),('BE',3000),('BE',3000),('KY',5000)]
b=os.path.expanduser('~/.pacman_term_hi')
class Q:
	__slots__='name','pair','y','x','dir','state','fright','acc','rev','rel','scatter'
	def __init__(A,name,pair,pos,rel,scatter,state):A.name,A.pair=name,pair;A.y,A.x=pos;A.dir=E;A.state=state;A.fright=False;A.acc=.0;A.rev=False;A.rel=rel;A.scatter=scatter
def j(level):
	B=level
	if B==1:A=[7,20,7,20,5,20,5]
	elif B<5:A=[7,20,7,20,5,1033,1/30]
	else:A=[5,20,5,20,5,1037,1/30]
	return A+[1e9]
class k:
	def __init__(B,scr,fps):
		C=scr;B.scr=C;B.frame=1./V(5,fps);C.keypad(True);C.nodelay(True)
		try:A.curs_set(0)
		except A.error:0
		B.setup_colors();B.hi=B.load_hi();B.dist=B.build_dist();B.blink=True;B.layout();B.new_game()
	def setup_colors(E):
		F={A:0 for A in('wall','flashwall','dot','pow','door','pac','fr','fl','eyes','text','bad','pop','fruit')};E.ghost_attr={}
		if A.has_colors():
			A.start_color()
			try:A.use_default_colors();D=-1
			except A.error:D=A.COLOR_BLACK
			B=A;G=208 if getattr(B,'COLORS',8)>=256 else B.COLOR_GREEN;H=[(1,B.COLOR_BLUE,B.COLOR_BLUE),(2,B.COLOR_WHITE,B.COLOR_WHITE),(3,B.COLOR_WHITE,D),(4,B.COLOR_YELLOW,D),(5,B.COLOR_RED,D),(6,B.COLOR_MAGENTA,D),(7,B.COLOR_CYAN,D),(8,G,D),(9,B.COLOR_WHITE,B.COLOR_BLUE),(10,B.COLOR_RED,B.COLOR_WHITE),(11,B.COLOR_WHITE,D),(12,B.COLOR_GREEN,D)]
			for(I,J,K)in H:
				try:A.init_pair(I,J,K)
				except A.error:0
			C=A.color_pair;F.update(wall=C(1),flashwall=C(2),dot=C(3),pow=C(3)|A.A_BOLD,door=C(6),pac=C(4)|A.A_BOLD,fr=C(9),fl=C(10),eyes=C(11),text=C(4)|A.A_BOLD,bad=C(5)|A.A_BOLD,pop=C(7)|A.A_BOLD,fruit=C(5)|A.A_BOLD);E.ghost_attr={5:C(5),6:C(6),7:C(7),8:C(8)}
		else:F.update(wall=A.A_REVERSE,flashwall=A.A_REVERSE|A.A_BOLD,pac=A.A_BOLD,text=A.A_BOLD,bad=A.A_BOLD,fr=A.A_DIM,fl=A.A_BOLD,pop=A.A_BOLD,fruit=A.A_BOLD);E.ghost_attr={5:0,6:0,7:0,8:0}
		E.A=F;E.wall_attr=F['wall']
	def load_hi(B):
		try:
			with open(b)as A:return L(A.read().strip())
		except(d,ValueError):return 0
	def save_hi(A):
		try:
			with open(b,'w')as B:B.write(W(A.hi))
		except d:0
	def build_dist(J):
		B={N:0};E=deque([N])
		while E:
			G,H=E.popleft()
			for I in T:
				A,D=G+I[0],(H+I[1])%C
				if(A,D)in B or not 0<=A<F:continue
				if R[A][D]in'#x-':continue
				B[A,D]=B[G,H]+1;E.append((A,D))
		return B
	def layout(A):A.rows,A.cols=A.scr.getmaxyx();A.ox=1;A.scale=2 if A.cols>=C*2+A.ox+22 else 1;A.px_panel=A.ox+C*A.scale+2;A.fits=A.rows>=F and A.cols>=C*A.scale+A.ox+1;A.full=True
	def new_game(A):A.score=0;A.lives=2;A.level=1;A.start_level()
	def start_level(A):A.g=[A[:]for A in R];A.walls=[(B,D)for B in K(F)for D in K(C)if A.g[B][D]=='#'];A.dots_left=sum(A.count('.')+A.count('o')for A in A.g);A.dots_eaten=0;A.fruit_t=.0;A.flash=False;A.wall_attr=A.A['wall'];A.full=True;A.reset_positions()
	def reset_positions(A):A.py,A.px=h;A.pdir=0,0;A.want=0,0;A.face=E;A.mouth=True;A.pacc=.0;A.ghosts=[Q('blinky',5,N,0,(-3,25),'out'),Q('pinky',6,(14,13),0,(-3,2),'house'),Q('inky',7,(14,11),30,(31,27),'house'),Q('clyde',8,(14,16),60,(31,0),'house')];A.sched=j(A.level);A.mode_i=0;A.mode_t=A.sched[0];A.fright_t=.0;A.combo=0;A.rel_dots=0;A.idle=.0;A.freeze=.0;A.popups=[];A.state='ready';A.t=2.2;A.msg='READY!',A.A['text'];A.pkey=None
	def add(A,pts):
		B=A.score;A.score+=pts
		if B<10000<=A.score:A.lives+=1
		if A.score>A.hi:A.hi=A.score
	def free(B,y,x,door=False):
		if y<0 or y>=F:return False
		A=B.g[y][x%C];return A not in'#x'and(door or A!='-')
	def pac_tps(A):return 8.+.5*J(A.level-1,4)
	def ghost_tps(A,g):
		B=g.state
		if B in('eyes','enter'):return 2e1
		if B=='house':return .0
		if B=='leave':return 5.
		if g.y==14 and(g.x<6 or g.x>21):return 4.
		if g.fright:return 4.5 if A.level==1 else 5. if A.level<5 else 5.5
		C=7.2+.4*J(A.level-1,5)
		if g.name=='blinky':
			if A.dots_left<=10:C*=1.1
			elif A.dots_left<=20:C*=1.05
		return C
	def target(A,g):
		if A.mode_i%2==0:return g.scatter
		B,C=A.py,A.px
		if g.name=='blinky':return B,C
		G,H=A.face
		if g.name=='pinky':
			if A.face==D:return B-4,C-4
			return B+4*G,C+4*H
		if g.name=='inky':
			E,F=B+2*G,C+2*H
			if A.face==D:E,F=B-2,C-2
			I=A.ghosts[0];return E+(E-I.y),F+(F-I.x)
		if(g.y-B)**2+(g.x-C)**2>64:return B,C
		return g.scatter
	def release(A):
		C={1:(0,30,60),2:(0,0,50)}.get(A.level,(0,0,0));D=4. if A.level<5 else 3.
		for B in A.ghosts[1:]:
			if B.state!='house':continue
			E={'pinky':0,'inky':1,'clyde':2}[B.name]
			if A.rel_dots>=C[E]or A.idle>=D:B.state='leave';A.idle=.0
			break
	def start_fright(A):
		C=a[A.level-1]if A.level<=H(a)else 0;A.combo=0
		for B in A.ghosts:
			if B.state in('out','leave','house'):
				if B.state=='out':B.rev=True
				if C>0:B.fright=True
		A.fright_t=float(C)
	def end_fright(A):
		A.fright_t=.0
		for B in A.ghosts:B.fright=False
	def pac_step(A):
		E=A.want
		if E!=(0,0)and A.free(A.py+E[0],A.px+E[1]):A.pdir=E
		F=A.pdir
		if F==(0,0):return
		B,D=A.py+F[0],(A.px+F[1])%C
		if not A.free(B,D):return
		A.py,A.px=B,D;A.face=F;A.mouth=not A.mouth;G=A.g[B][D]
		if G in'.o':
			A.g[B][D]=' ';A.dots_left-=1;A.dots_eaten+=1;A.rel_dots+=1;A.idle=.0
			if G=='.':A.add(10);A.pacc-=.12
			else:A.add(50);A.pacc-=.3;A.start_fright()
			if A.dots_eaten in(70,170):A.fruit_t=1e1
		if A.fruit_t>0 and B==U[0]and D in(13,14):K,I=P[J(A.level,H(P))-1];A.add(I);A.popups.append([B,D,W(I),1.5]);A.fruit_t=.0
	def ghost_step(I,g):
		K=g.state
		if K=='leave':
			if g.x!=13:g.x+=1 if g.x<13 else-1
			elif g.y>11:g.y-=1
			if(g.y,g.x)==N:g.state='out';g.dir=X.choice((E,G));g.rev=False
			return
		if K=='enter':
			g.y+=1
			if g.y>=14:g.y=14;g.state='leave'
			return
		if K=='eyes':
			if(g.y,g.x)==N:g.state='enter';return
			L,O=None,1e9
			for A in T:
				P,Q=g.y+A[0],(g.x+A[1])%C;M=I.dist.get((P,Q))
				if M is not None and M<O:O,L=M,(P,Q)
			if L:g.y,g.x=L
			return
		if K!='out':return
		F=-g.dir[0],-g.dir[1];B=[]
		for A in T:
			if A==F:continue
			if not I.free(g.y+A[0],g.x+A[1]):continue
			if A==D and not g.fright and(g.y,g.x)in i:continue
			B.append(A)
		if g.rev:
			g.rev=False
			if I.free(g.y+F[0],g.x+F[1]):B=[F]
		if not B:B=[F]
		if H(B)==1:A=B[0]
		elif g.fright:A=X.choice(B)
		else:R,S=I.target(g);A=J(B,key=lambda o:(g.y+o[0]-R)**2+(g.x+o[1]-S)**2)
		g.y+=A[0];g.x=(g.x+A[1])%C;g.dir=A
	def check(A):
		for B in A.ghosts:
			if B.state in('eyes','enter')or(B.y,B.x)!=(A.py,A.px):continue
			if B.fright:A.combo+=1;C=200*2**(A.combo-1);A.add(C);B.fright=False;B.state='eyes';A.popups.append([B.y,B.x,W(C),.6]);A.freeze=.6;return True
			A.state='dying';A.t=1.6;A.msg=None;return True
		return False
	def update(A,dt):
		B=dt
		for E in A.popups:E[3]-=B
		A.popups=[A for A in A.popups if A[3]>0];C=A.state
		if C=='ready':
			A.t-=B
			if A.t<=0:A.state='play';A.msg=None
		elif C=='play':A.play(B)
		elif C=='dying':
			A.t-=B
			if A.t<=0:
				if A.lives>0:A.lives-=1;A.reset_positions()
				else:A.state='over';A.msg='GAME OVER',A.A['bad'];A.save_hi()
		elif C=='clear':
			A.t-=B;D=L(V(A.t,0)/.25)%2==0
			if D!=A.flash:
				A.flash=D;A.wall_attr=A.A['flashwall']if D else A.A['wall']
				for(F,G)in A.walls:A.tile(F,G)
			if A.t<=0:A.level+=1;A.start_level()
	def play(A,dt):
		C=dt
		if A.freeze>0:A.freeze-=C;return
		if A.fright_t>0:
			A.fright_t-=C
			if A.fright_t<=0:A.end_fright()
		else:
			A.mode_t-=C
			if A.mode_t<=0 and A.mode_i<H(A.sched)-1:
				A.mode_i+=1;A.mode_t=A.sched[A.mode_i]
				for B in A.ghosts:
					if B.state=='out':B.rev=True
		if A.fruit_t>0:A.fruit_t-=C
		A.idle+=C;A.release();A.pacc+=A.pac_tps()*C;D=0
		while A.pacc>=1 and D<3:
			A.pacc-=1;D+=1;A.pac_step()
			if A.check():return
			if A.dots_left<=0:A.state='clear';A.t=2.2;A.flash=False;A.msg=None;return
		for B in A.ghosts:
			B.acc+=A.ghost_tps(B)*C;D=0
			while B.acc>=1 and D<3:
				B.acc-=1;D+=1;A.ghost_step(B)
				if A.check():return
	def handle_input(C):
		while True:
			D=C.scr.getch()
			if D==-1:return True
			if D==A.KEY_RESIZE:
				try:A.update_lines_cols()
				except AttributeError:0
				C.scr.clear();C.layout();continue
			if D in(B('q'),B('Q')):C.save_hi();return False
			if D in(B('r'),B('R')):
				if C.state in('over','pause'):C.new_game();continue
			if D in(B('p'),B('P'),B(' ')):
				if C.state=='pause':C.state=C.prev_state;C.msg=None
				elif C.state in('play','ready'):C.prev_state=C.state;C.state='pause';C.msg='PAUSED',C.A['text']
				continue
			if D in Z:C.want=Z[D]
	def put(B,y,x,s,attr=0):
		if y<0 or y>=B.rows or x<0 or x>=B.cols:return
		s=s[:B.cols-x-1]
		try:B.scr.addstr(y,x,s,attr)
		except A.error:0
	def tile(A,y,x):
		D=A.g[y][x];B=A.scale;C=A.ox+x*B
		if D=='#':A.put(y,C,' '*B,A.wall_attr)
		elif D=='.':A.put(y,C,'.'+' '*(B-1),A.A['dot'])
		elif D=='o':A.put(y,C,'O'+' '*(B-1)if A.blink else' '*B,A.A['pow'])
		elif D=='-':A.put(y,C,'-'*B,A.A['door'])
		else:A.put(y,C,' '*B)
	def actor(A,y,x,text,attr,xoff=0):B=A.scale;A.put(y,A.ox+x*B+xoff,text,attr);A.drawn.append((y,x,(H(text)+xoff+B-1)//B))
	def full_draw(A):
		A.scr.erase()
		for B in K(F):
			for D in K(C):
				if A.g[B][D]not in' x':A.tile(B,D)
		A.drawn=[];A.pkey=None;E='arrows/WASD move   P pause   R restart   Q quit'
		if A.rows>F:A.put(F,A.ox,E,0)
		A.full=False
	def pac_sprite(A):
		B=A.scale==2
		if A.state=='dying'and A.t<1.1:C=['\\/','()','--','..','  ']if B else['V','O','-','.',' '];F=J(4,L((1.1-V(A.t,0))/.22));return C[F]
		if not A.mouth or A.pdir==(0,0)and A.state!='ready':return'()'if B else'O'
		if A.state=='ready':return'()'if B else'O'
		H={G:'(>',E:'<)',D:'\\/',I:'/\\'}if B else{G:'>',E:'<',D:'V',I:'^'};return H[A.face]
	def draw_actors(A):
		for(N,F,G)in A.drawn:
			for O in K(G):
				if F+O<C:A.tile(N,F+O)
		A.drawn=[];B=A.scale;Q=A.state
		if A.fruit_t>0:S=P[J(A.level,H(P))-1][0];A.actor(U[0],U[1],S,A.A['fruit'],xoff=B//2)
		if not(Q=='clear'or Q=='dying'and A.t<1.1):
			for E in A.ghosts:
				if E.state in('eyes','enter'):I,D='oo'if B==2 else'o',A.A['eyes']
				elif E.fright:
					if A.fright_t<2 and L(A.fright_t*5)%2==0:I,D='MM'if B==2 else'M',A.A['fl']
					else:I,D='~~'if B==2 else'~',A.A['fr']
				else:I,D='MM'if B==2 else'M',A.ghost_attr[E.pair]
				A.actor(E.y,E.x,I,D)
		A.actor(A.py,A.px,A.pac_sprite(),A.A['pac'])
		for(N,F,M,T)in A.popups:A.actor(N,F,M,A.A['pop'])
		if A.msg:M,D=A.msg;G=(H(M)+B-1)//B;R=(C-G)//2;A.put(17,A.ox+R*B,M,D);A.drawn.append((17,R,G))
	def draw_panel(A):
		if A.cols-A.px_panel<14:return
		D=A.score,A.hi,A.level,A.lives,A.state
		if D==A.pkey:return
		A.pkey=D;B,C=A.px_panel,A.A;A.put(1,B,'SCORE',C['text']);A.put(2,B,'%-9d'%A.score);A.put(4,B,'HIGH',C['text']);A.put(5,B,'%-9d'%A.hi);A.put(7,B,'LEVEL',C['text']);A.put(8,B,'%-9d'%A.level);A.put(10,B,'LIVES',C['text']);A.put(11,B,'%-14s'%('(> '*A.lives))
		if A.state=='over':A.put(14,B,'R = play again',C['bad']);A.put(15,B,'Q = quit      ',C['bad'])
		else:A.put(14,B,' '*14);A.put(15,B,' '*14)
	def draw(A):
		B=L(M.monotonic()*3)%2==0
		if B!=A.blink:
			A.blink=B
			for C in(3,23):
				for D in(1,26):
					if A.g[C][D]=='o':A.tile(C,D)
		if A.full:A.full_draw()
		A.draw_actors();A.draw_panel();A.scr.refresh()
	def draw_small(A):A.scr.erase();A.put(0,0,'Window too small! You need %d rows x %d cols.'%(F,C*1+A.ox+1));A.put(1,0,'Enlarge or zoom out the terminal.');A.scr.refresh()
	def run(A):
		C=M.monotonic()
		while True:
			B=M.monotonic();E=J(B-C,.1);C=B
			if not A.handle_input():break
			if A.fits:
				if A.state!='pause':A.update(E)
				A.draw()
			else:A.draw_small()
			D=A.frame-(M.monotonic()-B)
			if D>0:M.sleep(D)
def l(scr,fps):k(scr,fps).run()
if __name__=='__main__':
	c=e.ArgumentParser(description='Terminal Pac-Man');c.add_argument('--fps',type=L,default=30,help='?');m=c.parse_args()
	try:A.wrapper(l,m.fps)
	except KeyboardInterrupt:0

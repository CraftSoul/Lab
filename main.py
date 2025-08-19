from kivy.app import App,Widget
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix. import 
from kivy.graphics import Color,Rectangle,Line
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.resources import resource_add_path
import random as r
from data import DATA
from os.path import exists,join,abspath
from os import mkdir
import sys


if __name__ == '__main__':
	if hasattr(sys, '_MEIPASS'):
		resource_add_path(join(sys._MEIPASS))
	resource_add_path(abspath("."))

Window.rotation=-90
Window.allow_screensaver=False
LabelBase.register(name='114',fn_regular='font.ttf')
layout=RelativeLayout()
holding=None
turn=0
ani=[]
oxygen=12
history=[]

class app(App):
	def __init__(self):
		super(app,self).__init__()
		self.bg=(source='/bg.png',allow_stretch=True,keep_ratio=True)
		Clock.schedule_interval(self.update,1/50)
		self.sample=Card(None,'抑制',0,pos_hint={'x':0.15,'y':0.275},size_hint=(0.15,0.45))
		self.dl=Button(text='保存',pos_hint={'x':0.15,'y':0.165},size_hint=(0.15,0.1),font_name='114',background_color=(3,2.73,2.4),color=(0,0,0))
		self.dl.bind(on_press=self.download)
		self.message=Popup(title='下载完成',title_font='114',content=Label(font_name='114'),size_hint=(0.7,0.4))
		self.index=0
		self.sample.bind(on_touch_down=self.renew)
		self.oxygen=Label(pos_hint={'x':-0.33,'y':-0.26},font_size='20sp',font_name='114')
		self.hp=Label(pos_hint={'x':-0.33,'y':-0.4},font_size='20sp',font_name='114')
		self.air=Button(background_color=(0,0,0,0))
		self.air.bind(on_press=self.sob)
		self.takethat=Button(text='出示',size_hint=(0.11,0.1),pos_hint={'x':0.78,'y':0.2},background_color=(0.5,0.2,0.2),font_name='114')
		self.amns=(source='/异议.png',pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.5,0.5),allow_stretch=True,keep_ratio=True)
		self.cnm=SoundLoader.load('/异议.ogg')
		self.cnm.bind(on_stop=self.aaa)
		self.takethat.bind(on_press=self.objection)
		self.endturn=Button(text='结束回合',size_hint=(0.11,0.1),pos_hint={'x':0.78,'y':0.05},background_color=(0.5,0.2,0.2),font_name='114')
		self.bgm=SoundLoader.load('/bgm.ogg')
		self.bgm.loop=True
		self.bgm.play()
		self.home=(pos_hint={'y':0},size_hint=(1,1.2),source='/home.png',allow_stretch=True,keep_ratio=True)
		u=Animation(pos_hint={'y':-0.2},duration=10)+Animation(pos_hint={'y':0},duration=10)
		u.repeat=True
		u.start(self.home)
		self.t=(source='/title.png',size_hint=(1,0.3),pos_hint={'y':0.6},allow_stretch=True,keep_ratio=True)
		self.help=Button(text='帮助',pos_hint={'x':0.35,'y':0.3},size_hint=(0.3,0.1),font_name='114',background_color=(3,2.73,2.4),color=(0,0,0))
		self.help.bind(on_press=self.guide)
		self.st=Button(text='开始',pos_hint={'x':0.35,'y':0.15},size_hint=(0.3,0.1),font_name='114',background_color=(3,2.73,2.4),color=(0,0,0))
		self.st.bind(on_press=self.go)
		self.bl=Rect((0,0,0,1),pos_hint={'y':1})
		self.inroduction=[Button(background_normal=f'/{x}.jpg') for x in range(4)]
		for x in self.inroduction:
			x.bind(on_press=layout.remove_widget)
		self.ending=1
		self.history=Label(pos_hint={'x':-0.1,'y':0},font_size='10sp',font_name='114',color=(0,0,0))
	def build(self):
		self.endturn.bind(on_press=sbs[0].endturn)
		layout.add_widget(self.home)
		layout.add_widget(self.t)
		layout.add_widget(self.sample)
		layout.add_widget(self.dl)
		layout.add_widget(self.help)
		layout.add_widget(self.st)
		layout.add_widget(self.bl)
		return layout
	def guide(self,i):
		if self.ending:
			for x in self.inroduction:
				layout.add_widget(x)
	def renew(self,a,t):
		if self.ending and self.sample.collide_point(*t.pos):
			self.index+=1
			if self.index==len(DATA):
				self.index=0
			layout.remove_widget(self.sample)
			self.sample=Card(None,list(DATA.keys())[self.index],0,pos_hint={'x':0.15,'y':0.275},size_hint=(0.15,0.45))
			layout.add_widget(self.sample,index=2)
			self.sample.bind(on_touch_down=self.renew)
	def download(self,i):
		if self.ending:
			self.path=join('/storage/emulated/0/Pictures/dl6_save',self.sample.name+'.png')
			if not exists('/storage/emulated/0/Pictures/dl6_save'):
				mkdir('/storage/emulated/0/Pictures/dl6_save')
			self.message.content.text=self.path
			self.sample.export_to_png(self.path)
			self.message.open()
	def go(self,s):
		if self.ending:
			self.ending=0
			a=Animation(pos_hint={'y':0},duration=0.5)+Animation(duration=1.3)+Animation(pos_hint={'y':-1},duration=0.2)
			a.start(self.bl)
			a.bind(on_complete=lambda a,b:layout.remove_widget(b))
			Clock.schedule_once(self.start,1.8)
	def start(self,dt):
		self.ending=1
		layout.remove_widget(self.home)
		layout.remove_widget(self.t)
		layout.remove_widget(self.sample)
		layout.remove_widget(self.dl)
		layout.remove_widget(self.help)
		layout.remove_widget(self.st)
		layout.add_widget(self.bg)
		layout.add_widget(Rect((0,0,0),pos_hint={'x':0.11,'y':0.01},size_hint=(0.12,0.3)))
		layout.add_widget(self.oxygen)
		layout.add_widget(self.hp)
		layout.add_widget(self.history)
		layout.add_widget(self.air)
		for x in sbs:
			if not x.is_player:
				layout.add_widget(x.head)
				layout.add_widget(x.ot)
				layout.add_widget(x.ht)
				layout.add_widget(x.ct)
			for y in range(4):
				x.draw()
		layout.remove_widget(self.bl)
		layout.add_widget(self.bl)
		sbs[0].on_turn()
	def update(self,dt):
		if self.ending:
			global oxygen,history
			if len(history)>10:
				history=history[-10:]
			self.history.text='\n'.join(history)
			if '大将军长枪' in sbs[0].cards and sbs[0].onturn and int(self.hp.text[3:])>sbs[0].hp:
				for o in range(len(sbs[0].cards)):
					if sbs[0].cards[o]=='大将军长枪' and sbs[0].card[o].skill[-1][1]!=2:
						sbs[0].card[o].skill[0]=sbs[0].card[o].skill[0][:2]+str(int(sbs[0].card[o].skill[0][2])-2)+sbs[0].card[o].skill[0][3:]
						sbs[0].card[o].discribe.text=sbs[0].card[o].skill[0]
						sbs[0].card[o].skill[1]=sbs[0].card[o].skill[1][:13]+sbs[0].card[o].skill[0][2]+sbs[0].card[o].skill[1][14:]
						sbs[0].card[o].skill[-1]=[sbs[0].card[o].skill[-1][0],sbs[0].card[o].skill[-1][1]-2,sbs[0].card[o].skill[-1][2]]
			if '抉择' in sbs[0].cards:
				for o in range(len(sbs[0].cards)):
					if sbs[0].cards[o]=='抉择':sbs[0].card[o].discribe.text=DATA['抉择'][0]%oxygen
			if sbs[0].oxygen<0:
				sbs[0].hp+=sbs[0].oxygen
				sbs[0].oxygen=0
			elif sbs[0].oxygen>10:
				sbs[0].hp+=sbs[0].oxygen-10
				sbs[0].oxygen=10
			if sbs[0].hp>10:
				sbs[0].hp=10
			elif sbs[0].hp<=0:
				self.bl.color.rgba=(0,0,0,0)
				self.dead()
			self.oxygen.text='氧气:'+str(sbs[0].oxygen)
			self.hp.text='体力:'+str(sbs[0].hp)
			for x in sbs[0].card:
				if holding is not x and x.cancel not in Animation._instances and x.pos_hint['y']>0.01:
					x.cancel.start(x)
			for x in sbs[1:]:
				if '大将军长枪' in x.cards and x.onturn and int(x.ht.text[3:])>x.hp:
					x.show('大将军长枪')
					for o in range(len(x.card)):
						if x.cards[o]=='大将军长枪' and x.card[o].skill[-1][1]!=2:
							x.card[o].skill[0]=x.card[o].skill[0][:2]+str(int(x.card[o].skill[0][2])-2)+x.card[o].skill[0][3:]
							x.card[o].discribe.text=x.card[o].skill[0]
							x.card[o].skill[1]=x.card[o].skill[1][:13]+x.card[o].skill[0][2]+x.card[o].skill[1][14:]
							x.card[o].skill[-1]=[x.card[o].skill[-1][0],x.card[o].skill[-1][1]-2,x.card[o].skill[-1][2]]
				if x.oxygen<0:
					x.hp+=x.oxygen
					x.oxygen=0
				elif x.oxygen>10:
					x.hp+=x.oxygen-10
					x.oxygen=10
				if x.hp>10:
					x.hp=10
				elif x.hp<=0:
					oxygen+=x.oxygen
					if x.onturn:
						x.endturn()
					layout.remove_widget(x.ot)
					layout.remove_widget(x.ht)
					layout.remove_widget(x.ct)
					del sbs[sbs.index(x)]
				x.ot.text='氧气:'+str(x.oxygen)
				x.ht.text='体力:'+str(x.hp)
				x.ct.text='手牌:'+str(len(x.cards))
			if ani and ani[0].a not in Animation._instances:
				ani[0].a.start(ani[0])
				ani[0].a.bind(on_complete=ani[0].finish)
			if len(sbs)==1 and sbs[0].hp>0:
				self.bl.color.rgba=(1,1,1,0)
				self.dead()
		if self.cnm.state=='play':
			if self.ending:
				layout.remove_widget(self.amns)
				layout.add_widget(self.amns)
			self.amns.pos_hint={'center_x':0.498+0.004*r.random(),'center_y':0.498+0.004*r.random()}
	def sob(self,i):
		global holding
		holding=None
		if len(sbs[0].card):
			sbs[0].choice=sbs[0].card[0]
	def objection(self,i):
		if self.cnm.state!='play' and self.ending:
			layout.add_widget(self.amns)
			self.cnm.play()
			if holding:
				sbs[0].takethat(holding)
	def aaa(self,i):
		layout.remove_widget(self.amns)
	def dead(self):
		if self.ending:
			self.ending=0
			self.bl.pos_hint={'y':0}
			qwq=Animation(a=1,duration=5,transition='linear' if len(sbs)==1 else 'out_bounce')+Animation(duration=5)+Animation(a=0,duration=5)
			qwq.start(self.bl.color)
			qwq.bind(on_complete=self.remove)
			qvq=Animation(volume=0,duration=5)+Animation(duration=5)+Animation(volume=1,duration=5)
			qvq.start(self.bgm)
			layout.add_widget(self.bl)
			Clock.schedule_once(self.restart,5)
	def restart(self,a):
		global holding,ani,history,sbs,layout,oxygen,turn
		holding=None
		ani=[]
		history=[]
		oxygen=12
		turn=0
		layout.clear_widgets()
		self.endturn.unbind(on_press=sbs[0].endturn)
		sbs=[Player('咪酱',1,0,{'x':1.1,'y':0.01},0),Player('御剑信',0,0.1,{'x':-0.11,'y':0.35},1),Player('灰根高太郎',0,0.5,{'x':0.6,'y':1},2)]
		self.build()
	def remove(self,a,b):
		self.bl.color.rgba=(0,0,0,1)
		self.bl.pos_hint={'y':1}
		self.ending=1

class Card(RelativeLayout):
	def __init__(self,player,name,da=1,**kwargs):
		super(Card,self).__init__(**kwargs)
		self.player=player
		self.name=name
		self.skill=list(DATA[name])
		self.hold=Animation(pos_hint={'y':0.05},duration=0.1)
		self.cancel=Animation(pos_hint={'y':0.01},duration=0.1)
		if da:self.renew(len(player.cards),0.5)
		else:self.a=Animation()
		with self.canvas:
			Color(0.3,0.2,0.2)
			self.rect=Rectangle(size=self.size)
			self.add_widget((source=f'/{name}.png',size_hint=(0.9,0.52),pos_hint={'x':0.05,'y':0.45},allow_stretch=True,keep_ratio=False))
			self.line=Line(points=[[0.98,0.48],[0.75,0.46],[0.25,0.46],[0.02,0.48]],color=(1,1,1))
			self.nt=Label(text=name,font_name='114',pos_hint={'y':-0.04},color=(0,0,0))
			self.add_widget(self.nt)
			self.discribe=Label(text=self.skill[0]%oxygen if name=='抉择' else self.skill[0],pos_hint={'y':-0.28},color=(1,1,1),font_name='114')
			self.add_widget(self.discribe)
		self.bind(size=self.u)
	def u(self,*args):
		self.rect.size=self.size
		self.nt.font_size=0.09*self.size_hint[1]*layout.height
		self.discribe.font_size=0.07*self.size_hint[1]*layout.height
		self.line.width=width=0.05*self.size_hint[1]*layout.height
		for x in range(8):
			if x%2:
				self.line.points[x]*=self.height
			else:
				self.line.points[x]*=self.width
	def on_touch_down(self,touch):
		if self.a not in Animation._instances and self.player:
			global holding
			if self.collide_point(*touch.pos):
				holding=self
				self.player.choice=self
				self.hold.start(self)
				return True
			return super(Card,self).on_touch_down(touch)
	def finish(self,a,b):
		del ani[0]
		layout.remove_widget(self)
	def renew(self,index,t):
		self.a=Animation(pos_hint={'x':0.13+0.108*index},duration=t,transition='out_quad')
		self.a.start(self)

class Player:
	def __init__(self,name,is_player,x,take,index):
		self.choice=None
		self.is_player=is_player
		self.oxygen=6
		self.hp=10
		self.cards=[]
		self.card=[]
		self.defendant=1
		self.name=name
		self.onturn=0
		self.combo=0
		self.take=take
		self.index=index
		if is_player:
			self.ttt=Button(text='确定',pos_hint={'x':0.78,'y':0.2},size_hint=(0.11,0.1),background_color=(0.5,0.2,0.2),font_name='114')
			self.ttt.bind(on_press=self.eureka)
			self.a=Button(text='A',pos_hint={'x':0.78,'y':0.2},size_hint=(0.11,0.1),background_color=(0.5,0.2,0.2),font_name='114')
			self.a.bind(on_press=self.shift)
			self.b=Button(text='B',pos_hint={'x':0.78,'y':0.05},size_hint=(0.11,0.1),background_color=(0.2,0.2,0.5),font_name='114')
			self.b.bind(on_press=self.shift)
			self.indicate=Button(text='指证',pos_hint={'x':0.78,'y':0.2},size_hint=(0.11,0.1),background_color=(0.5,0.2,0.2),font_name='114')
			self.indicate.bind(on_press=self.usa)
			self.o=Button(text='选择',pos_hint={'x':0.1,'y':0.5},size_hint=(0.1,0.1),background_color=(0.5,0.2,0.2,0.5),font_name='114')
			self.o.bind(on_press=self.ddj)
			self.t=Button(text='选择',pos_hint={'x':0.5,'y':0.5},size_hint=(0.1,0.1),background_color=(0.5,0.2,0.2,1),font_name='114')
			self.t.bind(on_press=self.ddj)
			self.oa=Animation(background_color=(0.5,0.2,0.2,0.5),duration=0.1)
			self.ca=Animation(background_color=(0.5,0.2,0.2,1),duration=0.1)
		else:
			self.head=(source=f'/{name}.png',size_hint=(0.1,0.2),pos_hint={'x':x,'y':0.6},allow_stretch=True,keep_ratio=True)
			self.ot=Label(font_name='114',pos_hint={'x':x-0.35,'y':0.26},font_size='20sp',color=(0,0,0))
			self.ht=Label(font_name='114',pos_hint={'x':x-0.35,'y':0.2},font_size='20sp',color=(0,0,0))
			self.ct=Label(font_name='114',pos_hint={'x':x-0.35,'y':0.14},font_size='20sp',color=(0,0,0))
	def draw(self,name=0):
		if len(self.cards)<5 and dl6.ending:
			if name:
				self.cards.append(name)
				self.show(name)
			else:
				self.cards.append(r.choice(list(DATA.keys())[:-3]))
			self.card.append(Card(self,self.cards[-1],self.is_player,pos_hint=self.take,size_hint=(0.1,0.3)))
			if self.is_player:
				layout.add_widget(self.card[-1])
	def abandon(self,card,used=0):
		if self.cards and dl6.ending:
			x=self.card.index(card)
			del self.cards[x]
			del self.card[x]
			global holding
			holding=None
			card.a=Animation(pos_hint={'x':0.7,'y':0.35},duration=0.5,transition='out_quad')+Animation(pos_hint={'x':1},duration=1,transition='in_quad')
			ani.append(card)
			if self.is_player:
				for y,z in enumerate(self.card[x:]):
					if z.a not in Animation._instances:
						z.renew(x+y+1,0.2)
			else:
				layout.add_widget(card)
			if used:
				history.append(f'使用{card.name}')
				if card.skill[-1]:
					exec(card.skill[1])
				elif self.is_player:
					layout.add_widget(self.a)
					layout.add_widget(self.b)
				else:
					qwq=r.choices((0,1),weights=(self.weight(card.skill[-3]),self.weight(card.skill[-2])))[0]
					history.append(f'抉择{"AB"[qwq]}')
					exec(card.skill[1+qwq])
			else:
				if card.name in ('思考者','勾玉'):
					exec(card.skill[-2])
				history.append(f'{self.name}弃置{card.name}')
		return card.name
	def takethat(self,card):
		self.wtf=card
		self.abandon(card,1)
		if not self.is_player:
			Clock.schedule_once(lambda x,dt=0:self.AI(1),3)
	def choose(self):
		if self.cards and dl6.ending:
			if self.is_player:
				self.choice=self.card[0]
				layout.add_widget(self.ttt)
			else:
				Clock.schedule_once(lambda x,dt=0:self.AI(0),1.5)
	def eureka(self,instance=None):
		if dl6.ending:
			if self.is_player:
				if dl6.cnm.state!='play':
					global holding
					layout.remove_widget(instance)
					self.abandon(self.choice)
			else:
				self.abandon(self.choice)
	def shift(self,instance):
		if dl6.ending:
			layout.remove_widget(self.a)
			layout.remove_widget(self.b)
			history.append(f'抉择{instance.text}')
			exec(self.wtf.skill[1+'AB'.index(instance.text)])
	def objection(self):
		if dl6.ending:
			if len(sbs)>=3:
				if self.is_player:
					layout.add_widget(self.indicate)
					layout.add_widget(self.o)
					layout.add_widget(self.t)
				else:
					self.defendant=(sbs.index(self)+r.randint(1,len(sbs)-1))%len(sbs)
					history.append(f'指证{sbs[self.defendant].name}')
					exec(self.wtf.skill[3 if self.wtf.name=='手枪' else 2])
			else:
				self.defendant=self.is_player
				history.append(f'指证{sbs[self.defendant].name}')
				exec(self.wtf.skill[3 if self.wtf.name=='手枪' else 2])
	def ddj(self,instance):
		if dl6.ending:
			self.oa.stop(self.o)
			self.ca.stop(self.o)
			self.oa.stop(self.t)
			self.ca.stop(self.t)
			if instance is self.o:
				self.defendant=1
				self.oa.start(self.o)
				self.ca.start(self.t)
			else:
				self.defendant=2
				self.ca.start(self.o)
				self.oa.start(self.t)
	def usa(self,instance):
		if dl6.ending:
			history.append(f'指证{sbs[self.defendant].name}')
			layout.remove_widget(instance)
			layout.remove_widget(self.o)
			layout.remove_widget(self.t)
			exec(self.wtf.skill[3 if self.wtf.name=='手枪' else 2])
	def on_turn(self,dt=0):
		if dl6.ending:
			global turn
			self.onturn=1
			history.append(f'{self.name}回合开始')
			self.cards.append('抉择' if oxygen else '挣扎')
			self.card.append(Card(self,self.cards[-1],0,pos_hint=self.take,size_hint=(0.1,0.3)))
			if self.is_player:
				layout.add_widget(dl6.takethat)
				layout.add_widget(dl6.endturn)
				turn+=1
				layout.add_widget(self.card[-1])
			self.takethat(self.card[-1])
			if turn>3:
				self.oxygen-=1
				if self.oxygen<0:
					self.combo+=1
					self.hp-=self.combo
					self.oxygen=0
				else:
					self.combo=0
	def endturn(self,instance=None):
		if dl6.ending and self.onturn:
			if self.is_player and not(self.ttt.parent or self.indicate.parent):
				layout.remove_widget(dl6.endturn)
				layout.remove_widget(dl6.takethat)
				Clock.schedule_once(sbs[self.index+1 if self.index+1<len(sbs) else 0].on_turn,1)
				self.onturn=0
			else:
				Clock.schedule_once(sbs[self.index+1 if self.index+1<len(sbs) else 0].on_turn,1)
				self.onturn=0
	def weight(self,points):
		return 5*points[0]*(8-len(self.cards)-points[0])+points[1]*(18-self.oxygen-points[1])+2*points[2]*(15-self.hp-points[2])
	def AI(self,a):
		if dl6.ending and (self.onturn or not a):
			if self.cards:
				if len(self.cards)==1:
					if a:
						self.endturn()
					else:
						self.choice=self.cards[0]
						self.eureka()
				else:
					w=[]
					for x in self.card:
						if x.skill[-1]:
							w.append(self.weight(x.skill[-1]))
						else:
							w.append((self.weight(x.skill[-3])+self.weight(x.skill[-2]))*0.5)
						if x.name=='金属探测器':
							w[-1]*=0.5
						elif x.name=='相机' and self.hp>5:
							w[-1]*=0.1
						elif not a:
							if x.name in ('思考者','勾玉'):
								w[-1]*=1.5
							elif x.name=='心灵枷锁':
								w[-1]*=0.01
					if a:
						if max(w)>=120 or len(self.cards)==5:
							self.takethat(r.choices(self.card,weights=w)[0])
						else:
							self.endturn()
					else:
						self.choice=r.choices(self.card,weights=(1-x/sum(w) for x in w))[0]
						self.eureka()
			elif a:
				self.endturn()
	def breathe(self,value):
		global oxygen
		self.oxygen+=value
		oxygen-=value
		if oxygen<0:
			self.oxygen+=oxygen
			oxygen=0
	def show(self,name):
		if not self.is_player:
			card=Card(self,name,pos_hint=self.take,size_hint=(0.1,0.3))
			layout.add_widget(card)
			card.a=Animation(pos_hint={'x':0.4*self.take['x']+0.27,'y':0.4*self.take['y']+0.21},duration=0.5,transition='out_quad')+Animation(pos_hint=self.take,duration=0.5,transition='in_quad')
			card.a.start(card)
			card.a.bind(on_complete=qwq)

def qwq(a,i):
	layout.remove_widget(i)
	del i

class Rect(Widget):
	def __init__(self,color,**kwargs):
		super(Rect,self).__init__(**kwargs)
		with self.canvas:
			self.color=Color(*color)
			self.rect=Rectangle(pos=self.pos,size=self.size)
		self.bind(pos=self.u,size=self.u)
	def u(self,*args):
		self.rect.pos=self.pos
		self.rect.size=self.size

sbs=[Player('咪酱',1,0,{'x':1.1,'y':0.01},0),Player('御剑信',0,0.1,{'x':-0.11,'y':0.35},1),Player('灰根高太郎',0,0.5,{'x':0.6,'y':1},2)]
dl6=app()
dl6.run()

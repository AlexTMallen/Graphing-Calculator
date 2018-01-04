
###--GRAPHING CALCULATOR--###
#imports
import random
import pygame
import statistics
import math
"""import scipy"""
from pygame import Rect, draw
from math import cos, sin, tan, log, log10, acos, asin, atan, e, pi
"""from scipy import stats"""

pygame.init()
pygame.font.init()
pygame.key.set_repeat(350,60)

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,170,0)
l_blue = (0,255,255)
magenta = (255,0,255)
black = (0,0,0)
white = (255,255,255)
l_grey = (230,230,230)
m_grey = (190,190,190)
d_grey = (150,150,150)

#window
w_width = 700
w_height = 500
w = pygame.display.set_mode([w_width,w_height])
w.fill(white)
pygame.display.set_caption("V3 GRAPHING CALCULATOR AND STATISTICAL UTILITY")

#clock
clock = pygame.time.Clock()


#setting the different fonts
font = "consolas"
font_xs = pygame.font.SysFont(font, 10)
font_sml = pygame.font.SysFont(font, 12)
font_med_sml = pygame.font.SysFont(font, 14)
font_reg = pygame.font.SysFont(font, 16)
font_lrg = pygame.font.SysFont(font, 21)
font_hug = pygame.font.SysFont(font, 38)


letters = "abcdefghijklmnopqrstuvwxyz"
caps_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

buttons = []
for x in range(500):
	if x <= 99 or x >= 152:
		buttons.append(["","","",l_grey,2,font_reg,"None"])
	elif x < 126:
		buttons.append([letters[x-100],letters[x-100],letters[x-100],l_grey,2,font_reg,"letter"])
	elif x < 152:
		buttons.append([caps_letters[x-126],caps_letters[x-126],caps_letters[x-126],l_grey,2,font_reg,"caps_letter"])
#list of the useable characters[i] = ["text to display","interpreted string to evaluate",button color,outline thickness,size of text,type of character]
buttons[0] = ["(","(","(",l_grey,2,font_reg,"unsimplified"]
buttons[1] = [")",")",")",l_grey,2,font_reg,"unsimplified"]
buttons[2] = ["^","^","**",l_grey,2,font_lrg,"operator"]
buttons[3] = ["+","+","+",l_grey,2,font_lrg,"operator"]
buttons[4] = ["7","7","7",white,2,font_reg,"number"]
buttons[5] = ["8","8","8",white,2,font_reg,"number"]
buttons[6] = ["9","9","9",white,2,font_reg,"number"]
buttons[7] = ["-","-","-",l_grey,2,font_lrg,"operator"]
buttons[8] = ["4","4","4",white,2,font_reg,"number"]
buttons[9] = ["5","5","5",white,2,font_reg,"number"]
buttons[10] = ["6","6","6",white,2,font_reg,"number"]
buttons[11] = ["*","*","*",l_grey,2,font_lrg,"operator"]
buttons[12] = ["1","1","1",white,2,font_reg,"number"]
buttons[13] = ["2","2","2",white,2,font_reg,"number"]
buttons[14] = ["3","3","3",white,2,font_reg,"number"]
buttons[15] = ["/","/","/",l_grey,2,font_lrg,"operator"]
buttons[16] = ["0","0","0",white,2,font_reg,"number"]
buttons[17] = [".",".",".",white,2,font_lrg,"number"]
buttons[18] = ["enter","","",l_grey,2,font_sml,"command"]
buttons[19] = ["","","",l_grey,2,font_sml,"command"]
buttons[20] = ["sin","sin(","sin(",l_grey,2,font_reg,"function"]
buttons[21] = ["cos","cos(","cos(",l_grey,2,font_reg,"function"]
buttons[22] = ["tan","tan(","tan(",l_grey,2,font_reg,"function"]
buttons[23] = ["log(a,b)","log(","log(",l_grey,2,font_xs,"function"]
buttons[24] = ["Ã�â‚¬","Ã�â‚¬","3.14159265359",l_grey,2,font_lrg,"unsimplified"]
buttons[25] = ["CLR","","",white,2,font_reg,"command"]
buttons[26] = ["arcsin","arcsin(","asin(",l_grey,2,font_sml,"function"]
buttons[27] = ["arccos","arccos(","acos(",l_grey,2,font_sml,"function"]
buttons[28] = ["arctan","arctan(","atan(",l_grey,2,font_sml,"function"]
buttons[29] = ["ln","ln(","log(",l_grey,2,font_reg,"function"]
buttons[30] = ["e","e","2.718281828",l_grey,2,font_lrg,"unsimplified"]
buttons[31] = ["BSPC","","",white,2,font_reg,"command"]
buttons[32] = ["csc","csc(","csc(",l_grey,2,font_reg,"function"]
buttons[33] = ["sec","sec(","sec(",l_grey,2,font_reg,"function"]
buttons[34] = ["cot","cot(","cot(",l_grey,2,font_reg,"function"]
buttons[35] = ["Î£","Î£","",l_grey,2,font_lrg,"function"]
buttons[36] = ["x","x","x",l_grey,2,font_lrg,"unsimplified"]
buttons[37] = ["DEL","","",white,2,font_reg,"command"]
buttons[41] = ["!","!","fact(",l_grey,2,font_lrg,"function"]
buttons[42] = ["abs","abs(","abs(",l_grey,2,font_reg,"symbol"]
buttons[43] = ["SPC"," "," ",white,2,font_reg,"symbol"]
buttons[44] = [",",",",",",l_grey,2,font_reg,"symbol"]
buttons[45] = ["_","_","_",l_grey,2,font_reg,"symbol"]
buttons[46] = ["\"","\"","\"",l_grey,2,font_reg,"symbol"]
buttons[47] = ["","","",l_grey,2,font_reg,"symbol"]
buttons[49] = ["MORE","","",white,2,font_reg,"command"]
buttons[50] = ["UP","","",l_grey,2,font_lrg,"command"]
buttons[51] = ["LEFT","","",l_grey,2,font_lrg,"command"]
buttons[52] = ["DOWN","","",l_grey,2,font_lrg,"command"]
buttons[53] = ["RIGHT","","",l_grey,2,font_lrg,"command"]
buttons[54] = ["CALCULATOR","","",d_grey,2,font_reg,"command"]
buttons[55] = ["GRAPH","","",d_grey,2,font_reg,"command"]
buttons[56] = ["STATS","","",d_grey,2,font_reg,"command"]
buttons[57] = ["TAB","","",d_grey,2,font_reg,"command"]
buttons[58] = ["SETTINGS","","",d_grey,2,font_reg,"command"]
buttons[59] = ["F1","","",white,2,font_reg,"command"]
buttons[60] = ["F2","","",white,2,font_reg,"command"]
buttons[61] = ["F3","","",white,2,font_reg,"command"]
buttons[62] = ["F4","","",white,2,font_reg,"command"]
buttons[63] = ["F5","","",white,2,font_reg,"command"]
buttons[64] = ["F6","","",white,2,font_reg,"command"]
buttons[65] = ["HIDE_KEYBOARD","","",white,2,font_reg,"command"]
buttons[66] = ["ZOOM_OUT","","",white,2,font_reg,"command"]
buttons[67] = ["ZOOM_IN","","",white,2,font_reg,"command"]
buttons[68] = ["TRACE","","",white,2,font_reg,"command"]
buttons[69] = ["SHIFT_RIGHT","","",white,2,font_reg,"command"]
buttons[70] = ["SHIFT_UP","","",white,2,font_reg,"command"]
buttons[71] = ["SHIFT_LEFT","","",white,2,font_reg,"command"]
buttons[72] = ["SHIFT_DOWN","","",white,2,font_reg,"command"]
buttons[73] = ["PLOT","","",white,2,font_reg,"command"]
buttons[74] = ["CALCULATE","","",white,2,font_reg,"command"]
buttons[75] = ["VIEW_PLOT","","",white,2,font_reg,"command"]
buttons[76] = ["1:BOXPLOT","","",white,2,font_reg,"command"]
buttons[77] = ["2:HISTOGRAM","","",white,2,font_reg,"command"]
buttons[78] = ["3:OGIVE","","",white,2,font_reg,"command"]
buttons[79] = ["4:SCATTERPLOT","","",white,2,font_reg,"command"]
buttons[80] = ["5:REGRESSION","","",white,2,font_reg,"command"]
buttons[81] = ["done","","",white,2,font_reg,"command"]
buttons[82] = ["back","","",white,2,font_reg,"command"]
buttons[84] = ["DELETE_PLOT1","","",white,2,font_reg,"command"]
buttons[85] = ["DELETE_PLOT2","","",white,2,font_reg,"command"]
buttons[86] = ["DELETE_PLOT3","","",white,2,font_reg,"command"]
buttons[87] = ["DELETE_PLOT4","","",white,2,font_reg,"command"]
buttons[88] = ["DELETE_PLOT5","","",white,2,font_reg,"command"]
buttons[89] = ["DELETE_PLOT6","","",white,2,font_reg,"command"]
buttons[90] = ["PAGE1","","",white,2,font_reg,"command"]
buttons[91] = ["PAGE2","","",white,2,font_reg,"command"]
buttons[92] = ["PAGE3","","",white,2,font_reg,"command"]
buttons[93] = ["PAGE4","","",white,2,font_reg,"command"]
buttons[94] = ["PAGE5","","",white,2,font_reg,"command"]
buttons[95] = ["PAGE6","","",white,2,font_reg,"command"]
buttons[96] = ["PAGE7","","",white,2,font_reg,"command"]
buttons[392] = ["LIST_BOX","","",white,2,font_reg,"command"]


b_text = 0
b_display = 1
b_resolve = 2
b_color = 3
b_thickness = 4
b_font = 5
b_type = 6

running = True


while running:
	try:
		#all of the hitboxes with an x value > 1000 are not on the screen in the calculate tab
		s_inputs = []
		for num in range(100):
			s_inputs.append(["","",Rect(-10000,20,200,25),num,num])
		#list of stats inputs[i] = ["text that decribes it","input",hitbox for editing,max index of inputs on that screen, min index]
		s_inputs[0] = ["LIST: ","L1",Rect(1330,20,200,25),0,2]
		s_inputs[1] = ["FREQUENCY LIST: ","",Rect(1330,60,200,25),0,2]
		s_inputs[2] = ["ADJUSTED: ","True",Rect(1330,100,200,25),0,2]
		s_inputs[5] = ["LIST: ","L1",Rect(1330,100,200,25),5,8]
		s_inputs[6] = ["FREQUENCY LIST: ","",Rect(1330,100,200,25),5,8]
		s_inputs[7] = ["NUMBER OF BARS: ","10",Rect(1330,100,200,25),5,8]
		s_inputs[8] = ["BAR WIDTH: ","",Rect(1330,100,200,25),5,8]
		s_inputs[10] = ["LIST: ","L1",Rect(1330,20,200,25),10,11]
		s_inputs[11] = ["FREQUENCY LIST: ","",Rect(1330,60,200,25),10,11]
		s_inputs[15] = ["X LIST: ","L2",Rect(1330,20,200,25),15,16]
		s_inputs[16] = ["Y LIST: ","L3",Rect(1330,60,200,25),15,16]
		s_inputs[20] = ["X LIST: ","L2",Rect(1330,20,200,25),20,22]
		s_inputs[21] = ["Y LIST: ","L3",Rect(1330,60,200,25),20,22]
		s_inputs[22] = ["LINE TYPE: ","linear",Rect(1330,100,200,25),20,22]
		s_inputs[99] = ["EDITING_LIST","",Rect(-1,-1,1,1),99,99]
		s_text = 0
		s_input = 1
		s_hitbox = 2
		s_min = 3
		s_max = 4
		
		s_calculations = [["", "", Rect(1300, 20 + (num % 8) * 28, 200, 25), num] for num in range(100)]
		#list of the metrics the user can calculate[i] = [text that decribes it","string version of the answer",hitbox for selecting, i]
		s_calculations[0][s_text] = "MINIMUM"
		s_calculations[1][s_text] = "FIRST QUARTILE"
		s_calculations[2][s_text] = "MEDIAN"
		s_calculations[3][s_text] = "THIRD QUARTILE"
		s_calculations[4][s_text] = "MAXIMUM"
		s_calculations[5][s_text] = "INTER-QUARTILE RANGE"
		s_calculations[6][s_text] = "RANGE"
		s_calculations[7][s_text] = "OUTLIERS"
		s_calculations[8][s_text] = "MEAN"
		s_calculations[9][s_text] = "STANDARD DEVIATION"
		s_calculations[10][s_text] = "VARIANCE"
		s_calculations[11][s_text] = "SUM"
		s_calculations[12][s_text] = "SUM OF X SQUARED"
		s_calculations[13][s_text] = "LENGTH"
		
		setting_names = [
			"Graph x min",
			"Graph x max",
			"Graph y min",
			"Graph y max",
			"F1 color",
			"F2 color",
			"F3 color",
			"F4 color",
			"F5 color",
			"F6 color"
			]
		num_unused_settings = 28 - len(setting_names)
		setting_names += ["< >"]*num_unused_settings
		
		###---RECTANGLES---###
		keyboard = Rect(50,250,640,255)
		keyboard_background = Rect(47,248,645,240)
		r_keyboard = Rect(500,250,190,240)
		l_keyboard = Rect(60,280,340,200)
		
		vert_pad = Rect(425,370,20,70)
		hor_pad = Rect(400,395,70,20)
		up_button = Rect(425,370,20,25)
		down_button = Rect(425,415,20,25)
		left_button = Rect(400,395,25,20)
		right_button = Rect(445,395,25,20)
		move_buttons = [left_button,right_button,up_button,down_button]
		display = Rect(50,50,640,180)
		move_xs = [417, 402, 414, 448]
		move_ys = [372, 385, 422, 387]
		
		tab1 = Rect(10,380,22,115)
		tab2 = Rect(10,305,22,70)
		tab3 = Rect(10,220,22,80)
		tab4 = Rect(10,135,22,80)
		tab5 = Rect(10,35,22,95)
		tabs = [tab1,tab2,tab3,tab4,tab5]
		
		function_box = Rect(55,2,250,250)
		left_bar = Rect(55,2,46,250)
		graph_box = Rect(305,0,380,248)
		F_buttons = [Rect(1070,(15 + num * 41),24,24) for num in range(6)]
		function_hitboxes = [Rect(1101,2 + 41 * num,204,41) for num in range(6)]
		
		hide_keyboard = Rect(keyboard.x+5,keyboard.y+5,20,20)
		
		zoom_bar = Rect(1685,0,15,248)
		zoom_in = Rect(1685,50,15,50)
		zoom_out = Rect(1685,0,15,50)
		trace_box = Rect(6185,100,15,50)
		shift_right = Rect(1660,112,25,25)
		shift_up = Rect(1483,0,25,25)
		shift_left = Rect(1305,112,25,25)
		shift_down = Rect(1483,223,25,25)
		shifts = [shift_right,shift_up,shift_left,shift_down]
		shift_points = [(668,107),(478,-3),(304,104),(476,232)]
		
		list_box = Rect(1055,2,120,250)
		label_box = Rect(55,2,50,30)
		list_label = font_reg.render("LIST",False,d_grey)
		list_texts = [
		font_reg.render("L1",False,red),
		font_reg.render("L2",False,green),
		font_reg.render("L3",False,blue),
		font_reg.render("L4",False,orange),
		font_reg.render("L5",False,magenta),
		font_reg.render("L6",False,l_blue)]
		
		L_buttons = [Rect(1070,(39 + num * 36),24,24) for num in range(6)]
		
		stats_tabs = [Rect(1199,10,25,60),Rect(1199,75,25,110)]
		
		active_plots_bar = Rect(229,0,80,248)
		plots_text = font_lrg.render("PLOTS",False,d_grey)
		view_plot = Rect(1232,225,69,20)
		view_plot_text = font_sml.render("view plot",False,d_grey)
		hide_plot_text = font_sml.render("hide plot",False,d_grey)
		plot_box = Rect(313,0,387,248)
		plot_boxes = [Rect(1330,(20 + num * 40),200,25) for num in range(5)]
		
		done_box = Rect(1500,210,80,25)
		done_text = font_reg.render("done",False,d_grey)
		back_box = Rect(1600,210,80,25)
		back_text = font_reg.render("back",False,d_grey)
		
		delete_plots = [Rect(760,60 + num * 40,20,20) for num in range(6)]
		
		page_selection_bar = Rect(229,0,35,248)
		page_number_boxes = [Rect(1232,num,30,34) for num in range(3,248,35)]
		page_box = Rect(264,0,436,248)
		
		#settings screen
		settings_background = Rect(45,0,655,248)
		settings_header = font_hug.render("SETTINGS",False,m_grey)
		settings_boxes = [Rect(1060 + 160 * (num // 7),50 + 29 * (num % 7),150,20) for num in range(28)]
		print(settings_boxes)
		
		
		###MAKING LIST OF HITBOXES FOR BUTTONS###
		i = 0
		hitboxes = []
		#range(152)
		for x in range(152):
			hitboxes.append(Rect(-100,-100,1,1))
		#range(152,252)
		for s in s_inputs:
			hitboxes.append(s[s_hitbox])
		#range(252,352)
		for s in s_calculations:
			hitboxes.append(s[s_hitbox])
		#range(352,380)
		for box in settings_boxes:
			hitboxes.append(box)
		#range(380,386)
		for box in function_hitboxes:
			hitboxes.append(box)
		#range(386,392)
		for box in L_buttons:
			hitboxes.append(box)
		hitboxes.append(list_box)
		
			
		y = r_keyboard.y + 10
		for b_row in range(5):
			x = r_keyboard.x
			for b_col  in range(4):
				
				hitboxes[i] = Rect(x,y,40,25)
				
				if i == 18:
					hitboxes[18] = Rect(x,y,87,25)
					print("-----",hitboxes[18])
					break
				i += 1
				x += int(r_keyboard.width/4)
			y += int(r_keyboard.height/5)
		i = 20
		y = l_keyboard.y + 10
		for b_row in range(5):
			x = l_keyboard.x
			for b_col in range(6):
				hitboxes[i] = Rect(x,y,50,25)
				
				i += 1
				x += int(l_keyboard.width/6)
			y += int(l_keyboard.height/5)
		hitboxes[50] = up_button
		hitboxes[51] = left_button
		hitboxes[52] = down_button
		hitboxes[53] = right_button
		i = 54
		for tab in tabs:
			hitboxes[i] = tab
			i += 1
		for f in F_buttons:
			hitboxes[i] = f
			i += 1
		hitboxes[65] = hide_keyboard
		hitboxes[66] = zoom_out
		hitboxes[67] = zoom_in
		hitboxes[68] = trace_box
		i = 69
		for rect in shifts:
			hitboxes[i] = shifts[i-69]
			i += 1
		hitboxes[73] = stats_tabs[0]
		hitboxes[74] = stats_tabs[1]
		hitboxes[75] = view_plot
		i = 76
		for plot in plot_boxes:
			hitboxes[i] = plot
			i += 1
		hitboxes[81] = done_box
		hitboxes[82] = back_box
		i = 84
		for delete in delete_plots:
			hitboxes[i] = delete
			i += 1
		i = 90
		for box in page_number_boxes:
			hitboxes[i] = box
			i += 1
		i = 97
		
		
		print(hitboxes[97])
		#making a list of what hitboxes(other than the ones on the keyboard and tabs) should be present for each screen
		calculator_hitboxes = []
		graphing_hitboxes = list(range(59,65)) + list(range(66,73)) + list(range(380,386))
		stats_plot_hitboxes = list(range(73,90)) + list(range(152,252)) + list(range(386,393))
		stats_calculate_hitboxes = list(range(73,75)) + list(range(90,97)) + list(range(252,352)) + list(range(386,393))
		settings_hitboxes = list(range(352,380))
		active_hitbox_list = "calculator_hitboxes"	
		print(stats_calculate_hitboxes)
		
		
		
		###---DRAWING FUNCTIONS---###
		def draw_keyboard():
			draw.rect(w,l_grey,keyboard_background)
			if keyboard_hidden and keyboard.y < 490:
				keyboard.y += 10
				r_keyboard.y += 10
				l_keyboard.y += 10
				hor_pad.y += 10
				vert_pad.y += 10
				for y in move_buttons:
					y.y += 10
				for y in move_ys:
					y += 10
			if not keyboard_hidden and keyboard.y > 250:
				keyboard.y -= 10
				r_keyboard.y -= 10
				l_keyboard.y -= 10
				hor_pad.y -= 10
				vert_pad.y -= 10
				for y in move_buttons:
					y.y -= 10
				for y in move_ys:
					y -= 10
			draw.rect(w,white,keyboard)
			draw.rect(w,d_grey,keyboard,4)
			y = r_keyboard.y + 10
			i = 0
			for b_row in range(5):
				x = r_keyboard.x
				for b_col  in range(4):
					
					button = buttons[i][b_font].render(buttons[i][b_text], False, d_grey)
					button = button.convert()
					outline = Rect(x,y,40,25)
					
					draw.rect(w,buttons[i][b_color],outline)
					draw.rect(w,d_grey,outline,buttons[i][b_thickness])
					w.blit(button, (x+5,y+3))
					
					if i == 18:
						outline = Rect(x,y,87,25)
						draw.rect(w,buttons[i][b_color],outline)
						draw.rect(w,d_grey,outline,buttons[i][b_thickness])
						button = font_lrg.render("enter", False, d_grey)
						w.blit(button, (x+5,y+3))
						
						break
					i += 1
					x += int(r_keyboard.width/4)
				y += int(r_keyboard.height/5)
				
			draw.line(w,m_grey,(r_keyboard.x - 15, r_keyboard.y + 10),(r_keyboard.x - 15, r_keyboard.y + r_keyboard.height - 10),4)
			draw.line(w,m_grey,(keyboard.x + 10, l_keyboard.y),(r_keyboard.x - 25, l_keyboard.y),4)
			draw.rect(w,black,hor_pad,4)
			draw.rect(w,black,vert_pad,4)
			draw.rect(w,d_grey,hor_pad)
			draw.rect(w,d_grey,vert_pad)
			
			y = l_keyboard.y + 10
			i = 20
			
			for b_row in range(5):
				x = l_keyboard.x
				for b_col  in range(6):
					
					button = buttons[i][b_font].render(buttons[i][b_text], False, d_grey)
					button = button.convert()
					outline = Rect(x,y,50,25)
					
					draw.rect(w,buttons[i][b_color],outline)
					draw.rect(w,d_grey,outline,buttons[i][b_thickness])
					w.blit(button, (x+5,y+3))
					
					i += 1
					x += int(l_keyboard.width/6)
				y += int(l_keyboard.height/5)
				
			rotation = 90
			for x in range(50,54):
				button = font_hug.render(">", False, l_grey)
				button = button.convert()
				button = pygame.transform.rotate(button, rotation)
				w.blit(button, (move_xs[x-50] ,move_ys[x-50] ))
				rotation += 90
			
			if not keyboard_hidden:
				draw.rect(w,d_grey,hide_keyboard,2)
				draw.polygon(w,m_grey,[(60,262),(65,269),(70,262)])
			else:
				draw.rect(w,d_grey,hide_keyboard,2)
				draw.polygon(w,m_grey,[(60,269),(65,262),(70,269)])
				
		def draw_functions():
			draw.rect(w,white,function_box)
			draw.rect(w,l_grey,left_bar)
			x = function_box.x
			y = function_box.y
			for num in range(1,6):
				y += int(function_box.height/6)
				draw.line(w,l_grey,(x,y),(x+function_box.width,y),2)
			y += int(function_box.height/6)
			for i in range(59,65):
				draw.ellipse(w,buttons[i][b_color],F_buttons[i-59])
			draw.rect(w,m_grey,function_box,8)
		
		def draw_lists():
			draw.rect(w,white,list_box)
			draw.rect(w,white,plot_box)
			draw.rect(w,l_grey,left_bar)
			x = list_box.x
			y = list_box.y + 30
			for num in range(6):
				draw.line(w,m_grey,(x,y),(x+left_bar.width,y),2)
				y += int((list_box.height - 30)/6)
			y += int((list_box.height - 20)/6)
			draw.rect(w,white,label_box)
			w.blit(list_label,(label_box.x+7,label_box.y+8))
			for i in range(0,6):
				w.blit(list_texts[i],(L_buttons[i].x+4,L_buttons[i].y+5))
			draw.rect(w,d_grey,L_buttons[selected_list],2)
			w.blit(list_texts[selected_list], (120,8))
			y = 25
			for num in range(12):
				draw.line(w,l_grey,(103,y),(172,y),2)
				y += int((list_box.height)/12)
			y = 30
			for num in lists[selected_list]:
				num_text = font_reg.render(str(num),False,d_grey)
				w.blit(num_text,(110,y))
				y += int((list_box.height)/12)
			stats_tabs[stats_tab].width += 5
			stats_tabs[stats_tab].x -= 5
			for tab in stats_tabs:
				draw.rect(w,white,tab)
				draw.rect(w,d_grey,tab,2)
				text = font_reg.render(buttons[stats_tabs.index(tab)+73][b_text],False,d_grey)
				text = pygame.transform.rotate(text, 90)
				w.blit(text, (tab.x+8,tab.y+10))
			draw.rect(w,black,stats_tabs[stats_tab],3)
			stats_tabs[stats_tab].width -= 5
			stats_tabs[stats_tab].x += 5
			draw.line(w,d_grey,(225,0),(225,250),8)
			draw.rect(w,m_grey,left_bar,8)
			draw.rect(w,m_grey,list_box,8)
		
		def draw_stats():
			if stats_tab == 0:
				draw.rect(w,white,active_plots_bar)
				draw.line(w,m_grey,(229,30),(309,30),3)
				draw.line(w,d_grey,(309,0),(309,248),8)
				w.blit(plots_text,(active_plots_bar.x+10,active_plots_bar.y+7))
				draw.rect(w,l_grey,view_plot)
				draw.rect(w,d_grey,view_plot,2)
				draw.rect(w,white,plot_box)
				y = 40
				for plot in plots:
					type_text = font_sml.render(plot.type,False,function_colors[int(plot.list[1])-1])
					w.blit(type_text,(235,y))
					list_text = font_reg.render(str(plot.list),False,function_colors[int(plot.list[1])-1])
					w.blit(list_text,(280,y))
					y += 40
				for delete in delete_plots:
					draw.line(w,black,(delete.x,delete.y),(delete.x+15,delete.y+15),2)
					draw.line(w,black,(delete.x,delete.y+15),(delete.x+15,delete.y),2)
				if plot_view:
					w.blit(hide_plot_text, (view_plot.x+4,view_plot.y+5))
				else:
					w.blit(view_plot_text, (view_plot.x+4,view_plot.y+5))
					if plot_making == 0:
						for plot in plot_boxes:
							draw.rect(w,l_grey,plot)
							text = font_reg.render(buttons[hitboxes.index(plot)][b_text],False,d_grey)
							w.blit(text, (plot.x+3,plot.y+8))
					elif plot_making == 1:
						for i in range(3):
							text1 = font_reg.render(s_inputs[i][s_text],False,d_grey)
							w.blit(text1,(s_inputs[i][s_hitbox].x+3,s_inputs[i][s_hitbox].y+8))
							text2 = font_reg.render(s_inputs[i][s_input],False,d_grey)
							w.blit(text2,(s_inputs[i][s_hitbox].x+text1.get_width(),s_inputs[i][s_hitbox].y+8))
						draw.rect(w,l_grey,done_box)
						w.blit(done_text, (done_box.x+3,done_box.y+8))
						draw.rect(w,l_grey,back_box)
						w.blit(back_text, (back_box.x+3,back_box.y+8))
					elif plot_making == 2:
						try:
							s_inputs[8][1] = str((float(max(lists[int(s_inputs[5][1][1])-1]))-float(min(lists[int(s_inputs[5][1][1])-1])))/int(s_inputs[7][1]))
						except:
							print("excepted",s_inputs[8],)
						for i in range(5,9):
							text1 = font_reg.render(s_inputs[i][s_text],False,d_grey)
							w.blit(text1,(plot_boxes[i-5].x+3,plot_boxes[i-5].y+8))
							text2 = font_reg.render(s_inputs[i][s_input],False,d_grey)
							w.blit(text2,(plot_boxes[i-5].x+text1.get_width(),plot_boxes[i-5].y+8))
						draw.rect(w,l_grey,done_box)
						w.blit(done_text, (done_box.x+3,done_box.y+8))
						draw.rect(w,l_grey,back_box)
						w.blit(back_text, (back_box.x+3,back_box.y+8))
					elif plot_making == 3:
						for i in range(10,12):
							text1 = font_reg.render(s_inputs[i][s_text],False,d_grey)
							w.blit(text1,(plot_boxes[i-10].x+3,plot_boxes[i-10].y+8))
							text2 = font_reg.render(s_inputs[i][s_input],False,d_grey)
							w.blit(text2,(plot_boxes[i-10].x+text1.get_width(),plot_boxes[i-10].y+8))
						draw.rect(w,l_grey,done_box)
						w.blit(done_text, (done_box.x+3,done_box.y+8))
						draw.rect(w,l_grey,back_box)
						w.blit(back_text, (back_box.x+3,back_box.y+8))
					elif plot_making == 4:
						for i in range(15,17):
							text1 = font_reg.render(s_inputs[i][s_text],False,d_grey)
							w.blit(text1,(plot_boxes[i-15].x+3,plot_boxes[i-15].y+8))
							text2 = font_reg.render(s_inputs[i][s_input],False,d_grey)
							w.blit(text2,(plot_boxes[i-15].x+text1.get_width(),plot_boxes[i-15].y+8))
						draw.rect(w,l_grey,done_box)
						w.blit(done_text, (done_box.x+3,done_box.y+8))
						draw.rect(w,l_grey,back_box)
						w.blit(back_text, (back_box.x+3,back_box.y+8))
					elif plot_making == 5:
						for i in range(20,23):
							text1 = font_reg.render(s_inputs[i][s_text],False,d_grey)
							w.blit(text1,(plot_boxes[i-20].x+3,plot_boxes[i-20].y+8))
							text2 = font_reg.render(s_inputs[i][s_input],False,d_grey)
							w.blit(text2,(plot_boxes[i-20].x+text1.get_width(),plot_boxes[i-20].y+8))
						draw.rect(w,l_grey,done_box)
						w.blit(done_text, (done_box.x+3,done_box.y+8))
						draw.rect(w,l_grey,back_box)
						w.blit(back_text, (back_box.x+3,back_box.y+8))
			elif stats_tab == 1:
				draw.rect(w,white,page_selection_bar)
				draw.rect(w,d_grey,page_selection_bar)
				pnum = 1
				for box in page_number_boxes:
					if pnum == current_page:
						draw.rect(w,white,box)
					else:
						draw.rect(w,l_grey,box)
					text = font_lrg.render(str(pnum),False,d_grey)
					w.blit(text,(box.x+5,box.y+3))
					pnum += 1
				draw.rect(w,white,page_box)
				for num in range((current_page - 1) * 8, current_page * 8):
					draw.rect(w,l_grey,s_calculations[num][s_hitbox])
					text1 = font_reg.render(s_calculations[num][s_text], False, d_grey)
					w.blit(text1,(s_calculations[num][s_hitbox].x + 3, s_calculations[num][s_hitbox].y + 8))
					text2 = font_reg.render(s_calculations[num][s_input], False, d_grey)
					w.blit(text2,(s_calculations[num][s_hitbox].x + 210, s_calculations[num][s_hitbox].y + 8))
					
		def draw_settings():
			draw.rect(w, white, settings_background)
			w.blit(settings_header, (300,5))
			i = 0
			for box in settings_boxes:
				draw.rect(w,l_grey,box)
				text1 = font_med_sml.render(setting_names[i]+": ",False,d_grey)
				w.blit(text1,(box.x + 5,box.y + 5))
				text2 = font_med_sml.render(settings[i],False,black)
				w.blit(text2,(box.x + text1.get_size()[0] + 5,box.y + 5))
				i += 1
				
		def draw_graph():
			global trace_index
			for rect in shifts:
				draw.rect(w,l_grey,rect)
			draw.line(w,black,(y_axis,graph_box.y),(y_axis,graph_box.y + graph_box.height),2)
			draw.line(w,black,(graph_box.x,x_axis),(graph_box.x + graph_box.width,x_axis),2)
			draw.rect(w,white,zoom_bar)
			draw.rect(w,m_grey,zoom_out)
			draw.rect(w,black,zoom_out,1)
			draw.rect(w,m_grey,zoom_in)
			draw.rect(w,black,zoom_in,1)
			arrow_text = font_lrg.render(">",False,d_grey)
			arrow_text = pygame.transform.rotate(arrow_text,90)
			w.blit(arrow_text, (zoom_out.x-3, zoom_out.y+13))
			w.blit(arrow_text, (zoom_out.x-3, zoom_out.y+28))
			arrow_text = pygame.transform.rotate(arrow_text,180)
			w.blit(arrow_text, (zoom_in.x-5, zoom_in.y+7))
			w.blit(arrow_text, (zoom_in.x-5, zoom_in.y+23))
			draw.rect(w,m_grey,trace_box)
			draw.rect(w,black,trace_box,1)
			trace_text = font_reg.render("TRACE",False,d_grey)
			trace_text = pygame.transform.rotate(trace_text,90)
			w.blit(trace_text,(trace_box.x+1,trace_box.y+3))
			
			arrow_text = font_hug.render(">",False,black)
			for point in shift_points:
				w.blit(arrow_text, point)
				arrow_text = pygame.transform.rotate(arrow_text, 90)
			
			if trace and len(graph_points[function_edit]) > 0:
				if trace_index >= len(graph_points[function_edit]):
					trace_index = len(graph_points[function_edit])-1
				if trace_index < 0:
					trace_index = 0
				print(trace_index)
				wx = graph_points[function_edit][trace_index][0]
				wy = graph_points[function_edit][trace_index][1]
				x = (wx-y_axis)/x_scale
				y = (wy-x_axis)/-y_scale
				trace_point = font_lrg.render("("+"{:1.4f}".format(x)+","+"{:1.4f}".format(y)+")",False,black)
				w.blit(trace_point, (510,10))
				draw.circle(w,black,graph_points[function_edit][trace_index],5,1)
		
		def draw_tabs():
		
			draw.line(w,d_grey,(38,0),(38,500),12)
			draw.line(w,black,(44,0),(44,500))
			for x in range(32):
				draw.line(w,(255-3*x,255-3*x,255-3*x),(x,0),(x,500))
			draw.line(w,black,(32,0),(32,500))
			y = 385
			i = 54
			for tab in tabs:
				draw.rect(w,white,tab)
				draw.rect(w,black,tab,1)
				text = buttons[i][b_font].render(buttons[i][b_text], False, d_grey)
				text = text.convert()
				text = pygame.transform.rotate(text, 90)
				w.blit(text, (16, y))
				y -= hitboxes[i+1].height + 5
				i += 1
			draw.rect(w,black,tabs[screen],3)
			
		def concatenate(list):
			try:
				out = list[0]
				first = True
				for i in list:
					if first:
						first = False
					else:
						out += i
			except IndexError:
				out = ""
			except Exception as e:
				out = e
				print(e)
			return out
		
		def buttons_dict(item):
			i = 0
			out = -1
			for button in buttons:
				if item in button:
					out = i
					break
			
				i += 1
			return out
		def s_dict(item):
			i = 0
			out = -1
			for list in s_inputs:
				if item in list:
					out = i
					break
				i += 1
			return out
		def csc(x):
			out = 1/sin(x)
			return out
		def sec(x):
			out = 1/cos(x)
			return out
		def cot(x):
			out = 1/tan(x)
			return out
		def fact(index):
			inp = ""
			for i in range(index-1, -1, -1):
				if buttons[buttons_dict(pressed_chars[i])][b_type] == "number":
					inp += pressed_chars[i]
			return inp
		
		def summize(index, limit, summand):
			out = 0
			print(limit,summand)
			for i in range(index, limit+1):
				out += eval(summand)
			return out
		
		#statistics functions
		def get_med(list):
			med_index = (len(list)-1)/2
			if med_index == int(med_index):
				med = list[int(med_index)]
			else:
				med = (list[int(med_index)]+list[int(med_index)+1])/2
			return med
		def get_5_num_sum(list):
			minimum = min(list)
			q1 = get_med(list[:int(len(list)/2)])
			med = get_med(list)
			q3 = get_med(list[int((len(list)+1)/2):])
			maximum = max(list)
			return [minimum,q1,med,q3,maximum]
		def get_outliers(list):
			list.sort()
			five_num_sum = get_5_num_sum(list)
			iqr = five_num_sum[3] - five_num_sum[1]
			upper_bound = five_num_sum[3] + 1.5 * iqr
			lower_bound = five_num_sum[1] - 1.5 * iqr
			outliers = [num for num in list if num >= upper_bound or num <= lower_bound]
			return outliers
			
		#updating vatriables to settings
		file = open("gc_settings.txt","r")
		setting_values = file.readlines()
		if setting_values == []:
			settings = ["-10","10","-10","10","red","green","blue","orange","magenta","l_blue"]
			settings += ["None"]*num_unused_settings
		else:
			settings = []
			i = 0
			for setting_value in setting_values:
				if i == 27:
					settings.append(setting_value)
				else:
					settings.append(setting_value[:len(setting_value)-1])
				i += 1
		
		class Win:
			x_min = -10
			default_x_min = -10
			x_max = 10
			default_x_max = 10
			y_min = -10
			default_y_min = -10
			y_max = 10
			default_y_max = 10
			precision = graph_box.width
			def __init__(self):
				self.x_min = float(settings[0])
				self.x_max = float(settings[1])
				self.y_min = float(settings[2])
				self.y_max = float(settings[3])
				
		#plot classes
		class Boxplot:
			type = "BOXP"
			list = "L1"
			freq_list = ""
			adjusted = False
			plotted = False
		
		class Histogram:
			type = "HIST"
			list = "L1"
			freq_list = ""
			num_bars = "10"
			plotted = False
		
		class Ogive:
			type = "OGIV"
			list = "L1"
			freq_list = ""
			plotted = False
		
		class Scatterplot:
			type = "SCTP"
			list = "L2"
			y_list = "L3"
			plotted = False
			
		class Regression:
			type = "REGR"
			list = "L2"
			y_list = "L3"
			line_type = "linear"
			plotted = False
			
		plot_classes = [Boxplot(),Histogram(),Ogive(),Scatterplot(),Regression()]
		
		cool_functions = [
		["0",".","1","*","(","1","0","*","x",")","^","c","o","s","1","0","*","x",")"],
		["5","*","e","^","(","-","(","0",".","2","*","x",")","^","2",")"],
		['5', 'sin(', 'arccos(', '0', '.', '2', 'x', ')', ')'],
		['log(', 'abs(', 'csc(', 'x', ')', ')', ')'],
		['log(', 'e', ',', 'abs(', 'x', ')', ')'],
		['ln(', 'sin(', 'x', ')', '+', '1', ')'],
		['x', 'sin(', '3', 'x', ')', '+', 'x'],
		['8', 'cos(', 'arctan(', 'x', ')', ')'],
		['5', 'sin(', '5', '/', 'x', ')'],
		]
		
		
		
		###---VARIABLES---###
		###GENERAL VARS###
		prev_pressed = []
		redraw = True
		window_redraw = True
		still_pressed = False
		enter = False
		keyboard_hidden = False
		keyboard_redraw = False
		blinker_on = 5
		blinker_loc = 0 
		menu_edit = 0
		screen = 0
		
		###STATS VARS###
		selected_list = 0
		lists = [["1.51","2.96","3.73","4.09","5.01","1.23"],[],[],[],[],[]]
		for num in range(random.randint(5,12)):
			lists[1].append(str(random.randint(0,1000)/100))
			lists[2].append(str(random.randint(0,1000)/100))
		stats_tab = 0
		s_current_input = 0
		list_entry = 0
		
		#plotting vars
		plots = []
		plot_view = False
		plot_making = 0
		plot_points = []
		plot_y_min = 100000
		plot_y_max = -100000
		done = False
		plotted = False
		max_height = 0
		
		#calculating vars
		current_page = 1
		recalculate_stats = True
		
		###FUNCTION VARS###
		active_functions = [True,True,True,True,True,True]
		function_colors = [eval(settings[i]) for i in range(4,10)]
		current_function = 0
		start_time = 0
		pressed_chars = ""
		output = ""
		char_list = []
		w_x = 5
		w_y = 5
		screen = 0
		tabs[screen] = Rect(7,tabs[screen].y-3,25,tabs[screen].height+6)
		functions = ["","","","","",""]
		function_edit = 0
		temp_functions = [random.choice(cool_functions),[],[],[],[],[]]
		graph_points = [[],[],[],[],[],[]]
		win = Win()
		graph_xs = [win.x_min, win.x_min, win.x_min, win.x_min, win.x_min, win.x_min]
		win_domain = win.x_max - win.x_min
		win_range = win.y_max - win.y_min
		y_scale = graph_box.height/win_range
		x_scale = graph_box.width/win_domain
		y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
		x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
		offset = win_domain/win.precision
		trace = False
		trace_index = 50
		graphed_functions = [True,True,True,True,True,True]
		
		###SETTINGS VARS###
		setting_editing = 0
		
		editing_sigma = False
		sigma = ["1","10","i"]
		sigma_edit = 0
		sigma_active = False
		
		
		
		###---MAIN LOOP---###
		
		while running:
			
			time = pygame.time.get_ticks()
			if time - start_time > 200:
				start_time = 0
				draw_keyboard()
				window_redraw = True
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				
				###---MOUSE INPUT---###
				
				elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:
					if event.type == pygame.MOUSEBUTTONUP:
						print("mousebuttton")
						#making a hitbox for cursor
						horizontal_pos, vertical_pos = pygame.mouse.get_pos()
						cursor = Rect(horizontal_pos-2,vertical_pos-2,8,8)
						
						if cursor.collidelist(hitboxes) >= 0:
							i = cursor.collidelist(hitboxes)
						else:
							i = 19
					
					elif event.type == pygame.KEYDOWN:
						i = 19
						#checking for shift key
						mods = pygame.key.get_mods()
						keys = list(pygame.key.get_pressed())
						for keys_index in prev_pressed:
							keys[keys_index] = 0
							if not 1 in keys:
								keys[keys_index] = 1
						prev_pressed = []
						for key in keys:
							if key == 1:
								prev_pressed.append(keys.index(1))
						if mods & pygame.KMOD_SHIFT:
							shift = True
						else:
							shift = False
						
						if mods & pygame.KMOD_SHIFT:
							for key in keys:
								if key == 1:
									temp_i = keys.index(1)
									break
							if temp_i >= 97 and temp_i < 123:#this converts the index of the capital alpha keys to their index in my list
								i = temp_i + 29    
							elif keys[pygame.K_EQUALS]:
								i = buttons_dict("+")
							elif keys[pygame.K_8]:
								i = buttons_dict("*")
							elif keys[pygame.K_6]:
								i = buttons_dict("**")
							elif keys[pygame.K_9]:
								i = buttons_dict("(")
							elif keys[pygame.K_0]:
								i = buttons_dict(")")
							elif keys[pygame.K_MINUS]:
								i = buttons_dict("_")
							elif keys[pygame.K_QUOTE]:
								i = buttons_dict("\"")
							else:
								i = 19
								print("I = 19")
								
						elif mods & pygame.KMOD_CTRL:
							if keys[pygame.K_i]:
								i = buttons_dict("ZOOM_IN")
							elif keys[pygame.K_o]:
								i = buttons_dict("ZOOM_OUT")
							elif keys[pygame.K_RIGHT]:
								i = buttons_dict("SHIFT_RIGHT")
							elif keys[pygame.K_UP]:
								i = buttons_dict("SHIFT_UP")
							elif keys[pygame.K_LEFT]:
								i = buttons_dict("SHIFT_LEFT")
							elif keys[pygame.K_DOWN]:
								i = buttons_dict("SHIFT_DOWN")
							
						
						else:
							for key in keys:
								if key == 1:
									temp_i = keys.index(1)
									break
							if 1 in keys and temp_i >= 97 and temp_i < 123:#this converts the index of the alpha keys to their index in my list
								
								i = temp_i + 3
							
							elif keys[pygame.K_0]:
								i = buttons_dict("0")
							elif keys[pygame.K_1]:
								i = buttons_dict("1")
							elif keys[pygame.K_2]:
								i = buttons_dict("2")
							elif keys[pygame.K_3]:
								i = buttons_dict("3")
							elif keys[pygame.K_4]:
								i = buttons_dict("4")
							elif keys[pygame.K_5]:
								i = buttons_dict("5")
							elif keys[pygame.K_6]:
								i = buttons_dict("6")
							elif keys[pygame.K_7]:
								i = buttons_dict("7")
							elif keys[pygame.K_8]:
								i = buttons_dict("8")
							elif keys[pygame.K_9]:
								i = buttons_dict("9")
							elif keys[pygame.K_PERIOD]:
								i = buttons_dict(".")
							elif keys[pygame.K_MINUS]:
								i = buttons_dict("-")
							elif keys[pygame.K_SLASH]:
								i = buttons_dict("/")
							elif keys[pygame.K_COMMA]:
								i = buttons_dict(",")
							elif keys[pygame.K_SPACE]:
								i = buttons_dict(" ")
							elif keys[pygame.K_RETURN]:
								i = buttons_dict("enter")
							elif keys[pygame.K_BACKSPACE]:
								i = buttons_dict("BSPC")
							elif keys[pygame.K_DELETE]:
								i = buttons_dict("DEL")
							elif keys[pygame.K_ESCAPE]:
								i = buttons_dict("CLR")
							elif keys[pygame.K_UP]:
								i = buttons_dict("UP")
							elif keys[pygame.K_LEFT]:
								i = buttons_dict("LEFT")
							elif keys[pygame.K_DOWN]:
								i = buttons_dict("DOWN")
							elif keys[pygame.K_RIGHT]:
								i = buttons_dict("RIGHT")
							elif keys[pygame.K_F1]:
								i = buttons_dict("F1")
							elif keys[pygame.K_F2]:
								i = buttons_dict("F2")
							elif keys[pygame.K_F3]:
								i = buttons_dict("F3")
							elif keys[pygame.K_F4]:
								i = buttons_dict("F4")
							elif keys[pygame.K_F5]:
								i = buttons_dict("F5")
							elif keys[pygame.K_F6]:
								i = buttons_dict("F6")
						
						
					if i != 19:
						if len(output) > 0:
							blinker_loc = 0
							if buttons[i][b_type] == "operator":
								char_list = ["("] + char_list[0:] + [")"]
							elif buttons[i][b_type] == "function":
								char_list = [buttons[i][b_display]] + ["("] + char_list[0:] + [")"]#making sure that the function comes first
								i = 19#blank so that it doesn't repeat the function
							else:
								char_list = []
							output = ""
						if editing_sigma:
							char_list = list(sigma[sigma_edit])
											
						if screen == 2:
							if s_current_input != 99:
								char_list = list(s_inputs[s_current_input][s_input])[0:]
							else:
								char_list = list(lists[selected_list][list_entry])[0:]
						elif screen == 4:
							char_list = list(str(settings[setting_editing]))
						index = len(char_list)+blinker_loc
						print("i-",i)
						print(hitboxes[i])
						char_list.insert(index, buttons[i][b_display])
						
						
						
						if not trace:		
							if buttons[i][b_text] == "!":
								char_list[index] += str(index) + ")"
							elif buttons[i][b_text] == "LEFT":
								blinker_loc -= 1
								if blinker_loc <= -1 * len(char_list):
									blinker_loc = -1 * len(char_list) + 1
								print("LEFT", blinker_loc)
							elif buttons[i][b_text] == "RIGHT":
								blinker_loc += 1
								if blinker_loc > 0:
									blinker_loc = 0
								print("RIGHT",blinker_loc)
						elif trace:
							if buttons[i][b_text] == "LEFT":
								trace_index -= 4
							elif buttons[i][b_text] == "RIGHT":
								trace_index += 4
						if screen == 1:
							print("screen 1")
							if i >= 59 and i < 65:#these are the buttons responsible for turning functions on and off
								active_functions[i-59] = not active_functions[i-59]
								enter = True
							elif buttons[i][b_text] == "UP":
								function_edit -= 1
								char_list = []
								blinker_loc = 0
							elif buttons[i][b_text] == "DOWN":
								function_edit += 1
								char_list = []
								blinker_loc = 0
							elif i >= 380 and i < 386:
								function_edit = i - 380
								char_list = []
								blinker_loc = 0
							elif buttons[i][b_text] == "ZOOM_OUT":
								win.x_min *= 1.25
								win.x_max *= 1.25
								win.y_min *= 1.25
								win.y_max *= 1.25
								win_domain = win.x_max - win.x_min
								win_range = win.y_max - win.y_min
								y_scale = graph_box.height/win_range
								x_scale = graph_box.width/win_domain
								y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
								x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
								offset = win_domain/win.precision
								for graph in range(len(graph_points)):
									graph_xs[graph] = win.x_min
									graph_points[graph] = []
								print("Zooomout")
							elif buttons[i][b_text] == "ZOOM_IN":
								win.x_min /= 1.25
								win.x_max /= 1.25
								win.y_min /= 1.25
								win.y_max /= 1.25
								win_domain = win.x_max - win.x_min
								win_range = win.y_max - win.y_min
								y_scale = graph_box.height/win_range
								x_scale = graph_box.width/win_domain
								y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
								x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
								offset = win_domain/win.precision
								for graph in range(len(graph_points)):
									graph_xs[graph] = win.x_min
									graph_points[graph] = []
								print("zooomin")
								print(win.x_min,win.x_max,win.y_min,win.y_max)
							elif buttons[i][b_text] == "TRACE":
								trace = not trace
							elif buttons[i][b_text] == "SHIFT_RIGHT":
								win.x_min += 10/x_scale
								win.x_max += 10/x_scale
								win_domain = win.x_max - win.x_min
								win_range = win.y_max - win.y_min
								y_scale = graph_box.height/win_range
								x_scale = graph_box.width/win_domain
								y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
								x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
								offset = win_domain/win.precision
								for graph in range(len(graph_points)):
									graph_xs[graph] = win.x_min
									graph_points[graph] = []
							elif buttons[i][b_text] == "SHIFT_UP":
								win.y_min += 10/y_scale
								win.y_max += 10/y_scale
								win_domain = win.x_max - win.x_min
								win_range = win.y_max - win.y_min
								y_scale = graph_box.height/win_range
								x_scale = graph_box.width/win_domain
								y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
								x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
								offset = win_domain/win.precision
								for graph in range(len(graph_points)):
									graph_xs[graph] = win.x_min
									graph_points[graph] = []
							elif buttons[i][b_text] == "SHIFT_LEFT":
								win.x_min -= 10/x_scale
								win.x_max -= 10/x_scale
								win_domain = win.x_max - win.x_min
								win_range = win.y_max - win.y_min
								y_scale = graph_box.height/win_range
								x_scale = graph_box.width/win_domain
								y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
								x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
								offset = win_domain/win.precision
								for graph in range(len(graph_points)):
									graph_xs[graph] = win.x_min
									graph_points[graph] = []
							elif buttons[i][b_text] == "SHIFT_DOWN":
								win.y_min -= 10/y_scale
								win.y_max -= 10/y_scale
								win_domain = win.x_max - win.x_min
								win_range = win.y_max - win.y_min
								y_scale = graph_box.height/win_range
								x_scale = graph_box.width/win_domain
								y_axis = -win.x_min/win_domain * graph_box.width + graph_box.x
								x_axis = win.y_min/win_range * graph_box.height + graph_box.y + graph_box.height
								offset = win_domain/win.precision
								for graph in range(len(graph_points)):
									graph_xs[graph] = win.x_min
									graph_points[graph] = []
							elif buttons[i][b_text] == "LEFT" or buttons[i][b_text] == "RIGHT":pass
							else:
								graph_xs[function_edit] = win.x_min
								graph_points[function_edit] = []
								
						elif screen == 2:
							just_clicked_stats = True
							not1 = False
							
							if buttons[i][b_text] == "PLOT":
								stats_tab = 0
								for num in eval(active_hitbox_list):
									hitboxes[num].x += 1000	
								active_hitbox_list = "stats_plot_hitboxes"
								for num in eval(active_hitbox_list):
									hitboxes[num].x -= 1000
									print(hitboxes[num])
							elif buttons[i][b_text] == "CALCULATE":
								stats_tab = 1
								for num in eval(active_hitbox_list):
									hitboxes[num].x += 1000
								active_hitbox_list = "stats_calculate_hitboxes"
								for num in eval(active_hitbox_list):
									hitboxes[num].x -= 1000
									print(num,hitboxes[num])
							if stats_tab == 0: #for clarity--thinking about adding new stats tabs
								if buttons[i][b_text] == "VIEW_PLOT":
									plot_view = not plot_view
								elif buttons[i][b_text] == "done":
									done = True
								elif buttons[i][b_text] == "back":
									plot_making = 0
									buttons[76] = ["1:BOXPLOT","","",white,2,font_reg,"command"]
									buttons[77] = ["2:HISTOGRAM","","",white,2,font_reg,"command"]
									buttons[78] = ["3:OGIVE","","",white,2,font_reg,"command"]
									buttons[79] = ["4:SCATTERPLOT","","",white,2,font_reg,"command"]
									buttons[80] = ["5:REGRESSION","","",white,2,font_reg,"command"]
								elif buttons[i][b_text] == "1:BOXPLOT":
									plot_making = 1
									buttons[76][b_text] = s_inputs[0][s_text]
									buttons[77][b_text] = s_inputs[1][s_text]
									buttons[78][b_text] = s_inputs[2][s_text]
									buttons[79][b_text] = s_inputs[3][s_text]
									buttons[80][b_text] = s_inputs[4][s_text]
								elif buttons[i][b_text] == "2:HISTOGRAM":
									plot_making = 2
									buttons[76][b_text] = s_inputs[5][s_text]
									buttons[77][b_text] = s_inputs[6][s_text]
									buttons[78][b_text] = s_inputs[7][s_text]
									buttons[79][b_text] = s_inputs[8][s_text]
									buttons[80][b_text] = s_inputs[9][s_text]
								elif buttons[i][b_text] == "3:OGIVE":
									plot_making = 3
									print("OGIV")
									buttons[76][b_text] = s_inputs[10][s_text]
									buttons[77][b_text] = s_inputs[11][s_text]
									buttons[78][b_text] = s_inputs[12][s_text]
									buttons[79][b_text] = s_inputs[13][s_text]
									buttons[80][b_text] = s_inputs[14][s_text]
								elif buttons[i][b_text] == "4:SCATTERPLOT":
									plot_making = 4
									buttons[76][b_text] = s_inputs[15][s_text]
									buttons[77][b_text] = s_inputs[16][s_text]
									buttons[78][b_text] = s_inputs[17][s_text]
									buttons[79][b_text] = s_inputs[18][s_text]
									buttons[80][b_text] = s_inputs[19][s_text]
								elif buttons[i][b_text] == "5:REGRESSION":
									plot_making = 5
									buttons[76][b_text] = s_inputs[20][s_text]
									buttons[77][b_text] = s_inputs[21][s_text]
									buttons[78][b_text] = s_inputs[22][s_text]
									buttons[79][b_text] = s_inputs[23][s_text]
									buttons[80][b_text] = s_inputs[24][s_text]
			
								elif i >= 84 and i < 90: #the DELETE_PLOT<i - 84> buttons used to delete plots
									for points in plot_points:
										if i-84 in points:
											plot_points.remove(points)
									for points in plot_points:
										if i-84 < points[0]:
											plot_points[plot_points.index(points)][0] -= 1
									plots.remove(plots[i-84])
									for num in range(4):
										if num < len(plots):
											hitboxes[num+84].x = 240
										else:
											hitboxes[num+84].x = 1240
									
							elif stats_tab == 1:#for clarity
								
								if i >= 90 and i < 97: #the PAGE<i - 90> buttons used for switching pages
									current_page = i - 89
									
							if i >= 76 and i < 81:
								s_current_input = 5*(plot_making-1)+i-76
							elif buttons[i][b_text] == "LIST_BOX":
									s_current_input = 99
									
							if i >= 386 and i < 392:
								selected_list = i-386
								list_entry = 0
								lists[selected_list].append("")
								
							if s_current_input == 99:
								if buttons[i][b_text] == "DOWN":
									list_entry += 1
									blinker_loc = 0
									if list_entry == len(lists[selected_list]):
										if lists[selected_list][list_entry-1] == "":
											list_entry = 0
										else:
											lists[selected_list].append("")
									if list_entry > len(lists[selected_list]):
										list_entry = 0
								elif buttons[i][b_text] == "UP":
									print("UP")
									list_entry -= 1
									blinker_loc = 0
									if list_entry < 0:
										if lists[selected_list][len(lists[selected_list])-1] == "":
											list_entry = len(lists[selected_list])-1
										else:
											list_entry = len(lists[selected_list])
											lists[selected_list].append("")
											
							if s_current_input != 99:
								if buttons[i][b_text] == "DOWN":
									if s_current_input+1 > s_inputs[s_current_input][s_max]:
										s_current_input = s_inputs[s_current_input][s_min]-1
									s_current_input += 1
									blinker_loc = 0
								elif buttons[i][b_text] == "UP":
									if s_current_input-1 < s_inputs[s_current_input][s_min]:
										s_current_input = s_inputs[s_current_input][s_max]+1
									s_current_input -= 1
									blinker_loc = 0
					
						elif screen == 4:
							if i >= 352 and i < 380:
								setting_editing = i - 352
							elif buttons[i][b_text] == "DOWN":
								setting_editing += 1
								if setting_editing > 27:
									setting_editing = 27
							elif buttons[i][b_text] == "UP":
								setting_editing -= 1
								if setting_editing < 0:
									setting_editing = 0
							
						if buttons[i][b_text] == "BSPC":#backspace
							print(char_list)
							char_list[index] = ""
							char_list[index-1] = ""
							print("BSPC",char_list)
			
						elif buttons[i][b_text] == "DEL":
							char_list[index] = ""
							if blinker_loc < 0:
								char_list[index+1] = ""
								blinker_loc += 1
						elif buttons[i][b_text] == "CLR":
							char_list = []
							pressed_chars = ""
						elif buttons[i][b_text] == "Î£":
							sigma_active = True
							char_list = []
						elif buttons[i][b_text] == "CALCULATOR":
							tabs[screen] = Rect(10,tabs[screen].y+3,22,tabs[screen].height-6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x += 1000
							screen = 0
							active_hitbox_list = "calculator_hitboxes"
							tabs[screen] = Rect(7,tabs[screen].y-3,25,tabs[screen].height+6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x -= 1000
							char_list = []
							w.fill(l_grey)
							
						elif buttons[i][b_text] == "GRAPH":
							tabs[screen] = Rect(10,tabs[screen].y+3,22,tabs[screen].height-6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x += 1000
							screen = 1
							active_hitbox_list = "graphing_hitboxes"
							tabs[screen] = Rect(7,tabs[screen].y-3,25,tabs[screen].height+6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x -= 1000
							w.fill(l_grey)
							graphed_functions = [False,False,False,False,False,False]
							for x in range(51):
								draw.line(w,(230-x,230-x,230-x),(0,50-x),(700,50-x))
								
						elif buttons[i][b_text] == "STATS":
							just_clicked_stats = True
							tabs[screen] = Rect(10,tabs[screen].y+3,22,tabs[screen].height-6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x += 1000
							screen = 2
							active_hitbox_list = "stats_plot_hitboxes"
							tabs[screen] = Rect(7,tabs[screen].y-3,25,tabs[screen].height+6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x -= 1000
							char_list = []
							w.fill(l_grey)
							
						elif buttons[i][b_text] == "SETTINGS":
							tabs[screen] = Rect(10,tabs[screen].y+3,22,tabs[screen].height-6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x += 1000
							screen = 4
							active_hitbox_list = "settings_hitboxes"
							tabs[screen] = Rect(7,tabs[screen].y-3,25,tabs[screen].height+6)
							for num in eval(active_hitbox_list):
								hitboxes[num].x -= 1000
						elif buttons[i][b_text] == "HIDE_KEYBOARD":
							keyboard_hidden = not keyboard_hidden
						elif buttons[i][b_text] == "enter":
							enter = True
						print(eval(active_hitbox_list),"\n".join([str(hitboxes[num]) for num in eval(active_hitbox_list)]))
						while "" in char_list:
							char_list.remove("")
						x = 0
						while x < len(char_list):
							if x + 2 < len(char_list) and "l" == char_list[x] and "o" == char_list[x+1] and "g" == char_list[x+2]:
								char_list = char_list[:x] + ["log("] + char_list[x+3:]
							elif x + 1 < len(char_list) and "l" == char_list[x] and "n" == char_list[x+1]:
								char_list = char_list[:x] + ["ln("] + char_list[x+2:] 
							elif x + 5 < len(char_list) and "a" == char_list[x] and "r" == char_list[x+1] and "c" == char_list[x+2] and "s" == char_list[x+3] and "i" == char_list[x+4] and "n" == char_list[x+5]:
								char_list = char_list[:x] + ["arcsin("] + char_list[x+6:]
							elif x + 5 < len(char_list) and "a" == char_list[x] and "r" == char_list[x+1] and "c" == char_list[x+2] and "c" == char_list[x+3] and "o" == char_list[x+4] and "s" == char_list[x+5]:
								char_list = char_list[:x] + ["arccos("] + char_list[x+6:]
							elif x + 5 < len(char_list) and "a" == char_list[x] and "r" == char_list[x+1] and "c" == char_list[x+2] and "t" == char_list[x+3] and "a" == char_list[x+4] and "n" == char_list[x+5]:
								char_list = char_list[:x] + ["arctan("] + char_list[x+6:]
							elif x + 2 < len(char_list) and "s" == char_list[x] and "i" == char_list[x+1] and "n" == char_list[x+2]:
								char_list = char_list[:x] + ["sin("] + char_list[x+3:]
							elif x + 2 < len(char_list) and "c" == char_list[x] and "o" == char_list[x+1] and "s" == char_list[x+2]:
								char_list = char_list[:x] + ["cos("] + char_list[x+3:]
							elif x + 2 < len(char_list) and "t" == char_list[x] and "a" == char_list[x+1] and "n" == char_list[x+2]:
								char_list = char_list[:x] + ["tan("] + char_list[x+3:]	
							elif x + 2 < len(char_list) and "c" == char_list[x] and "s" == char_list[x+1] and "c" == char_list[x+2]:
								char_list = char_list[:x] + ["csc("] + char_list[x+3:]	
							elif x + 2 < len(char_list) and "c" == char_list[x] and "o" == char_list[x+1] and "t" == char_list[x+2]:
								char_list = char_list[:x] + ["cot("] + char_list[x+3:]	
							elif x + 2 < len(char_list) and "s" == char_list[x] and "e" == char_list[x+1] and "c" == char_list[x+2]:
								char_list = char_list[:x] + ["sec("] + char_list[x+3:]
							elif x + 2 < len(char_list) and "a" == char_list[x] and "b" == char_list[x+1] and "s" == char_list[x+2]:
								char_list = char_list[:x] + ["abs("] + char_list[x+3:]					
							elif x + 1 < len(char_list) and "p" == char_list[x] and "i" == char_list[x+1]:
								char_list = char_list[:x] + ["Ã�â‚¬"] + char_list[x+2:]
							x += 1
						if (buttons[i][b_display] != "" or buttons[i][b_text] == "DEL" or buttons[i][b_text] == "CLR" or buttons[i][b_text] == "BSPC"):
							if editing_sigma:
								sigma[sigma_edit] = concatenate(char_list)
							if screen == 2:
								print("reset")
								if s_current_input != 99:
									s_inputs[s_current_input][s_input] = concatenate(char_list)
									print("sinput",s_inputs[s_current_input][s_input])
								else:
									try:
										lists[selected_list][list_entry] = concatenate(char_list)
									except ValueError:
										lists[selected_list][list_entry] = ""
							elif screen == 4:
								print(char_list,settings)
								settings[setting_editing] = concatenate(char_list)
								print(char_list,settings)
						just_clicked_stats = False
						draw.rect(w,d_grey,hitboxes[i],4)
						pygame.display.flip()
						start_time = time
						keyboard_redraw = True
						window_redraw = True
						output = ""
						print(blinker_loc)
					
					
				elif event.type == pygame.KEYUP:
					redraw = True
					window_redraw = True
								
		
				
					
					
			###---DRAWING WINDOW---###		
			
			if screen == 0:
				if window_redraw:
				
					#screen borders
					w.fill(l_grey)
					for x in range(51):
						draw.line(w,(230-x,230-x,230-x),(0,50-x),(700,50-x))
					
					draw.rect(w, white, display)
					draw.rect(w,d_grey, display, 4)
					draw_keyboard()
					draw_tabs()
					
					w_x = 10
					w_y = 15
					
					#interpreting text
					temp_char_list = char_list[0:]
					x = 0
					
					pressed_chars = concatenate(temp_char_list)
					
					display_text = font_lrg.render(pressed_chars, False, d_grey)
					w.blit(display_text, (display.x + w_x, display.y + w_y))
					
					if 0:
						index_text = font_sml.render("i="+str(sigma[0]),False,m_grey)
						limit_text = font_sml.render(str(sigma[1]),False,m_grey)
						summand_text = font_reg.render(str(sigma[2]),False,m_grey)
						w.blit(index_text, (display.x + 10 + 1.33*font_reg.size(concatenate(temp_char_list[:sum[3]]))[0], display.y + 31))
						w.blit(limit_text, (display.x + 10 + 1.33*font_reg.size(concatenate(temp_char_list[:sum[3]]))[0], display.y + 8))
						w.blit(summand_text, (display.x + 10 + 1.33*font_reg.size(concatenate(temp_char_list[:sum[3]]))[0]+11, display.y + 17))
					
					w_y += 25
					
					if len(output) > 0:
						output_text = font_lrg.render(output, False, d_grey)
						x = display.x + display.width - (output_text.get_width() + 20)
						w.blit(output_text, (x, display.y + w_y))
						window_redraw = False
					
					left_width, useless = font_lrg.size(concatenate(temp_char_list[:len(temp_char_list) + blinker_loc]))
					blinker_x = display.x + 10 + left_width
					blinker_on += 1
					if blinker_on > 200:
						if blinker_on == 300:
							blinker_on = 0			
						draw.line(w,black,(blinker_x,display.y + 15),(blinker_x,display.y + 30))
					
					
					pygame.display.flip()
					
			elif screen == 1:
				if window_redraw:
					#screen borders
					
					draw.rect(w,white,graph_box)
					for index in range(len(functions)):
						if active_functions[index]:
							buttons[index + 59][b_color] = function_colors[index]
							if len(graph_points[index]) > 1:
								draw.lines(w,buttons[index+59][b_color],False,graph_points[index],1)
						else:
							buttons[index + 59][b_color] = white
							
					draw_graph()
					draw_functions()
					draw_keyboard()
					draw_tabs()
					
					if function_edit < 0:
						function_edit = 0
					elif function_edit > 5:
						function_edit = 5
					
					char_list = temp_functions[function_edit]
					
					#interpreting text
					x = 0
					while x < len(char_list):
						if x + 2 < len(char_list) and "l" == char_list[x] and "o" == char_list[x+1] and "g" == char_list[x+2]:
							char_list = char_list[:x] + ["log("] + char_list[x+3:]
						elif x + 1 < len(char_list) and "l" == char_list[x] and "n" == char_list[x+1]:
							char_list = char_list[:x] + ["ln("] + char_list[x+2:] 
						elif x + 5 < len(char_list) and "a" == char_list[x] and "r" == char_list[x+1] and "c" == char_list[x+2] and "s" == char_list[x+3] and "i" == char_list[x+4] and "n" == char_list[x+5]:
							char_list = char_list[:x] + ["arcsin("] + char_list[x+6:]
						elif x + 5 < len(char_list) and "a" == char_list[x] and "r" == char_list[x+1] and "c" == char_list[x+2] and "c" == char_list[x+3] and "o" == char_list[x+4] and "s" == char_list[x+5]:
							char_list = char_list[:x] + ["arccos("] + char_list[x+6:]
						elif x + 5 < len(char_list) and "a" == char_list[x] and "r" == char_list[x+1] and "c" == char_list[x+2] and "t" == char_list[x+3] and "a" == char_list[x+4] and "n" == char_list[x+5]:
							char_list = char_list[:x] + ["arctan("] + char_list[x+6:]
						elif x + 2 < len(char_list) and "s" == char_list[x] and "i" == char_list[x+1] and "n" == char_list[x+2]:
							char_list = char_list[:x] + ["sin("] + char_list[x+3:]
						elif x + 2 < len(char_list) and "c" == char_list[x] and "o" == char_list[x+1] and "s" == char_list[x+2]:
							char_list = char_list[:x] + ["cos("] + char_list[x+3:]
						elif x + 2 < len(char_list) and "t" == char_list[x] and "a" == char_list[x+1] and "n" == char_list[x+2]:
							char_list = char_list[:x] + ["tan("] + char_list[x+3:]	
						elif x + 2 < len(char_list) and "c" == char_list[x] and "s" == char_list[x+1] and "c" == char_list[x+2]:
							char_list = char_list[:x] + ["csc("] + char_list[x+3:]	
						elif x + 2 < len(char_list) and "c" == char_list[x] and "o" == char_list[x+1] and "t" == char_list[x+2]:
							char_list = char_list[:x] + ["cot("] + char_list[x+3:]	
						elif x + 2 < len(char_list) and "s" == char_list[x] and "e" == char_list[x+1] and "c" == char_list[x+2]:
							char_list = char_list[:x] + ["sec("] + char_list[x+3:]
						elif x + 2 < len(char_list) and "a" == char_list[x] and "b" == char_list[x+1] and "s" == char_list[x+2]:
							char_list = char_list[:x] + ["abs("] + char_list[x+3:]					
						elif x + 1 < len(char_list) and "p" == char_list[x] and "i" == char_list[x+1]:
							char_list = char_list[:x] + ["Ã�â‚¬"] + char_list[x+2:]
						x += 1
						
					temp_functions[function_edit] = char_list
					
					x = function_box.x + 70
					y = function_box.y + 13
					
					for function in temp_functions:
						display_text = font_lrg.render(concatenate(function), False, m_grey)
						w.blit(display_text, (x, y))
						y += 41
					
					left_width, useless = font_lrg.size(concatenate(temp_functions[function_edit][:len(temp_functions[function_edit]) + blinker_loc]))
					blinker_x = function_box.x + 68 + int(left_width)
					blinker_y = function_box.y + 12 + 41 * function_edit
					blinker_on += 1
					if blinker_on > 200:
						if blinker_on == 300:
							blinker_on = 0
							print(blinker_loc)
						draw.line(w,black,(blinker_x,blinker_y),(blinker_x,blinker_y + 20))
						
					pygame.display.flip()
					
			elif screen == 2:
				if window_redraw:
				
					w.fill(l_grey)
					for x in range(51):
						draw.line(w,(230-x,230-x,230-x),(0,50-x),(700,50-x))
						
					draw_lists()
					draw_keyboard()
					draw_tabs()
					draw_stats()
					
					if plot_view:
						for num in range(340,641,75):
							text = font_sml.render("{:1.3f}".format(plot_x_min+(num-340)/plot_x_scale),False,d_grey)
							w.blit(text,(num,210))
							draw.line(w,black,(num+10,198),(num+10,208))
						
						for plot in plots:
							if plot.type == "HIST" and plot.plotted:
								draw.line(w,black,(652,50),(652,202),2)
								hist_axis_text = font_sml.render("histogram frequency",False,d_grey)
								hist_axis_text = pygame.transform.rotate(hist_axis_text,-90)
								w.blit(hist_axis_text,(670,60))
								for num in range(max_height+1):
									text = font_sml.render(str(num),False,d_grey)
									w.blit(text,(660,200-num*hist_scale))
									draw.line(w,black,(646,200-num*hist_scale),(656,200-num*hist_scale))
									
							elif plot.type == "OGIV" and plot.plotted:
								draw.line(w,black,(348,50),(348,202),2)
								for num in range(0,101,20):
									draw.line(w,black,(344,200-(num*ogiv_scale)),(354,200-(num*ogiv_scale)))
									text = font_sml.render(str(num),False,d_grey)
									w.blit(text,(329,200-(num*ogiv_scale)))
								ogiv_axis_text = font_sml.render("ogive rank percentile",False,d_grey)
								ogiv_axis_text = pygame.transform.rotate(ogiv_axis_text,90)
								w.blit(ogiv_axis_text,(315,50))
								
							elif plot.type == "SCTP" or plot.type == "REGR":
								draw.line(w,black,(348,50),(348,202),2)
								for num in range(200,50,-30):
									text = font_sml.render("{:1.2f}".format(plot_y_min+(200-num)/plot_y_scale),False,d_grey)
									w.blit(text,(316,num+1))
									draw.line(w,black,(344,num),(354,num))
									
						draw.line(w,black,(348,202),(650,202),2)
						
						sctp_indexes = [plots.index(plot) for plot in plots if plot.type == "SCTP"]
		
						for points_index in range(len(plot_points)):
							if points_index in sctp_indexes:
								for point in plot_points[points_index][1]:
									print(point)
									draw.circle(w,plot_points[points_index][2],point,4,1)
							else:
								draw.lines(w,plot_points[points_index][2],False,plot_points[points_index][1],2)
						
								
					if s_current_input != 99 and not plot_view and s_current_input//5 + 1 == plot_making:
						left_width = font_reg.size(s_inputs[s_current_input][s_input][:len(s_inputs[s_current_input][s_input])+blinker_loc])[0]
						blinker_x = plot_boxes[s_current_input%5].x + int(left_width) + int(font_reg.size(s_inputs[s_current_input][s_text])[0])
						blinker_y = plot_boxes[s_current_input%5].y + 8
						blinker_on += 1
						if blinker_on > 200:
							if blinker_on == 300:
								blinker_on = 0
							draw.line(w,black,(blinker_x,blinker_y),(blinker_x,blinker_y + 15))
					elif s_current_input == 99:
						if len(str(lists[selected_list][list_entry])) > 0:
							left_width, useless = font_reg.size(str(lists[selected_list][list_entry])[:len(str(lists[selected_list][list_entry]))+blinker_loc])
							blinker_x = 110 + int(left_width)
						else:
							blinker_x = 110
						blinker_y = 29+int((list_box.height)/12)*list_entry
						blinker_on += 1
						if blinker_on > 200:
							if blinker_on == 300:
								blinker_on = 0
							draw.line(w,black,(blinker_x,blinker_y),(blinker_x,blinker_y + 15))
						
					pygame.display.flip()
					
			elif screen == 4:
				
				draw_keyboard()
				draw_tabs()
				draw_settings()
				
				left_width = font_med_sml.size(str(settings[setting_editing])[:len(str(settings[setting_editing])) + blinker_loc])[0]
				name_width = font_med_sml.size(setting_names[setting_editing])[0]
				blinker_x = 80 + 160 * (setting_editing // 7) + name_width + int(left_width)
				blinker_y = 50 + 29 * (setting_editing % 7)
				blinker_on += 1
				if blinker_on > 200:
					if blinker_on == 300:
						blinker_on = 0
					draw.line(w,black,(blinker_x,blinker_y),(blinker_x,blinker_y + 15))
				
				pygame.display.flip()	
				
				
				
				
				
			###---CALCULATING---###
			
			if screen == 0: 
				if enter:
					try:
							
						index = 0
						resolved_string = ""
						for x in range(len(temp_char_list)):
							i = buttons_dict(temp_char_list[x])
							if x > 0 and buttons[i][b_type] == "unsimplified" and buttons[i][b_text] != ")" and (buttons[buttons_dict(temp_char_list[x-1])][b_type] == "number" or (buttons[buttons_dict(temp_char_list[x-1])][b_type] == "unsimplified" and temp_char_list[x-1] != "(")):
								resolved_string += "*"
							elif x > 0 and buttons[i][b_type] == "function" and (buttons[buttons_dict(temp_char_list[x-1])][b_type] == "number" or (buttons[buttons_dict(temp_char_list[x-1])][b_type] == "unsimplified" and temp_char_list[x-1] != "(")):
								resolved_string += "*"
							elif temp_char_list[x] == "Î£ ":
								resolved_string += "summize("+str(index)+")"
								index += 1
							resolved_string += buttons[i][b_resolve]
						
						x = None#this is so that the input of x will error
						print("---",resolved_string)
						output = str(eval(resolved_string))
						window_redraw = True
								
					except Exception as e:
						output = str(e)
						print(e)
						
					enter = False
					
			elif screen == 1:
		
				for index in range(len(functions)):
				
					if active_functions[index]:#for every active function update it
						
						resolved_string = ""
						for x in range(len(temp_functions[index])):
							i = buttons_dict(temp_functions[index][x])
							
							if x > 0 and buttons[i][b_type] == "unsimplified" and buttons[i][b_text] != ")" and (buttons[buttons_dict(temp_functions[index][x-1])][b_type] == "number" or (buttons[buttons_dict(temp_functions[index][x-1])][b_type] == "unsimplified" and temp_functions[index][x-1] != "(")):
								resolved_string += "*"
							elif x > 0 and buttons[i][b_type] == "function" and (buttons[buttons_dict(temp_functions[index][x-1])][b_type] == "number" or (buttons[buttons_dict(temp_functions[index][x-1])][b_type] == "unsimplified" and temp_functions[index][x-1] != "(")):
								resolved_string += "*"
							resolved_string += buttons[i][b_resolve]
						
						functions[index] = resolved_string
						if graph_xs[index] < win.x_max - 4/x_scale: #graph it if it hasn't already finished graphing
						
							temp_points = []
							for num in range(10):
								try:
									x = graph_xs[index]
								
									fx = eval(functions[index])
									temp_points.append((int(y_axis+x_scale*x),int(x_axis-y_scale*fx)))
									
								except Exception as e:
									pass
									
								graph_xs[index] += offset
							
							#draw.line(w,buttons[index+59][b_color],(int(graph_box.x + x_scale*(x - offset - win.x_min)), int(graph_box.height + graph_box.y - y_scale*(prev_fx - win.y_min))),(int(graph_box.x + x_scale*(x - win.x_min)), int(graph_box.height + graph_box.y - y_scale*(now_fx - win.y_min))),2)
							for point in temp_points:	
								graph_points[index].append(point)
			elif screen == 2:
				float_lists = []
				for list_index in range(len(lists)):
					float_lists.append([])
					for string in lists[list_index]:
						try:
							float_lists[list_index].append(float(string))
						except ValueError:
							pass
				
				if stats_tab == 0:	
					if done and plot_making > 0:
						for plot in plots:
							plot.plotted = False
							plot_points = []
						print("plot points:",plot_points)
						
						if plot_making == 1:
							plots.append(Boxplot())
							plots[len(plots)-1].list = s_inputs[5*(plot_making-1)][s_input]
							plots[len(plots)-1].freq_list = s_inputs[5*(plot_making-1)+1][s_input]
							plots[len(plots)-1].adjusted = s_inputs[5*(plot_making-1)+2][s_input]
							hitboxes[83+len(plots)].x *= -1
						elif plot_making == 2:
							plots.append(Histogram())
							plots[len(plots)-1].list = s_inputs[5*(plot_making-1)][s_input]
							plots[len(plots)-1].freq_list = s_inputs[5*(plot_making-1)+1][s_input]
							plots[len(plots)-1].num_bars = s_inputs[5*(plot_making-1)+2][s_input]
							hitboxes[83+len(plots)].x *= -1
						elif plot_making == 3:
							plots.append(Ogive())
							plots[len(plots)-1].list = s_inputs[5*(plot_making-1)][s_input]
							plots[len(plots)-1].freq_list = s_inputs[5*(plot_making-1)+1][s_input]
							hitboxes[83+len(plots)].x *= -1
						elif plot_making == 4:
							plots.append(Scatterplot())
							plots[len(plots)-1].list = s_inputs[5*(plot_making-1)][s_input]
							plots[len(plots)-1].y_list = s_inputs[5*(plot_making-1)+1][s_input]
							hitboxes[83+len(plots)].x *= -1
						elif plot_making == 5:
							plots.append(Regression())
							plots[len(plots)-1].list = s_inputs[5*(plot_making-1)][s_input]
							plots[len(plots)-1].y_list = s_inputs[5*(plot_making-1)+1][s_input]
							plots[len(plots)-1].line_type = s_inputs[5*(plot_making-1)+2][s_input]
							hitboxes[83+len(plots)].x *= -1
				
						if len(plots) >= 1:
							list_indexes = []
							for plot in plots:
								list_indexes.append(int(plot.list[1])-1)
							plot_x_min = 0.8*min(float_lists[list_indexes[0]])
							plot_x_max = 1.25*max(float_lists[list_indexes[0]])
							for list_index in list_indexes:
								if 0.8*min(float_lists[list_index]) < plot_x_min:
									plot_x_min = 0.8*min(float_lists[list_index])
									for plot in plots:
											plot.plotted = False
											plot_points = []
								if 1.25*max(float_lists[list_index]) > plot_x_max:
									plot_x_max = 1.25*max(float_lists[list_index])
									for plot in plots:
											plot.plotted = False
											plot_points = []
		
							plot_x_scale = 300/(plot_x_max-plot_x_min)
							plot_x_range = plot_x_max-plot_x_min
						done = False			
						
					for i in range(len(plots)):
						if not plots[i].plotted:
							if plots[i].type == "BOXP":
								print("BOXP")
								list_index = int(plots[i].list[1])-1
								float_lists[list_index].sort()
								numbers = get_5_num_sum(float_lists[list_index])
								conv_nums = []
								for num in numbers:
									conv_nums.append(int(350+(num-plot_x_min)*plot_x_scale))
								upper = 0
								middle = 25
								lower = 50
								for plot in plots:
									if plot.type == "BOXP":
										upper += 52
										middle += 52
										lower += 52
									if plots.index(plot) == i:
										break
								plot_points.append([i,[
								(conv_nums[0],upper),
								(conv_nums[0],middle),
								(conv_nums[0],lower),
								(conv_nums[0],middle),
								(conv_nums[1],middle),
								(conv_nums[1],upper),
								(conv_nums[1],lower),
								(conv_nums[2],lower),
								(conv_nums[2],upper),
								(conv_nums[1],upper),
								(conv_nums[3],upper),
								(conv_nums[3],lower),
								(conv_nums[2],lower),
								(conv_nums[3],lower),
								(conv_nums[3],middle),
								(conv_nums[4],middle),
								(conv_nums[4],upper),
								(conv_nums[4],lower)
								],function_colors[int(plots[i].list[1])-1]])
								print(numbers)
								print(conv_nums)
								print(plot_points)
							elif plots[i].type == "HIST":
								print("HIST")
								list_index = int(plots[i].list[1])-1
								float_lists[list_index] = sorted(float_lists[list_index])
								minimum = min(float_lists[list_index])
								maximum = max(float_lists[list_index])
								step = (plot_x_max-plot_x_min)/int(plots[i].num_bars)
								bars = []
								for bar_num in range(int(plots[i].num_bars)):
									bars.append([])
									for num in float_lists[list_index]:
										if num >= plot_x_min+step*bar_num and num < plot_x_min+step*(bar_num+1):
											bars[len(bars)-1].append(num)
								for bar in bars:
									if len(bar) > max_height:
										max_height = len(bar)
										for plot in plots:
											plot.plotted = False
											plot_points = []
								hist_scale = 100/max_height
								print(bars)
								hist_points = []
								for bar_index in range(len(bars)):
									hist_points.append((350+((step*bar_index*plot_x_scale)-plot_x_min),200))
									hist_points.append((350+((step*bar_index*plot_x_scale)-plot_x_min),200-(hist_scale*len(bars[bar_index]))))
									hist_points.append((350+((step*(bar_index+1)*plot_x_scale)-plot_x_min),200-(hist_scale*len(bars[bar_index]))))
									hist_points.append((350+((step*(bar_index+1)*plot_x_scale)-plot_x_min),200))
								hist_points.append((350,200))
								plot_points.append([i,hist_points,function_colors[int(plots[i].list[1])-1]])
								
							elif plots[i].type == "OGIV":
								list_index = int(plots[i].list[1])-1
								float_lists[list_index] = sorted(float_lists[list_index])
								list_length = len(float_lists[list_index])
								ogiv_scale = 150/100
								ogiv_points = []
								percentile = 50/list_length
								for num in float_lists[list_index]:
									ogiv_points.append((350+plot_x_scale*(num-plot_x_min),200-percentile*ogiv_scale))
									percentile += 100/list_length
								plot_points.append([i,ogiv_points,function_colors[int(plots[i].list[1])-1]])
								
							elif plots[i].type == "SCTP":
								list_index = int(plots[i].list[1])-1
								y_list_index = int(plots[i].y_list[1])-1
								if 0.8*min(float_lists[y_list_index]) < plot_y_min:
									plot_y_min = 0.8*min(float_lists[y_list_index])
									for plot in plots:
											plot.plotted = False
											plot_points = []
								if 1.25*max(float_lists[y_list_index]) > plot_y_max:
									plot_y_max = 1.25*max(float_lists[y_list_index])
									for plot in plots:
											plot.plotted = False
											plot_points = []
								plot_y_scale = 150/(plot_y_max-plot_y_min)
								sctp_points = []
								for num in range(len(float_lists[list_index])):
									sctp_points.append((int(350+(float_lists[list_index][num]-plot_x_min)*plot_x_scale),200-int((float_lists[y_list_index][num]-plot_y_min)*plot_y_scale)))
								plot_points.append([i,sctp_points,function_colors[int(plots[i].list[1])-1]])
													
							elif plots[i].type == "REGR":
								list_index = int(plots[i].list[1])-1
								y_list_index = int(plots[i].y_list[1])-1
								if 0.8*min(float_lists[y_list_index]) < plot_y_min:
									plot_y_min = 0.8*min(float_lists[y_list_index])
									for plot in plots:
											plot.plotted = False
											plot_points = []
								if 1.25*max(float_lists[y_list_index]) > plot_y_max:
									plot_y_max = 1.25*max(float_lists[y_list_index])
									for plot in plots:
											plot.plotted = False
											plot_points = []
								plot_y_scale = 150/(plot_y_max-plot_y_min)
								if plots[i].line_type == "linear":
								
									#calculating the correlation coefficient r
									sum_x = sum(float_lists[list_index])
									sum_y = sum(float_lists[y_list_index])
									n = len(float_lists[list_index])
									sum_xy = 0
									sum_x2 = 0
									sum_y2 = 0
									for num in range(n):
										sum_xy += float_lists[list_index][num] * float_lists[y_list_index][num]
										sum_x2 += float_lists[list_index][num] ** 2
										sum_y2 += float_lists[y_list_index][num] ** 2
									r = (n * sum_xy - sum_x * sum_y) / (((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5)
									
									#calculating the standard deviations of both lists
									"""mean_x = sum(float_lists[list_index]) / n
									mean_y = sum(float_lists[y_list_index]) / n
									x_variation = 0
									y_variation = 0
									for num in range(n):
										x_variation += (float_lists[list_index][num] - mean_x) ** 2
										y_variation += (float_lists[y_list_index][num] - mean_y) ** 2
									sx = ((x_variation) / (n - 1)) ** 0.5
									sy = ((y_variation) / (n - 1)) ** 0.5"""
									sx = statistics.stdev(float_lists[list_index])
									sy = statistics.stdev(float_lists[y_list_index])
			
									#calcualating LSRL
									b1 = r * sy / sx
									#y = b0 + b1x ----- y - b1x = b0 ----- and substitute in the centroid point for x and y to calculate b0
									xbar = statistics.mean(float_lists[list_index])
									ybar = statistics.mean(float_lists[y_list_index])
									b0 = ybar - b1 * xbar
									def regression(x):
										global b0, b1
										out = b0 + b1 * x
										return out
								
								#defining the points to plot
								regr_points = []
								x = plot_x_min
								while x < plot_x_max:
									rx = regression(x)
									if rx < plot_y_max and rx > plot_y_min:
										regr_points.append((350 + (x - plot_x_min) * plot_x_scale, 200 - (rx - plot_y_min) * plot_y_scale))
									x += plot_x_range / 300	
								plot_points.append([i,regr_points,function_colors[int(plots[i].list[1])-1]])
				
						plots[i].plotted = True
				
				elif stats_tab == 1:
					if recalculate_stats:
						if current_page == 1:
							float_lists[selected_list].sort()
							five_num_sum = get_5_num_sum(float_lists[selected_list])
							for num in range(5):
								s_calculations[num][s_input] = str(five_num_sum[num])
							s_calculations[5][s_input] = str(float(s_calculations[3][s_input]) - float(s_calculations[1][s_input]))
							s_calculations[6][s_input] = str(float(s_calculations[4][s_input]) - float(s_calculations[0][s_input]))
							s_calculations[7][s_input] = ", ".join([str(num) for num in get_outliers(float_lists[selected_list])])
						elif current_page == 2:
							s_calculations[8][s_input] = str(statistics.mean(float_lists[selected_list]))
							s_calculations[9][s_input] = str(statistics.stdev(float_lists[selected_list]))
							s_calculations[10][s_input] = str(statistics.variance(float_lists[selected_list]))
							s_calculations[11][s_input] = str(sum(float_lists[selected_list]))
							s_calculations[12][s_input] = str(sum([num ** 2 for num in float_lists[selected_list]]))
							s_calculations[13][s_input] = str(len(float_lists[selected_list]))
		
	except Exception as error:

		error_box = Rect(75,200,550,120)
		ok_box = Rect(570,290,40,20)
		w_box = Rect(0,0,w_width,w_height)
		draw.rect(w,l_grey,error_box)
		draw.rect(w,white,ok_box)
		error_header = font_hug.render("ERROR",False,m_grey)
		error_text = font_reg.render(str(error),False,d_grey)
		ok_text = font_reg.render("OK",False,m_grey)
		w.blit(error_header,(error_box.x+225,error_box.y+10))
		w.blit(error_text,(error_box.x+(error_box.width-error_text.get_size()[0])/2,error_box.y+60))
		w.blit(ok_text,(ok_box.x+5,ok_box.y+3))
		
		local_running = True
		
		while running and local_running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					
				elif event.type == pygame.MOUSEBUTTONUP:
					x, y = pygame.mouse.get_pos()
					cursor_loc = Rect(x,y,1,1)
					
					if ok_box.colliderect(cursor_loc):
						local_running = False
			
			pygame.display.flip()








#storing the users settings to a text file


original_settings = ["-10","10","-10","10","red","green","blue","orange","magenta","l_blue"]
original_settings += ["None"]*num_unused_settings
for i in range(len(settings)):
	try:
		eval(settings[i])
	except Exception as e:
		print(e)
		settings[i] = original_settings[i]
file = open("gc_settings.txt","w")
file.write("\n".join(settings))
file.close()
		

			

import string,tkinter.filedialog,tkinter.font,os,tkinter as tk;from math import*;from PIL import Image,ImageTk;from io import BytesIO;flp,ld,rt,a_c,pxc='',{},tk.Tk(),[g for g in'M@#RESKUq$XPAkb0Th95YCzsa3%LoJufr]v}7li|)=>_~":\^.` '],['00','05','0a','0f','14','19','1e','23','28','2d','32','37','3c','41','46','4b','50','55','5a','5f','64','69','6e','73','78','7d','82','87','8c','91','96','9b','a0','a5','aa','af','b4','b9','be','c3','c8','cd','d2','d7','dc','e1','e6','eb','f0','f5','fa','fe'];tac,font=a_c,tkinter.font.Font(size=10);rt.title('Ascii Art Converter');tk.Label(rt,text='Character Palette:',font=('Arial',15,'bold')).place(x=33,y=128);rt.minsize(204,310);rt.geometry("204x310");rt.maxsize(204,310)
for i in range(len(pxc)):
 ld[i]=tk.Entry(rt,bg='#'+pxc[i][-2:]*3,fg=f'#{pxc[0]*3}'if int(i)>=30 else'#'+'ff'*3,width=1,font="Courier")
for y in range(7):
 for g in range(y*10,10+y*10):
  try:
   ld[g].place(x=(g+1)*20-19-y*200,y=153+y*25)
  except:
   pass
def r_c(x=0):
 global lbl,ld
 for lbl in list(ld.values()):
  lbl.delete(0,tk.END);lbl.insert(0,string=tac[x]);x+=1
cf,s_e,p_e,f_s_e=(__import__('tkinter.ttk')).Label(rt,text='No File Selected',font=('Helvetica',12,'bold'),bg='#'+pxc[40]*3),tk.Entry(rt,width=3),tk.Entry(rt,width=3),tk.Entry(rt,width=3);r_c();[item[0].insert(0,string=item[1])for item in[(s_e,'80'),(p_e,'0.8'),(f_s_e,'10')]];[tk.Label(rt,text=lbl[0],font=8).place(x=5,y=lbl[1])for lbl in[('Font Size',82),('Result Size²',108),('Proportion',56)]];[item[0].place(x=90,y=item[1])for item in[(s_e,104),(p_e,52),(f_s_e,78)]];cf.place(relx=.5,y=15,anchor="center")
def p_f():
 def sc_img(img,n_w):
  (og_w,og_h)=img.size;return img.resize((n_w,int((og_h/floor(og_w/float(p_e.get())))*n_w)))
 global flp,ow,ol,a_c,ld,aopt,d_b,cpb
 try:
  ow.destroy()
 except:
  pass
 a_c,ow=[str(lbl.get()+' ')[0]for lbl in list(ld.values())],tk.Tk();ow.title(str(os.path.basename(flp))+' (converted)');ow.resizable(False,False)
 try:
  with Image.open(BytesIO(open(flp,"rb").read()))as m_i:
   o_b=BytesIO();m_i.convert('L');m_i=__import__('numpy').array(m_i)
   try:
    m_i[m_i[...,-1]==0]=[255]*3+[0]
   except Exception as e:
    print(e);pass
  Image.fromarray(m_i).save(o_b,"png");o_b.seek(0);aopt="\n".join([''.join([a_c[floor((pixel_value/5))]for pixel_value in list((sc_img(Image.open(fp=o_b).convert('L'),int(s_e.get()))).getdata())])[index:index+int(s_e.get())]for index in range(0,len(''.join([a_c[floor((pixel_value/5))]for pixel_value in list((sc_img(Image.open(fp=o_b).convert('L'),int(s_e.get()))).getdata())])),int(s_e.get()))]);olstr,d_b['state'],cpb['state']=aopt,tk.NORMAL,tk.NORMAL
 except:
  olstr='Failed'
 ol=tk.Label(ow,text=olstr,state="normal");ol.place(x=0,y=0);ol.pack();ol.configure(font=("Courier",int(f_s_e.get())));ow.minsize(int(ol.winfo_x()),int(ol.winfo_y()));cf.configure(text=str(os.path.basename(flp)))
def ch_f():
 try:
  global flp,ow,ol,cb;w,fs=tk.Canvas(rt,width=204,height=540),' files';flp=tkinter.filedialog.askopenfilename(filetypes=[("PNG"+fs,"*.png"),("EPS"+fs,"*.eps"),("GIF"+fs,"*.gif"),("ICNS"+fs,"*.icns"),("ICO"+fs,"*.ico"),("IM"+fs,"*.im"),("JPEG"+fs,"*.jpeg"),("MSP"+fs,"*.msp"),("PCX"+fs,"*.pcx"),("BMP"+fs,"*.bmp"),("PPM"+fs,"*.ppm"),("SGI"+fs,"*.sgi"),("SPIDER"+fs,"*.spider"),("TIFF"+fs,"*.tiff"),("WebP"+fs,"*.webp"),("XBM"+fs,"*.xbm"),("JPG"+fs,"*.jpg"),]);w.create_rectangle(2,2,200,238,fill="black",outline='black');w.place(x=0,y=310);cf.configure(text='No File Selected');rt.maxsize(204,310);cb['state'],cpb['state'],d_b['state']=tk.DISABLED,tk.DISABLED,tk.DISABLED if str(os.path.basename(flp))=='' else cf.configure(text=str(os.path.basename(flp)));rt.maxsize(204,552);global img;img,cb['state']=ImageTk.PhotoImage(Image.open(flp).resize((180,int(180*1.2)),Image.ANTIALIAS)),tk.NORMAL;imglabel=tk.Label(rt,image=img).place(x=9,y=320);rt.geometry("204x552")
 except:
  rt.maxsize(204,310)
def c_f():
 global aopt;c_w=tk.Tk();[g()for g in[c_w.withdraw,c_w.clipboard_clear]];c_w.clipboard_append(aopt);[g()for g in[c_w.update,c_w.destroy]]
def d_f():
 global aopt,flp;path,file,done,tryindex=os.path.expanduser("~")+"/Downloads/",str(os.path.splitext(os.path.basename(flp))[0]),False,1
 try:
  d_f=open(path+file+'.txt','x')
 except:
  while done==False:
   try:
    d_f,done=open(path+file+' '+str(tryindex)+'.txt','x'),True
   except:
    tryindex+=1
 d_f.write(aopt);d_f.close()
cb,cpb,d_b=tk.Button(rt,text="Convert!",font=font,command=p_f,state=tk.DISABLED,width=8,height=3),tk.Button(rt,text="Copy Text",font=font,command=c_f,state=tk.DISABLED,width=8,height=1),tk.Button(rt,text='Download',state=tk.DISABLED,command=d_f)
[g for g in[tk.Button(rt,text='Choose File',command=ch_f).place(x=10,y=30),tk.Button(rt,text=' Reset Characters ',command=r_c).place(x=45,y=283)]]
[button[0].place(x=button[1],y=button[2])for button in [ (cb, 135, 85), (cpb, 134, 60), (d_b, 110, 30)]];rt.mainloop()
from tkinter import *
import pygame
import random

music=["song1.mp3","song2.mp3","song3.mp3","song4.mp3","song5.mp3"]#ע�⣡�����������������ļ�����������ļ����ơ�
i=0
n = len(music)

root=Tk()
root.title("���ֲ�����")

def play():
    file=music[i]
    pygame.mixer.init()
    pygame.mixer.music.load(file)#���ر����ļ�
    
    pygame.mixer.music.play()#��������

    print(i)
    
def stop():
    pygame.mixer.music.stop()#ֹͣ����

def suiji_song():
    global i#�á�i����������������def��ʹ��
    i=random.randint(0,n-1)#ע�⣡����ġ�4������������ļ�������һ���������׸裬�������ġ�
    play()#�������

def next_song():#��һ��
    stop()
    global i
    if i==4:#ע�⣡����ġ�4������������ļ�������һ���������׸裬�������ġ�
        i=0
    else:
        i=i+1
    play()

def last_song():#��һ��
    stop()
    global i
    if i==0:
        i=4#ע�⣡����ġ�4������������ļ�������һ���������׸裬�������ġ�
    else:
        i=i-1
    play()

b1=Button(root,text="�����ʼ",width=10,command=suiji_song)
b1.grid(row=0,column=0,padx=10,pady=10)

b2=Button(root,text="��һ��",width=10,command=next_song)
b2.grid(row=0,column=1,padx=10,pady=10)

b3=Button(root,text="��һ��",width=10,command=last_song)
b3.grid(row=0,column=2,padx=10,pady=10)

b4=Button(root,text="ֹͣ",width=20,command=stop)
b4.grid(row=1,column=0,padx=10,pady=10,columnspan=3)

b5=Button(root,text="�˳�",width=20,command=root.destroy)
b5.grid(row=2,column=0,padx=10,pady=10,columnspan=3)


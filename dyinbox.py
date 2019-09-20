import tkinter
import json
import requests

#ウィンドウを作る
root = tkinter.Tk()
root.title=("Append to Inbox of Dynalist")
root.geometry("500x200")
root.configure(bg='white')

#Returnキーが押された時のアクション
def ok(o):
    
    # テキストボックスの内容を取得
    t = text.get()
    
    dict = {
	'token'  :  'SECRET_TOKEN',
	'index'  :  '0',
	'content'  : t
    }

    response = requests.post('https://dynalist.io/api/v1/inbox/add', json.dumps(dict), headers={'Content-Type': 'application/json'})
    
    #responseをJSON形式に変換
    r=json.loads(response.text)
    
    #投稿した後には入力欄の内容を消す
    text.delete(0, tkinter.END)
    
    #responseを表示するラベル
    res = tkinter.Label(root, text=r["_code"]+': '+t,width=48,background="#ffffff",font=("","12"))
    res.place(y=80)
    
    #入力欄にフォーカスする
    text.focus_set()
    
#ESCキーが押されたときのアクション
def cancel(c):
    text.delete(0, tkinter.END)  #入力欄の内容を消す
    text.focus_set()

#入力欄
text = tkinter.Entry(root,font=("","12"),bg='white',fg='black')  #「12は」入力欄のフォントサイズ。変更可能。
text.pack(fill='x',padx=30,pady=30,anchor=tkinter.CENTER)
text.bind('<Key-Return>', ok)
text.bind('<Key-Escape>', cancel)
text.focus_set()

#左下のラベル
h1 = tkinter.Label(root, text="Enter:Post / Esc:Erase",background="#fff",font=("","9"))
h1.pack(anchor=tkinter.W,side=tkinter.BOTTOM,padx=30)
title = tkinter.Label(root, text="[Append to Inbox of Dynalist]",background="#fff",font=("","9"))
title.pack(anchor=tkinter.W,side=tkinter.BOTTOM,padx=30)

root.mainloop()

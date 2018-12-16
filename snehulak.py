import tkinter
canvas=tkinter.Canvas(width=600, height=800, bg="#00FFFF")

canvas.pack()

canvas.create_oval(250, 100, 350, 200, fill="white", outline="black") #hlava
canvas.create_oval(200, 200, 400, 400, fill="white", outline="black") #draha cast
canvas.create_oval(150, 400, 450, 700, fill="white", outline="black") #treti cast

canvas.create_oval(290, 250, 310, 270, fill="black", outline="black") #knoflik
canvas.create_oval(290, 350, 310, 370, fill="black", outline="black") #knoflik
canvas.create_oval(290, 500, 310, 520, fill="black", outline="black") #knoflik
canvas.create_oval(290, 600, 310, 620, fill="black", outline="black") #knoflik

canvas.create_oval(270, 133, 280, 153, fill="black", outline="black") #oko
canvas.create_oval(320, 133, 330, 153, fill="black", outline="black") #oko

canvas.create_polygon(300, 155, 340, 165, 300, 175, fill="orange", outline="black") #nos
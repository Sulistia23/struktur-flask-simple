from flask import Flask

app = Flask(__name__)

@app.route("/get")
def cerita_get():
    return (
        "Pagi itu langit tampak redup. "
        "Raka berjalan perlahan menuju halte, memandangi dedaunan jatuh di jalanan basah. "
        "Ia tidak tahu, bahwa hari itu akan mengubah segalanya."
    )

@app.route("/post")
def cerita_post():
    return (
        "Siang menjelang, dan Raka menemukan sebuah buku kecil di kursi taman. "
        "Di dalamnya ada tulisan tangan: 'Temukan aku di bawah pohon beringin tua.' "
        "Hatinya berdebar, antara penasaran dan takut."
    )

@app.route("/delete")
def cerita_delete():
    return (
        "Senja tiba. Surat terakhir itu ia bakar perlahan, menyisakan abu dan kenangan. "
        "Beberapa hal, pikir Raka, memang harus dihapus agar yang baru bisa tumbuh."
    )

@app.route("/detail/<tokoh>")
def cerita_detail(tokoh):
    return (
        f"{tokoh} menatap langit malam yang penuh bintang. "
        f"Hari-hari panjang telah dilalui, dan kini hanya ketenangan yang tersisa. "
        f"Begitulah kisah {tokoh}, yang akhirnya menemukan arti dari perjalanan hidup."
    )

if __name__ == "__main__":
    app.run(debug=True)

from database.db import initialize_database
from services.catalog_service import CatalogService
from models.product import Product
from utils.validator import validate_price

initialize_database()
service = CatalogService()

def menu():
    print("\n=== SISTEM KATALOG FASHION ===")
    print("1. Tambah Produk")
    print("2. Lihat Semua Produk")
    print("3. Hapus Produk")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        name = input("Nama produk: ")
        category = input("Kategori (baju, rok, topi, dll): ")
        price_input = input("Harga: ")

        price = validate_price(price_input)
        if price is None:
            print("Harga tidak valid!")
            continue

        product = Product(name, category, price)
        service.add_product(product)
        print("Produk berhasil ditambahkan!")

    elif pilihan == "2":
        products = service.show_products()
        if not products:
            print("Belum ada produk.")
        else:
            print("\nDaftar Produk:")
            for item in products:
                print(f"{item[0]}. {item[1]} | {item[2]} | Rp {item[3]}")

    elif pilihan == "3":
        id_del = input("Masukkan ID produk yang ingin dihapus: ")
        service.delete_product(id_del)
        print("Produk dihapus!")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid! Coba lagi.")

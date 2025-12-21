import customtkinter as ctk
import tkinter as tk

import dashboard
import add_recipe
import manage_recipes
import settings
import database

# Veritabanını başlat
database.setup_database()

class CookBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CookBook")
        self.root.geometry("1200x600")
        
        # Dil ayarını yükle
        self.current_lang = settings.get_lang()
        
        # CustomTkinter tema ayarları
        ctk.set_appearance_mode("light")  # "light" veya "dark"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
        
        # UI'ı oluştur
        self.create_ui()
        
        # İlk açılışta Dashboard'u göster
        self.show_dashboard()
    
    def create_ui(self):
        """UI bileşenlerini oluştur"""
        # Sidebar Frame
        self.sidebar_frame = ctk.CTkFrame(self.root, width=200, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")
        self.sidebar_frame.pack_propagate(False)
        
        # Uygulama başlığı
        app_title = ctk.CTkLabel(
            self.sidebar_frame,
            text="🍳 CookBook",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        app_title.pack(pady=(20, 30))
        
        # Ana içerik Frame
        self.main_content_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.main_content_frame.pack(side="right", fill="both", expand=True)
        
        # Menü butonlarını oluştur
        self.create_menu_buttons()
    
    def create_menu_buttons(self):
        """Menü butonlarını oluştur/güncelle"""
        # Eski butonları temizle
        for widget in self.sidebar_frame.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()
        
        # Başlığı tekrar ekle
        app_title = ctk.CTkLabel(
            self.sidebar_frame,
            text="🍳 CookBook",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        app_title.pack(pady=(20, 30))
        
        # Menü öğeleri
        menu_items = [
            ("🏠 Dashboard", "Dashboard"),
            ("➕ " + ("Tarif Ekle" if self.current_lang == "tr" else "Add Recipe"), "Add Recipe"),
            ("📋 " + ("Tarifleri Yönet" if self.current_lang == "tr" else "Manage Recipes"), "Manage Recipes"),
            ("⚙️ " + ("Ayarlar" if self.current_lang == "tr" else "Settings"), "Settings")
        ]
        
        # Butonları oluştur
        for text, action in menu_items:
            button = ctk.CTkButton(
                self.sidebar_frame,
                text=text,
                command=lambda a=action: self.menu_click(a),
                font=ctk.CTkFont(size=14),
                height=40,
                corner_radius=8
            )
            button.pack(fill="x", pady=8, padx=15)
        
        # Ayırıcı
        separator_frame = ctk.CTkFrame(self.sidebar_frame, height=2, fg_color="gray70")
        separator_frame.pack(fill="x", pady=20, padx=15)
        
        # Tema değiştir butonu
        theme_text = "🌓 " + ("Tema" if self.current_lang == "tr" else "Theme")
        theme_btn = ctk.CTkButton(
            self.sidebar_frame,
            text=theme_text,
            command=self.toggle_theme,
            font=ctk.CTkFont(size=14),
            height=40,
            corner_radius=8,
            fg_color="gray40",
            hover_color="gray50"
        )
        theme_btn.pack(fill="x", pady=8, padx=15)
    
    def menu_click(self, button_text):
        """Menü tıklama olayını işle"""
        # İçeriği temizle
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()
        
        # Seçili ekranı göster
        if button_text == "Dashboard":
            self.show_dashboard()
        elif button_text == "Add Recipe":
            self.show_add_recipe()
        elif button_text == "Manage Recipes":
            self.show_manage_recipes()
        elif button_text == "Settings":
            self.show_settings()
    
    def show_dashboard(self):
        """Dashboard'u göster"""
        dashboard.show_dashboard(self.main_content_frame, self.current_lang)
    
    def show_add_recipe(self):
        """Tarif ekleme ekranını göster"""
        add_recipe.show_add_recipe_screen(self.main_content_frame, self.current_lang)
    
    def show_manage_recipes(self):
        """Tarif yönetim ekranını göster"""
        manage_recipes.show_manage_recipe_screen(self.main_content_frame, self.current_lang)
    
    def show_settings(self):
        """Ayarlar ekranını göster"""
        settings.show_settings(
            self.main_content_frame, 
            self.current_lang,
            on_language_change=self.on_language_change
        )
    
    def on_language_change(self, new_lang):
        """Dil değiştiğinde çağrılır"""
        self.current_lang = new_lang
        
        # Menü butonlarını güncelle
        for widget in self.sidebar_frame.winfo_children():
            widget.destroy()
        self.create_menu_buttons()
        
        # Dashboard'a dön
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()
        self.show_dashboard()
    
    def toggle_theme(self):
        """Tema değiştir (light/dark)"""
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Light":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


# Uygulamayı başlat
if __name__ == "__main__":
    root = ctk.CTk()
    app = CookBookApp(root)
    root.mainloop()
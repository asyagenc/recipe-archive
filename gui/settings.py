import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from texts import texts
import json
import os

# Ayarları saklamak için dosya
SETTINGS_FILE = 'app_settings.json'

def load_settings():
    """Ayarları dosyadan yükle"""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                return settings.get('language', 'en')
        except:
            return 'en'
    return 'en'

def save_settings_to_file(language):
    """Ayarları dosyaya kaydet"""
    settings = {'language': language}
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)

def get_lang():
    """Mevcut dili döndür"""
    return load_settings()

def show_settings(parent_frame, language, on_language_change=None):
    """Ayarlar ekranını göster"""
    current_lang = language
    
    # Frame'i temizle
    for widget in parent_frame.winfo_children():
        widget.destroy()
    
    # Ana container
    container = ctk.CTkFrame(parent_frame, fg_color="transparent")
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Başlık
    title_label = ctk.CTkLabel(
        container,
        text="⚙️ " + ("Ayarlar" if current_lang == "tr" else "Settings"),
        font=ctk.CTkFont(size=32, weight="bold")
    )
    title_label.pack(anchor="w", pady=(0, 30))
    
    # Dil ayarları kartı
    lang_card = ctk.CTkFrame(container, corner_radius=15)
    lang_card.pack(fill="x", pady=15)
    
    lang_inner = ctk.CTkFrame(lang_card, fg_color="transparent")
    lang_inner.pack(fill="x", padx=30, pady=30)
    
    # Dil başlığı
    language_title = ctk.CTkLabel(
        lang_inner,
        text="🌐 " + texts[current_lang]["language_label"],
        font=ctk.CTkFont(size=20, weight="bold")
    )
    language_title.pack(anchor="w", pady=(0, 10))
    
    # Dil açıklaması
    lang_desc = ctk.CTkLabel(
        lang_inner,
        text=("Uygulama dilini seçin / Select application language" if current_lang == "tr"
              else "Select application language"),
        font=ctk.CTkFont(size=13),
        text_color="gray60"
    )
    lang_desc.pack(anchor="w", pady=(0, 20))
    
    # Dil seçimi frame
    lang_selection_frame = ctk.CTkFrame(lang_inner, fg_color="transparent")
    lang_selection_frame.pack(anchor="w", pady=10)
    
    language_var = tk.StringVar(value=current_lang)
    
    # İngilizce radio button
    en_radio = ctk.CTkRadioButton(
        lang_selection_frame,
        text="🇬🇧 English",
        variable=language_var,
        value="en",
        font=ctk.CTkFont(size=14)
    )
    en_radio.pack(anchor="w", pady=8)
    
    # Türkçe radio button
    tr_radio = ctk.CTkRadioButton(
        lang_selection_frame,
        text="🇹🇷 Türkçe",
        variable=language_var,
        value="tr",
        font=ctk.CTkFont(size=14)
    )
    tr_radio.pack(anchor="w", pady=8)
    
    # Kaydet butonu frame
    button_frame = ctk.CTkFrame(container, fg_color="transparent")
    button_frame.pack(anchor="w", pady=(30, 0))
    
    def save_and_reload():
        new_lang = language_var.get()
        
        # Ayarları kaydet
        save_settings_to_file(new_lang)
        
        # Bilgi mesajı
        messagebox.showinfo(
            "✓ " + ("Başarılı" if new_lang == "tr" else "Success"),
            ("Dil ayarı kaydedildi!\nDeğişiklikler uygulandı." if new_lang == "tr" 
             else "Language setting saved!\nChanges applied.")
        )
        
        # Callback çağır
        if on_language_change:
            on_language_change(new_lang)
    
    save_button = ctk.CTkButton(
        button_frame,
        text="💾 " + texts[current_lang]["save_btn"],
        command=save_and_reload,
        font=ctk.CTkFont(size=16, weight="bold"),
        height=45,
        corner_radius=10,
        fg_color="#27ae60",
        hover_color="#229954"
    )
    save_button.pack(side="left", padx=5)
    
    # Bilgi kutusu
    info_card = ctk.CTkFrame(container, corner_radius=15, fg_color=("#e8f4f8", "#1a3a4a"))
    info_card.pack(fill="x", pady=(30, 0))
    
    info_inner = ctk.CTkFrame(info_card, fg_color="transparent")
    info_inner.pack(padx=25, pady=20)
    
    info_text = (
        "ℹ️ Dil değişikliği tüm uygulamayı etkiler.\nDeğişiklikler hemen uygulanacaktır." 
        if current_lang == "tr" else
        "ℹ️ Language change affects the entire application.\nChanges will be applied immediately."
    )
    
    ctk.CTkLabel(
        info_inner,
        text=info_text,
        font=ctk.CTkFont(size=13),
        justify="left"
    ).pack(anchor="w")
    
    # Tema ayarları kartı
    theme_card = ctk.CTkFrame(container, corner_radius=15)
    theme_card.pack(fill="x", pady=15)
    
    theme_inner = ctk.CTkFrame(theme_card, fg_color="transparent")
    theme_inner.pack(fill="x", padx=30, pady=30)
    
    theme_title = ctk.CTkLabel(
        theme_inner,
        text="🎨 " + ("Tema" if current_lang == "tr" else "Theme"),
        font=ctk.CTkFont(size=20, weight="bold")
    )
    theme_title.pack(anchor="w", pady=(0, 10))
    
    theme_desc = ctk.CTkLabel(
        theme_inner,
        text=("Açık veya koyu tema seçin" if current_lang == "tr"
              else "Select light or dark theme"),
        font=ctk.CTkFont(size=13),
        text_color="gray60"
    )
    theme_desc.pack(anchor="w", pady=(0, 20))
    
    def change_theme():
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Light":
            ctk.set_appearance_mode("dark")
            theme_button.configure(text="☀️ " + ("Açık Tema" if current_lang == "tr" else "Light Theme"))
        else:
            ctk.set_appearance_mode("light")
            theme_button.configure(text="🌙 " + ("Koyu Tema" if current_lang == "tr" else "Dark Theme"))
    
    current_mode = ctk.get_appearance_mode()
    button_text = ("🌙 Koyu Tema" if current_mode == "Light" else "☀️ Açık Tema") if current_lang == "tr" else (
        "🌙 Dark Theme" if current_mode == "Light" else "☀️ Light Theme"
    )
    
    theme_button = ctk.CTkButton(
        theme_inner,
        text=button_text,
        command=change_theme,
        font=ctk.CTkFont(size=14),
        height=40,
        corner_radius=10
    )
    theme_button.pack(anchor="w")
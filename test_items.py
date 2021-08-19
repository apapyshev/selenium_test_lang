link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_links(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element_by_xpath("//form[@id='add_to_basket_form']/button[@type='submit']")

    assert button.text in ("Añadir al carrito", "Ajouter au panier", "Добавить в корзину", "Add to basket", "In Warenkorb legen" , "أضف الى سلة التسوق",
                           "Afegeix a la cistella", "Vložit do košíku", "Læg i kurv", "Προσθήκη στο καλάθι", "Lisää koriin", "Aggiungi al carrello", "장바구니 담기",
                           "Voeg aan winkelmand toe", "Dodaj do koszyka", "Adicionar ao carrinho", "Adicionar à cesta", "Adauga in cos", "Pridať do košíka"
                           ) , "Кнопка не найдена"

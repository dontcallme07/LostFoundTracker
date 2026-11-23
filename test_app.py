import app

def test_add_lost_item():
    app.items.clear()
    app.add_item("Wallet", "Library", "Lost")

    assert len(app.items) == 1
    assert app.items[0]["name"] == "Wallet"
    assert app.items[0]["location"] == "Library"
    assert app.items[0]["status"] == "Lost"

def test_add_found_item():
    app.items.clear()
    app.add_item("Phone", "Canteen", "Found")

    assert app.items[0]["name"] == "Phone"
    assert app.items[0]["status"] == "Found"

def test_search_item(capsys):
    app.items.clear()
    app.add_item("Keys", "Classroom", "Found")

    app.search_item("Keys")

    output = capsys.readouterr().out
    assert "Keys" in output
    assert "Classroom" in output

def test_item_not_found(capsys):
    app.items.clear()
    app.search_item("Laptop")

    output = capsys.readouterr().out
    assert "Item not found." in output
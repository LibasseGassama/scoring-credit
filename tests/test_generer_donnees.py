from src.generer_donnees import generer_donnees


def test_generer_donnees_renvoie_500_lignes_avec_decision():
    df = generer_donnees()
    assert df.shape[0] == 500
    assert "decision" in df.columns

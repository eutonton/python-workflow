import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_mensagem(client):
    response = client.get('/mensagem')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'mensagem': 'Olá, esta é uma mensagem via GET!'}

def test_post_mensagem(client):
    response = client.post('/mensagem', json={'mensagem': 'Teste via pytest'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['mensagem_recebida'] == 'Teste via pytest'
    assert data['status'] == 'Mensagem recebida com sucesso!'

def test_get_visit_places(client, token):
    response = client.get(
        '/visit_places',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json() == {'visit_places': []}


def test_create_user(client, session, token):
    response = client.post(
        '/visit_places',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'teste',
            'description': 'teste',
            'visit_turn': 'teste',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'name': 'teste',
        'description': 'teste',
        'visit_turn': 'teste',
        'id': 1,
        'user_id': 1,
    }


def test_delete_user(client, visit_place, token):
    response = client.delete(
        f'/visit_places/{visit_place.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'Visit Place deleted'}

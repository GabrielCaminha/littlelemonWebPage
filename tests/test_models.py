from django.test import TestCase
from restaurant.models import Reserva, MenuItem
from datetime import datetime

class ReservaTest(TestCase):
    def test_reserva_valida(self):
        """Testa a criação de uma reserva válida."""
        reserva = Reserva.objects.create(
            nome="Reserva Teste",
            number_guests=4,
            booking_date=datetime.now()
        )
        self.assertEqual(str(reserva), "Reserva Teste")

    def test_reserva_invalida_guests_acima_limite(self):
        """Testa a falha ao criar uma reserva com mais de 6 convidados."""
        with self.assertRaises(ValueError) as e:
            Reserva.objects.create(
                nome="Reserva Inválida",
                number_guests=7,
                booking_date=datetime.now()
            )
        self.assertEqual(str(e.exception), "A reserva maxima e 6.")

    def test_reserva_invalida_guests_abaixo_limite(self):
        """Testa a falha ao criar uma reserva com menos de 1 convidado."""
        with self.assertRaises(ValueError) as e:
            Reserva.objects.create(
                nome="Reserva Inválida",
                number_guests=0,
                booking_date=datetime.now()
            )
        self.assertEqual(str(e.exception), "A reserva maxima e 6.")


class MenuItemTest(TestCase):
    def test_menuitem_valido(self):
        """Testa a criação de um item de menu válido."""
        menu_item = MenuItem.objects.create(
            title="Prato Especial",
            price=50.00,
            inventory=3
        )
        # Ajustar o teste para o retorno esperado do método __str__
        self.assertEqual(str(menu_item), "Prato Especial : 50.00")

    def test_menuitem_invalido_inventory_acima_limite(self):
        """Testa a falha ao criar um item de menu com estoque acima de 5."""
        with self.assertRaises(ValueError) as e:
            MenuItem.objects.create(
                title="Item Inválido",
                price=25.00,
                inventory=6
            )
        self.assertEqual(str(e.exception), "O estoque maxima e 5.")

    def test_menuitem_invalido_inventory_abaixo_limite(self):
        """Testa a falha ao criar um item de menu com estoque abaixo de 1."""
        with self.assertRaises(ValueError) as e:
            MenuItem.objects.create(
                title="Item Inválido",
                price=25.00,
                inventory=0
            )
        self.assertEqual(str(e.exception), "O estoque maxima e 5.")

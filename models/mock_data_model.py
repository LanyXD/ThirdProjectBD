# datos de prueba


class MockDataModel:
    def __init__(self):
        self.clients = [
            {"_id": 1,
             "nombre": "Juan Pérez",
             "nit": "1234567-8",
             "telefono": "555-1010",
             "direccion": "Av. Central #45"},
            {"_id": 2,
             "nombre": "María López",
             "nit": "8889990-1",
             "telefono": "555-2020",
             "direccion": "Calle Real #23"},
            {"_id": 3,
             "nombre": "Carlos Díaz",
             "nit": "7788123-4",
             "telefono": "555-3030",
             "direccion": "Zona 1, Lote 15"},
        ]

        self.products = [
            {"_id": 101, "nombre": "Tortilla de Maíz", "unidad": "1 lb", "precio": 6.00},
            {"_id": 102, "nombre": "Tostada Mediana Amarilla", "unidad": "bolsa(25u)", "precio": 11.00},
            {"_id": 103, "nombre": "Tostada Grande Amarilla", "unidad": "bolsa(25u)", "precio": 13.00},
            {"_id": 104, "nombre": "Tostada Extragrande Amarilla", "unidad": "bolsa(25u)", "precio": 15.00},
            {"_id": 101, "nombre": "Tortilla de Maíz", "unidad": "1 lb", "precio": 6.00},
            {"_id": 102, "nombre": "Tostada Mediana Amarilla", "unidad": "bolsa(25u)", "precio": 11.00},
            {"_id": 103, "nombre": "Tostada Grande Amarilla", "unidad": "bolsa(25u)", "precio": 13.00},
            {"_id": 104, "nombre": "Tostada Extragrande Amarilla", "unidad": "bolsa(25u)", "precio": 15.00},
            {"_id": 101, "nombre": "Tortilla de Maíz", "unidad": "1 lb", "precio": 6.00},
            {"_id": 102, "nombre": "Tostada Mediana Amarilla", "unidad": "bolsa(25u)", "precio": 11.00},
            {"_id": 103, "nombre": "Tostada Grande Amarilla", "unidad": "bolsa(25u)", "precio": 13.00},
            {"_id": 104, "nombre": "Tostada Extragrande Amarilla", "unidad": "bolsa(25u)", "precio": 15.00},
        ]

        self.sales = [
            {
                "_id": "V001",
                "cliente": "Juan Pérez",
                "fecha": "2025-10-31",
                "detalle": [
                    {"producto": "Tortilla de Maíz", "cantidad": 2, "subtotal": 20.00},
                    {"producto": "Totopos", "cantidad": 1, "subtotal": 8.00},
                ],
                "total": 28.00,
                "pago": 30.00,
                "cambio": 2.00,
            },
            {
                "_id": "V002",
                "cliente": "María López",
                "fecha": "2025-11-01",
                "detalle": [
                    {"producto": "Tortilla de Harina", "cantidad": 3, "subtotal": 36.00},
                ],
                "total": 36.00,
                "pago": 40.00,
                "cambio": 4.00,
            },
        ]

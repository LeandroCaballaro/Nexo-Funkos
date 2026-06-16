from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Precio = models.FloatField()
    Cantidad = models.IntegerField()
    Descripcion = models.TextField(max_length=50)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')

    def __str__(self):
        return self.Nombre

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    total = models.FloatField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')

    def __str__(self):
        return f"Pedido {self.id_pedido}"

class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    codigo_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='codigo_producto')
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    def __str__(self):
        return f"Detalle {self.id_detalle}"

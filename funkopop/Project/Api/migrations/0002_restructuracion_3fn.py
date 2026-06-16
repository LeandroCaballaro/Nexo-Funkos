from django.db import migrations, models
import django.db.models.deletion


def populate_categoria(apps, schema_editor):
    Categoria = apps.get_model('Api', 'Categoria')
    Producto = apps.get_model('Api', 'Producto')

    for producto in Producto.objects.all():
        if producto.Categoria:
            cat, _ = Categoria.objects.get_or_create(nombre=producto.Categoria)
            producto.id_categoria = cat
            producto.save()


def reverse_populate_categoria(apps, schema_editor):
    Producto = apps.get_model('Api', 'Producto')
    for producto in Producto.objects.all():
        if producto.id_categoria:
            producto.Categoria = producto.id_categoria.nombre
            producto.save()


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.Categoria', db_column='id_categoria'),
        ),
        migrations.RunPython(populate_categoria, reverse_populate_categoria),
        migrations.RemoveField(
            model_name='producto',
            name='Categoria',
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Categoria', db_column='id_categoria'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.CASCADE, to='Api.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('codigo_producto', models.ForeignKey(db_column='codigo_producto', on_delete=django.db.models.deletion.CASCADE, to='Api.Producto')),
                ('id_pedido', models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.CASCADE, to='Api.Pedido')),
            ],
        ),
    ]

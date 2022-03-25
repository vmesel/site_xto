# Generated by Django 4.0.2 on 2022-03-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0007_clustersmpsmlinc_cluster_matrix'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterMatrixDefinitive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.CharField(blank=True, max_length=2000, null=True)),
                ('matrix_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('transcripts_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('gene_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('gene_type', models.CharField(blank=True, max_length=2000, null=True)),
                ('is_detected', models.CharField(blank=True, max_length=2000, null=True)),
                ('enrichment', models.CharField(blank=True, max_length=2000, null=True)),
                ('adjusted_p_value', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]

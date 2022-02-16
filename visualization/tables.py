from visualization.models import GeneLocation, ClusterSMPSmlinc
from table import Table
from table.columns import Column, LinkColumn, Link

from table.utils import A


class GeneLocationTable(Table):
    gene_id = LinkColumn(field='gene_id', header="SmLINC", links=[Link(text=A('gene_id'), viewname="sm_view", kwargs={"gene_id":A('gene_id')})])
    chromosome = Column(field='chromosome', header="Chromosome")
    chromosome_start = Column(field='chromosome_start', header="Chromosome Start")
    chromosome_end = Column(field='chromosome_end', header="Chromosome End")
    strand = Column(field='strand', header="Strand")
    block_counts = Column(field='block_counts', header="# of Exons")
    class Meta:
        model = GeneLocation
        search_placeholder = "Search for your SmLINC"


class SmLincExpression(Table):
    gene_id = LinkColumn(field='gene_id__smp', header="SmLINC", links=[Link(text=A('gene_id'), viewname="lncrnas_cluster_view", kwargs={"gene_id":A('gene_id')})])
    transcripts_id = Column(field='transcripts_id', header="Transcript ID")
    gene_type = Column(field='gene_type', header="Gene Type")
    is_detected = Column(field='is_detected', header="Is Detected")

    class Meta:
        model = ClusterSMPSmlinc
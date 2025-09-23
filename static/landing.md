# Explore LepBase data

LepBase contains data for
:count{taxonomy=ncbi result=assembly query="tax_tree(7088)" inline description="assemblies in LepBase"} assemblies across
:count{taxonomy=ncbi result=taxon query="tax_tree(7088) AND tax_rank(species)" inline includeEstimates description="Lepidoptera species in LepBase"} species. The map below summarises the geographic distibutions of these species as a count of included species per country, based on [GBIF](https://www.gbif.org) occurrence data.

```report
report: map
x: country_code
rank: species
includeEstimates: true
mapThreshold: 2000
regionField: country_code
geoBounds: -180,90,180,-45
result: taxon
taxonomy: ncbi
ratio: 2.4
size: 12
```

## Search templates

We have created a set of advanced search templates to highlight some of the ways to explore the data in LepBase. The templates below can be used to generate an oxford plot to compare assemblies of two taxa and to plot assembly metrics in windows along each chromosome of an assembly.

Visit the [templates page](/templates) for more examples.

:::grid{container direction="row" spacing="1"}

::include{pageId=templates/oxfordPlotByTaxon.md size=6 className=unpadded}

::include{pageId=templates/windowPlotByTaxon.md size=6 className=unpadded}

::grid[&nbsp;&nbsp;more [oxford plot templates](/templates/oxford)]{size=6}
::grid[&nbsp;&nbsp;more [window-based templates](/templates/windows)]{size=6}

:::

## Ribbon plots

:hub allows exploration of synteny through ribbon plots between pairs of complete assemblies or subsets of chromosomes

```report
report: ribbon
x: assembly_id=queryA.assembly_id,queryB.assembly_id AND collate(sequence_id,name) AND feature_type=lepidoptera_odb10-busco-gene AND status!=duplicated
queryA: assembly--tax_name(Hypena proboscidalis) AND refseq_category=representative genome,reference genome
queryB: assembly--tax_name(Laspeyria flexula) AND refseq_category=representative genome,reference genome
xOpts: ;;;;Hypena proboscidalis
yOpts: ;;;;Laspeyria flexula
cat: merian_unit[32]
compactLegend: true
reorient: true
result: feature
taxonomy: ncbi
ratio: 2
```

## Window statistic plots

```report
report: scatter
x: midpoint_proportion AND assembly_id=queryA.assembly_id AND feature_type=window-1000000 AND gc
xField: midpoint_proportion
queryA: assembly--tax_name(Pieris brassicae)
y: gc
cat: sequence_id[31]
includeEstimates: true
plotRatio: auto
scatterThreshold: -1
pointSize: 15
result: feature
taxonomy: ncbi
ratio: 2
```

## BUSCO counts

Busco identities are recorded for each taxon, allowing plots of BUSCO counts against other assembly metrics.

```report
report: scatter
x: tax_tree(Lepidoptera) AND assembly_span AND lepidoptera_odb10_complete
y: lepidoptera_odb10_complete_count
rank: species
cat: family[6]
includeEstimates: false
scatterThreshold: -1
result: taxon
taxonomy: ncbi
size: 12
ratio: 2
caption: Lepidoptera BUSCO completeness against assembly span for the families represented in LepBase
```

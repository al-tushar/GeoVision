# GeoVision
## Post-Disaster Building Damage Assessment from Satellite Imagery

GeoVision is a student software engineering project exploring building damage
classification from post-disaster satellite imagery.

### Current experimental stage
- Dataset: xView2 Challenge dataset, accessed through Kaggle.
- Labels: no-damage, minor-damage, major-damage, destroyed.
- Experiment: building-crop classification using 128x128 RGB crops.
- Large pilot: 6,288 training crops and 1,675 validation crops.
- Validation was separated by source image to avoid image overlap between splits.
- The small CNN pilot had weak results; this is an experimental baseline, not
  a validated operational disaster-assessment system.

### Repository contents
- `train_crops_128_manifest.csv`: training crop metadata.
- `val_crops_128_manifest.csv`: validation crop metadata.
- `geovision_pilot_cnn.pth`: earlier pilot checkpoint, if included.
- `geovision_pilot_cnn_balanced.pth`: balanced pilot checkpoint, if included.

The CSV files intentionally omit local Kaggle image paths. The images and full
dataset manifests are not included in this export.

### Dataset
The xView2 dataset is provided by its respective owners. Obtain it through an
authorized source and follow its applicable license and terms. This repository
does not redistribute the original dataset.

### Status
Research and development in progress. Model performance and generalization
still require further evaluation.

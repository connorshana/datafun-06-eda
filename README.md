# Argos and GPS data for a polar bear track

[https://doi.org/10.5061/dryad.4qrfj6q96](https://doi.org/10.5061/dryad.4qrfj6q96)

It is rare to be able to validate state-space models for Argos data. This dataset provides a unique opportunity to do so, because it contains simultaneous Argos and GPS data for a polar bear. The GPS locations are extremely accurate (≤30 m) compared to Argos data, which can have errors as large as 36 km depending on the quality class. The dataset contains one year of movement data, starting on April 20, 2009. The dataset was used in the associated Ecological Monographs paper to show how to fit state-space models to ecological data.

This adult female polar bear was collared in the Beaufort Sea, Northwest Territories, Canada, in April of 2009. We used a Gen 4 Telonics Collar. For collaring details, see Auger-Méthé et al. (2016) Home ranges in moving habitats: polar bears and sea ice. Ecography 39: 26−35.

The polar bear handling procedures were approved by the University of Alberta Biological Sciences Animal Policy and Welfare Committee (Permits 600904. Wildlife research permits were obtained from the Government of the Northwest Territories (Wildlife Research Permit WL005596).

## Description of the data and file structure

PB\_Argos.csv – One year of Argos locations. DateTime contains the date and time of the locations, QualClass contains the quality category of the Argos location, Lat contains the latitude, and Lon contains the longitude.
PB\_GPS.csv – One year of daily GPS locations. DateTime contains the date and time of the locations, Lat contains the latitude, and Lon contains the longitude.
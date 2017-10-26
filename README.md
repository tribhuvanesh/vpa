[![image-title-here](overview.jpg){:class=”img-responsive”}](https://arxiv.org/abs/1703.10660)

## Abstract
With an increasing number of users sharing information online, privacy implications entailing such actions are a major concern.
For explicit content, such as user profile or GPS data, devices (e.g. mobile phones) as well as web services (e.g. facebook) offer to set privacy settings in order to enforce the users' privacy preferences.

We propose the first approach that extends this concept to image content in the spirit of a _Visual Privacy Advisor_.  First, we categorize personal information in images into 68 image attributes and collect a dataset, which allows us to train models that predict such information directly from images. Second, we run a user study to understand the privacy preferences of different users w.r.t. such attributes. Third, we propose models that predict user specific privacy score from images in order to enforce the users' privacy preferences. Our model is trained to predict the user specific privacy risk and even outperforms the judgment of the users, who often fail to follow their own privacy preferences on image data.

## Resources
  - [Paper](https://arxiv.org/abs/1703.10660)
  - [Poster](http://resources.mpi-inf.mpg.de/d2/orekondy/orekondy17iccv.pdf)
  - [Code](https://github.com/tribhuvanesh/vpa)

## Bibtex
```
@inproceedings{orekondy17iccv,
  title = {Towards a Visual Privacy Advisor: Understanding and Predicting Privacy Risks in Images},
  author = {Tribhuvanesh Orekondy and Bernt Schiele and Mario Fritz},
  year = {2017},
  date = {2017-10-29},
  booktitle = {IEEE International Conference on Computer Vision (ICCV)},
  keywords = {2017},
  pubstate = {published},
  tppubtype = {inproceedings}
}
```

## Dataset
This dataset is released under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/). For images, original licenses apply (refer to `source_url` and `openimages_id` in respective annotation file).

  - **train**: [images](https://datasets.d2.mpi-inf.mpg.de/orekondy17iccv/train2017.tar.gz) (10k images, 21G), [annotations](https://datasets.d2.mpi-inf.mpg.de/orekondy17iccv/train2017_anno.tar.gz)
  - **val**: [images](https://datasets.d2.mpi-inf.mpg.de/orekondy17iccv/val2017.tar.gz) (4.1k images, 8.8G), [annotations](https://datasets.d2.mpi-inf.mpg.de/orekondy17iccv/val2017_anno.tar.gz)
  - **test**: [images](https://datasets.d2.mpi-inf.mpg.de/orekondy17iccv/test2017.tar.gz) (8k images, 17G), [annotations](https://datasets.d2.mpi-inf.mpg.de/orekondy17iccv/test2017_anno.tar.gz)

## People
  - [Tribhuvanesh Orekondy](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/people/tribhuvanesh-orekondy/)
  - [Bernt Schiele](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/people/bernt-schiele/)
  - [Mario Fritz](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/people/mario-fritz/)

## Press Coverage
  - [Forbes](https://www.forbes.com/sites/kevinmurnane/2017/04/10/your-selfies-can-hurt-you-but-theres-a-privacy-adviser-that-can-help/#189b66e7589a)
  - [Vocativ](http://www.vocativ.com/418862/ai-privacy-assistants-expose-sensitive-info/)
  - [Vice](https://motherboard.vice.com/en_us/article/3dmwqk/are-your-selfies-leaking-your-fingerprints-this-ai-will-let-you-know)
  - [iapp](https://iapp.org/news/a/researchers-develop-tool-to-warn-users-about-posting-personal-data-online/)

## Acknowledgement
This research was supported by the German Research Foundation (DFG CRC 1223).
